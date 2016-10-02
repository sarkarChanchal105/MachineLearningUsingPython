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


param_range =[0.001,0.001,0.1,1.0,10.0,100.00]

#param_range =[i/1000 for i in range (1,10000,10)  ]


## partiion the data into traning and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)


## create a pipiline to exuete the Data Preporocessing and classification model
pipeline_lr = Pipeline([('sc1',StandardScaler()),('clf',LogisticRegression(penalty='l2',random_state=0))])

## Create learning curves using the pipiline.Set train sizes using the linespace. It uses kfold cross validation/
train_scores, test_scores = validation_curve(estimator=pipeline_lr,X=x_train,y=y_train,param_name='clf__C',param_range=param_range,cv=10)


## Mean accuracy on Trainig Data. Standard deviation of Score.
train_mean = np.mean(train_scores,axis=1)
train_std = np.std(train_scores,axis=1)

## Mean accuracy on Testing Data. Standard deviation of Score.
test_mean = np.mean(test_scores,axis=1)
test_std = np.std(test_scores,axis=1)


## plot the mean of training means based on train sizes
plt.plot(param_range,train_mean,color='blue',marker='o',markersize='5',label='training accuracy')

## indicates the variance of the mean
plt.fill_between(param_range, train_mean + train_std, train_mean - train_std,alpha =0.15,color='blue')

## plot the mean of test means based on train sizes
plt.plot(param_range,test_mean,color='green', ls= '--',marker='s',markersize='5',label='Validation accuracy')

## indicates the variance of the mean
plt.fill_between(param_range, test_mean + test_std, test_mean - test_std,alpha =0.15,color='green')


plt.grid()
## show the x-axis in log scale
plt.xscale('log')
plt.xlabel('Number of training samples')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.ylim(0.8,1.0)
plt.show()


