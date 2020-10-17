import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
import texts
from nltk.tokenize import word_tokenize

def tokenize(text):
    return word_tokenize(text)



def log():
    os.system('cls')
    tokens = tokenize(texts.one)
    log_section('TOKENS')
    print(tokens)

def log_section(title):
    print(title)
    print("-"*200)
    print()


log()