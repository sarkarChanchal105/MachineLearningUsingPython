from sklearn.grid_search import GridSearchCV
from sklearn.svm import  SVC
import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve, validation_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import Machine_Learning.CommonFunctions.commonvariables as common
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
import numpy as np


x=common.x_breast
y=common.y_breast


param_range =[0.0001,0.001,0.01,0.1,1.0,10.0,100.00,1000.00]
#param_range =[i/1000 for i in range (1,10000,10)  ]

param_grid=[{'clf__C': param_range,'clf__kernel':['linear']},
            {'clf__C':param_range,'clf__gamma': param_range,'clf__kernel': ['rbf'] }]


#print (param_grid)


## partiion the data into traning and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)


## create a pipiline to exuete the Data Preporocessing and classification model
pipeline_lr = Pipeline([('scl',StandardScaler()),('clf',SVC(random_state=0))])

## define and execute the Grid Search algorithm to find the best parameter
gs= GridSearchCV(estimator=pipeline_lr,param_grid=param_grid,scoring='accuracy',cv=10,n_jobs=1)
gs.fit(x_train,y_train
       )
print("Best Scopre :{} Best Parameters :{} ".format(gs.best_score_,gs.best_params_))


## use the best parameters to run the model on test data

clf = gs.best_estimator_
clf.fit(x_train,y_train)
print("Test Accuracy : %.3f" % clf.score(x_test,y_test))



