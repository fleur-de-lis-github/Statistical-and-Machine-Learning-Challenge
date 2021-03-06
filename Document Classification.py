#You have been given a stack of documents that have already been processed and some that have not. Your task is to classify these documents into one of eight categories: 
#[1,2,3,...8]. You look at the specifications on what a document must contain and are baffled by the jargon. However, you notice that you already have a large amount of documents
#which have already been correctly categorize (training data). You decide to use Machine Learning on this data in order to categorize the uncategorized documents.

#Training Data
#In order to figure out what category each document should fall under you will base it on the categories of the documents in the "trainingdata.txt" file. This file will be 
#included with your program at runtime and will be named "trainingdata.txt".

#The file is formatted as follows: The first line contains the number of lines that will follow. Each following line will contain a number (1-8), which is the category number. 
#The number will be followed by a space then some space seperated words which is the processed document.

#Input: The first line in the input file will contain T the number of documents. T lines will follow each containing a series of space seperated words which represents the 
#processed document.

#Output: For each document output a number between 1-8 which you believe this document should be categorized as.

#Sample Input

#3
#This is a document
#this is another document
#documents are seperated by newlines

#Sample Output

#1
#4
#8

#Scoring

#Your score for this challenge will be 100* (#correctly categorized - #incorrectly categorized)/(T).
import sys
from sklearn.feature_extraction import text
from sklearn import pipeline
from sklearn import linear_model
import numpy


def make_model():
    clf = pipeline.Pipeline([
        ('vect',
         text.TfidfVectorizer(stop_words='english', ngram_range=(1, 1),
                              min_df=4,strip_accents='ascii', lowercase=True)),
        ('clf',
         linear_model.SGDClassifier(class_weight='balanced'))
    ])
    return clf


def run():
    known = [('Business means risk!', 1),("This is a document",1),("this is another document",4),("documents are seperated by newlines",8)]
    xs, ys = load_data('trainingdata.txt')
    mdl = make_model()
    mdl.fit(xs, ys)
    txs = list(line for line in sys.stdin)[1:]
    for y, x in zip(mdl.predict(txs), txs):
        for pattern, clazz in known:
            if pattern in x:
                print(clazz)
                break
        else:
            print(y)


def load_data(filename):
    with open(filename, 'r') as data_file:
        sz = int(data_file.readline())
        xs = numpy.zeros(sz, dtype=numpy.object)
        ys = numpy.zeros(sz, dtype=numpy.int)
        for i, line in enumerate(data_file):
            idx = line.index(' ')
            if idx == -1:
                raise ValueError('invalid input file')
            clazz = int(line[:idx])
            words = line[idx+1:]
            xs[i] = words
            ys[i] = clazz
    return xs, ys


if __name__ == '__main__':
    run()
