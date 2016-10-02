import pandas as pd
import numpy as np
from  sklearn.preprocessing import OneHotEncoder, LabelEncoder

## Create a Data Frame using python Pandas
df=pd.DataFrame([
    ['green','M','10.1','Class1'],
    ['red','L','13.5','Class2'],
    ['blue','XL','15.3','Class3'],
    ['type 2','XL','15.3','Class3'],
])
## Define the columns of the Data Frame
df.columns=['color','size','price','classlabel']
print (df)

## Create a Disctionary to map the size to integer values
size_mappings ={'XL':3,'L':2,'M':1}
print (size_mappings)
## Create a Disctionary to inverse map the interger value of size to categorical values
inverse_size_mappings ={v :k for k,v in size_mappings.items()}
print ("Hello ",inverse_size_mappings)
print ("MAPPING ORDINAL FEATURES TO INTEGER VALUES")
## map the categroeical Size to integer.
df['size']=df['size'].map(size_mappings)
print (df)

print ("ENCODING CLASS LABELS TO INTEGER")
class_mapping ={label:idx for idx, label in enumerate(np.unique(df['classlabel']))}
print (class_mapping)
df['classlabel']=df['classlabel'].map(class_mapping)
print (df)


print ("PERFORM ONE-HOT CODING ON NOMINAL FEATURES")
x=df.values
color_le=LabelEncoder()
print ('aaaaa',x[:,0])
print("Before OHE "+'\n',x)

x[:,0]=color_le.fit_transform(x[:,0])
ohe= OneHotEncoder(categorical_features=[0])
x=ohe.fit_transform(x).toarray()
print ("aftrer OHE"+'\n',x)

print ("Generate Dummy columns using One-Hot Coding",'\n',pd.get_dummies(df[['color','size','price']]))
