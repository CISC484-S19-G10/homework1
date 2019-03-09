CLASS_COL = 'Class'

import math

def info_gain(data, attr):
	pass

def entropy(data):
	#get the counts of each class, i
	counts = data[CLASS_COL].value_counts()

	#divide by the number of rows to get the proportion, p_i, for each value i
	proportions = 1.0 * counts / data.shape[0]
	
	#then sum -p_i * log_2(p_i) for each i
	total = 0
	for p in proportions:
		if p != 0:	
			total += -p * math.log(p, 2)
	return total
