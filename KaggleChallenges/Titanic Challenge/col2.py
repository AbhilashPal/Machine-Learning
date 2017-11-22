import csv

def getTdata():
	k = []
	data=open('datasets/test.csv')
	data = csv.reader(data)
	header = next(data)
	for i in data:
		k.append(i)
	return (k)
	