
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
#from  Machine_Learning.CommonFunctions import  PlotDecisionRegion
from Machine_Learning.CommonFunctions import PlotDecisionRegion
import matplotlib.pyplot as plt
import numpy as np
import sys
import pandas as pd

lr=LogisticRegression(C=1000.0,random_state=0)

iris=datasets.load_iris()
df=iris.data

x= iris.data[:,[2,3]]
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

sc=StandardScaler()
sc.fit(x_train)
x_train_std=sc.transform(x_train)
x_test_std=sc.transform(x_test)
x_combined=np.vstack((x_train_std,x_test_std))
y_combined=np.hstack((y_train,y_test))
#print (y_combined)

#sys.exit()

lr.fit(x_train_std,y_train)

#print (lr.coef_)

#print (x_test,lr.predict(x_test_std))

plt.xlabel('Petal Length (Standardized)')

plt.ylabel('Petal width (Standardized)')

#PlotDecisionRegion.plot_decision_regions(x_combined,y_combined,classifier=lr,test_idx=range(105,150))



y_pred = lr.predict(x_test_std)
##print (x_test_std[0])
print(lr.predict_proba(x_test_std)[0])

output= pd.DataFrame(lr.predict_proba(x_test_std),columns=[np.unique(y_train)])

print(output)

# PlotDecisionRegion.plot_decision_regions(x_test_std,y_test,classifier=lr,test_idx=range(0,45))
# print ("Miss Classified in Test Samples %d" %(y_pred!=y_test).sum() )
#plt.show()

#print (lr.predict_proba(x_test_std[0,:]))
