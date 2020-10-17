import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
import texts
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

def tokenize(text):
    return word_tokenize(text)

def frequency_distinct(tokens, plot=False):

    frequency_distinct = FreqDist(tokens)
    if (plot):
       frequency_distinct.plot()
    return frequency_distinct


def log():
    os.system('cls')
    tokens = tokenize(texts.one)
    freq_dist = frequency_distinct(tokens)

    log_section('TOKENS', tokens)
    log_section('FREQUENCY DISTINCT', freq_dist)

def log_section(title, data):
    print(title)
    print("-"*200)
    print()
    print(data)


log()