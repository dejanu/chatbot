#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read corpus and generate the domain-specific lexicon.
"""
import re
import os

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

def read_corpus_words(filename):
    """ print domain knoledge aka first words from corpus"""
    with open(os.path.join('datasets', filename), 'r', errors='ignore') as f:
        for line in f:
            # try to print first word from each line
            l = []
            try:
                l.append(line.split()[0])
            except IndexError:
                pass
            print(set(l))