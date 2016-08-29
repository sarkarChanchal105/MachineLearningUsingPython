import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

colors=['blue','green','red','cyan','magenta','yellow','black','pink','lightgreen','lightblue','gray','indigo','orange']

## Get the win sample data from UCI portal to pandas data frame
df_wine=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df_breast=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data',header=None)


## Define the columns of the Data Frame
df_wine.columns=['Class Label','Alcohol','Malic Acid','Ash',
           'Alcalinity of Ash','Magnesium',
          'Total Phenols','Flavanoids',
          'Nonflavanoid phenols',
          'Proanthocyanins',
          'Color intensity','Hue',
          '0D280/0D315 of diluted wines',
          'Proline']

## X is the feature , Y is the Target.
x,y = df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values

## Split the data into Train ans Test (70:30
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


## Standardize the data
sc=StandardScaler()
x_train_std=sc.fit_transform(x_train)
x_test_std=sc.fit_transform(x_test)




### Preprocrsing for Breast Cancer
x_breast=df_breast.loc[:,2:].values
y_breast=df_breast.loc[:,1].values
