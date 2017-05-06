import numpy as np

from sklearn.externals import joblib
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib

from constants import *

role_clf = None

categories_to_token = {ROLE_CATEGORIES_NEW[i]:i for i in range(0,len(ROLE_CATEGORIES_NEW))}
token_to_categories = {v: k for k, v in categories_to_token.iteritems()}

def initialize_models():
    global role_clf
    model_data = joblib.load('models/dist/role_clf.sk')
    role_clf = model_data.get('role_clf')

def predit_one_abs(name):
    predicted = role_clf.predict(np.array([name]))
    return token_to_categories[predicted[0]]

def predict_one_proba(name):
    predicted = role_clf.predict_proba(np.array([name]))
    predicted_dict = dict(zip([token_to_categories[x] for x in role_clf.classes_], predicted[0]))
    return predicted_dict
