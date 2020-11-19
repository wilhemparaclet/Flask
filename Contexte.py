#On importe Flask, render_template et jsonify  
from flask import Flask,render_template,jsonify,Response

#On importe json
import json 

app = Flask(__name__)

#Definir les routes
@app.route("/")

def index():
    return "Welcome to my app"

#On instancie notre livre
books=[
    {
        "id":1,
        "titre" : 'untitre',
    },
    {
        "id":2,
        "titre": "unautretitrerandom",
    }
]

#On affiche les livres continue dans la liste
@app.route("/api/books", methods=["GET"])

#Ont utilise la fonction jsonnify pour afficher l'intégralité d'un fichier type json
def afficher_book() :
	return jsonify(books)

@app.route("/api/books/<int:book_id>", methods=["GET"])

def search(book_id):

    # On créer un tableau vide afin de stocké les résultats
    livre = []

    #On parcours la liste books
    for book in books:

    	# pour chaque livre qui a un id identique à celui dans l'url on l'ajoute dans notre tableau de résultat
        if book["id"] == book_id:

            livre.append(book)
            #On affiche le résultat du livre trouver
            return jsonify(livre)

        else :
        	# il affiche un message d'erreur
            return "Aucun livre ne conrespond à cette identifiants"

@app.route("/api/books/<string:book_title>")

#
def title(book_title) :

    #On créer un tableau vide pour stocké les livres trouvés
    trouver = []

    #On parcours notre liste & pour chaque livres trouvés on l'ajoute à notre tableau vide
    for book in books :

        #Si la condition est exact, alors on l'ajoute au tableau
        if book["titre"] == book_title :

            trouver.append(book)

            #on retourne le résult
            return jsonify(trouver)

        else :

            #affiche un message d'erreur
            return "Aucun livre ne corresonds a ceux titre ce titre"

@app.route('/config')
def config():
    with open("books.json","r") as f:
        return Response(headers={"Content-Type":"application/json"},response=f.read())

if __name__ == "__main__":
    app.run(debug=True)