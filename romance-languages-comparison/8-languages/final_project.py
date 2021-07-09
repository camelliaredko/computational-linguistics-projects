# Final Project CS366
# Olga Redko

from nltk.corpus import wordnet as wn
from unidecode import unidecode
from nltk.metrics import *
import sys
import os
import pickle
from operator import itemgetter
from xlsxwriter.workbook import Workbook

# Importing list of English words
english_file = open(os.path.join(os.getcwd(), 'top_3000_english_words.txt'))

english_list = []
spanish_list = []
portuguese_list = []
italian_list = []
french_list = []
romanian_list = []
catalan_list = []
galician_list = []

# index_count used to ensure that the translations of each English word share the same index
index_count = 0

for english_word in english_file.readlines():
    english_word = english_word.replace("\n", "")
    # List with the English word is appended to the list of lists with English words
    english_list.append([english_word])
    # Empty list is appended to the individual list of lists with foreign words
    spanish_list.append([])
    portuguese_list.append([])
    italian_list.append([])
    french_list.append([])
    romanian_list.append([])
    catalan_list.append([])
    galician_list.append([])
    # Going through each synset of the English word
    for ss in wn.synsets(english_word):
     #   print("Word =", english_word, "Synset = ",ss.name(), ss)
     # Inserting the translations of a synset within a list with a shared index in individual foreign lists of lists
        spanish_list[index_count].extend(ss.lemma_names('spa'))
        portuguese_list[index_count].extend(ss.lemma_names('por'))
        italian_list[index_count].extend(ss.lemma_names('ita'))
        french_list[index_count].extend(ss.lemma_names('fra'))
        romanian_list[index_count].extend(ss.lemma_names('ron'))
        catalan_list[index_count].extend(ss.lemma_names('cat'))
        galician_list[index_count].extend(ss.lemma_names('glg'))
    index_count += 1

english_file.close()

# Replacing empty lists [] with ['-'] to prevent errors when trying to index list elements through numbers
spanish_list = [['-'] if list == [] else list for list in spanish_list]
portuguese_list = [['-'] if list == [] else list for list in portuguese_list]
italian_list = [['-'] if list == [] else list for list in italian_list]
french_list = [['-'] if list == [] else list for list in french_list]
romanian_list = [['-'] if list == [] else list for list in romanian_list]
catalan_list = [['-'] if list == [] else list for list in catalan_list]
galician_list = [['-'] if list == [] else list for list in galician_list]

# Replacing '_' with ' ' in lists so that elements are more convenient for humans to read
# (e.g., 'de_alguna_manera' would become 'de alguna manera').
spanish_list = [[word.replace('_', ' ') for word in list] for list in spanish_list]
portuguese_list = [[word.replace('_', ' ') for word in list] for list in portuguese_list]
italian_list = [[word.replace('_', ' ') for word in list] for list in italian_list]
french_list = [[word.replace('_', ' ') for word in list] for list in french_list]
romanian_list = [[word.replace('_', ' ') for word in list] for list in romanian_list]
catalan_list = [[word.replace('_', ' ') for word in list] for list in catalan_list]
galician_list = [[word.replace('_', ' ') for word in list] for list in galician_list]

# Preprocessing lists so that when MED scores are calculated, differences in diacritics and capitalization are ignored
spanish_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in spanish_list]
portuguese_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in portuguese_list]
italian_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in italian_list]
french_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in french_list]
romanian_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in romanian_list]
catalan_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in catalan_list]
galician_list_preprocessed = [[unidecode(word.lower()) for word in list] for list in galician_list]

# Foreign MED lists are prepared, and their expected finished format is the following:
# [[index_of_1st_foreign_word_with_lowest_MED_score_when_compared_to_words_of_the_same_meaning_in_other_languages,
# the_previous_element's_MED_score],
# [index_of_2nd_foreign_word_with_lowest_MED_score_when_compared_to_words_of_the_same_meaning_in_other_languages,
# the_previous_element's_MED_score], ...]
spanish_MED_list = []
portuguese_MED_list = []
italian_MED_list = []
french_MED_list = []
romanian_MED_list = []
catalan_MED_list = []
galician_MED_list = []


