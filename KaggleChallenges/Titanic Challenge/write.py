import csv
def writeresult(L):
	returns_path = "datasets/testresult.csv"
	file = open(returns_path,'w')
	writer = csv.writer(file)
	writer.writerow(["PassengerId","Survived"],)
	for i in range(len(L)-1):
		RecordNo = i+892
		Label = L[i]
		writer.writerow([RecordNo,Label],)