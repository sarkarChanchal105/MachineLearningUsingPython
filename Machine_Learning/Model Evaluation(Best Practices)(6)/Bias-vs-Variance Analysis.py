import matplotlib.pyplot as plt
from sklearn.learning_curve import learning_curve
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
import Machine_Learning.CommonFunctions.commonvariables as common
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
import numpy as np

x=common.x_breast
y=common.y_breast

## partiion the data into traning and test
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=1)


## create a pipiline to exuete the Data Preporocessing and classification model
pipeline_lr = Pipeline([('sc1',StandardScaler()),('clf',LogisticRegression(penalty='l2',random_state=0))])

train_sizes,train_scores, test_scores = learning_curve(estimator=pipeline_lr,X=x_train,y=y_train,train_sizes=np.linspace(0.1,1.0,10),cv=10,n_jobs=1)

train_mean = np.mean(train_scores,axis=1)
train_std = np.std(train_scores,axis=1)

test_mean = np.mean(test_scores,axis=1)
test_std = np.std(test_scores,axis=1)


plt.plot(train_sizes,train_mean,color='blue',marker='o',markersize='5',label='training accuracy')

plt.fill_between(train_sizes, train_mean + train_std, train_mean - train_std,alpha =0.5,color='blue')
