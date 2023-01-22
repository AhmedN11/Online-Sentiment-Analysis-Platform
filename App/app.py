import pickle
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import numpy as np

from flask import Flask, request, render_template


LR = pickle.load(open('../Models/LR.pickle', 'rb'))
vectorizer = pickle.load(open('../Models/TFIDF.pickle', 'rb'))

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

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


app = Flask(__name__, template_folder='template')


@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("query")
        L = ['Neutral', 'Positive', 'Negative']
        result = LR.predict(transform_input(sentence))[0]
        # return "This text is " + L[int(result)]
        mylist = [L[int(result)]]
        return render_template('result.html', mylist=mylist)
    return render_template("index.html")

if __name__=='__main__':
    app.run()
