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
from sklearn.cross_validation import train_test_split,StratifiedKFold,cross_val_score
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.grid_search import  GridSearchCV
from sklearn.pipeline import  Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer


df=pd.read_csv('input/movie_data.csv',encoding='iso-8859-1')

df.columns=['Reviews','Sentiment']

x_train,y_train,x_test,y_test=train_test_split(df['Reviews'].values,df['Sentiment'].values,test_size=0.5,random_state=0)


tfidf = TfidfVectorizer(strip_accents=None,lowercase=False,preprocessor=None)

def tokenizer(text):
    return text.split()

porter = PorterStemmer()
def tokenizer_porter(text):
    return [porter.stem(word) for word in text.split() ]


stop=stopwords.words('english')
param_grid=[{'vect__ngram_range' :[(1,1)],
             'vect__stop_words':[stop,None],
             'vect__tokenizer': [tokenizer,tokenizer_porter],
             },
    {

    },
    {

    }



]