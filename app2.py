from flask import Flask, render_template, redirect, url_for, request, flash
import psycopg2

conn = psycopg2.connect(host="localhost",database="SA", user="postgres", password="DOUmama94")
cur=conn.cursor()

app= Flask(__name__)
app.secret_key = "flash message"

@app.route('/general')
def gene():
     return render_template('general.html')

@app.route('/accueil')
def acueil():
    return render_template('accueil.html')

"""
@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

@app.route('/video3')
def vidoe3():
   return render_template('video3.html')

# @app.route('/referentiel')
# def referentiel():
 """  


###############################  Referents  ################################

## ***************************  LISTE DES REFERENTIELS  ***************** ##

@app.route('/liste',methods = ['POST','GET'])
def liste():
   cur=conn.cursor()
   cur.execute("SELECT * FROM reference")
   data= cur.fetchall()
   conn.commit()
   flash("Vous avez ajoué un référent avec succés!")
   if request.method == 'POST':
      nom_ref = request.form['nom_ref']
      cur.execute("INSERT INTO reference (nom_ref) VALUES (%s)", (nom_ref,))
      conn.commit()
      return redirect (url_for('liste'))
   return render_template('liste.html',dat=data)




#********************************MODIFIER UN REFERENTIEL**********************************************#

@app.route('/referentiel',methods = ['POST', 'GET'])
def referentiel():
   cur=conn.cursor()
   cur.execute("SELECT * FROM reference")
   data=cur.fetchall()

   flash("Vous avez ajoué un référent avec succés!")
   if request.method == 'POST':
      nom_ref = request.form['nom_ref']
      cur.execute("INSERT INTO reference (nom_ref) VALUES (%s)", (nom_ref,))
      conn.commit()
      return redirect (url_for('referentiel'))
   return render_template('referentiel.html',dat=data)

#**************************************************************************#

@app.route('/update',methods = ['POST', 'GET'])
def modif():
   cur=conn.cursor()
   cur.execute("SELECT * FROM reference")
   data=cur.fetchall()
   if request.method == 'POST':
      id = request.form['id_ref']
      nom = request.form['nom_ref']
      cur.execute("UPDATE reference SET nom_ref=%s WHERE id_ref=%s",(nom,id))
      conn.commit()
      return redirect (url_for('referentiel',dat=data))
   # return render_template('referentiel.html',dat=data)
   

                           ##############"  NOUVEAU REFERENTIEL"############

@app.route('/new_ref',methods = ['POST', 'GET'])
def new_ref():
   flash("Vous avez ajoué un référent avec succés!")
   if request.method == 'POST':
      nom_ref = request.form['nom_ref']
      # cur=conn.cursor()
      cur.execute("INSERT INTO reference (nom_ref) VALUES (%s) ", (nom_ref,) )
      conn.commit()
      # conn.close()
      return redirect (url_for('new_ref'))
   return render_template('new_ref.html', )


###########################"  LISTE PROMOTION"  ####################################""

@app.route('/liste_promo',methods = ['POST', 'GET'])
def liste_promo():
   flash("Vous avez ajouté une promotion avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM promotion")
   prom=cur.fetchall()

   cur=conn.cursor()
   cur.execute("SELECT * FROM reference")
   reff=cur.fetchall()

   if request.method == 'POST':
      nom_promo = request.form['nom_promo']
      date_debut = request.form['date_debut']
      date_fin = request.form['date_fin']
      nomRef = int(request.form['nom_ref'])
      
      cur.execute("INSERT INTO promotion (nom_promo, date_debut, date_fin, id_ref) VALUES (%s,%s,%s,%s) ", (nom_promo, date_debut, date_fin, nomRef) )
      conn.commit()
      return redirect (url_for('promotion'))
   return render_template('liste_promo.html',referentiell=reff, promotion=prom)


################################# CREATION ET AJOUT Promotion  ##########################################

@app.route('/promotion',methods = ['POST', 'GET'])
def promotion():
   flash("Vous avez ajouté une promotion avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM promotion")
   prom=cur.fetchall()

   cur=conn.cursor()
   cur.execute("SELECT * FROM reference")
   reff=cur.fetchall()

   if request.method == 'POST':
      nom_promo = request.form['nom_promo']
      date_debut = request.form['date_debut']
      date_fin = request.form['date_fin']
      nomRef = int(request.form['nom_ref'])
      
      cur.execute("INSERT INTO promotion (nom_promo, date_debut, date_fin, id_ref) VALUES (%s,%s,%s,%s) ", (nom_promo, date_debut, date_fin, nomRef) )
      conn.commit()
      return redirect (url_for('promotion'))
   return render_template('promo.html',referentiell=reff, promotion=prom)


                              #########   MODIFIER PROMOTION ##########

