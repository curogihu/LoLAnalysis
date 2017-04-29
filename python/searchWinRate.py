from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import numpy as np
import datetime

data = np.loadtxt("../output/target/teamResult.csv", delimiter=',')
Y = data[:, 0:1] # 0 = lose, 1 = win
X = data[:,1:] # contains, championIds, top, jg, mid, adc, sup

label = Y.reshape(len(X))

# iris = datasets.load_iris()
# X = iris.data
# Y = iris.target

# print(X)
print(label)
"""
clf = RandomForestClassifier()
clf.fit(X, Y)
print(clf.feature_importances_)
"""

# print(resultLabel.transpose())

# print(resultLabel.T)
# print(resultLabel.ravel)
# resultLabel = resultLabel.ravel


clf = RandomForestClassifier()
clf.fit(X, label)

print(clf.predict([[68,24,8,67,432]]))
print(clf.predict_proba([[68,24,8,67,432]]))

# print(data)
# print(resultLabel)
# print(teamData)

