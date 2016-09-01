""" L1 and L2 regularization """

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
import Machine_Learning.CommonFunctions.commonvariables as common
import matplotlib.pyplot as plt



df_wine=common.df_wine


#print('class labels',np.unique(df_wine['Class Label']))
#print(df_wine.head())

x_train_std=common.x_train_std
x_test_std=common.x_test_std
y_train=common.y_train
y_test=common.y_test
print ("Logistic Regression with L1 regularization")
lr =LogisticRegression(penalty='l1',C=0.1)
lr.fit(x_train_std,y_train)
print ("Training Accuracy :",lr.score(x_train_std,y_train))
print ("Testing Accuracy :",lr.score(x_test_std,y_test))

#print ("The intercepts are ",'\n',lr.intercept_)
#print ("The weights are ",'\n',lr.coef_)

print ("Logistic Regression with L2 regularization")
lr =LogisticRegression(penalty='l2',C=0.1)
lr.fit(x_train_std,y_train)
print ("Training Accuracy :",lr.score(x_train_std,y_train))
print ("Testing Accuracy :",lr.score(x_test_std,y_test))





param_range =[0.00001,0.0001,0.001,0.01,0.1,1.0,10.0,100.00,1000.00]
regularization=['l1','l2']
train_score=[]
test_score=[]
markers=('s','x','o','^','v')
idx=0
for penalty in regularization:
    for c in param_range:
        lr =LogisticRegression(penalty=penalty,C=c)
        lr.fit(x_train_std,y_train)
        train_score.append(lr.score(x_train_std,y_train))
        test_score.append(lr.score(x_test_std,y_test))

    plt.plot(param_range,train_score,color='blue', ls= '--',marker=markers[idx],markersize='5',label='training accuracy for pentalty:'+penalty)
    plt.plot(param_range,test_score,color='green', ls= '--',marker=markers[idx],markersize='5',label='testing accuracy for pentalty:'+penalty)
    train_score=[]
    test_score=[]
    plt.xscale('log')
    idx+=1

plt.legend(loc='lower right')
plt.xlabel('Regularilzation Strength')
plt.ylabel('Accuracy')
plt.show()
# plt.xscale('log')
# plt.plot(score,param_range)
# plt.show()




