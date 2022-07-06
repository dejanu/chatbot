#!/usr/bin/env python3

import nltk
import numpy as np
import random
import string
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# extend stop words
from sklearn.feature_extraction import text

# divide our text into sentences and words since the cosine similarity of the user 
# input (of the vectorized form of the input sentence) will actually be compared with each sentence

# import corpus
f=open('tech_corpus.txt','r',errors='ignore')
raw_doc=f.read()
f.close()

# convert to lowercase
raw_doc=raw_doc.lower()

# remove special characters and empty spaces
raw_doc = re.sub(r'\[[0-9]*\]', ' ', raw_doc)
raw_doc = re.sub(r'\s+', ' ', raw_doc)

# divide text into sentences and words
# cosine similarity of the user inout will actually be compared with each sentence
article_sentences = nltk.sent_tokenize(raw_doc)
article_words = nltk.word_tokenize(raw_doc)

# remove the punctuation from the user input text and will also lemmatize the text
# so that the words are in the same form
wnlemmatizer = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    """take a list of words as input and lemmatize the corresponding lemmatized list of words"""
    return [wnlemmatizer.lemmatize(token) for token in tokens]

punctuation_removal = dict((ord(punctuation), None) for punctuation in string.punctuation)

def get_processed_text(document):
    """removes the punctuation from the passed text"""
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(punctuation_removal)))

greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)

def generate_response(user_input):
    RuleRobo_response = ''
    article_sentences.append(user_input)

    my_additional_stop_words = ['-','.',':','!','?','ha', 'le', 'u', 'wa']
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words=text.ENGLISH_STOP_WORDS.union(my_additional_stop_words))
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        return f"{RuleRobo_response} could you please rephrase it..."
    else:
        RuleRobo_response = RuleRobo_response + article_sentences[similar_sentence_number]
        return RuleRobo_response

continue_dialogue = True
print("I am RuleRobo. You can ask me any tech question:")
while(continue_dialogue == True):
    human_text = input().lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            continue_dialogue = False
            print("RuleRobo: Most welcome")
        else:
            if generate_greeting_response(human_text) != None:
                print("RuleRobo: " + generate_greeting_response(human_text))
            else:
                print("RuleRobo: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("RuleRobo: Good bye...")