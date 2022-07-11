#!/usr/bin/env python3

from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

from corpusreader import read_corpus


text = "God is Great! I won the lottery!"

# # output of word tokenizer in NLTK can be converted to Data Frame
# print(word_tokenize(text))
# print(sent_tokenize(text))

# Stemming is a method of normalization of words
raw_doc=read_corpus('incidents_corpus.txt')
print(word_tokenize(raw_doc))
# print(sent_tokenize(raw_doc))

# create dictionary of words and their frequencies
from nltk.probability import FreqDist
fdist = FreqDist(sent_tokenize(raw_doc))
print(fdist)
# fdist.most_common(10)
# fdis.max()