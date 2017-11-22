import numpy as np

def clean(L):
	for i in L:
		if i[1]=='male':
			i[1] = 1
		else:
			i[1] = 2
		if i[6] == 'Q':
			i[6] = 1
		elif i[6] == 'S':
			i[6] = 2
		else:
			i[6] = 3
	return L
def makeint(L):
	v=0.0
	M=[]
	for i in L:
		MM=[]
		for j in i:
			try:
				v=float(j)
			except ValueError:
				pass
			MM.append(v)
		M.append(MM)
	return M


def normalize(L,val):
	Newlist = []
	for i in L:
		Newlist.append(i[val])
	avg = float(sum(Newlist)/len(Newlist))
	R = max(Newlist)-min(Newlist)
	for i in Newlist:
		i = (i-avg)/R
	for i in range(len(L)):
		L[i][val] = Newlist[i]
	return L