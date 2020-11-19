from flask import Flask,render_template
from jinja2 import Template

app = Flask(__name__)
    

@app.route("/")
def index(name='Wilhem'):
    return "Hello {}".format(name.capitalize())

@app.route("/")
@app.route("/text/")
def text():
    return render_template('text.html', name = 'Wilhem')

@app.route("/")
@app.route("/txt/")
def txt():
    return render_template('txt.html', name = 'Daniel')


if __name__ == "__main__":
    app.run(debug=True)
    

