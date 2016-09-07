from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from Machine_Learning.CommonFunctions import PlotDecisionRegion
import matplotlib.pyplot as plt
import numpy as np
import sys


iris=datasets.load_iris()
df=iris.data

x=iris.data[:,[2,3]]

#print (x)

y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

sc=StandardScaler()
sc.fit(x_train)

x_train_std = sc.transform(x_train)
x_test_std = sc.transform(x_test)

forest = RandomForestClassifier(criterion='entropy',n_estimators=10,random_state=1,n_jobs=2)

forest.fit(x_train,y_train)
x_combined = np.vstack((x_train,x_test))
y_combined = np.hstack((y_train,y_test))

PlotDecisionRegion.plot_decision_regions(x_combined,y_combined,classifier=forest,test_idx=range(105,150))


plt.xlabel('Petal Length')
plt.ylabel('Petal Width')

plt.legend(loc='upper left')

plt.show()

print (x)
y_predict =forest.predict(x)
print(y_predict)
print ("Miss classified samples are %d" %(y_predict!=y).sum() )

#print (y_predict[2])
# print ((c for c in range(0,10)) )
#
# print(sum(i for i in range(1,1000) if i%3 == 0 or i%5 == 0))
from sklearn.tree import DecisionTreeClassifier,export_graphviz





