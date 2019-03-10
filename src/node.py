from heuristics import best_split 

#Left branches are attribute values of 0
#Right branches are attribute values of 1

#Slow, I think I may be copying data down each split of the tree then
#just filtering it like I want to
def build_tree(node, data, heuristic):
	#At each layer, filter the data so that it only sees data that should be at that branch
	filtered_subset = data
	for key in node.previous_splits:
		filtered_subset = filtered_subset[filtered_subset[key] == node.previous_splits[key]]
	
	#If this subset is pure, we don't need to split anymore
	if heuristic(filtered_subset) == 0:
		if not filtered_subset.empty:
			node.class_value = filtered_subset.iloc[0]["Class"]
		else:
			node.class_value = None
		return 0
	else:
		#Get the best attribute to split on
		best_attr = best_split(filtered_subset, heuristic)
		node.split_attribute = best_attr
		
		#Partition the left and right nodes
		node.left = Node(node.previous_splits.copy())
		node.left.previous_splits[best_attr] = 0

		node.right = Node(node.previous_splits.copy())
		node.right.previous_splits[best_attr] = 1

		#get rid of the attribute we just used
		#del node.right.previous_splits[best_attr]
		#del node.left.previous_splits[best_attr]

		#Recurse!
		build_tree(node.left, filtered_subset, heuristic)
		build_tree(node.right, filtered_subset, heuristic)

class Node:
	def __init__(self, previous_splits=None):
		self.left = None
		self.right = None
		self.split_attribute = None
		self.class_value = None

		self.previous_splits = previous_splits
		#set previous splits to a new dict if none given
		#(cannot do this via default args since that would have every instance
		#share the same dict)
		if self.previous_splits == None:
			self.previous_splits = {}

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
