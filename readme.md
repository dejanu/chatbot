# Terms

* Corpus - collection of text documents, is a body of written or spoken material upon which a linguistic analysis is based (mainly used for NLP)
* Dataset - collection of data 
* Tokenization - process of breaking a sentence into words
* Lemmatization - process of finding the base form of a word
* Stemming - process of reducing a word to its root form, finding similiar words and removing suffixes
* Bag of Words - a vector representation of a document, where each word is represented by a number, and the number is the number of times the word appears in the document
* Term Frequency (Tf) - number of times a word appears in a document
* Inverse Document (Idf) Frequency - number of documents in a corpus that contain a word

# Implementation

* TfidfVectorizer - Convert a collection of raw documents to a matrix of TF-IDF features.
* Term Frequency and Inverse Document Frequency is one of the most important techniques used for information retrieval to represent how important a specific word or phrase is to a given document.

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