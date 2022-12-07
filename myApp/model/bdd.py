import sqlite3
import hashlib

CHEMIN_BASE="myApp/model/base.db"


def get_membresData():
    """
    Ajoute un utilisateur dans la base de données SQL
    """
    connection = sqlite3.connect(CHEMIN_BASE)

    request = """
    SELECT * 
    FROM Membres
    """

    cursor = connection.execute(request)
    res=[]
    for x in cursor:
        if x!=None:
            res.append(x)
    
    connection.commit()
    connection.close()
    return res


def verifAuthData(login,mdp):
    connection = sqlite3.connect(CHEMIN_BASE)
    mdp=hashlib.sha256(mdp.encode())
    mdpC=mdp.hexdigest()
    request = '''
               SELECT * FROM Identification
                WHERE login="'''+login+'" AND motPasse="'+mdpC+'"'
    cursor = connection.execute(request)
    res=[]
    for x in cursor:
        res.append(x)

    connection.commit()
    connection.close()
    return res

def SuppMembreBdd(idUser):
    """
    Change le mot de passe dans la base de données SQL
    """
    connection = sqlite3.connect(CHEMIN_BASE)

    request = """
    DELETE from Membre
        where idUser='"""+idUser+"'"

    connection.execute(request)
    connection.commit()
    connection.close()

def add_membreData(nom,prenom,mail,login,motPasse,statut,newmdp=1):
    """
    Change le mot de passe dans la base de données SQL
    """
    connection = sqlite3.connect(CHEMIN_BASE)

    request = "INSERT INTO identification (nom, prenom, mail, login, motPasse, statut, newMdp) VALUES ('{}','{}','{}','{}','{}',{},{});".format(nom,prenom,mail,login,motPasse,statut,newmdp)

    connection.execute(request)
    connection.commit()
    connection.close()
    
def updateMembreData(champ, idUser,newvalue):
    connection = sqlite3.connect(CHEMIN_BASE)

    request = "UPDATE identification SET "+champ+"='"+newvalue+"' WHERE idUser = "+idUser+";"

    connection.execute(request)
    connection.commit()
    connection.close()