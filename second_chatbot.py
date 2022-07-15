#!/usr/bin/env python3

import nltk
import numpy as np
import random
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# extend stop words
from sklearn.feature_extraction import text

# # disable SSL check no goood
# import ssl
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context


from corpusreader import read_corpus
from corpusreader import corpus_keyword_detector

raw_doc=read_corpus('tech_corpus.txt')
corpus_keywords = corpus_keyword_detector('tech_corpus.txt')

# download all the nltk data: will be saved ~/nltk_data
nltk.download('all')
# # using the Punk tokenizer
# nltk.download('punkt')

# using the WordNet dictionary for stemming and lemming
nltk.download('wordnet')
nltk.download('stopwords')

article_sentences = nltk.sent_tokenize(raw_doc)
article_words = nltk.word_tokenize(raw_doc)

# remove the punctuation from the user input text and will also lemmatize the text
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

    my_additional_stop_words = ['-',';','.',':','!','?','ha', 'le', 'u', 'wa']
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words=text.ENGLISH_STOP_WORDS.union(my_additional_stop_words))
    all_word_vectors = word_vectorizer.fit_transform(article_sentences)
    similar_vector_values = cosine_similarity(all_word_vectors[-1], all_word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]

    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]

    if vector_matched == 0:
        return f'{RuleRobo_response} could you please rephrase it...my domain knowledge is limited to {",".join(corpus_keywords)}'
    else:
        RuleRobo_response = RuleRobo_response + article_sentences[similar_sentence_number]
        return RuleRobo_response

continue_dialogue = True
print(f'\033[1;32;40m RuleRobo. Ask me any corpus related question...my domain knowledge is limited to {",".join(corpus_keywords)} \033[0m')
while(continue_dialogue == True):
    human_text = input().lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            continue_dialogue = False
            print("\033[1;32;40m RuleRobo: Most welcome")
        else:
            if generate_greeting_response(human_text) != None:
                print("\033[1;32;40m RuleRobo: " + generate_greeting_response(human_text))
            else:
                print("\033[1;32;40m RuleRobo: ", end="")
                print(generate_response(human_text))
                article_sentences.remove(human_text)
    else:
        continue_dialogue = False
        print("\033[1;32;40m RuleRobo: Good bye...")