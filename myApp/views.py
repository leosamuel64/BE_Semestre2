from flask import Flask, render_template, redirect, session, request
from .model import bdd

app=Flask(__name__)
app.template_folder = "template"
app.static_folder="static"
app.config.from_object('myApp.config')

@app.route('/')
def index():
    return render_template("index.html", titre='Home')

@app.route('/prevision.html')
def prevision():
    return render_template("prevision.html", titre='Prévisions')

@app.route('/administration.html')
def administration():
    return render_template("administration.html", titre='Administration')

@app.route('/compte.html')
def compte():
    return render_template("compte.html", titre='Compte')

@app.route('/login.html')
def login():
    return render_template("login.html", titre='Authentification')

@app.route('/webmaster.html')
def webmaster():
    return render_template("webmaster.html", titre='WebMasters')


# -------------------------------------------------------------------------------------



@app.route('/verif_login', methods=["POST"])
def verif_mdp():
    print(request.form)
    login=request.form["login"]
    mdp=request.form["mdp"]
    res = bdd.verifAuthData(login,mdp)
    match res:
        case []:
            session['connected']=False
            session['msg']="Echec de l'authentification"
            return redirect('/login.html')
        case _:
            session['connected']=True
            session['msg']="Authentification réussie"
            session["idUser"]=res[0][0]
            session["nom"]=res[0][1]
            session["prenom"]=res[0][2]
            session["mail"]=res[0][3]
            session["login"]=res[0][4]
            session["statut"]=res[0][6]
            session["newMdp"]=res[0][7]
            
            return redirect('/')
            
@app.route('/logout')
def logout():
    session['connected']=False
    return redirect('/')
            
