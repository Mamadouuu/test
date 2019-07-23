#Importation de flask
from flask import Flask, render_template, url_for


#Création de l'application avec la variable app
app = Flask (__name__)
#.route('/'):demande de la page d'accueil
#Permet d'ajouter des méta-données:information supplémentaire pour configurer la fonction

 

@app.route('/')
def accueil():
    return render_template('accueil.html')


#Exécution de l'application avec run()
if (__name__) == '__main__':
    app.run(debug=True)   #acivation du serveur directement pas besoin de redémarrer l'app