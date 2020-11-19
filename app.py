from flask import Flask,render_template,jsonify
from jinja2 import Template

import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('text.html', name = 'Wilhem')

@app.route("/txt/")
def txt():
    return render_template('txt.html', name = 'Daniel')
book=[
    {
       'id':1,
       'titre' : 'un titre',
    },
    {
       'id':2,
       'titre': 'un autre titre random',
    }
]
book_json = json.dumps(book, separators=(',',':'))

@app.route('/api/books/', methods=["GET"])
def books():
    return book_json

if __name__ == "__main__":
    app.run(debug=True)
    
