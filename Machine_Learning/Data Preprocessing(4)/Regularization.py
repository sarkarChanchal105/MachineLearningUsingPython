""" L1 and L2 regularization """

import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
import Machine_Learning.CommonFunctions.commonvariables as common



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
