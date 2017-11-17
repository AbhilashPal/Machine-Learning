
from sklearn import tree 							              	# Classifier #1
from sklearn.svm import SVC							   	        # Classifier #2
from sklearn.neural_network import MLPClassifier	  					# Classifier #3
from sklearn.neighbors import KNeighborsClassifier						# Classifier #4
from sklearn.ensemble import RandomForestClassifier						# Classifier #5

from sklearn.metrics import accuracy_score
def classifier(n):
	if n == 0:
		return tree.DecisionTreeClassifier()
	elif n == 1:
		return SVC(kernel="linear", C=1)
	elif n == 2:
		return MLPClassifier(alpha=1)
	elif n == 3:
		return KNeighborsClassifier(2)
	else:
		return RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1)
def getclassifier(n):
	if n == 0:
		return "Decision Tree Classifier"
	elif n == 1:
		return "Support Vector Machine Classifier"
	elif n == 2:
		return "Multi Layer Perceptron Classifier"
	elif n == 3:
		return "K-Nearest Neighbors Classifier"
	else:
		return "Random Forest Classifier"
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'male', 'female',
     'female', 'male', 'male']

AccScoreList = []
for i in range(5):
	clf = classifier(i)
	clf = clf.fit(X,Y)
	prediction = clf.predict(X)
	accscore = accuracy_score(Y,prediction)
	AccScoreList.append(accscore)
	print("Accuracy score of classifier : {}".format(getclassifier(i))," is ",accscore)
print()
for i in range(5):
	if AccScoreList[i] == max(AccScoreList):
		print("The Best Classifier is : {}".format(getclassifier(i))," with ",AccScoreList[i]*100," percent accuracy")
		break
