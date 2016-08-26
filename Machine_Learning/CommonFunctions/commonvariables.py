import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

colors=['blue','green','red','cyan','magenta','yellow','black','pink','lightgreen','lightblue','gray','indigo','orange']
df_wine=pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data',header=None)
df_wine.columns=['Class Label','Alcohol','Malic Acid','Ash',
           'Alcalinity of Ash','Magnesium',
          'Total Phenols','Flavanoids',
          'Nonflavanoid phenols',
          'Proanthocyanins',
          'Color intensity','Hue',
          '0D280/0D315 of diluted wines',
          'Proline']

x,y = df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)

sc=StandardScaler()
x_train_std=sc.fit_transform(x_train)
x_test_std=sc.fit_transform(x_test)
