### This program presents the pictorial depiction of the impact on the weights of the features based on the different values of
### regularilization parameters. In this case we used Logistic regression.
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import Machine_Learning.CommonFunctions.commonvariables as common
import sys

colors=common.colors
weights,params = [],[]
df_wine=common.df_wine
x_train_std=common.x_train_std
x_test_std=common.x_test_std
y_train=common.y_train

fig=plt.figure()
ax=plt.subplot(111)


## Execute the Logistic Regression  using L1 regularization (lasso) with different Regularization factor.
## In this C is the factor. Penalty =l1 means L1 regularization.
for c in np.arange(-4,6):
    lr=LogisticRegression(penalty='l1',C=10**c,random_state=0)
    lr.fit(x_train_std,y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)

weights = np.array(weights)
for column,color in zip(range(weights.shape[1]),colors):
    #print ("{},{}".format(column,color))
    plt.plot(params,weights[:,column],label=df_wine.columns[column+1],color=color)
    #print ("{},{}".format(params,weights[:,column]))
    #plt.show()


plt.axhline(0,color='black',linestyle='--',linewidth=3)
#plt.xlim([10**(-5),10**(-6)])
plt.xlabel('C')
plt.ylabel('Weight Coeffients')
plt.xscale('log')
plt.legend(loc='upper left')
ax.legend(loc='upper center',bbox_to_anchor=(1.38,1.03),ncol=1,fancybox=True)

plt.show()