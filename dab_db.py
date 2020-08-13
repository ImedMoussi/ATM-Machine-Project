import sqlite3
from pandas import read_csv

# cnct = sqlite3.connect(':memory:')
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
                    [CodeClient] CHAR(10) REFERENCES [Client]([CodeClient]) ON DELETE CASCADE,
                    [Solde] CURRENCY(50, 2) DEFAULT (00.00)); """)

    # La table "Carte":
    cur.execute(""" CREATE TABLE IF NOT EXISTS [Carte](
                    [NumCompte] CHAR(10) REFERENCES [Compte]([NumCompte]) ON DELETE CASCADE,
                    [CodeClient] CHAR(10) REFERENCES [Client]([CodeClient]) ON DELETE CASCADE,
                    [NumCarte] CHAR(10) PRIMARY KEY NOT NULL UNIQUE,
                    [CodeSecret] INTEGER(4) NOT NULL UNIQUE,
                    [DateExpiration] DATE NOT NULL,
                    [EtatCarte] BOOLEAN NOT NULL); """)

# TODO: Try-except; pour eviter le problème UNIQUE
# Remplir la table "Client":
clt = read_csv("Clients.csv")
clt.to_sql('Client', cnct, if_exists='append', index=False)

# Remplir la table "Compte":
cnt = read_csv("Comptes.csv")
cnt.to_sql('Compte', cnct, if_exists='append', index=False)

# Remplir la table "Carte":
crt = read_csv("Cartes.csv")
crt.to_sql('Carte', cnct, if_exists='append', index=False)


# ---------------------------------------------------------------------------------------------
def clients_info():
    client_info = cur.execute(" SELECT * from Client ")
    return client_info.fetchall()


def accounts_info():
    account_info = cur.execute(" SELECT * FROM Compte ")
    return account_info.fetchall()


def cards_info():
    card_info = cur.execute(" SELECT * FROM Carte ")
    return card_info.fetchall()


# ---------------------------------------------------------------------------------------------
def client(client_name):
    clnt = cur.execute(" SELECT * FROM Client WHERE NomPrenom = ? ", (client_name,))
    return clnt.fetchone()


def compte(code_client):
    cmpt = cur.execute(" SELECT * FROM Compte WHERE CodeClient = ? ", (code_client,))
    return cmpt.fetchone()


def carte(num_compte):
    cart = cur.execute(" SELECT * FROM Carte WHERE NumCompte = ? ", (num_compte,))
    return cart.fetchone()


# def secret_code(card_num):  # -----GUI-----
#     card_code = cur.execute(""" SELECT CodeSecret FROM Carte WHERE NumCarte = ? """, (card_num,))
#     return card_code.fetchone()


def ajouter_client(code_client, nom_prenom, code_agence, tel, email):
    with cnct:
        cur.execute(" INSERT INTO Client Values (?, ?, ?, ?, ?) ",
                    (code_client, nom_prenom, code_agence, tel, email))


def ajouter_compte(num_compte, code_client, solde):
    with cnct:
        cur.execute(" INSERT INTO Compte Values (?, ?, ?) ", (num_compte, code_client, solde))


def supprimer_compte(code_client):
    with cnct:
        cur.execute(" DELETE FROM Compte WHERE CodeClient = ? ", (code_client,))


def ajouter_carte(num_compte, code_client, num_carte, code_secret, date_exp, etat):
    with cnct:
        cur.execute(" INSERT INTO Carte Values (?, ?, ?, ?, ?, ?) ",
                    (num_compte, code_client, num_carte, code_secret, date_exp, etat))


def supprimer_carte(num_carte):
    with cnct:
        cur.execute(" DELETE FROM Carte WHERE NumCarte = ? ", (num_carte,))


# TODO: see if with cnct works or not !!?
