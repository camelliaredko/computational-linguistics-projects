Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> wood = '<s> How much wood would a wood chuck chuck if a wood chuck could chuck wood ? </s> <s> As much wood as a wood chuck could if a wood chuck could chuck wood . </s>'
>>> w2grams = nltk.bigrams(wood.split())
>>> w2gramfd = nltk.FreqDist(w2grams)
>>> w1gramfd = nltk.FreqDist(wood.split())
>>> for bigram in w2gramfd.most_common():
	for unigram in w1gramfd.most_common():
		if bigram[0][0] == unigram[0]:
			print(bigram[0])
			print(bigram[1]/unigram[1])

			
('a', 'wood')
1.0
('wood', 'chuck')
0.5
('chuck', 'could')
0.42857142857142855
('much', 'wood')
1.0
('if', 'a')
1.0
('could', 'chuck')
0.6666666666666666
('chuck', 'wood')
0.2857142857142857
('<s>', 'How')
0.5
('How', 'much')
1.0
('wood', 'would')
0.125
('would', 'a')
1.0
('chuck', 'chuck')
0.14285714285714285
('chuck', 'if')
0.14285714285714285
('wood', '?')
0.125
('?', '</s>')
1.0
('</s>', '<s>')
0.5
('<s>', 'As')
0.5
('As', 'much')
1.0
('wood', 'as')
0.125
('as', 'a')
1.0
('could', 'if')
0.3333333333333333
('wood', '.')
0.125
('.', '</s>')
1.0
>>> sentence_list = ['<s> How much wood . </s>', '<s> How much wood ? </s>', '<s> As much wood chuck chuck chuck wood . </s> ', '<s> How would a wood chuck chuck ? </s> ']
>>> sentence_list_2grams = []
>>> for sentence in sentence_list:
	ws2grams_list = list(nltk.bigrams(sentence.split()))
	sentence_list_2grams.append(ws2grams_list)

	
>>> w2gram_probability = 1
>>> for sentence in sentence_list_2grams:
	for bigram in sentence:
		for unigram in w1gramfd.most_common():
			if bigram[0] == unigram[0]:
				w2gram_probability = w2gramfd[bigram]/unigram[1] * w2gram_probability
	print(sentence)
	print(w2gram_probability)
	w2gram_probability = 1

	
[('<s>', 'How'), ('How', 'much'), ('much', 'wood'), ('wood', '.'), ('.', '</s>')]
0.0625
[('<s>', 'How'), ('How', 'much'), ('much', 'wood'), ('wood', '?'), ('?', '</s>')]
0.0625
[('<s>', 'As'), ('As', 'much'), ('much', 'wood'), ('wood', 'chuck'), ('chuck', 'chuck'), ('chuck', 'chuck'), ('chuck', 'wood'), ('wood', '.'), ('.', '</s>')]
0.0001822157434402332
[('<s>', 'How'), ('How', 'would'), ('would', 'a'), ('a', 'wood'), ('wood', 'chuck'), ('chuck', 'chuck'), ('chuck', '?'), ('?', '</s>')]
0.0
>>> 
