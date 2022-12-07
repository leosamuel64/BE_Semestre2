from flask import Flask, render_template, redirect, session, request
from .model import bdd
from . import fonctions
from flask_mail import Mail, Message



app=Flask(__name__)
app.template_folder = "template"
app.static_folder="static"
app.config.from_object('myApp.config')
email = Mail(app)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'cea3170a21d1f1'
app.config['MAIL_PASSWORD'] = 'baa685dcdf4b56'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

@app.route('/')
def index():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("index.html", titre='Home')

@app.route('/prevision.html')
def prevision():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("prevision.html", titre='Prévisions')

@app.route('/administration.html')
def administration():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("administration.html", titre='Administration')

@app.route('/compte.html')
def compte():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("compte.html", titre='Compte')

@app.route('/login.html')
def login():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("login.html", titre='Authentification')

@app.route('/webmaster.html')
def webmaster():
    if 'newMdp' in session and session['newMdp']=='1':
        return redirect('/newMdp.html')
    else:
        return render_template("webmaster.html", titre='WebMasters')

@app.route('/newMdp.html')
def nouveauMdp():
    return render_template("newMdp.html", titre='nouveau mot de passe')


# -------------------------------------------------------------------------------------



@app.route('/verif_login', methods=["POST"])
def verif_mdp():
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
    session.clear()
    return redirect('/')
            
@app.route('/ajouteCompte', methods=["POST"])
def ajouteCompte():
    nom=request.form["nom"]
    prenom=request.form["prenom"]
    mail=request.form["mail"]
    login=request.form["login"]
    statut=request.form["statut"] 
    mdp=fonctions.randomPassword()
    bdd.add_membreData(nom,
                       prenom,
                       mail,
                       login,
                       fonctions.hashMdp(mdp),
                       statut)
    session['newMdp']=mdp
    # msg=Message('Creation de compte',
    #             sender='yomale9967@cosaxu.com',
    #             recipients=[mail])
    # msg.body='Votre login est : {} \n\n Votre mot de passe est: {}'.format(login,mdp)
    # email.send(msg)
    
    return redirect('/compte.html')

@app.route('/newMdp', methods=["POST"])
def changeMdp():
    mdp1=request.form["mdp1"]
    mdp2=request.form["mdp2"]
    
    if mdp1==mdp2:
        bdd.updateMembreData('motPasse',str(session['idUser']),str(fonctions.hashMdp(mdp1)))
        bdd.updateMembreData('newMdp',str(session['idUser']),'0')
        session['newMdp']=0
        return redirect('/')
    else:
        return redirect('/newMdp.html')
    
    
    