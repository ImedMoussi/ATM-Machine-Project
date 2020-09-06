import sqlite3
from pandas import read_csv

cnct = sqlite3.connect('DAB_BDD.db')
cur = cnct.cursor()

with cnct:
    # La table "Clients":
    cur.execute(""" CREATE TABLE IF NOT EXISTS [Client](
                    [CodeClient] CHAR(10) PRIMARY KEY NOT NULL UNIQUE,
                    [NomPrenom] CHAR(25) NOT NULL, 
                    [CodeAgence] INTEGER(3),
                    [Tel] CHAR(10), 
                    [Email] CHAR(30)); """)

    # La table "Compte":
    cur.execute(""" CREATE TABLE IF NOT EXISTS [Compte](
                    [NumCompte] CHAR(10) PRIMARY KEY NOT NULL UNIQUE,
                    [CodeClient] CHAR(10) REFERENCES [Client]([CodeClient]),
                    [Solde] FLOAT(50,2) DEFAULT (0.00)); """)

    # La table "Carte":
    cur.execute(""" CREATE TABLE IF NOT EXISTS [Carte](
                    [NumCompte] CHAR(10) REFERENCES [Compte]([NumCompte]),
                    [CodeClient] CHAR(10) REFERENCES [Client]([CodeClient]),
                    [NumCarte] CHAR(10) PRIMARY KEY NOT NULL UNIQUE,
                    [CodeSecret] INTEGER(4) NOT NULL UNIQUE,
                    [DateExpiration] DATE NOT NULL,
                    [EtatCarte] BOOLEAN NOT NULL); """)

try:
    # Remplir la table "Client":
    clts = read_csv(r"CSV\Clients.csv")
    clts.to_sql('Client', cnct, if_exists='append', index=False)

    # Remplir la table "Compte":
    cnts = read_csv(r"CSV\Comptes.csv", dtype={'NumCompte': 'str'})
    cnts.to_sql('Compte', cnct, if_exists='append', index=False)

    # Remplir la table "Carte":
    crts = read_csv(r"CSV\Cartes.csv", dtype={'NumCompte': 'str', 'NumCarte': 'str'})
    crts.to_sql('Carte', cnct, if_exists='append', index=False)
except:
    pass


def clients():
    clnts = cur.execute("SELECT * from Client;")
    return clnts.fetchall()


def accounts():
    accts = cur.execute("SELECT * FROM Compte;")
    return accts.fetchall()


def cards():
    carts = cur.execute("SELECT * FROM Carte;")
    return carts.fetchall()


def client_info(code_client):
    clnt_info = cur.execute("SELECT * FROM Client WHERE CodeClient = ?;", (code_client,))
    return clnt_info.fetchone()


def compte_info(code_client):
    cmpt_info = cur.execute("SELECT * FROM Compte WHERE CodeClient = ?;", (code_client,))
    return cmpt_info.fetchone()


def carte_info(num_carte):
    cart_info = cur.execute("SELECT * FROM Carte WHERE NumCarte = ?;", (num_carte,))
    return cart_info.fetchone()


def ajouter_client(code_client, nom_prenom, code_agence, tel, email):
    with cnct:
        cur.execute("INSERT INTO Client VALUES (?, ?, ?, ?, ?);",
                    (code_client, nom_prenom, code_agence, tel, email))


def ajouter_compte(num_compte, code_client, solde):
    with cnct:
        cur.execute("INSERT INTO Compte VALUES (?, ?, ?);", (num_compte, code_client, solde))


def supprimer_compte(num_compte):
    with cnct:
        cur.execute("DELETE FROM Compte WHERE NumCompte = ?;", (num_compte,))
        cur.execute("DELETE FROM Carte WHERE NumCompte = ?;", (num_compte,))


def retirer(num_compte, montant):
    with cnct:
        cur.execute("UPDATE Compte SET Solde = Solde - ? WHERE NumCompte = ?;", (montant, num_compte))


def deposer(num_compte, montant):
    with cnct:
        cur.execute("UPDATE Compte SET Solde = Solde + ? WHERE NumCompte = ?;", (montant, num_compte))


def ajouter_carte(num_compte, code_client, num_carte, code_secret, date_exp, etat):
    with cnct:
        cur.execute("INSERT INTO Carte VALUES (?, ?, ?, ?, ?, ?);",
                    (num_compte, code_client, num_carte, code_secret, date_exp, etat))


def supprimer_carte(num_carte):
    with cnct:
        cur.execute("DELETE FROM Carte WHERE NumCarte = ?;", (num_carte,))


def change_etat(etat, num_carte):
    with cnct:
        cur.execute("UPDATE Carte SET EtatCarte = ? WHERE NumCarte = ?;", (etat, num_carte))


def change_code(num_carte, new_code):
    with cnct:
        cur.execute("UPDATE Carte SET CodeSecret = ? WHERE NumCarte = ?;", (new_code, num_carte))

# TODO: Ki takhlass la date exp twali la carte invalide (bloquer)
