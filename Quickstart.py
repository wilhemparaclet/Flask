#Flask App

#On importe Flask 
from flask import Flask


#On import la librairie pour charger des templates
from flask import render_template

#On créer l'instance de l'appli Flask
#Le paramètre name sert à déterminer le nom de l’application en fonction de si elle est démarrée en tant qu’application ou alors en tant que module d’une application.

#Si le paramètre name = main alors ça veut dire que l'appli est démarrée
app = Flask(__name__)

#Il s'agit d'un décorateur = défini l'URL ou un requête via ce décorateur
@app.route("/")

def index():
 return "Hello DC!"

#On definit une seconde vue about
@app.route("/txt/<name>")

def hello(name = None) :
	return render_template('txt.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)

