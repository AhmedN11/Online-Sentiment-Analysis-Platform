from flask import Flask, request, render_template
from processing import *


app = Flask(__name__, template_folder='template')


@app.route('/', methods =["GET", "POST"])
def index():
    if request.method == "POST":
        sentence = request.form.get("query")
        L = ['Neutral', 'Positive', 'Negative']
        result = LR.predict(transform_input(sentence))[0]
        mylist = [L[int(result)]]
        return render_template('result.html', mylist=mylist)
    return render_template("index.html")

if __name__=='__main__':
    app.run()