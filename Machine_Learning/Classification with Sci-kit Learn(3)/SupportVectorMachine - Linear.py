from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from CommonFunctions import  PlotDecisionRegion
import matplotlib.pyplot as plt
import numpy as np
import sys

iris=datasets.load_iris()
df=iris.data

x=iris.data[:,[2,3]]

#print (x)

y=iris.target

#print (y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)
#x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

sc=StandardScaler()
(sc.fit(x_train))

x_train_std=sc.transform(x_train)

x_test_std=sc.transform(x_test)

svm=SVC(kernel='linear',C=0.9, random_state=0)
svm=SVC(kernel='rbf',C=1000.0, gamma=0.02, random_state=0)

svm.fit(x_train_std,y_train)

x_combined_std=np.vstack((x_train_std,x_test_std))

y_combined=np.hstack((y_train,y_test))

PlotDecisionRegion.plot_decision_regions(x_combined_std,y_combined,classifier=svm,test_idx=range(105,150))


plt.xlabel('Petal Length (Standardized)')

plt.ylabel('Petal Width (Standardized)')

plt.legend(loc='upper left')
y_pred= svm.predict(x_test_std)

# PlotDecisionRegion.plot_decision_regions(x_test_std,y_test,classifier=svm,test_idx=range(0,45))
# print ("Miss Classified in Test Samples %d" %(y_pred!=y_test).sum() )
plt.show()





