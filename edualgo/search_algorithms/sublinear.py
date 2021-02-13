import numpy as np
from random import choice

def sublinear(inplist, x, hint = False):
	randlist = np.array(inplist)
	np.random.shuffle(randlist)
	s = randlist[:int(len(inplist)**0.5)]
	p = s[0]
	q = s[0]
	min_p = p - x
	max_q = x - q
	for i in range(len(s)):
		if s[i] <= x and x - s[i] < min_p:
			p = s[i]
			min_p = p - x
		if s[i] > x and s[i] - x < max_q:
			q = s[i]
			max_q = x - q

	for i in range(inplist.index(p),inplist.index(q)):
		if inplist[i] == x:
			hint = True
			break
	return hint

arr = [i for i in range(0,10000,3)]
iterations = 10000
listoutputs = []

for i in range(iterations):
	n = choice(arr)
	pre = sublinear(arr, n, hint = False)
	listoutputs.append(pre)
print('Number of Trials:', len(listoutputs))
print('Number of Trues:', listoutputs.count(True))
print('Numer of False:', listoutputs.count(False))


# Output: Number of Trials:10000  Number of Trues:9309  Numer of False:691
