from io import StringIO
import pandas as pd
from sklearn.preprocessing import Imputer
csv_data = '''A,B,C,D
1,2,3,4
5,6,,8
10,11,12,'''

df =pd.read_csv(StringIO(csv_data)) ## Read the data into a Pandas data frame

print ("Data frame before imputing "+'\n',df)

imputer= Imputer(missing_values='NaN',strategy='mean',axis=1)
imputer =imputer.fit(df)
df=imputer.transform(df.values)
print ("Data frame after imputing ",'\n',df)


