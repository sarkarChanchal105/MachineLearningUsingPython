import numpy as np
from sklearn.feature_extraction.text import CountVectorizer ,TfidfTransformer


tfidf=TfidfTransformer()
count=CountVectorizer()

np.set_printoptions(precision=2)

# docs=np.array(['The sun is Shinning',
#                'The weather1 is sweet',
#                'I want you weather2'
#
#                ])

docs=np.array(['The sun is Shinning',
                ])


bag=count.fit_transform(docs)

print(count.vocabulary_)
print(bag.toarray())
print(tfidf.fit_transform(count.fit_transform(docs)).toarray())