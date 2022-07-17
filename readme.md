# General

* NLP - Natural Language Processing : text classification, sentiment-analysis, chatbot, language processing.
* Types of Conversational Agents:
  * Rule Based ( follow a specific set of rules, not flexible but they give pretty accurate responses )
  * Learning Based:
      * Generative - generate respons on the fly
      * Retrieval-based - retrieve a certain response from corpus

# Terms

* Corpus - collection of text documents, is a body of written or spoken material upon which a linguistic analysis is based (mainly used for NLP)
* Dataset - collection of data 
* Tokenization - process of breaking a sentence into words
* Stemming - process of reducing a word to its root by removing suffixes
* Lemmatization - process of finding the base form of a word with the use of a vocabulary and morphological analysis of words, normally aiming to remove inflectional endings only and to return the base or dictionary form of a word, which is known as the lemma
* Lemmatization takes more time than stemming: lemmatize the word `caring` it returns `care` and stemming returns `car`. Lemmatization is computationally more expensive since it involves look-up tables. Lemmatization and stemming are special cases of normalization. They identify a canonical representative for a set of related word forms.
* Bag of Words - a vector representation of a document, where each word is represented by a number, and the number is the number of times the word appears in the document
* Term Frequency (Tf) - number of times a word appears in a document aka Keyword extraction
* Inverse Document (Idf) Frequency - number of documents in a corpus that contain a word.
, measure as measured as log(total number of sentences / Number of sentences with term t)
* Fallback Rate (FBR) - number of times when the bot is unable to answer a question and falls back to a default response "Sorry, I don't understand"
* Intent - a goal or purpose of a conversation

# Implementation

* TfidfVectorizer - Convert a collection of raw documents to a matrix of TF-IDF features.
* Term Frequency and Inverse Document Frequency is a text vectorization techniques used for information retrieval to represent how important a specific word or phrase is to a given document.
* Tfidf is a BoW(bag of words) algorithm that can help you identify the intent, but not relation between those intents.
* The matrix that is obtained from vectorized tfidf along with the label will just tell the machine that if for some text, similar matrix is obtained, this is the label. Which is handy in classification, but not for chatbot responses.
* Flow to get a response from the chatbot:
    * Get the user input
    * Vectorize the user input
    * Get the similarity between the user input and the corpus
    * Get the index of the most similar text from the corpus
    * Get the response from the corpus at the index
    * Return the response

# Keyword Extraction
    * BoWC (Bag of Weighted Concepts) - creates concepts by clustering word vectors (embedding)
    * keywords extraction methods: Rake `pip install rake-nltk`, Yake, Keybert, and Textrank (methods to extract keywords from a single text)

# Issues

* NLTK resources not found:
    * Solution: `python3 -c "import nltk; nltk.download('all')"`
```bash
LookupError: 
**********************************************************************
  Resource omw-1.4 not found.
  Please use the NLTK Downloader to obtain the resource:

  >>> import nltk
  >>> nltk.download('omw-1.4')
```

* Weak corpus:
    * Solution: The reason is that you have used custom tokenizer and used default stop_words='english' so while extracting features a check is made to see if there is any inconsistency between stop_words and tokenizer. [link](https://stackoverflow.com/questions/60280307/tokenizing-the-stop-words-generated-tokens-ha-le-u-wa-not-in-stop-w)
```bash
 UserWarning: Your stop_words may be inconsistent with your preprocessing. Tokenizing the stop words generated tokens ['ha', 'le', 'u', 'wa'] not in stop_words.
 ```

 * Which is the best stemmer:
    * Solution: The best stemmer is snowball stemmer. It is a stemmer that is based on the snowball algorithm. It is a good stemmer for English.
    * [doc](https://www.nltk.org/api/nltk.stem.html#module-nltk.stem.snowball)
    * [link](https://stackoverflow.com/questions/24647400/what-is-the-best-stemming-method-in-python)


* Dockerfile build:
    * installing numpy `raise RuntimeError("Broken toolchain: cannot link a simple C program")` solved by changing the baseimage `FROM python:3.8-slim`

# Cloud Implementations:
    * https://www.youtube.com/watch?v=bxF2LWZcUR8&t=92s
    * https://docs.microsoft.com/en-us/power-virtual-agents/teams/fundamentals-get-started-teams

# Chatbot image:
    * Start chatbot: `docker run -v $PWD/datasets:/app/datasets -itu 0 dejanualex/chatbot:2.0 bash`