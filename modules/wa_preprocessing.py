import pandas as pd
import numpy as np
import re
import nltk
import spacy
import string
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

"""
Preprocessing:
[X] Rimozione righe con campo messaggio vuoto
[X] Trasformazione colonna datetime in formato datetime
[X] Lowecase sui messaggi
[X] Rimozione tag e siti internet
[ ] Rimozione parola omesso/a
[X] Stemming
[ ] Lemmatization
[X] Rimozione punctuations
"""

PUNCT_TO_REMOVE = string.punctuation

stemmer = SnowballStemmer("italian")
lemmatizer = WordNetLemmatizer()

# Importo la lista delle stopwords
with open('./resources/stopwords.txt') as sw:
    STOPWORDS = sw.read().replace('\n', ' ').split(' ')
    sw.close() 

def lowercase_transform(df):
    df['message'] = df['message'].str.lower()

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])

def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])

def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])

def remove_urls(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)

def remove_tags(text):
    url_pattern = re.compile(r'@\d|@\S+')
    return url_pattern.sub(r'', text)

def remove_omesso(text):
    url_pattern = re.compile(r'[Oo]mess[oa]')
    return url_pattern.sub(r'', text)

def tag_and_http_removal(df):
    pass

def open_and_process_csv(file_name, is_sentiment):
    df = pd.read_csv(file_name, delimiter='~')
    df.dropna(axis=0, how='any', inplace=True)
    df['datetime'] = pd.to_datetime(df['datetime'], dayfirst=True)
    print('Trasformo i messaggi in lowercase')
    lowercase_transform(df)
    print('Rimuovo la punteggiatura')
    df['message'] = df['message'].apply(lambda text: remove_punctuation(text))
    print('Rimuovo le stopwords')
    df['message'] = df['message'].apply(lambda text: remove_stopwords(text))
    print('Rimuovo gli url')
    df['message'] = df['message'].apply(lambda text: remove_urls(text))
    print('Rimuovo i tags')
    df['message'] = df['message'].apply(lambda text: remove_tags(text))
    print('Rimuovo la parola omesso')
    df['message'] = df['message'].apply(lambda text: remove_omesso(text))
    if is_sentiment == 'Y' or is_sentiment == 'y':
        print('Procedo con lo stemming delle parole')
        df['message'] = df['message'].apply(lambda text: stem_words(text))
        print('Procedo con il lemmatization delle parole')
        df['message'] = df['message'].apply(lambda text: lemmatize_words(text))
    return df