#https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data
import pandas as pd

df =pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data',header=None,sep='\s+')

df.columns=[CRIM,]