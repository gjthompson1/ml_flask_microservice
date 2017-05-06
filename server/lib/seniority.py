import numpy as np

from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

from constants import *

seniority_clf = None

categories_to_token = {SENIORITY_CATEGORIES_NEW[i]:i for i in range(0,len(SENIORITY_CATEGORIES_NEW))}
token_to_categories = {v: k for k, v in categories_to_token.iteritems()}

def initialize_models():
    global seniority_clf
    model_data = joblib.load('models/dist/seniority_clf.sk')
    seniority_clf = model_data.get('seniority_clf')

def predit_one_abs(name):
    predicted = seniority_clf.predict(np.array([name]))
    return token_to_categories[predicted[0]]

def predict_one_proba(name):
    predicted = seniority_clf.predict_proba(np.array([name]))
    predicted_dict = dict(zip([token_to_categories[x] for x in seniority_clf.classes_], predicted[0]))
    return predicted_dict
