#!/usr/bin/python3

import argparse

def parse_args():
	parser = argparse.ArgumentParser()

	#required args
	parser.add_argument('dir', \
	                    help='the directory containing the datasets')

	#optional args
	parser.add_argument('--train', default='training_set.csv', \
	                    help='the name of the file containing the training data')
	parser.add_argument('--test', default='test_set.csv', \
	                    help='the name of the file containg the testing data')
	parser.add_argument('--valid', default='validation_set.csv', \
	                    help='the name of the file containg the validation data') 

	return parser.parse_args()

def main():
	args = parse_args()
	print(args.dir, args.train, args.test, args.valid)

if __name__=='__main__':
	main()
