CLASS_COL = 'Class'

import math

def varianceImpurity(data):
	counts = data['class'].value_counts()
	k0 = counts[0]
	k1 = counts[1]
	k = data.count() 	

	vi = (k0/k)*(k1/k)

	return vi

def entropy(data):
	#get the counts of each class, j
	counts = data[CLASS_COL].value_counts()

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
	total_gain = entropy(data)
	
	#for each value, v, of the attribute...
	for v in values:
		#find the subset of instances with the given value of attr
		s_v = data[data[attr] == v]

		#get the proprion of instances which have value v for attr
		p_v = s_v.shape[0] / n_data

		#subtract that proption times the heaursistic of the subset from the total_gain
		total_gain -= p_v * heuristic(s_v)
	
	return total_gain
