# YOUR NAME HERE: Olga Redko
# ASSN 02: "Who Said It?"


### Some STEPs are already COMPLETE.
### Commands you need to EDIT are marked as such.
###   <-- They are shown as empty lists/None object/0.0, etc.
###    <-- so that the script can be run without breaking.

import nltk, random

#------------------------------------------------ STEP 1 (COMPLETE)
print("1. Loading Austen and Melville sentences...")
a_sents_all = nltk.corpus.gutenberg.sents('austen-emma.txt')
m_sents_all = nltk.corpus.gutenberg.sents('melville-moby_dick.txt')

#------------------------------------------------ STEP 2
print("2. Discarding short sentences and labeling...")
a_sents = [(s, 'austen') for s in a_sents_all if len(s)>2]
m_sents = [(s2, 'melville') for s2 in m_sents_all if len(s2)>2]    # EDIT

#------------------------------------------------ STEP 3
print("3. Joining the two author sentence lists...")
sents = a_sents + m_sents      # EDIT

#------------------------------------------------ STEP 4 (COMPLETE)
print("4. Sentence stats:")
print(" # of total sentences:", len(sents))
print(" # of Austen sentences:", len(a_sents))
print(" # of Melville sentences:", len(m_sents))

#------------------------------------------------ STEP 5
print("5. Shuffling...")
# EDIT -- shuffle sents here
random.Random(10).shuffle(sents) # random seed
# random.shuffle(sents) # alternative random that's not a seed

#------------------------------------------------ STEP 6
print("6. Partitioning...")
test_sents = sents[:1000]     # EDIT
devtest_sents = sents[1000:2000]  # EDIT
train_sents = sents[2000:]    # EDIT

print(" # of test sentences:", len(test_sents))
print(" # of devtest sentences:", len(devtest_sents))
print(" # of training sentences:", len(train_sents))

#------------------------------------------------ STEP 7 (COMPLETE)
print("7. Defining a feature-generator function...")
mainchars = {'Emma', 'Harriet', 'Ahab', 'Weston', 'Knightley', 'Elton',
             'Woodhouse', 'Jane', 'Stubb', 'Queequeg', 'Fairfax', 'Churchill',
             'Frank', 'Starbuck', 'Pequod', 'Hartfield', 'Bates', 'Highbury',
             'Perry', 'Bildad', 'Peleg', 'Pip', 'Cole', 'Goddard',
             'Campbell', 'Donwell', 'Dixon', 'Taylor', 'Tashtego'}

noCharNames = False    # For [PART B] Q3
if noCharNames :
    print('NOTE: Top 35 proper nouns have been neutralized.')

def gen_feats(sent):
    featdict = {}
    for w in sent:
        if noCharNames == True:
            if w in mainchars: w = 'MontyPython'
        featdict['contains-'+w.lower()] = 1
    return featdict

#------------------------------------------------ STEP 8
print("8. Generating feature sets...")
test_feats = [(gen_feats(d), c) for (d,c) in test_sents]     # EDIT
devtest_feats = [(gen_feats(d), c) for (d,c) in devtest_sents]  # EDIT
train_feats = [(gen_feats(d), c) for (d,c) in train_sents]    # EDIT

#------------------------------------------------ STEP 9
print("9. Training...")
whosaid = nltk.NaiveBayesClassifier.train(train_feats)      # EDIT

#------------------------------------------------ STEP 10
print("10. Testing...")
accuracy = nltk.classify.accuracy(whosaid, test_feats)      # EDIT
print(" Accuracy score:", accuracy)

#------------------------------------------------ STEP 11
print("11. Sub-dividing development testing set...")
# aa: real author Austen, guessed Austen
# mm: real author Melville, guessed Melville
# am: real author Austen, guessed Melville
# ma: real author Melville, guessed Austen
aa, mm, am, ma = [], [], [], []
for (sent, auth) in devtest_sents:
    guess = whosaid.classify(gen_feats(sent))
    if auth == 'austen' and guess == 'austen':
        aa.append( (auth, guess, sent) )
    # EDIT below to populate mm, am, ma
    if auth == 'melville' and guess == 'melville':
        mm.append((auth, guess, sent))
    if auth == 'austen' and guess == 'melville':
        am.append((auth, guess, sent))
    if auth == 'melville' and guess == 'austen':
        ma.append((auth, guess, sent))

#------------------------------------------------ STEP 12
print("12. Sample CORRECT and INCORRECT predictions from dev-test set:")
print("-------")
for x in (aa, mm, am, ma):  # EDIT change (aa) to (aa, mm, am, ma)
    auth, guess, sent = random.choice(x)
    print('REAL=%-8s GUESS=%-8s' % (auth, guess))  # string formatting
    print(' '.join(sent))
    print("-------")
