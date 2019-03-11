#!/usr/bin/python3

import argparse
import os
import pandas
from heuristics import *
from node import *

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

	#for heur in [entropy, varianceImpurity]:
	#	root = Node()
	#	root.build_tree(train, heur)	
	#	root.print_subtree(0)

	root = Node()
	root.build_tree(train, entropy)
	root.print_subtree(0)

	acc = accuracy(root, test)
	print(acc)
	
	pruned_root = root.prune_tree(5, 5, valid)
	pruned_acc = accuracy(pruned_root, test)
	print(pruned_acc)

if __name__=='__main__':
	main()
