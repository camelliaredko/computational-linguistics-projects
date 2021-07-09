# Olga Redko

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus.reader.wordnet import information_content
import os

information_content_file = wordnet_ic.ic('ic-brown-resnik-add1.dat')
wsd_test_file = open(os.path.join(os.getcwd(), 'wsd_contexts.txt'))
wsd_gold_file = open(os.path.join(os.getcwd(), 'wsd_contexts.txt.gold.txt'))
results = open("results.out", "w")

def resnik_similarity(word1, word2):
    synset1noun = wn.synsets(word1, pos=wn.NOUN)
    synset2noun = wn.synsets(word2, pos=wn.NOUN)
    highest_sim_score = 0

    for syn1n in synset1noun:
        for syn2n in synset2noun:
            common_hypernyms = syn1n.common_hypernyms(syn2n)
            for hypernym in common_hypernyms:
                sim_score = information_content(hypernym, information_content_file)
                if sim_score > highest_sim_score:
                    highest_sim_score = sim_score
    result = highest_sim_score
    return result

for line in wsd_test_file.readlines():
    word = line.split("\t")[0].replace(" ", "")
    contexts = line.split("\t")[1]
    synsetID = wsd_gold_file.readline().split(".")[1][:2].replace(" ", "")
    for context_word in contexts.split(","):
        context_word = context_word.replace("\n", "")
        resnik_result = resnik_similarity(word, context_word)
        similarity_score = resnik_result
        #print(word + "," + context_word + "," + str(similarity_score))
        #print(synsetID)
        results.write(word + "," + context_word + "," + str(similarity_score) + "\n")
        results.write(synsetID + "\n")


wsd_test_file.close()
wsd_gold_file.close()
results.close()