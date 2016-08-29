import pandas as pd
import Machine_Learning.CommonFunctions.commonvariables as common
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler

import numpy as np


x=common.x_breast
y=common.y_breast
le = LabelEncoder()
y=le.fit_transform(y)

## partiion the data into traning and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)
## create a pipiline to exuete the Data Preporocessing and classification model
pipeline_lr = Pipeline([('sc1',StandardScaler()),('pca',PCA(n_components=2)),('clf',LogisticRegression(random_state=1))])
## fit the data into pipiline which will preprocess and run the classifier
pipeline_lr.fit(x_train,y_train)
#print (pipeline_lr.score(x_test,y_test))

## create Kfold samples
kfold = StratifiedKFold(y=y_train,n_folds=10,random_state=1)

#print (kfold.y)
print('Number of records Train ',len(x_train))
print('Number of records Test',len(x_test))
scores =[]
# iter=0
#
# print(kfold)
# print (list(enumerate(kfold)))
#
#

for k ,(train,test) in enumerate(kfold):
    pipeline_lr.fit(x_train[train],y_train[train])
    score = pipeline_lr.score(x_train[test],y_train[test])
    scores.append(score)
    print ('Fold: %s, Class dist.: %s, Acc: %.3f' % (k+1,np.bincount(y_train[train]),score))
print ("Cross validation accuracy score: %.3f +/- %.3f" % (np.mean(scores),np.std(scores)))



##### Another approacj ##########

print ("\n::Kfold Cross validation using another approach::")
scores = cross_val_score(estimator=pipeline_lr,X=x_train,y=y_train,cv=10,n_jobs=1)
print ("Cross validation accuracy score: %.3f +/- %.3f" % (np.mean(scores),np.std(scores)))