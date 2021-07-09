Olga Redko
2/10/2020

Python 3.6.8 (default, Oct  7 2019, 12:59:55)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.corpus import movie_reviews
>>> movie_reviews.words()
['plot', ':', 'two', 'teen', 'couples', 'go', 'to', ...]
>>> len(movie_reviews.words())  # number of words
1583820
>>> len(movie_reviews.fileids())  # number of fileids
2000
>>> len(movie_reviews.raw())  #number of raw
7786004
>>> movie_reviews.fileids()

>>> movie_reviews.raw()

movie_reviews
>>> movie_reviews.categories()
['neg', 'pos']
>>> print(len(movie_reviews.fileids('pos')))  # number of pos reviews
1000
>>> print(len(movie_reviews.fileids('neg')))  # number of neg reviews
1000
>>> documents = [(list(movie_reviews.words(fileid)), category)  # label documents with appropriate categories
		 for category in movie_reviews.categories()
		 for fileid in movie_reviews.fileids(category)]

>>> documents[0]


>>> documents[0][1]
'neg'
>>> documents[0][0]

>>> import random
>>> random.shuffle(documents)  # shuffle documents order randomly
>>> all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
>>> word_features = [w for (w,f) in all_words.most_common(2000)]
>>> myreview = """Mr. Matt Damon was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."""
>>> myreview_toks = nltk.word_tokenize(myreview.lower())  # lowercase, and then tokenize
>>> myreview_toks
['mr.', 'matt', 'damon', 'was', 'outstanding', ',', 'fantastic', ',', 'excellent', ',', 'wonderfully', 'subtle', ',', 'superb', ',', 'terrific', ',', 'and', 'memorable', 'in', 'his', 'portrayal', 'of', 'mulan', '.']
>>> def document_features(document):  # feature extractor so the classifier knows which aspects of the data to pay attention to
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains({})'.format(word)] = (word in document_words)
	return features

>>> myreview_feats = document_features(myreview_toks)     # generate word feature dictionary
>>> featuresets = [(document_features(d), c) for (d,c) in documents]
>>> train_set, test_set = featuresets[100:], featuresets[:100]
>>> classifier = nltk.NaiveBayesClassifier.train(train_set)
>>> classifier.classify(myreview_feats)    # classify
'pos'
>>> classifier.prob_classify(myreview_feats).prob('pos')  # probability of 'pos' label
0.9776834274330332
>>> classifier.prob_classify(myreview_feats).prob('neg')  # probability of 'neg' label
0.02231657256700326
>>> myreview_feats.items()

>>> myreview2 = """Mr. Steve Seagal was outstanding, fantastic, excellent, wonderfully subtle, superb, terrific, and memorable in his portrayal of Mulan."""
>>> myreview2_toks = nltk.word_tokenize(myreview2.lower())  # lowercase, and then tokenize
>>> myreview2_toks
['mr.', 'steve', 'seagal', 'was', 'outstanding', ',', 'fantastic', ',', 'excellent', ',', 'wonderfully', 'subtle', ',', 'superb', ',', 'terrific', ',', 'and', 'memorable', 'in', 'his', 'portrayal', 'of', 'mulan', '.']
>>> myreview2_feats = document_features(myreview2_toks)     # generate word feature dictionary
>>> classifier.classify(myreview2_feats)    # classify
'neg'
>>> classifier.prob_classify(myreview2_feats).prob('pos')  # probability of 'pos' label
0.24022959858142634
>>> classifier.prob_classify(myreview2_feats).prob('neg')  # probability of 'neg' label
0.7597704014185692
>>> myreview2_feats

>>> myreview3 = "Mr. Matt Damon was outstanding, fantastic."
>>> myreview3_toks = nltk.word_tokenize(myreview3.lower())  # lowercase, and then tokenize
>>> myreview3_toks
['mr.', 'matt', 'damon', 'was', 'outstanding', ',', 'fantastic', '.']
>>> myreview3_feats = document_features(myreview3_toks)     # generate word feature dictionary
>>> classifier.classify(myreview3_feats)     # classify
'neg'
>>> classifier.prob_classify(myreview3_feats).prob('pos')  # probability of 'pos' label
2.7479759451209218e-05
>>> classifier.prob_classify(myreview3_feats).prob('neg')  # probability of 'neg' label
0.9999725202405724
>>> classifier.prob_classify(myreview_feats).prob('neg')  # probability of 'neg' label
0.02231657256700326
>>> 
