#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read corpus and generate the domain-specific lexicon.
"""
import re
import os

# keyword extractor
from rake_nltk import Rake
from nltk.corpus import stopwords


from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize

import nltk
nltk.download('stopwords')
nltk.download('all')
nltk.download('punkt')

def read_corpus(filename):
    """
    Read corpus from datasets dir and return the raw text.
    """
    with open(os.path.join('datasets', filename), 'r', errors='ignore') as f:
        raw_doc=f.read()
        # convert to lowercase
        raw_doc=raw_doc.lower()
        # remove special characters and empty spaces
        raw_doc = re.sub(r'\[[0-9]*\]', ' ', raw_doc)
        raw_doc = re.sub(r'\s+', ' ', raw_doc)
        return raw_doc

def corpus_keyword_detector(filename):
    """
    Read corpus and generate the domain-specific knowledge base."""
    with open(os.path.join('datasets', filename), 'r', errors='ignore') as f:
        raw_doc=f.read()

        # create keyword extractor
        r = Rake()

        # Extraction given the text.
        r.extract_keywords_from_text(raw_doc)

        # Extraction given the list of strings where each string is a sentence.
        # r.extract_keywords_from_sentences(sent_tokenize(raw_doc))
        keywords_list=[]
        for sentence in sent_tokenize(raw_doc):
            r.extract_keywords_from_text(sentence)
            # print(f"{r.get_ranked_phrases()[0]}\n---------")
            
            # append highest ranked word to the list
            keywords_list.append(r.get_ranked_phrases()[0])
        return keywords_list
        # # Get the keyword scores in descending order.
        # keywords = r.get_ranked_phrases()
        # # Get keyword phrases ranked with scores, highest to lowest.
        # keywords_with_scores = r.get_ranked_phrases_with_scores()
        # print(keywords)


if __name__ == "__main__":

    corpus_keyword_detector(filename='tech_corpus.txt')