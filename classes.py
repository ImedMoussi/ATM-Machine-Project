import numpy as np
from datetime import datetime
from __MiniProjet import dab_db


class Client:

    def __init__(self, code_client=None, client_name=None, code_agence=None, tel=None, email=None):
        self.CodeClient = code_client
        self.NomPrenom = client_name
        self.CodeAgence = code_agence
        self.Tel = tel
        self.Email = email

    @staticmethod
    def generate_client_code():
        while True:
            client = str(np.random.randint(1, 99999)).rjust(5, "0")
            codes = [i[0] for i in dab_db.clients_info()]
            if client in codes:
                continue
            return client

    def ajouter_client(self, nom_prenom, code_agence, tel, email):
        self.CodeClient = Client.generate_client_code()
        self.NomPrenom = nom_prenom
        self.CodeAgence = code_agence
        self.Tel = tel
        self.Email = email
        dab_db.ajouter_client(self.CodeClient, self.NomPrenom, self.CodeAgence, self.Tel, self.Email)

    class Compte:

        def __init__(self, code_client, num_compte=None, solde=0.00):
            self.NumCompte = num_compte
            self.CodeClient = code_client
            self.Solde = solde

        def debiter(self, montant):
            self.Solde -= montant
            return self.Solde

        def crediter(self, montant):
            self.Solde += montant
            return self.Solde

        def consulter_solde(self):
            return self.Solde

        def ajouter_compte(self, code_client):
            self.NumCompte = str(max(int(i[0]) for i in dab_db.accounts_info()) + 1)
            self.CodeClient = code_client
            self.Solde = 0.00
            dab_db.ajouter_compte(self.NumCompte, self.CodeClient, self.Solde)

        def supprimer_compte(self, code_client):
            self.NumCompte = None
            self.Solde = 0.00
            dab_db.supprimer_compte(code_client)

        class Carte:

            def __init__(self, num_compte, code_client, num_carte=None, code_secret=None,
                         date_expiration=None, etat_carte=None):
                self.NumCompte = num_compte
                self.CodeClient = code_client
                self.NumCarte = num_carte
                self.CodeSecret = code_secret
                self.DateExpiration = date_expiration
                self.EtatCarte = etat_carte

            @staticmethod
            def generate_card_number():
                lst = list()
                while True:
                    for i in range(4):
                        s = str(np.random.randint(1, 9999)).rjust(4, '0')
                        lst.append(s)
                    num = '-'.join(lst)
                    numero_cartes = [i[2] for i in dab_db.cards_info()]
                    if num in numero_cartes:
                        continue
                    return num

            @staticmethod
            def generate_secret_code():
                while True:
                    code = int(str(np.random.randint(1, 9999)).rjust(4, "0"))
                    codes = [i[3] for i in dab_db.cards_info()]
                    if code in codes:
                        continue
                    return code

            def ajouter_carte(self, num_compte, code_client):
                self.NumCompte = num_compte
                self.CodeClient = code_client
                self.NumCarte = Client.Compte.Carte.generate_card_number()
                self.CodeSecret = Client.Compte.Carte.generate_secret_code()
                self.DateExpiration = datetime.now().date()
                # TODO: year += 4 yrs, GO TO Try code, maybe I'll create a function do this ...
                self.EtatCarte = True
                dab_db.ajouter_carte(self.NumCompte, self.CodeClient, self.NumCarte,
                                     self.CodeSecret, self.DateExpiration, self.EtatCarte)

            def blouquer_carte(self):
                self.EtatCarte = False

            @staticmethod
            def supprimer_carte(num_carte):
                dab_db.supprimer_carte(num_carte)

            def deblouquer_cart(self):
                self.EtatCarte = True

            def modifier_code_secret(self, code):
                self.CodeSecret = code


# TODO: the last function ... how it work !!?
