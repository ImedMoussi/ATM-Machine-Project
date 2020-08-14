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
                    [CodeClient] CHAR(10) REFERENCES [Client]([CodeClient]),
                    [Solde] FLOAT(50, 2) DEFAULT (0.00)); """)

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
    clt = read_csv("Clients.csv")
    clt.to_sql('Client', cnct, if_exists='append', index=False)

    # Remplir la table "Compte":
    cnt = read_csv("Comptes.csv")
    cnt.to_sql('Compte', cnct, if_exists='append', index=False)

    # Remplir la table "Carte":
    crt = read_csv("Cartes.csv")
    crt.to_sql('Carte', cnct, if_exists='append', index=False)
except:
    pass


def clients():
    clnt_info = cur.execute("SELECT * from Client")
    return clnt_info.fetchall()


def accounts():
    acc_info = cur.execute("SELECT * FROM Compte")
    return acc_info.fetchall()


def cards():
    card_info = cur.execute("SELECT * FROM Carte")
    return card_info.fetchall()


def client_info(code_client):
    clnt = cur.execute("SELECT * FROM Client WHERE CodeClient = ?", (code_client,))
    return clnt.fetchone()


def compte_info(code_client):
    cmpt = cur.execute("SELECT * FROM Compte WHERE CodeClient = ?", (code_client,))
    return cmpt.fetchone()


def carte_info(num_carte):
    cart = cur.execute("SELECT * FROM Carte WHERE NumCarte = ?", (num_carte,))
    return cart.fetchone()


def ajouter_client(code_client, nom_prenom, code_agence, tel, email):
    with cnct:
        cur.execute("INSERT INTO Client VALUES (?, ?, ?, ?, ?)",
                    (code_client, nom_prenom, code_agence, tel, email))


def ajouter_compte(num_compte, code_client, solde):
    with cnct:
        cur.execute("INSERT INTO Compte VALUES (?, ?, ?)", (num_compte, code_client, solde))


def supprimer_compte(num_compte):
    with cnct:
        cur.execute("DELETE FROM Compte WHERE NumCompte = ?", (num_compte,))
        cur.execute("DELETE FROM Carte WHERE NumCompte = ?", (num_compte,))


def deposit(montant, num_compte):
    with cnct:
        cnct.execute("UPDATE Compte SET Solde = Solde + ? WHERE NumCompte = ?", (montant, num_compte))


def withdraw(montant, num_compte):
    with cnct:
        cnct.execute("UPDATE Compte SET Solde = Solde - ? WHERE NumCompte = ?", (montant, num_compte))


def ajouter_carte(num_compte, code_client, num_carte, code_secret, date_exp, etat):
    with cnct:
        cur.execute("INSERT INTO Carte VALUES (?, ?, ?, ?, ?, ?)",
                    (num_compte, code_client, num_carte, code_secret, date_exp, etat))


def supprimer_carte(num_carte):
    with cnct:
        cur.execute("DELETE FROM Carte WHERE NumCarte = ?", (num_carte,))


def change_etat(etat, num_carte):
    with cnct:
        cnct.execute("UPDATE Carte SET EtatCarte = ? WHERE NumCarte = ?", (etat, num_carte))


def change_code(new_code, num_carte):
    with cnct:
        cnct.execute("UPDATE Carte SET CodeSecret = ? WHERE NumCarte = ?", (new_code, num_carte))