@app.route('/tt',methods = ['POST', 'GET'])
def edit():
      flash("Vous avez modifié une promotion avec succés!")
      cur=conn.cursor()
      cur.execute("SELECT * FROM reference ")
      reff=cur.fetchall()

      if request.method == 'POST':
         id_promo = request.form['id_promo']
         nom_promo = request.form['nom_promo']
         date_debut = request.form['date_debut']
         date_fin = request.form['date_fin']
         # nomRef = (request.form['nom_ref'])
         
         cur.execute("UPDATE promotion SET nom_promo = %s, date_debut = %s, date_fin = %s WHERE id_promo=%s ", (nom_promo, date_debut, date_fin, id_promo) )
         conn.commit()
         return redirect (url_for('promotion',referentiell=reff))
      # return render_template('promo.html')

#**********************************************************************************************************#
# @app.route('/edit_prom',methods = ['POST', 'GET'])
# def edit_prom():
#    cur=conn.cursor()
#    cur.execute("SELECT * FROM promotion  ")
#    prom=cur.fetchall()

#    if request.method == 'POST':
#       id_promo = request.form['id_promo']
#       nom_promo = request.form['nom_promo']
#       date_debut = request.form['date_debut']
#       date_fin = request.form['date_fin']
#       id_ref = request.form['id_ref']

#          # nomRef = int(request.form['nom_ref'])
         
#       cur.execute("UPDATE promotion SET nom_promo=%s, date_debut=%s, date_fin=%s WHERE id_promo=%s,id_ref=%s", (nom_promo,date_debut,date_fin,id_promo,id_ref)  )
#       conn.commit()
#    return redirect (url_for('promotion',promo=prom))


                           #################"" NOUVEAU PROMOTION ###########

@app.route('/new_prom',methods = ['POST', 'GET'])
def new_prom():
   flash("Vous avez ajouté une promotion avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM reference  ")
   reff=cur.fetchall()

   if request.method == 'POST':
      nom_promo = request.form['nom_promo']
      date_debut = request.form['date_debut']
      date_fin = request.form['date_fin']
      nomRef = int(request.form['nom_ref'])
      
      cur.execute("INSERT INTO promotion (nom_promo, date_debut, date_fin, id_ref) VALUES (%s,%s,%s,%s) ", (nom_promo, date_debut, date_fin, nomRef) )
      conn.commit()
   return render_template('new_prom.html',  i=reff)






################################  LISTE APPRENANT ########################

@app.route('/liste_apprenant',methods = ['POST', 'GET'])
def liste_apprenant():
   flash("Vous avez ajouté un apprenant avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM promotion")
   promm=cur.fetchall()

   cur=conn.cursor()
   cur.execute("SELECT * FROM apprenant")
   appren=cur.fetchall()

   if request.method == 'POST':
      matricule = request.form['matricule']
      prenom_app = request.form['prenom']
      nom_app = request.form['nom']
      phon = int(request.form['phon'])
      email = request.form['email']
      statut = request.form['statut']
      nomprom = int(request.form['nom_promo'])
      cur.execute("INSERT INTO apprenant (matricule, prenom_app, nom_app, phon, email,statut, id_promo) VALUES (%s,%s,%s,%s,%s,%s,%s) ", (matricule, prenom_app, nom_app, phon, email,statut, nomprom) )
      conn.commit()
      return redirect (url_for('liste_apprenant'))
   return render_template('liste_apprenant.html', promotion=promm, apprenant=appren)



#################################### Apprenant  #########################

@app.route('/apprenant',methods = ['POST', 'GET'])
def apprenant():
   flash("Vous avez ajouté un apprenant avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM promotion")
   promm=cur.fetchall()

   cur=conn.cursor()
   cur.execute("SELECT * FROM apprenant")
   appren=cur.fetchall()

   if request.method == 'POST':
      matricule = request.form['matricule']
      prenom_app = request.form['prenom']
      nom_app = request.form['nom']
      phon = int(request.form['phon'])
      email = request.form['email']
      statut = request.form['statut']
      nomprom = int(request.form['nom_promo'])
      cur.execute("INSERT INTO apprenant (matricule, prenom_app, nom_app, phon, email,statut, id_promo) VALUES (%s,%s,%s,%s,%s,%s) ", (matricule, prenom_app, nom_app, phon, email, statut, nomprom) )
      conn.commit()
      return redirect (url_for('apprenant'))
   return render_template('apprenant.html', promotion=promm, apprenant=appren)



                                ################### MODIFIER APPRENANT #####################

@app.route('/kk',methods = ['POST', 'GET'])
def edite():
      flash("Vous avez modifié une promotion avec succés!")
      cur=conn.cursor()
      cur.execute("SELECT * FROM promotion ")
      promm=cur.fetchall()


      if request.method == 'POST':
         id = request.form['id_app']
         matricule = request.form['matricule']
         prenom_app = request.form['prenom']
         nom_app = request.form['nom']
         phon = int(request.form['phon'])
         email = request.form['email']
         statut = request.form['statut']
         # nomprom = request.form['nom_promo']
         # nomRef = (request.form['nom_ref'])
         
         cur.execute("UPDATE apprenant SET matricule = %s, prenom_app = %s, nom_app  = %s, phon = %s, email = %s,statut = %s WHERE id_app = %s " , (matricule, prenom_app, nom_app, phon, email,statut, id) )
         # cur.execute("UPDATE promotion SET nom_promo = %s, date_debut = %s, date_fin = %s WHERE id_promo=%s ", (nom_promo, date_debut, date_fin, id_promo) )
         conn.commit()
         return redirect (url_for('apprenant',promotion=promm))
      


