import pandas as pd
import numpy as np
import pickle
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

LR = pickle.load(open('../Models/LR.pickle', 'rb'))
vectorizer = pickle.load(open('../Models/TFIDF.pickle', 'rb'))

def process_text(sentence) :
        
    tokenized = word_tokenize(str(sentence))
    tokenized_lowcase = [word.lower() for word in tokenized]
    filtered_sentence = [word for word in tokenized_lowcase if not word in stop_words and word.isalpha()]
    stemmed = [stemmer.stem(word) for word in filtered_sentence]
    final = ' '.join(stemmed)
    return final


def transform_input(sentence) :
    sentence = process_text(sentence)
    sentence = pd.DataFrame({'body' : [sentence]})
    sentence = vectorizer.transform(np.array(sentence).reshape(-1,))
    return sentence