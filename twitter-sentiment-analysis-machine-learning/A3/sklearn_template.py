from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
import numpy as np
import pandas
import csv


def test_classifier(X_train, y_train, X_test, y_test, classifier):
    from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
    print("")
    print("=======================================================")
    classifier_name = str(type(classifier).__name__)
    print("Testing " + classifier_name)

    model = classifier.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("=================== Results ===========================")
    print(confusion_matrix(y_test, predictions))
    print(classification_report(y_test, predictions))
    print(accuracy_score(y_test, predictions))
    print("=======================================================")

    print(
        "Number of mislabeled points out of a total %d points : %d" % (X_test.shape[0], (y_test != predictions).sum()))
    return


def select_features(X, y):
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    import operator

    #skb = SelectKBest(chi2, k=5)
    skb = SelectKBest(chi2, k=10)
    skb.fit_transform(X, y)

    support = skb.get_support()

    n = 1
    features = dict()

    for col_name, score in zip(X.columns.values[support], skb.scores_[support]):
        features[col_name] = score

    for feature, score in sorted(features.items(), key=operator.itemgetter(1), reverse=True):
        print("%d. %s %.2f" % (n, feature, score))
        n += 1

    print(X.columns.values[support])

    return


## Read the comma-separated tweet data with headers
# X = pandas.read_csv('tweets.csv',sep=',')
X = pandas.read_csv(r'/home/olgaredko/Desktop/assignment-3-twitter-sentiment-oredko-master/A3/all_tweets_3.1.csv', sep=',')

## Shuffle the tweets, which are sorted by sentiment in the original file 
X = shuffle(X, random_state=0)

## Remove the last column and save it in y
y = X.pop('Sentiment').values

## Print the first few lines and a summary of the training file
print(X.head())
print(X.shape)

## Split the data into training and test sets. Adjust the test_size parameter to change
## the split percentage
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

## ADD REMAINING CODE HERE

# 3.1:
#print(test_classifier(X_train, y_train, X_test, y_test, svm.SVC()))
#print(test_classifier(X_train, y_train, X_test, y_test, GaussianNB()))
print(test_classifier(X_train, y_train, X_test, y_test, LogisticRegression()))
#print(test_classifier(X_train, y_train, X_test, y_test, RandomForestClassifier()))


# 3.2, 3.3:
row_count = 999
while row_count < 11000:
    X_train, X_test, y_train, y_test = train_test_split(X[0:row_count], y[0:row_count], test_size=0.5, random_state=0)
    print("*******************************************************")
    print("Results for the first " + str((row_count + 1) / 2) + " rows trained: ")
    select_features(X_train, y_train)
    print(test_classifier(X_train, y_train, X_test, y_test, LogisticRegression()))
    row_count += 1000

