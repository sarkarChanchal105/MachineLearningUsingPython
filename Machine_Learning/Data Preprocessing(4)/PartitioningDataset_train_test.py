import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df_wine=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)

df_wine.columns=['Class Label','Alcohol','Malic Acid','Ash',
           'Alcalinity of Ash','Magnesium',
          'Total Phenols','Flavanoids',
          'Nonflavanoid phenols',
          'Proanthocyanins',
          'Color intensity','Hue',
          '0D280/0D315 of diluted wines',
          'Proline']

print('class labels',np.unique(df_wine['Class Label']))
#print(df_wine.head())

x,y = df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


print("STANDARDIZATION AND NORMAIZATION")
mms = MinMaxScaler()
x_train_norm = mms.fit_transform(x_train)
x_test_norm = mms.fit_transform(x_test)
print (x_train_norm)

stsdc = StandardScaler()
x_train_std=stsdc.fit_transform(x_train)
x_test_std=stsdc.fit_transform(x_test)