def spanish_MED():
    # spanish_MED_index used so that comparisons are made between words of the same meaning through a shared index
    spanish_MED_index = 0
    for spanish_words in spanish_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for spanish_word in spanish_words:
            for portuguese_word in portuguese_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, portuguese_word) < min_MED:
                    min_MED = edit_distance(spanish_word, portuguese_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
            for italian_word in italian_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, italian_word) < min_MED:
                    min_MED = edit_distance(spanish_word, italian_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
            for french_word in french_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, french_word) < min_MED:
                    min_MED = edit_distance(spanish_word, french_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
            for romanian_word in romanian_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, romanian_word) < min_MED:
                    min_MED = edit_distance(spanish_word, romanian_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
            for catalan_word in catalan_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, catalan_word) < min_MED:
                    min_MED = edit_distance(spanish_word, catalan_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
            for galician_word in galician_list_preprocessed[spanish_MED_index]:
                if edit_distance(spanish_word, galician_word) < min_MED:
                    min_MED = edit_distance(spanish_word, galician_word)
                    min_MED_word_index = spanish_words.index(spanish_word)
        spanish_MED_list.append([min_MED_word_index, min_MED])
        spanish_MED_index += 1

#spanish_MED()

def portuguese_MED():
    # portuguese_MED_index used so that comparisons are made between words of the same meaning through a shared index
    portuguese_MED_index = 0
    for portuguese_words in portuguese_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for portuguese_word in portuguese_words:
            if edit_distance(portuguese_word, spanish_list_preprocessed[portuguese_MED_index][spanish_MED_list[portuguese_MED_index][0]]) < min_MED:
                min_MED = edit_distance(portuguese_word, spanish_list_preprocessed[portuguese_MED_index][spanish_MED_list[portuguese_MED_index][0]])
                min_MED_word_index = portuguese_words.index(portuguese_word)
        portuguese_MED_list.append([min_MED_word_index, min_MED])
        portuguese_MED_index += 1

#portuguese_MED()

def italian_MED():
    # italian_MED_index used so that comparisons are made between words of the same meaning through a shared index
    italian_MED_index = 0
    for italian_words in italian_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for italian_word in italian_words:
            if edit_distance(italian_word, spanish_list_preprocessed[italian_MED_index][spanish_MED_list[italian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(italian_word, spanish_list_preprocessed[italian_MED_index][spanish_MED_list[italian_MED_index][0]])
                min_MED_word_index = italian_words.index(italian_word)
            if edit_distance(italian_word, portuguese_list_preprocessed[italian_MED_index][portuguese_MED_list[italian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(italian_word, portuguese_list_preprocessed[italian_MED_index][portuguese_MED_list[italian_MED_index][0]])
                min_MED_word_index = italian_words.index(italian_word)
        italian_MED_list.append([min_MED_word_index, min_MED])
        italian_MED_index += 1

#italian_MED()

def french_MED():
    # french_MED_index used so that comparisons are made between words of the same meaning through a shared index
    french_MED_index = 0
    for french_words in french_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for french_word in french_words:
            if edit_distance(french_word, spanish_list_preprocessed[french_MED_index][
                spanish_MED_list[french_MED_index][0]]) < min_MED:
                min_MED = edit_distance(french_word, spanish_list_preprocessed[french_MED_index][
                    spanish_MED_list[french_MED_index][0]])
                min_MED_word_index = french_words.index(french_word)
            if edit_distance(french_word, portuguese_list_preprocessed[french_MED_index][
                portuguese_MED_list[french_MED_index][0]]) < min_MED:
                min_MED = edit_distance(french_word, portuguese_list_preprocessed[french_MED_index][
                    portuguese_MED_list[french_MED_index][0]])
                min_MED_word_index = french_words.index(french_word)
            if edit_distance(french_word, italian_list_preprocessed[french_MED_index][
                italian_MED_list[french_MED_index][0]]) < min_MED:
                min_MED = edit_distance(french_word, italian_list_preprocessed[french_MED_index][
                    italian_MED_list[french_MED_index][0]])
                min_MED_word_index = french_words.index(french_word)
        french_MED_list.append([min_MED_word_index, min_MED])
        french_MED_index += 1

#french_MED()

def romanian_MED():
    # romanian_MED_index used so that comparisons are made between words of the same meaning through a shared index
    romanian_MED_index = 0
    for romanian_words in romanian_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for romanian_word in romanian_words:
            if edit_distance(romanian_word, spanish_list_preprocessed[romanian_MED_index][
                spanish_MED_list[romanian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(romanian_word, spanish_list_preprocessed[romanian_MED_index][
                    spanish_MED_list[romanian_MED_index][0]])
                min_MED_word_index = romanian_words.index(romanian_word)
            if edit_distance(romanian_word, portuguese_list_preprocessed[romanian_MED_index][
                portuguese_MED_list[romanian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(romanian_word, portuguese_list_preprocessed[romanian_MED_index][
                    portuguese_MED_list[romanian_MED_index][0]])
                min_MED_word_index = romanian_words.index(romanian_word)
            if edit_distance(romanian_word, italian_list_preprocessed[romanian_MED_index][
                italian_MED_list[romanian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(romanian_word, italian_list_preprocessed[romanian_MED_index][
                    italian_MED_list[romanian_MED_index][0]])
                min_MED_word_index = romanian_words.index(romanian_word)
            if edit_distance(romanian_word, french_list_preprocessed[romanian_MED_index][
                french_MED_list[romanian_MED_index][0]]) < min_MED:
                min_MED = edit_distance(romanian_word, french_list_preprocessed[romanian_MED_index][
                    french_MED_list[romanian_MED_index][0]])
                min_MED_word_index = romanian_words.index(romanian_word)
        romanian_MED_list.append([min_MED_word_index, min_MED])
        romanian_MED_index += 1

#romanian_MED()

def catalan_MED():
    # catalan_MED_index used so that comparisons are made between words of the same meaning through a shared index
    catalan_MED_index = 0
    for catalan_words in catalan_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for catalan_word in catalan_words:
            if edit_distance(catalan_word, spanish_list_preprocessed[catalan_MED_index][
                spanish_MED_list[catalan_MED_index][0]]) < min_MED:
                min_MED = edit_distance(catalan_word, spanish_list_preprocessed[catalan_MED_index][
                    spanish_MED_list[catalan_MED_index][0]])
                min_MED_word_index = catalan_words.index(catalan_word)
            if edit_distance(catalan_word, portuguese_list_preprocessed[catalan_MED_index][
                portuguese_MED_list[catalan_MED_index][0]]) < min_MED:
                min_MED = edit_distance(catalan_word, portuguese_list_preprocessed[catalan_MED_index][
                    portuguese_MED_list[catalan_MED_index][0]])
                min_MED_word_index = catalan_words.index(catalan_word)
            if edit_distance(catalan_word, italian_list_preprocessed[catalan_MED_index][
                italian_MED_list[catalan_MED_index][0]]) < min_MED:
                min_MED = edit_distance(catalan_word, italian_list_preprocessed[catalan_MED_index][
                    italian_MED_list[catalan_MED_index][0]])
                min_MED_word_index = catalan_words.index(catalan_word)
            if edit_distance(catalan_word, french_list_preprocessed[catalan_MED_index][
                french_MED_list[catalan_MED_index][0]]) < min_MED:
                min_MED = edit_distance(catalan_word, french_list_preprocessed[catalan_MED_index][
                    french_MED_list[catalan_MED_index][0]])
                min_MED_word_index = catalan_words.index(catalan_word)
            if edit_distance(catalan_word, romanian_list_preprocessed[catalan_MED_index][
                romanian_MED_list[catalan_MED_index][0]]) < min_MED:
                min_MED = edit_distance(catalan_word, romanian_list_preprocessed[catalan_MED_index][
                    romanian_MED_list[catalan_MED_index][0]])
                min_MED_word_index = catalan_words.index(catalan_word)
        catalan_MED_list.append([min_MED_word_index, min_MED])
        catalan_MED_index += 1

#catalan_MED()

def galician_MED():
    # galician_MED_index used so that comparisons are made between words of the same meaning through a shared index
    galician_MED_index = 0
    for galician_words in galician_list_preprocessed:
        min_MED = sys.maxsize
        min_MED_word_index = 0
        for galician_word in galician_words:
            if edit_distance(galician_word, spanish_list_preprocessed[galician_MED_index][
                spanish_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, spanish_list_preprocessed[galician_MED_index][
                    spanish_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
            if edit_distance(galician_word, portuguese_list_preprocessed[galician_MED_index][
                portuguese_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, portuguese_list_preprocessed[galician_MED_index][
                    portuguese_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
            if edit_distance(galician_word, italian_list_preprocessed[galician_MED_index][
                italian_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, italian_list_preprocessed[galician_MED_index][
                    italian_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
            if edit_distance(galician_word, french_list_preprocessed[galician_MED_index][
                french_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, french_list_preprocessed[galician_MED_index][
                    french_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
            if edit_distance(galician_word, romanian_list_preprocessed[galician_MED_index][
                romanian_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, romanian_list_preprocessed[galician_MED_index][
                    romanian_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
            if edit_distance(galician_word, catalan_list_preprocessed[galician_MED_index][
                catalan_MED_list[galician_MED_index][0]]) < min_MED:
                min_MED = edit_distance(galician_word, catalan_list_preprocessed[galician_MED_index][
                    catalan_MED_list[galician_MED_index][0]])
                min_MED_word_index = galician_words.index(galician_word)
        galician_MED_list.append([min_MED_word_index, min_MED])
        galician_MED_index += 1

#galician_MED()

## Pickling
## Used so that I don't have to run the time-consuming methods spanish_MED(), portuguese_MED(), italian_MED(), and
## french_MED() to obtain important data every time I run final_project.py.
#with open("spanish_MED_list.txt", "wb") as fp:
#    pickle.dump(spanish_MED_list, fp)
#with open("portuguese_MED_list.txt", "wb") as fp:
#    pickle.dump(portuguese_MED_list, fp)
#with open("italian_MED_list.txt", "wb") as fp:
#    pickle.dump(italian_MED_list, fp)
#with open("french_MED_list.txt", "wb") as fp:
#    pickle.dump(french_MED_list, fp)
#with open("romanian_MED_list.txt", "wb") as fp:
#    pickle.dump(romanian_MED_list, fp)
#with open("catalan_MED_list.txt", "wb") as fp:
#    pickle.dump(catalan_MED_list, fp)
#with open("galician_MED_list.txt", "wb") as fp:
#    pickle.dump(galician_MED_list, fp)

# Unpickling
with open("spanish_MED_list.txt", "rb") as fp:
    spanish_MED_list = pickle.load(fp)
with open("portuguese_MED_list.txt", "rb") as fp:
    portuguese_MED_list = pickle.load(fp)
with open("italian_MED_list.txt", "rb") as fp:
    italian_MED_list = pickle.load(fp)
with open("french_MED_list.txt", "rb") as fp:
    french_MED_list = pickle.load(fp)
with open("romanian_MED_list.txt", "rb") as fp:
    romanian_MED_list = pickle.load(fp)
with open("catalan_MED_list.txt", "rb") as fp:
    catalan_MED_list = pickle.load(fp)
with open("galician_MED_list.txt", "rb") as fp:
    galician_MED_list = pickle.load(fp)

# index_count used to ensure that words with the same meaning (shared index) are considered
index_count = 0

# After being filled in, similar_words_MED_sum has the following format:
# [[1st_spanish_word, 1st_portuguese_word, 1st_italian_word, 1st_french_word, 1st_summed_min_MED_scores],
# [2nd_spanish_word, 2nd_portuguese_word, 2nd_italian_word, 2nd_french_word, 2nd_summed_min_MED_scores], ...]
similar_words_MED_sum = []

# min_MED_sum_data collects information to calculate the percentages of each summed minimum MED score
min_MED_sum_data = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0,
                    16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0, 26:0, 27:0, 28:0, 29:0, '30+':0}

for english_element in english_list:
    for english_word in english_element:
        list = []
        # If none of the words are empty words/words that lack a translation,
        # append the original words with the lowest MED scores as well as the summed minimum MED scores
        # to similar_words_MED_sum
        if spanish_list[index_count][spanish_MED_list[index_count][0]] != '-' and portuguese_list[index_count][
            portuguese_MED_list[index_count][0]] != '-' and italian_list[index_count][
            italian_MED_list[index_count][0]] != '-' and french_list[index_count][
            french_MED_list[index_count][0]] != '-' and romanian_list[index_count][
            romanian_MED_list[index_count][0]] != '-' and catalan_list[index_count][
            catalan_MED_list[index_count][0]] != '-' and galician_list[index_count][galician_MED_list[index_count][0]] != '-':
            list.append(english_word)
            list.append(spanish_list[index_count][spanish_MED_list[index_count][0]])
            list.append(portuguese_list[index_count][portuguese_MED_list[index_count][0]])
            list.append(italian_list[index_count][italian_MED_list[index_count][0]])
            list.append(french_list[index_count][french_MED_list[index_count][0]])
            list.append(romanian_list[index_count][romanian_MED_list[index_count][0]])
            list.append(catalan_list[index_count][catalan_MED_list[index_count][0]])
            list.append(galician_list[index_count][galician_MED_list[index_count][0]])
            MED_sum = spanish_MED_list[index_count][1] + portuguese_MED_list[index_count][1] + \
                      italian_MED_list[index_count][1] + french_MED_list[index_count][1] + \
                      romanian_MED_list[index_count][1] + catalan_MED_list[index_count][1] + galician_MED_list[index_count][1]
            list.append(MED_sum)
            similar_words_MED_sum.append(list)
            # Collecting data to calculate the percentages of each summed minimum MED score
            if MED_sum < 30:
                min_MED_sum_data[MED_sum] += 1
            else:
                min_MED_sum_data['30+'] += 1
        index_count += 1

# Printing out data about summed minimum MED scores
print("There is a total of", len(similar_words_MED_sum), "summed minimum MED scores.")
for key in min_MED_sum_data:
    print("There are", min_MED_sum_data[key], "cases where the summed minimum MED score is", key, ". Thus,",
          100*min_MED_sum_data[key]/len(similar_words_MED_sum), "% of summed minimum MED scores have a score of", key, ".")

# Order lists in similar_words_MED_sum by their summed MED scores (the eighth element of a list within the list)
sorted_similar_words_MED_sum = sorted(similar_words_MED_sum, key = itemgetter(8))

# Create a non-colored spreadsheet that displays the contents of sorted_similar_words_MED_sum.
workbook = Workbook('comparison_sheet_noncolored.xlsx')
worksheet = workbook.add_worksheet()
col = 0

for row, data in enumerate(sorted_similar_words_MED_sum):
    worksheet.write_row(row, col, data)

workbook.close()

# Create a color-coded spreadsheet that displays the contents of sorted_similar_words_MED_sum.

workbook = Workbook('comparison_sheet_colored.xlsx')
worksheet = workbook.add_worksheet()

# Specify the formats of colors to be added to the spreadsheet
red_acute = workbook.add_format({'color': 'red'}) # Colors for á, é, í, ó, ú, Á, É, Í, Ó, Ú
blue_grave = workbook.add_format({'color': 'blue'}) # Colors for à, è, ì, ò, ù, À, È, Ì, Ò, Ù
green_circumflex = workbook.add_format({'color': 'green'}) # Colors for â, ê, ô, î, Â, Ê, Ô, Î
yellow_cedilla = workbook.add_format({'color': 'orange'}) # Colors for ç, Ç
brown_diaeresis = workbook.add_format({'color': 'brown'}) # Colors for ü, ë, ï, Ü, Ë, Ï
pink_tilde = workbook.add_format({'color': 'pink'}) # Colors for ñ, ã, õ, Ñ, Ã, Õ

orange_breve = workbook.add_format({'color': 'orange'}) # Colors for ă, Ă
purple_comma = workbook.add_format({'color': 'purple'}) # Colors for ș, ț, Ș, Ț

black = workbook.add_format({'color': 'black'}) # Default color

for row, data in enumerate(sorted_similar_words_MED_sum):
    col = 0
    for word in data:
        word = str(word)
        if len(word) < 2:
            word += " "
        colored_word = []
        for letter in word:
            if (letter == 'á' or letter == 'é' or letter == 'í' or letter == 'ó' or letter == 'ú' or
                    letter == 'Á' or letter == 'É' or letter == 'Í' or letter == 'Ó' or letter == 'Ú'):
                colored_word.extend((red_acute, letter))
            elif (letter == 'à' or letter == 'è' or letter == 'ì' or letter == 'ò' or letter == 'ù' or
                    letter == 'À' or letter == 'È' or letter == 'Ì' or letter == 'Ò' or letter == 'Ù'):
                colored_word.extend((blue_grave, letter))
            elif (letter == 'â' or letter == 'ê' or letter == 'ô' or letter == 'î' or
                    letter == 'Â' or letter == 'Ê' or letter == 'Ô' or letter == 'Î'):
                colored_word.extend((green_circumflex, letter))
            elif (letter == 'ç' or
                    letter == 'Ç'):
                colored_word.extend((yellow_cedilla, letter))
            elif (letter == 'ü' or letter == 'ë' or letter == 'ï' or
                    letter == 'Ü' or letter == 'Ë' or letter == 'Ï'):
                colored_word.extend((brown_diaeresis, letter))
            elif (letter == 'ñ' or letter == 'ã' or letter == 'õ' or
                    letter == '̈Ñ' or letter == 'Ã' or letter == 'Õ'):
                colored_word.extend((pink_tilde, letter))
            elif (letter == 'ă' or
                  letter == 'Ă'):
                colored_word.extend((orange_breve, letter))
            elif (letter == 'ș' or letter == 'ț' or
                    letter == 'Ș' or letter == 'Ț'):
                colored_word.extend((purple_comma, letter))
            else:
                colored_word.extend((black, letter))
        # Write out the word
        worksheet.write_rich_string(row, col, *colored_word)
        # Move onto the next column to write into
        col += 1

workbook.close()