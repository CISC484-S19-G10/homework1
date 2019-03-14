from heuristics import best_split, CLASS_COL
import random
import copy
import pandas

#Left branches are attribute values of 0
#Right branches are attribute values of 1

class Node:

	def __init__(self, previous_splits=None):
		self.left = None
		self.right = None
		self.split_attribute = None
		self.set_class_value(None)
		self.data = None

		self.previous_splits = previous_splits
		#set previous splits to a new dict if none given
		#(cannot do this via default args since that would have every instance
		#share the same dict)
		if self.previous_splits is None:
			self.previous_splits = {}

	def set_class_value(self, val, internal_nodes=None):
		if internal_nodes:
			if val == None:
				internal_nodes.add(self)
			elif self in internal_nodes:
				internal_nodes.remove(self)
		self.class_value = val

	def inseparable(self, data):
		new_data = data.iloc[:, 0:data.shape[1]-1]
		curr = new_data.iloc[0]
		insep = True

		for index, row in new_data.iterrows():
			compare = (curr == row)
			for r in compare:
				insep = insep and r

		return insep
		#print(data.duplicated)

	def build_tree(self, data, heuristic):
		if data.empty:
			self.class_value = None
			return
		
		#if we've got a pure dataset or we're out of attributes...
		elif len(data[CLASS_COL].unique()) == 1 or data.shape[1] == 1 or self.inseparable(data):
			#select the most common class value
			counts = data[CLASS_COL].value_counts()
			self.set_class_value(counts.idxmax())
			self.data = data
			#print(self.data)
			return

		#otherwise, get the best attribute to split on
		best_attr = best_split(data, heuristic)
		self.split_attribute = best_attr
	
		#create new nodes
		self.left = Node()
		self.right = Node()
		#print(self.data)

		for node, val in [[self.left, 0], [self.right, 1]]:
			#make a copy of the filtered dataset
			filtered_data = data[data[best_attr] == val]
			#print(filtered_data)
			
			#remove the selected attribute from the dataset
			#del filtered_data[best_attr]
			#print("AA")

			#recurse!
			node.build_tree(filtered_data, heuristic)

	def print_subtree(self, indent):
		if self != None and self.split_attribute != None:
			left_subtree_print = ""
			right_subtree_print = ""

			for i in range(0, indent):
				left_subtree_print+="| "
				right_subtree_print+="| "


			left_subtree_print += self.split_attribute+" = 0: "
			if self.left.split_attribute == None:
				left_subtree_print += str(self.left.class_value)

			print(left_subtree_print)
			self.left.print_subtree(indent+1)

			right_subtree_print += self.split_attribute+" = 1: "
			if self.right.split_attribute == None:
				right_subtree_print += str(self.right.class_value)

			print(right_subtree_print)

			self.right.print_subtree(indent+1)
	
	def get_internal_nodes(self, internal_nodes=None):
		if internal_nodes is None:
			internal_nodes = set()
		
		if self.left is not None or \
			self.right is not None:
			internal_nodes.add(self)

		if self.left is not None:
			self.left.get_internal_nodes(internal_nodes=internal_nodes)
	
		if self.right is not None:
			self.right.get_internal_nodes(internal_nodes=internal_nodes)

		return internal_nodes

	def copy_subtree(self, node):
		copy_node = copy.deepcopy(node)

		if node.left != None:
			copy_node.left = self.copy_subtree(node.left)
		
		if node.right != None:
			copy_node.right = self.copy_subtree(node.right)
		
		if node.data is not None:
			copy_node.data = node.data.copy()
		
		return copy_node

	def classify(self, instance):
		current_node = self
		while current_node.split_attribute != None:
			if instance[current_node.split_attribute] == 1:
				current_node = current_node.right
			else:
				current_node = current_node.left

		return current_node.class_value

	def accuracy(self, validation):
		correct = 0
		for index, row in validation.iterrows():
			classified_as = self.classify(row)
			if classified_as == row["Class"]:
				correct+=1
			#print("Classified As: "+str(classified_as)+", Actual: "+str(row["Class"]))
			#return 0
			#print(row)
		return correct / validation.shape[0]

	def prune_tree(self, l, k, validation):
		best_tree = self
		best_accuracy = self.accuracy(validation)

		for i in range(1, l):
			temp = self.copy_subtree(self)
			internal_nodes = temp.get_internal_nodes()
			m = random.randint(1, k+1)
			for j in range(1, m):
				if not internal_nodes:
					break

				#make node p a leaf node
				p = random.sample(internal_nodes, 1)
				p[0].collapse()

			new_accuracy = temp.accuracy(validation)
			#print((new_accuracy, best_accuracy))
			if new_accuracy > best_accuracy:
				best_accuracy = new_accuracy
				best_tree = temp
		
		return best_tree
	
	def collapse(self, internal_nodes=None):
		#combine the data from our children with our data
		data_list = [self.data]
		if self.left != None:
			self.left.collapse()
			data_list.append(self.left.data)
			self.left = None
		if self.right != None:
			self.right.collapse()
			data_list.append(self.right.data)
			self.right = None

		#print(data_list)
		#if data_list is not None:
		self.data = pandas.concat(data_list, sort=False)

		if internal_nodes and self in internal_nodes:
			internal_nodes.remove(self)

		#select the most common class value
		counts = self.data[CLASS_COL].value_counts()
		self.class_value = counts.idxmax()
		self.split_attribute = None

	#used to select a random non-leaf node
	def tree_to_list(self, currNode, a = []): 
		#only add non-leaf nodes
		if currNode != None and currNode.left != None and currNode.right != None:
			self.tree_to_list(currNode.left, a)
			a += [currNode]
			self.tree_to_list(currNode.right, a)