print()



#------------------------------------------------ STEP 13
print("13. Looking up 40 most informative features...")

# EDIT -- use .show_most_informative_feats_all()
whosaid.show_most_informative_features(40)
print()

#------------------------------------------------ Part B Additions
print("Part B Additions")
sent1toks = nltk.word_tokenize("Anne was to leave them on the morrow, an event which they all dreaded.")
sent2toks = nltk.word_tokenize("So Alice began telling them her adventures from the time when she first saw the White Rabbit.")

print('Guess for "Anne was to leave them on the morrow, an event which they all dreaded.": ')
print(whosaid.classify(gen_feats(sent1toks)))
print('Guess for "So Alice began telling them her adventures from the time when she first saw the White Rabbit.": ')
print(whosaid.classify(gen_feats(sent2toks)))
print()

sent1feats = gen_feats(sent1toks)
sent2feats = gen_feats(sent2toks)

print(whosaid.prob_classify(sent1feats).prob('austen'))
print(whosaid.prob_classify(sent1feats).prob('melville'))
print(whosaid.prob_classify(sent2feats).prob('austen'))
print(whosaid.prob_classify(sent2feats).prob('melville'))
print()

sent3toks = nltk.word_tokenize("He knows the truth")
sent4toks = nltk.word_tokenize("She knows the truth")
sent5toks = nltk.word_tokenize("blahblahblah blahblah")

sent3feats = gen_feats(sent3toks)
sent4feats = gen_feats(sent4toks)
sent5feats = gen_feats(sent5toks)

print(whosaid.classify(gen_feats(sent3toks)))
print(whosaid.classify(gen_feats(sent4toks)))
print(whosaid.classify(gen_feats(sent5toks)))

print(whosaid.prob_classify(sent3feats).prob('austen'))
print(whosaid.prob_classify(sent3feats).prob('melville'))

print(whosaid.prob_classify(sent4feats).prob('austen'))
print(whosaid.prob_classify(sent4feats).prob('melville'))

print(whosaid.prob_classify(sent5feats).prob('austen'))
print(whosaid.prob_classify(sent5feats).prob('melville'))
print()

austen_counter = 0
melville_counter = 0

for x in train_sents:
    if x[1] == 'austen':
        austen_counter += 1
    else:
        melville_counter += 1

print(austen_counter)
print(melville_counter)
print()

very_austen = 0
very_melville = 0

for v in train_sents:
    if ('very' in v[0] or 'Very' in v[0]) and v[1] == 'austen':
        very_austen += 1
    if ('very' in v[0] or 'Very' in v[0]) and v[1] == 'melville':
        very_melville += 1

print(very_austen)
print(very_melville)
print(very_austen/austen_counter)
print(very_melville/melville_counter)
print()

print(whosaid.feature_weights('contains-very', 1))
print()

print(whosaid.feature_weights('contains-whale', 1))
print(whosaid.feature_weights('contains-ahab', 1))
print(whosaid.feature_weights('contains-marriage', 1))
print(whosaid.feature_weights('contains-emma', 1))
print(whosaid.feature_weights('contains-bates', 1))
print(whosaid.feature_weights('contains-groom', 1))
print(whosaid.feature_weights('contains-cautiously', 1))
# print(whosaid.feature_weights('contains-internet', 1)) # produces an error

sent6toks = nltk.word_tokenize("She hates the internet")
sent7toks = nltk.word_tokenize("She hates the")
sent6feats = gen_feats(sent6toks)
sent7feats = gen_feats(sent7toks)
print(whosaid.prob_classify(sent6feats).prob('austen'))
print(whosaid.prob_classify(sent7feats).prob('austen'))
print()

print(whosaid.feature_weights('contains-he', 1))
print(whosaid.feature_weights('contains-knows', 1))
print(whosaid.feature_weights('contains-the', 1))
print(whosaid.feature_weights('contains-truth', 1))
print()

# aa: real author Austen, guessed Austen
# mm: real author Melville, guessed Melville
# am: real author Austen, guessed Melville
# ma: real author Melville, guessed Austen

print(len(aa) + len(mm))
print(nltk.classify.accuracy(whosaid, devtest_feats))
# print((len(aa) + len(mm)) / 1000) # alternative way to calculate accuracy for the development test data
print((len(aa) + len(ma))/1000)
print((len(mm) + len(am))/1000)
print(len(aa) / (len(aa) + len(ma)))
print(len(mm) / (len(mm) + len(am)))
print()

# for x in am: print(' '.join(x[2]))

for x in am:
    print(' '.join(x[2]))
    am_feats = gen_feats(x[2])
    print(whosaid.prob_classify(am_feats).prob('melville'))