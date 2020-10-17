import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
import texts
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk import ne_chunk

def tokenize(text):
    return word_tokenize(text)

def frequency_distinct(tokens, plot=False, show_items=True):
    frequency_distinct = FreqDist(tokens)
    if (plot):
       frequency_distinct.plot()
    if (show_items):
        print(frequency_distinct.items())
    return frequency_distinct


def log():
    os.system('cls')
    tokens = tokenize(texts.one)
    freq_dist = frequency_distinct(tokens)

    log_section('TOKENS', tokens)
    log_section('FREQUENCY DISTINCT')

def log_section(title, data=''):
    print(title)
    print("-"*200)
    print()
    print(data)


def remove_stop_words(tokens, language='english'):
    stopwords_collection = set(stopwords.words(language))
    return [word for word in tokens if word not in stopwords_collection]


def remove_punctuation(text):
    result = [char for char in text if char.isalnum() or char.isalpha() or char.isspace()]
    return ''.join(result)


# log()

# ----------------------------

string = remove_punctuation(texts.two)
string = tokenize(string)
string = remove_stop_words(string)
freq_dist = frequency_distinct(string, False, False)
most_frequents = freq_dist.most_common(10)
print(most_frequents)

# filtered_tokens = (remove_punctuation(texts.two))
# print(filtered_tokens)