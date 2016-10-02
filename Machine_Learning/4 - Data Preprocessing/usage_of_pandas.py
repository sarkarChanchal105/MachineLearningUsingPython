import pandas as pd

from io import StringIO
csv_data = '''A,B,C,D
1,2,3,4
5,6,,8
10,11,12,'''

df =pd.read_csv(StringIO(csv_data)) ## Read the data into a Pandas data frame
#print (df)

print (df.isnull().sum()) ## check the number of  null fields in earch row
# print(df.dropna()) ## remove the rows that have null values
#
# print(df.dropna(axis=1)) ## drop the columns that has atleast one NAN

k=df.isnull().sum()

for c,field in zip(k,df.columns):
    print (c,field)
    #print (k[2])
