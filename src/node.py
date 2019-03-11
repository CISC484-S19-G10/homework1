from heuristics import best_split, CLASS_COL
import random

#Left branches are attribute values of 0
#Right branches are attribute values of 1

class Node:
	def __init__(self, previous_splits=None):
		self.left = None
		self.right = None
		self.split_attribute = None
		self.class_value = None
		self.data = None

		self.previous_splits = previous_splits
		#set previous splits to a new dict if none given
		#(cannot do this via default args since that would have every instance
		#share the same dict)
		if self.previous_splits == None:
			self.previous_splits = {}

	def build_tree(self, data, heuristic):
		if data.empty:
			self.class_value = None
			return
		
		#if we've got a pure dataset or we're out of attributes...
		elif len(data[CLASS_COL].unique()) == 1 or data.shape[1] == 1:
			#select the most common class value
			counts = data[CLASS_COL].value_counts()
			self.class_value = counts.idxmax()
			self.data = data
			return

		#otherwise, get the best attribute to split on
		best_attr = best_split(data, heuristic)
		self.split_attribute = best_attr
	
		#create new nodes
		self.left = Node()
		self.right = Node()

		for node, val in [[self.left, 0], [self.right, 1]]:
			#make a copy of the filtered dataset
			filtered_data = data[data[best_attr] == val]
			
			#remove the selected attribute from the dataset
			del filtered_data[best_attr]

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
			 

	def prune_tree(self, l, k):
		best_tree = self
		best_accuracy = accuracy(self, validation)
		for i in range(1, l):
			temp = self
			m = random.randint(1, k+1)
			for j in range(1, m):
				interior_nodes = tree_to_list(temp)
				p = random.randint(0, len(interior_nodes))
				#make node p a leaf node
				interior_nodes[p].collapse()			
			#figure out how to fit in accuracy check
			new_accuracy = 0 #temp.accuracy(validation)
			if new_accuracy > best_accuracy:
				best_tree = temp
		return best_tree
	
	def collapse(self):
		if self.left != None:
			collapse(self.left)
			self.data += self.left.data
			self.left = None
		if self.right != None:
			collapse(self.right)
			self.data += self.right.data
			self.right = None

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
