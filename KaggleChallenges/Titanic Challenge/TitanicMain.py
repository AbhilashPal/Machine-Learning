from sklearn.neural_network import MLPClassifier	# Model
import col1						# Returns list of  vectors of features needed(X,Y)
import col2						# Opens testset and reads the needed features.(X). Predicts Ys for  every X.
import cleandata				# Cleans data into integers.
import write as wr 				# writes stuff into another csv file.


TraindataXY = col1.getdata()
TraindataX = []
Element=[]
#Getting Xi features.
for i in TraindataXY:
	Element = [i[2],i[4],i[5],i[6],i[7],i[9],i[11]]
	TraindataX.append(Element)
#Fixing Unfilled ages. Filling with avg age.
avg_age = 0
summation = 0
for i in TraindataX:
	try:
		summation+=int(i[2])
	except:
		i[2] = None
avg_age = int(summation/len(TraindataX))
for i in TraindataX:
	if i[2]==None:
		i[2]=avg_age
TraindataX = cleandata.clean(TraindataX)
for i in range(5):
	print(TraindataX[i])
TraindataX = cleandata.makeint(TraindataX)
# Mean Normalization
""" is not hapenning
for i in range(len(TraindataX[0])):
	if i!=1 and i!=4:
		TraindataX=cleandata.normalize(TraindataX,i)

"""
for i in range(5):
	print(TraindataX[i])
# Getting Labels.
TraindataY=[]
for i in TraindataXY:
	TraindataY.append(i[1])

# Getting Model
clf = MLPClassifier(alpha=0.00001)
clf = clf.fit(TraindataX,TraindataY)	# Training Model




# Getting Test data
TestX_init = col2.getTdata()
TestX = []
for i in TestX_init:
	Element = [i[1],i[3],i[4],i[5],i[6],i[8],i[10]]
	TestX.append(Element)
# Fixing Missing Ages
for i in TestX:
	if i[2]==None:
		i[2]=avg_age
TestX = cleandata.clean(TestX)
for i in range(5):
	print(TestX[i])
TestX = cleandata.makeint(TestX)
"""
for i in range(len(TestX[0])):
	if i!=1 and i!=4:
		TestX=cleandata.normalize(TestX,i)
"""
for i in range(5):
	print(TestX[i])
#Cleaned Data. Testing model.
TestY = clf.predict(TestX)
# Writing to csv file
wr.writeresult(TestY)