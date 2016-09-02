from sklearn.grid_search import GridSearchCV
from sklearn.svm import  SVC
from sklearn.tree import DecisionTreeClassifier
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
gs= GridSearchCV(estimator=pipeline_lr,param_grid=param_grid,scoring='accuracy',cv=2,n_jobs=1)

scores=cross_val_score(gs,x_train,y_train,scoring='accuracy',cv=5)

print ("CV Accuracy %0.3f +/- %0.3f " % (np.mean(scores),np.std(scores)) )


### use grid search on Decision Tree Classifier
gs=GridSearchCV(estimator=DecisionTreeClassifier(random_state=0), param_grid=[{'max_depth':[1,2,3,4,5,6,7,None]}],scoring='accuracy',cv=2)

scores=cross_val_score(gs,x_train,y_train,scoring='accuracy',cv=5)

print ("CV Accuracy %0.3f +/- %0.3f " % (np.mean(scores),np.std(scores)) )


