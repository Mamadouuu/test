
from flask import Flask, render_template, request, flash, url_for, redirect
import psycopg2 as psy
import psycopg2

####################" Création des tables dans la base de données SA " ########################

conn = psycopg2.connect(host="localhost",database="SA", user="postgres", password="DOUmama94")

cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Reference(
                        id_ref serial PRIMARY KEY NOT NULL,
                        nom_ref text NULL)
                    """)


cur.execute("""CREATE TABLE IF NOT EXISTS Promotion(
                        id_promo serial PRIMARY KEY NOT NULL,
                        nom_promo text NULL,
                        date_debut text NULL,
                        date_fin text NULL,
                        id_ref int REFERENCES Reference)
                    """)



cur.execute("""CREATE TABLE IF NOT EXISTS Apprenant(
                        id_app serial PRIMARY KEY NOT NULL,
                        matricule text NULL,
                        prenom_app text NULL,
                        nom_app text NULL,
                        phon int NULL,
                        email text NULL,
                        statut text NULL,
                        id_promo int REFERENCES Promotion)
                    """)

conn.commit()
conn.close()

"""
###################################  Connection entre ################################
curseur = conn.cursor()
app = Flask(__name__) #permet de localiser les ressources cad les templates

@app.route('/')
def index():
    return render_template("accueil.html")



@app.route('/referent/nouveau', methods=["POST"])
def inf_ref():
    if request.method == "POST":
        nom_ref = request.form["nom_ref"]
        requete_ajout_ref = "INSERT INTO referentiel (libelle) VALUES (%s)"
        curseur.execute(requete_ajout_ref,(nom_ref,))
        conn.commit()
        return redirect(url_for('ajouter_ref'))



if __name__ == '__main__': #si le fichier est executer alors execute le bloc
    app.run(debug=True) #debug=True relance le serveur à chaque modification
"""



