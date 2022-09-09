from flask import Flask, render_template, request, send_file, redirect, url_for, Response, redirect
from personnage import *
from compteurEnnemisTues import *
from fight import *
from createMob import *

app = Flask(__name__, template_folder='.')

import sys 
import os

@app.route('/', methods=['GET','POST'])

def home():
    if request.form:
        compteurkills = 0
        listeVaincus = []
        pseudo = request.form['pseudo']
        
        MonPerso = personnage(pseudo, 20, 5, 2)


        while MonPerso[1] > 0:
            Ennemi = createMob()
            fight(MonPerso, Ennemi)

            if MonPerso[1] > 0:
                compteurkills=compteurEnnemisTue(compteurkills)
                listeVaincus.append(Ennemi)
        
        return render_template('/templates/home.html', pseudo=pseudo, compteurkills=compteurkills, listeVaincus=listeVaincus)
    return render_template('/templates/home.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8001)