@app.route('/redi',methods = ['POST', 'GET'])
def redirecte():
      if request.method == 'POST':
         matricule = request.form['matricule']
         prenom_app = request.form['prenom']
         nom_app = request.form['nom']
         phon = int(request.form['phon'])
         email = request.form['email']
         statut = request.form['statut']
         nomprom = int(request.form['nom_promo'])
         cur.execute("INSERT INTO apprenant (matricule, prenom_app, nom_app, phon, email,statut, id_promo) VALUES (%s,%s,%s,%s,%s,%s) ", (matricule, prenom_app, nom_app, phon, email, statut, nomprom) )
         conn.commit()
         return redirect(url_for('redirect'))
      return render_template('suspendre.html')




                                ################### SUSPENDRE APPRENANT #####################

@app.route('/supendre',methods = ['POST', 'GET'])
def suspendre():
      flash("Vous avez suspendu une promotion avec succés!")
      cur=conn.cursor()
      cur.execute("SELECT * FROM promotion ")
      promm=cur.fetchall()

      cur=conn.cursor()
      cur.execute("SELECT * FROM apprenant")
      appren=cur.fetchall()


      if request.method == 'POST':
         id = request.form['id_app']
         matricule = request.form['matricule']
         prenom_app = request.form['prenom']
         nom_app = request.form['nom']
         phon = int(request.form['phon'])
         email = request.form['email']
         statut = request.form['statut']
         # nomprom = request.form['nom_promo']
         # nomRef = (request.form['nom_ref'])
         
         cur.execute("UPDATE apprenant SET matricule = %s, prenom_app = %s, nom_app  = %s, phon = %s, email = %s, statut = %s WHERE id_app = %s " , (matricule, prenom_app, nom_app, phon, email,statut, id) )
         # cur.execute("UPDATE promotion SET nom_promo = %s, date_debut = %s, date_fin = %s WHERE id_promo=%s ", (nom_promo, date_debut, date_fin, id_promo) )
         conn.commit()
         return redirect (url_for('apprenant',promotion=promm))
      return render_template('suspendre.html', promotion=promm, apprenant=appren)

      # return render_template('suspendre.html' ,promotion=promm)
      
#### ###################################   ANNULER APPRENANT  ###########################

@app.route('/annuler/<string:id_app>',methods = ['POST', 'GET'])
def annuler(id_app):
   cur=conn.cursor()
   cur.execute("DELETE FROM apprenant WHERE id_app = %s", (id_app))
   conn.commit()
   redirect(url_for('apprenant'))


                                 ##################   NOUVEAU APPRENANT  ####################
@app.route('/new_app',methods = ['POST', 'GET'])
def new_app():
   flash("Vous avez ajouét un apprenant avec succés!")
   cur=conn.cursor()
   cur.execute("SELECT * FROM promotion")
   promm=cur.fetchall()
   if request.method == 'POST':
      matricule = request.form['matricule']
      prenom_app = request.form['prenom']
      nom_app = request.form['nom']
      phon = int(request.form['phon'])
      email = request.form['email']
      statut = request.form['statut']
      nomprom = request.form['nom_promo']
      cur.execute("INSERT INTO apprenant (matricule, prenom_app, nom_app, phon, email,statut, id_promo) VALUES (%s,%s,%s,%s,%s,%s,%s) ", (matricule, prenom_app, nom_app, phon, email,statut, nomprom) )
      conn.commit()
   return render_template('new_app.html', prom=promm)



 

# @app.route('/dd',methods = ['POST', 'GET'])
# def edite():
#    flash("Vous avez modifié un apprenant avec succés!")
#    cur=conn.cursor()
#    cur.execute("SELECT * FROM promotion")
#    promm=cur.fetchall()
#    if request.method == 'POST':
#       id_app = request.form['id_app']
#       matricule = request.form['matricule']
#       prenom_app = request.form['prenom']
#       nom_app = request.form['nom']
#       phon = int(request.form['phon'])
#       email = request.form['email']
#       # nomprom = request.form['nom_promo']
#       cur.execute("UPDATE apprenant SET matricule = %s, prenom_app = %s, nom_app  = %s, phon = %s, email = %s, WHERE id_app =%s" ,(matricule, prenom_app, nom_app, phon, email, id_app) )
#       conn.commit()
#       return redirect (url_for('apprenant', promotion=promm))
#    # return render_template('edit_app.html', apprenant=appren)


if __name__ == "__main__":
   
   app.run(debug=True)


