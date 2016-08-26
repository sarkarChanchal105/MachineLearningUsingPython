# Lazy Learning
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from  CommonFunctions import  PlotDecisionRegion
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import sys



iris=datasets.load_iris()

x=iris.data[:,[2,3]]
y=iris.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

knn= KNeighborsClassifier(n_neighbors=5,p=20000000000000000,metric='minkowski',n_jobs=2)

sc=StandardScaler()
sc.fit(x_train)
x_train_std=sc.transform(x_train)
x_test_std=sc.transform(x_test)

knn.fit(x_train_std,y_train)

x_combined = np.vstack((x_train_std,x_test_std))
y_combined = np.hstack((y_train,y_test))

PlotDecisionRegion.plot_decision_regions(x_combined,y_combined,classifier=knn,test_idx=range(105,150))

plt.xlabel('Petal Length  (Standard)')
plt.ylabel('Petal width (Standard)')
plt.legend(loc='upper left')

plt.show()

