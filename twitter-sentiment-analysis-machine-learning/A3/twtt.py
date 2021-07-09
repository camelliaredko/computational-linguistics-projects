# Olga Redko

import sys
import csv

sentiment_file = sys.argv[-3]
ark_output = sys.argv[-2]
tagged_tweets = sys.argv[-1]

with open(tagged_tweets, "w") as tfile, open(sentiment_file) as sfile, open(ark_output) as afile:
    stsvreader = csv.reader(sfile, delimiter="\t")
    atsvreader = csv.reader(afile, delimiter="\t")
    tsv_writer = csv.writer(tfile, delimiter='\t', lineterminator='\n')
    slines = sfile.readlines()
    alines = afile.readlines()
    row_count = 0
    for lines in range(0, len(slines)):
            tweet_pos = ''
            token_count = 0
            sentiment_number = slines[row_count].split("\t")[0]
            tweet = alines[row_count].split("\t")[0].split()
            pos = alines[row_count].split("\t")[1].split()
            for token in tweet:
                if tweet_pos == '':
                    tweet_pos += token + '_' + pos[token_count]
                else:
                    tweet_pos += ' ' + token + '_' + pos[token_count]
                token_count += 1
            tsv_writer.writerow([sentiment_number, tweet_pos])
            row_count += 1

tfile.close()
sfile.close()
afile.close()


