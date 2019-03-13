#!/usr/bin/python3

import argparse
import os
import pandas
import sys
from heuristics import *
from node import *


arg_format = True

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
	if not arg_format:
		args = parse_args()
		#assume all files are in the specified directory
		train = os.path.join(args.dir, args.train)
		test = os.path.join(args.dir, args.test)
		valid = os.path.join(args.dir, args.valid)

	l_prune = int(sys.argv[1])
	k_prune = int(sys.argv[2])
	train = sys.argv[3]
	valid = sys.argv[4]
	test = sys.argv[5]
	to_print = sys.argv[6]

	#read in the csvs
	train = pandas.read_csv(train)
	test = pandas.read_csv(test)
	valid = pandas.read_csv(valid)
	header = "---------------"

	names = ["ENTROPY", "VARIANCE IMPURITY"]
	heurs = [entropy, varianceImpurity]

	for index, heur in enumerate(heurs):
		print(names[index]+":")
		root = Node()
		root.build_tree(train, heur)
		acc = root.accuracy(test)
		pruned_root = root.prune_tree(l_prune, k_prune, valid)	
		pruned_acc = pruned_root.accuracy(test)
		print("UNPRUNED ACCURACY: "+str(acc))
		
		print("PRUNED ACCURACY: "+str(pruned_acc))	

		if to_print == "yes":
			print(header)
			print("UNPRUNED TREE:")
			print(header)
			print()
			root.print_subtree(0)
			print(header)
			print("PRUNED TREE")
			print(header)
			print()
			pruned_root.print_subtree(0)

		print()	
		#root.print_subtree(0)

	#root = Node()
	#root.build_tree(train, entropy)
	#root.print_subtree(0)

	#acc = root.accuracy(test)
	#print(acc)
	#for i in range(5,15):
		#pruned_root = root.prune_tree(30, i, valid)
		#pruned_acc = pruned_root.accuracy(test)
		#print(pruned_acc)
	#pruned_root.print_subtree(0)

if __name__=='__main__':
	main()
