"""
Data Source : http://ai.stanford.edu/~amaas/data/sentiment/

NLTK Book : http://www.nltk.org/book
"""
import numpy as np
import pyprind
import pandas as pd
import os
import re
import nltk
nltk.download('stopwords')
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

pbar = pyprind.ProgBar(50000)
labels ={'pos':1, 'neg':0}

df=pd.DataFrame()
# for s in ('test','train'):
#     for l in ('pos','neg'):
#         path='input/aclImdb/%s/%s' %(s,l)
#         #print(path)
#         for file in os.listdir(path):
#             #print (file)
#              with open(os.path.join(path,file),encoding='utf8') as infile:
#                  #print (file)
#                  txt=infile.read()
#                  df=df.append([[txt,labels[l]]],ignore_index=True)
#                  pbar.update()
#
# df.columns=['Reviews','Sentiment']
#
# np.random.seed(0)
# df=df.reindex(np.random.permutation(df.index))
# df.to_csv('input/movie_data.csv',index=False)

df=pd.read_csv('input/movie_data.csv',encoding='iso-8859-1')

def preprocessor(text):
    text=re.sub('<[^>]*>','',text)
    emoticons=re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)',text)
    text=re.sub('[\W]+',' ',text.lower())+ '/'.join(emoticons).replace('-','')
    return text

def tokenizer(text):
    return text.split()




def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split() ]

F='running like running like anything whats'
print(tokenizer_porter(F))

stop=stopwords.words('english')
array=[w for w in tokenizer_porter(F) if w not in stop]

print (array)

#print(preprocessor(df.loc[0,'Reviews'][-50:]))

#print(df.columns)

df['Reviews']=df['Reviews'].apply(preprocessor)

#print (df['Reviews'])

#print(tokenizer('running like running and thus they run'))

#print(preprocessor())
