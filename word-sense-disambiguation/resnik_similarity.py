# Olga Redko

import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from nltk.corpus.reader.wordnet import information_content
brown_ic = wordnet_ic.ic('ic-brown-resnik-add1.dat')

def resnik_similarity(word1, word2):
    synset1noun = wn.synsets(word1, pos=wn.NOUN)
    synset2noun = wn.synsets(word2, pos=wn.NOUN)

    highest_sim_score = 0
    sim_score = 0
    for syn1n in synset1noun:
        for syn2n in synset2noun:
            common_hypernyms = syn1n.common_hypernyms(syn2n)
            for hypernym in common_hypernyms:
                sim_score = information_content(hypernym, brown_ic)
                if sim_score > highest_sim_score:
                    highest_sim_score = sim_score
    return highest_sim_score

print(resnik_similarity('dog', 'cat'))

