import csv

def getdata():
	k = []
	data=open('datasets/train.csv')
	data = csv.reader(data)
	header = next(data)
	for i in data:
		k.append(i)
	return (k)
	