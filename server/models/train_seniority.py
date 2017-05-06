import sys
sys.path.append('..')

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

from sklearn import metrics

from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

from lib.constants import *

categories_to_token = {SENIORITY_CATEGORIES_NEW[i]:i for i in range(0,len(SENIORITY_CATEGORIES_NEW))}
token_to_categories = {v: k for k, v in categories_to_token.iteritems()}

df = pd.read_csv('../data/titles.csv')
df['title'] = df['title'].apply(lambda x : unicode(x,errors='ignore'))
df['target'] = df['seniority_new'].apply(lambda x: categories_to_token[str(x)])

# clf = Pipeline([('vect', CountVectorizer(ngram_range=(1, 3))),('clf', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, n_iter=5, random_state=42))])
clf = Pipeline([('vect', CountVectorizer()),('clf', MultinomialNB())])
clf = clf.fit(np.array(df['title']), np.array(df['target']))

model_data = {}
model_data['seniority_clf'] = clf
joblib.dump(model_data,'dist/seniority_clf.sk',compress=9)

## TESTING ##
# predicted = clf.predict(np.array(test['title']))
# np.mean(predicted == np.array(test['target']))
#
# print metrics.classification_report(np.array(test['target']), predicted,target_names=SENIORITY_CATEGORIES_NEW)
# print metrics.confusion_matrix(np.array(test['target']), predicted)
