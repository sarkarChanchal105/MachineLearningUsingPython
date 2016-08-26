import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

names = ['Bob','Jessica','Mary','John','Mel']

random.seed(500)

random_names=[names[random.randint(low=0,high=len(names))] for i in range(1000)]

#print (random_names)

# print the first 10 records
#print (random_names[:10])

births =[random.randint(low=0,high=1000) for i in range(1000)]

# print the first 10 records
#print (births[:10])

## Merge the dataset

BabyDataSet=list(zip(random_names,births))
#print (BabyDataSet[:10])

df=pd.DataFrame(data=BabyDataSet,columns=['Names','Births'])
#print (df[:10])


## Write data to csv file
df.to_csv('BirthRecords1901',header=False,index=None)

## read the data from csv
df=pd.read_csv('BirthRecords1901',header=None)
#print (df.info)

print (df.head)



