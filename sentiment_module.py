import nltk

from nltk.corpus import stopwords
import random
import pickle
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB , BernoulliNB
from sklearn.linear_model import LogisticRegression , SGDClassifier
from sklearn.svm import SVC , LinearSVC , NuSVC


from nltk.classify import ClassifierI
from statistics import mode

import io

class VoteClassifier(ClassifierI):
    def __init__(self , *classifiers):
        self._classifiers = classifiers
        
    def classify(self , features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
    
    def confidence(self , features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
    
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf 


#j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]


documents = []
all_words = []
# # pos_f = open("short_reviews/positive.txt","r")
# pos_reviews = open("short_reviews/positive.txt","r").read()
# # pos_f.close()
# neg_f = open("short_reviews/negative.txt","r")
# neg_reviews = neg_f.read()
# neg_f.close()

# pos_f = io.open("short_reviews/positive.txt", encoding='latin-1')
# pos_reviews = pos_f.read()
# neg_f = io.open("short_reviews/negative.txt", encoding='latin-1')
# neg_reviews = neg_f.read()

# for pos_review in pos_reviews.split('\n'):
#     documents.append((pos_review,"pos"))
#     words = word_tokenize(pos_review)
#     words = nltk.pos_tag(words)
#     for word in words:
#         if word[1][0] in allowed_word_types:#string indexing 0
#             all_words.append(word[0].lower())

# for neg_review in neg_reviews.split('\n'):
#     documents.append((neg_review,"neg"))
#     words = word_tokenize(neg_review)
#     words = nltk.pos_tag(words)
#     for word in words:
#         if word[1][0] in allowed_word_types:#string indexing 0
#             all_words.append(word[0].lower())


# print("no of reviews " , len(documents))

# random.shuffle(documents)

# print(all_words[:15])


# all_words = nltk.FreqDist(all_words)
# # print(list(all_words.keys())[:15])
# # print(list(all_words.values())[:15])
# print(all_words.most_common(15))
# print()

# word_features = []

# for tup in  all_words.most_common(5000):
#     word_features.append(tup[0])

word_features_f = open("pickledalgos/word_features.pickle","rb")
word_features = pickle.load(word_features_f)
word_features_f.close()

def find_features(document):
    document = nltk.word_tokenize(document)
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
        
    return features

# featuresets = [(find_features(document),category) for (document,category) in documents]

featuresets_f = open("pickledalgos/featuresets.pickle","rb")
featuresets = pickle.load(featuresets_f)
featuresets_f.close()


# set that we'll train our classifier with
training_set = featuresets[:10000]

# set that we'll test against. 100
testing_set = featuresets[10000:]

# classifier = nltk.NaiveBayesClassifier.train(training_set)




# classifier_f = open("pickledalgos/naivebayesclassifiernew.pickle","wb")
# pickle.dump(classifier , classifier_f) 
# classifier_f.close()

classifier_f = open("pickledalgos/naivebayesclassifiernew.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()


# print("Naive classifier acc % : " , (nltk.classify.accuracy(classifier,testing_set))*100)
# classifier.show_most_informative_features(15)

# MNB_classifier = SklearnClassifier(MultinomialNB())
# MNB_classifier.train(training_set)
# print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

MNB_classifier_f = open("pickledalgos/MNB_classifier.pickle","rb")
MNB_classifier = pickle.load( MNB_classifier_f) 
MNB_classifier_f.close()

# BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
# BernoulliNB_classifier.train(training_set)
# print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

BernoulliNB_classifier_f = open("pickledalgos/BernoulliNB_classifier.pickle","rb")
BernoulliNB_classifier  = pickle.load(BernoulliNB_classifier_f) 
BernoulliNB_classifier_f.close()

# LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
# LogisticRegression_classifier.train(training_set)
# print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

LogisticRegression_classifier_f = open("pickledalgos/LogisticRegression_classifier.pickle","rb")
LogisticRegression_classifier = pickle.load(LogisticRegression_classifier_f) 
LogisticRegression_classifier_f.close()

# SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
# SGDClassifier_classifier.train(training_set)
# print("SGDClassifier_classifier accuracy percent:", (nltk.classify.accuracy(SGDClassifier_classifier, testing_set))*100)

SGDClassifier_classifier_f = open("pickledalgos/SGDClassifier_classifier.pickle","rb")
SGDClassifier_classifier = pickle.load(SGDClassifier_classifier_f) 
SGDClassifier_classifier_f.close()

# LinearSVC_classifier = SklearnClassifier(LinearSVC())
# LinearSVC_classifier.train(training_set)
# print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

LinearSVC_classifier_f = open("pickledalgos/LinearSVC_classifier.pickle","rb")
LinearSVC_classifier = pickle.load(LinearSVC_classifier_f) 
LinearSVC_classifier_f.close()

# NuSVC_classifier = SklearnClassifier(NuSVC())
# NuSVC_classifier.train(training_set)
# print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

NuSVC_classifier_f = open("pickledalgos/NuSVC_classifier.pickle","rb")
NuSVC_classifier = pickle.load(NuSVC_classifier_f) 
NuSVC_classifier_f.close()

voted_classifier = VoteClassifier(classifier, 
                                  NuSVC_classifier,
                                  LinearSVC_classifier,
                                  SGDClassifier_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)

# print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

# print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[100][0]), "Confidence %:",voted_classifier.confidence(testing_set[100][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[500][0]), "Confidence %:",voted_classifier.confidence(testing_set[500][0])*100)


def sentiment(text):
    feature = find_features(text)
    return voted_classifier.classify(feature),voted_classifier.confidence(feature) 

