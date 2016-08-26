##http://askubuntu.com/questions/97552/how-to-install-dot-provided-by-graphviz
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier,export_graphviz
#from  Machine_Learning.CommonFunctions import  PlotDecisionRegion
from CommonFunctions import PlotDecisionRegion
import matplotlib.pyplot as plt
import numpy as np
import sys

iris=datasets.load_iris()
df=iris.data

x=iris.data[:,[2,3]]
# print (x.shape)
# print (x)
#print (iris.data[-2:,[0,1]])
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

sc=StandardScaler()
sc.fit(x_train)
x_train_std=sc.transform(x_train)
x_test_std=sc.transform(x_test)

tree = DecisionTreeClassifier(criterion='entropy',max_depth=3, random_state=0)
tree.fit(x_train,y_train)

x_combined = np.vstack((x_train,x_test))
y_combined = np.hstack((y_train,y_test))

#print(x_train)
print ("======================")


# print(x_train[0:5,:])
# print ("======================")
# print(x_test[0:5,:])
# print ("======================")
# x_combined = np.vstack((x_train[0:5,:],x_test[0:5,:]))
# print (x_combined[0:10,:])


#print(y_train)
# print ("======================")
#print(y_test)
# print ("======================")
# x_combined = np.vstack((x_train[0:5,:],x_test[0:5,:]))
# print (x_combined[0:10,:])
#
#sys.exit()


PlotDecisionRegion.plot_decision_regions(x_combined,y_combined,classifier=tree,test_idx=range(105,150))

plt.xlabel("Petal Lenght in CM")
plt.ylabel("Petal Width in CM")
plt.legend(loc='upper left')
plt.show()
export_graphviz(tree,out_file='tree.dot',feature_names=['Petal Lenght','Petal Width'])
