from __future__ import division
import numpy as np
from nltk.corpus import stopwords
import re
stoplist = set(stopwords.words('english'))

path='/Users/salilnavgire/Downloads/new_sentiment/module/vectors/'
labels = np.load(str(path)+'labels.npy')
pi = np.load(str(path)+'pi.npy')
theta = np.load(str(path)+'theta.npy')
searchidf = np.load(str(path)+'searchidf.npy')
feature_names = np.load(str(path)+'feature_names.npy')


def review_clean(raw_review, stoplist):
    letters_only = re.sub("[^a-zA-Z]", " ", raw_review)
    words = letters_only.lower().split()
    meaningful_words = [w for w in words if not w in stoplist]
    return ' '.join(meaningful_words)


def generate_ngrams(review, stoplist):
    word = review_clean(review, stoplist)
    ulist = word.split(' ')
    nlist = zip(ulist, ulist[1:]) + zip(ulist, ulist[1:], ulist[2:])
    for res in nlist:
        ulist.append(' '.join(sorted(res)))
    return ulist


def vector_similarity(ulist, searchidf, feature_names):
    vector = np.zeros(len(feature_names))
    for i in xrange(len(ulist)):
        try:
            vector[feature_names.tolist().index(ulist[i])] += 1
        except ValueError:
            pass
    feature_vector = (np.transpose(vector)*searchidf)
    return feature_vector


def sentiment_score(pi, theta, labels, feature_vector):
    results = (pi + np.dot(feature_vector, np.transpose(theta)))
    final = results - min(results)
    return np.dot((final/sum(final)), labels)

'''
def sentiment_score_3(pi, theta, labels, feature_vector):
    results = (pi + np.dot(feature_vector, np.transpose(theta)))
    final = results - min(results)
    #mul = (final/sum(final)) * labels
    probabilities = np.argsort(final/sum(final))
    mul = 0
    for i in range(3):
        mul +=
'''

def score(review):
    ulist = generate_ngrams(review, stoplist)

    feature_vector = vector_similarity(ulist, searchidf, feature_names)

    return sentiment_score(pi, theta, labels, feature_vector)
