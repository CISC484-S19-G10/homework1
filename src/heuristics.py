CLASS_COL = 'Class'

import math

def info_gain(data, attr):
	pass

def entropy(data):
	#get the counts of each class, i
	counts = data[CLASS_COL].value_counts()

	#then sum -p_i * log_2(p_i) for each i
	total = 0
	for c in counts:
		if c != 0:
			p = c / data.shape[0]
			total += -p * math.log(p, 2)
	return total
