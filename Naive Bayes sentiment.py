# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:44:17 2018

@author: hp
"""

# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset from the working directory
#Differentiating review from sentiment using tabs & removing quotes
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3)

# Cleaning the texts
#Importing word processing libraries
import re
import nltk
#Downloading stopwords
nltk.download('stopwords')
#Importing stopwords from nltk
from nltk.corpus import stopwords
#Importing stemmer class
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1000):
    #Using regex so that data contains only alphabets
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    #Converting all alphabets to lower case
    review = review.lower()
    #Spliting review sentences into list of words
    review = review.split()
    #Stemmer object
    ps = PorterStemmer()
    #Choosing only words which are in english and also NOT included in the stopwords package
    #Using set of dataset words for faster processing
    #Applying stemming to all the words in the review set 
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    #Re-joining the list of words
    review = ' '.join(review)
    corpus.append(review)


# Creating the Bag of Words model

#Tokenizing the corpus
from sklearn.feature_extraction.text import CountVectorizer
#Using default parameters
cv = CountVectorizer()
#Fitting the corpus into variables 
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
#Keeping 20% of dataset for prediction

 
#NAIVE BAYES

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

#from sklearn.naive_bayes import MultinomialNB
#classifier = MultinomialNB()

classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

#Calculating the accuracy
from sklearn import metrics
asc = metrics.accuracy_score(y_test, y_pred)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)



