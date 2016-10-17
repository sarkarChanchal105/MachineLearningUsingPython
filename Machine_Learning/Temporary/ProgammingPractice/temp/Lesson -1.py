import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt

######### Create data set and import that data set into Panda
names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names,births))
print (BabyDataSet)
df =pd.DataFrame(data=BabyDataSet,columns=('Name','Births'))
print (df)

######### Write the DataSet to a CSV file
df.to_csv('BirthRecords',index=False,header=False)

######### Read the DataSet from a CSV file
df=pd.read_csv(r'BirthRecords',header=None,names=['Names','Births'])

##### Sort the dataset based on the values of Births
sorted = df.sort_values(['Births'],ascending=False)
print (sorted.head(1))
print (df['Births'].max())


##### Present the data ####
df['Births'].plot()
maxValue=df['Births'].max()
maxName=df['Names'][df['Births']==df['Births'].max()].values
Text=str(maxValue)+ " " + maxName
plt.annotate(Text, xy=(1, maxValue), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
print("The most popular name")
df[df['Births'] == df['Births'].max()]

plt.show()




