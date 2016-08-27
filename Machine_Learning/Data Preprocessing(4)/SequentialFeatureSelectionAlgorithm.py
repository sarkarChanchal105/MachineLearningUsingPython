import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.base import clone
from sklearn.neighbors import KNeighborsClassifier
from itertools import combinations
import matplotlib.pyplot as plt

import Machine_Learning.CommonFunctions.commonvariables as common
df_wine=common.df_wine
x_train_std=common.x_train_std
x_test_std=common.x_test_std
y_train=common.y_train
y_test=common.y_test

class SBS():
    ## initialize the variables
    def __init__(self,estimator,k_features,scoring=accuracy_score,test_size=0.25,random_state=1):
        self.scoring=scoring
        self.estimator = clone(estimator)
        self.k_features=k_features
        self.test_size=test_size
        self.random_state=random_state

    ## define the fit method to use
    def fit(self,x,y):

        dim=x_train_std.shape[1] # get the number of features in the dataset
        self.indices_=tuple(range(dim)) # create a tuple with the number of features
        self.subsets_=[self.indices_]
        score = self._calc_score(x_train_std,y_train,x_test_std,y_test,self.indices_) # get the score of the classifier with full features
        self.scores_=[score] ## Store the score in this array

        ### for each subset of feature run the classifier algorithm and get the scores.
        while dim > self.k_features:
            scores =[]
            subsets =[]
            for p in combinations(self.indices_,r=dim-1):
                score=self._calc_score(x_train_std,y_train,x_test_std,y_test,p)
                scores.append(score)
                subsets.append(p)
            best = np.argmax(scores)
            self.indices_=subsets[best]
            self.subsets_.append(self.indices_)
            dim -= 1

            self.scores_.append(scores[best])
        self.k_score =self.scores_
        return self


    def transform(self,x):
        return x[:,self.indices_]

    ### define the funtion that calculates the scores of the classifier.
    def _calc_score(self,x_train,y_train,x_test,y_test,indices):
        self.estimator.fit(x_train[:,indices],y_train)
        y_pred = self.estimator.predict(x_test[:,indices])
        score = self.scoring(y_test,y_pred)
        return score


## declare a K-nearest neighbor classifier.
knn =KNeighborsClassifier(n_neighbors=2)
sbs=SBS(knn,k_features=1)
sbs.fit(x_test_std,y_train)

## plot the accuracy and number of feature
k_feat = [len(k) for k in sbs.subsets_]
plt.plot(k_feat,sbs.scores_,marker='o')
plt.ylim([0.7,1.1])
plt.ylabel('Accuracy')
plt.xlabel('Number of features')
plt.grid()
plt.show()


## get the feature that generates the highest accuracy
k5 = list(sbs.subsets_[np.argmax(sbs.scores_)+1])
print(df_wine.columns[1:][k5])

