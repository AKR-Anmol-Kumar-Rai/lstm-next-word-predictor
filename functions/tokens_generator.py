import nltk
from nltk import word_tokenize

def token_generator(sentence):
    sentence = word_tokenize(sentence.lower())
    return sentence
