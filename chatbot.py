#!/usr/bin/env python3

import numpy as np
import nltk
import string
import random

# libs from response generation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
# extend stop words
from sklearn.feature_extraction import text


# import corpus
f=open('scorpus.txt','r',errors='ignore')
raw_doc=f.read()

# convert to lowercase
raw_doc=raw_doc.lower()

# download all the nltk data: will be saved ~/nltk_data
nltk.download('all')
# using the Punk tokenizer
#nltk.download('punkt')
# using the WordNet dictionary
nltk.download('wordnet')

# convert doc to list of sentences and words
sentence_tokens=nltk.sent_tokenize(raw_doc,language='english')
word_tokens=nltk.word_tokenize(raw_doc,language='english')

# # print sentence tokens
# print(f'Sentence tokens:{[sentence_tokens[:2]]}')
# # print word tokens
# print(f'Word tokens:{[word_tokens[:2]]}')

# Text preprocessing
lemmer = nltk.stem.WordNetLemmatizer()
# WordNet is a semantically-oriented dictionary of English included in NLTK.
def LemTokens(tokens):
    """ Lemmatize tokens """
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    """ Lemmatize and normalize text """
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Define the greeting function
GREET_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREET_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSES)

def response(user_response):
    """Generate a response to the users input"""
    robo1_response=''
    my_additional_stop_words = ['-','.',':','!','?','ha', 'le', 'u', 'wa']
 #   TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words=text.ENGLISH_STOP_WORDS.union(my_additional_stop_words))
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        robo1_response = robo1_response + "I am sorry! I don't understand you"
        return robo1_response
    else:
        robo1_response = robo1_response + sentence_tokens[idx]
        return robo1_response   

# Define the conversation function
flag=True
print("ROBO: My name is Robo. I will answer your queries about corpus topic. If you want to exit, type Bye!")  
while(flag==True):
    user_response = input().lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'):
            flag=False
            print("ROBO: You are welcome...")
        else:
            if(greeting(user_response)!=None):
                print("ROBO: "+greeting(user_response))
            else:
                print("ROBO: ",end="")
                print(response(user_response))
                sentence_tokens.append(user_response)
    else:
        flag=False
        print("ROBO: Bye! take care..")