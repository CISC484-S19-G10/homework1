CLASS_COL = 'Class'

import math
import operator
from functools import reduce

def varianceImpurity(data):
	#we get the of number of instances of each class, j
	counts = data[CLASS_COL].value_counts()
	
	#take the product of the counts
	counts_product = reduce(operator.mul, counts)

	#skip the division if it's zero, cause we already know the answer
	if counts_product == 0 or len(counts) == 1:
		return 0

	#then normalise by the number of instances in the dataset
	#print(counts)

	return counts_product / math.pow(data.shape[0], len(counts))

def entropy(data):
	#get the number of instances of each class, j
	counts = data[CLASS_COL].value_counts()
	#print(counts)

	#then sum -p_j * log_2(p_j) for each j
	total = 0
	for c in counts:
		#we just claim 0 * log(0) = 0 cause we're engineers today, I guess
		if c != 0:
			p = c / data.shape[0]
			total += -p * math.log(p, 2)
	
	return total

def gain(data, attr, heuristic=entropy):
	values = data[attr].unique()

	n_data = data.shape[0]
	total_gain = heuristic(data)
	
	#for each value, v, of the attribute...
	for v in values:
		#find the subset of instances with the given value of attr
		s_v = data[data[attr] == v]

		#get the proprion of instances which have value v for attr
		p_v = s_v.shape[0] / n_data

		#subtract that proption times the heaursistic of the subset from the total_gain
		total_gain -= p_v * heuristic(s_v)
	
	return total_gain
	
	return correct/validation.shape[0]
	#print("EME")
	#print(instance)

# Given a subset and a heuristic, returns the attribute that has
# the greatest info gain
def best_split(subset, heuristic):
	#Get all of the attribute columns (but not our class column)
	col_names = list(subset)
	col_names = col_names[0:len(col_names)-1]

	#Find the attribute that has the max infogain
	return max(col_names, key=lambda a: gain(subset, a, heuristic=heuristic))
