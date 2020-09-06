from __MiniProjet import data_base as db


class Client:

    def __init__(self, code_client, client_name, code_agence, tel, email):
        self.CodeClient = code_client
        self.NomPrenom = client_name
        self.CodeAgence = code_agence
        self.Tel = tel
        self.Email = email

    def ajouter_client(self):
        db.ajouter_client(self.CodeClient, self.NomPrenom, self.CodeAgence, self.Tel, self.Email)

    class Compte:

        def __init__(self, code_client, num_compte=None, solde=0):
            self.NumCompte = num_compte
            self.CodeClient = code_client
            self.Solde = solde

        def debiter(self, montant):
            self.Solde -= montant
            db.retirer(self.NumCompte, montant)

        def crediter(self, montant):
            self.Solde += montant
            db.deposer(self.NumCompte, montant)

        def consulter_solde(self):
            return self.Solde

        def ajouter_compte(self, num_compte):
            self.NumCompte = num_compte
            self.Solde = 0
            db.ajouter_compte(self.NumCompte, self.CodeClient, self.Solde)

        def supprimer_compte(self):
            db.supprimer_compte(self.NumCompte)
            self.NumCompte = None
            self.Solde = 0

        class Carte:

            def __init__(self, num_compte, code_client, num_carte, code_secret,
                         date_expiration, etat_carte=True):
                self.NumCompte = num_compte
                self.CodeClient = code_client
                self.NumCarte = num_carte
                self.CodeSecret = code_secret
                self.DateExpiration = date_expiration
                self.EtatCarte = etat_carte

            def ajouter_carte(self):
                db.ajouter_carte(self.NumCompte, self.CodeClient, self.NumCarte,
                                 self.CodeSecret, self.DateExpiration, self.EtatCarte)

            def bloquer_carte(self, num_carte):
                self.NumCarte = num_carte
                self.EtatCarte = False
                db.change_etat(self.EtatCarte, self.NumCarte)

            def supprimer_carte(self, num_carte):
                self.NumCarte = num_carte
                db.supprimer_carte(self.NumCarte)

            def debloquer_cart(self, num_carte):
                self.NumCarte = num_carte
                self.EtatCarte = True
                db.change_etat(self.EtatCarte, self.NumCarte)

            def modifier_code_secret(self, num_carte, code):
                self.NumCarte = num_carte
                self.CodeSecret = code
                db.change_code(self.NumCarte, self.CodeSecret)

# TODO: public & private
