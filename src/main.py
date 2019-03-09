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

	best_split(train, entropy)

	

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
