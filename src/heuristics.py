def info_gain(data, attr):
	pass

def entropy(data):
	pass


def varianceImpurity(data):
	counts = data['class'].value_counts()
	k0 = counts[0]
	k1 = counts[1]
	k = data.count() 	

	vi = (k0/k)*(k1/k)

	return vi

