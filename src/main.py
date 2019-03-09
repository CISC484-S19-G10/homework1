#!/usr/bin/python3

import argparse
import os
import pandas
from heuristics import *

def parse_args():
	parser = argparse.ArgumentParser()

	#required args
	parser.add_argument('dir', \
	                    help='the directory containing the datasets')

	#optional args
	parser.add_argument('--train', default='training_set.csv', \
	                    help='the name of the file containing the training data in the given dir')
	parser.add_argument('--test', default='test_set.csv', \
	                    help='the name of the file containg the testing data in the given dir')
	parser.add_argument('--valid', default='validation_set.csv', \
	                    help='the name of the file containg the validation data in the given dir') 

	return parser.parse_args()

def main():
	args = parse_args()
	
	#assume all files are in the specified directory
	train = os.path.join(args.dir, args.train)
	test = os.path.join(args.dir, args.test)
	valid = os.path.join(args.dir, args.valid)

	#read in the csvs
	train = pandas.read_csv(train)
	test = pandas.read_csv(test)
	valid = pandas.read_csv(valid)

	root = Node()
	build_tree(root, train)

	print_subtree(root,0)

#Left branches are attribute values of 0
#Right branches are attribute values of 1

#Slow, I think I may be copying data down each split of the tree then
#just filtering it like I want to
def build_tree(node, data):
	#At each layer, filter the data so that it only sees data that should be at that branch
	filtered_subset = data
	for key in node.previous_splits:
		filtered_subset = filtered_subset[filtered_subset[key] == node.previous_splits[key]]
	
	#If this subset is pure, we don't need to split anymore
	if entropy(filtered_subset) == 0:
		if not filtered_subset.empty:
			node.class_value = filtered_subset.iloc[0]["Class"]
		else:
			node.class_value = None
		return 0
	else:
		#Get the best attribute to split on
		best_attr = best_split(filtered_subset, entropy)
		node.split_attribute = best_attr
		
		#Partition the left and right nodes
		node.left = Node(node.previous_splits.copy())
		node.left.previous_splits[best_attr] = 0

		node.right = Node(node.previous_splits.copy())
		node.right.previous_splits[best_attr] = 1

		#Recurse!
		build_tree(node.left, filtered_subset)
		build_tree(node.right, filtered_subset)

class Node:
	def __init__(self, previous_splits={}):
		self.left = None
		self.right = None
		self.split_attribute = None
		self.previous_splits = previous_splits
		self.class_value = None

def print_subtree(node, indent):
	if node != None and node.split_attribute != None:
		left_subtree_print = ""
		right_subtree_print = ""

		for i in range(0, indent):
			left_subtree_print+="| "
			right_subtree_print+="| "


		left_subtree_print += node.split_attribute+" = 0: "
		if node.left.split_attribute == None:
			left_subtree_print += str(node.left.class_value)

		print(left_subtree_print)
		print_subtree(node.left,indent+1)

		right_subtree_print += node.split_attribute+" = 1: "
		if node.right.split_attribute == None:
			right_subtree_print += str(node.right.class_value)

		print(right_subtree_print)

		print_subtree(node.right,indent+1)

# Given a subset and a heuristic, returns the attribute that has
# the greatest info gain
def best_split(subset, heuristic):
	#Get all of the attribute columns (but not our class column)
	col_names = list(subset)
	col_names = col_names[0:len(col_names)-1]

	#Find the attribute that has the max infogain
	#There's probably a more pythonic way to do this...
	max_info_gain = -1
	max_info_gain_col = ""
	for col in col_names:
		info_gain = gain(subset, col, heuristic)
		if(info_gain > max_info_gain):
			max_info_gain = info_gain
			max_info_gain_col = col

	return max_info_gain_col

if __name__=='__main__':
	main()
