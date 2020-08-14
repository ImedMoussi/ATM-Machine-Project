from __MiniProjet import dab_db


class Client:

    def __init__(self, code_client, client_name, code_agence, tel, email):
        self.CodeClient = code_client
        self.NomPrenom = client_name
        self.CodeAgence = code_agence
        self.Tel = tel
        self.Email = email

    def ajouter_client(self):
        dab_db.ajouter_client(self.CodeClient, self.NomPrenom, self.CodeAgence, self.Tel, self.Email)

    class Compte:

        def __init__(self, code_client, num_compte=None, solde=0.00):
            self.NumCompte = num_compte
            self.CodeClient = code_client
            self.Solde = solde

        def debiter(self, montant):
            self.Solde -= montant
            dab_db.withdraw(montant, self.NumCompte)
            return self.Solde

        def crediter(self, montant):
            self.Solde += montant
            dab_db.deposit(montant, self.NumCompte)
            return self.Solde

        def consulter_solde(self):
            return self.Solde

        def ajouter_compte(self):
            self.NumCompte = str(max(int(i[0]) for i in dab_db.accounts()) + 1)
            self.Solde = 0
            dab_db.ajouter_compte(self.NumCompte, self.CodeClient, self.Solde)

        def supprimer_compte(self):
            dab_db.supprimer_compte(self.NumCompte)
            self.NumCompte = None
            self.Solde = 0.00

        class Carte:

            def __init__(self, num_compte, code_client, num_carte, code_secret,
                         date_expiration, etat_carte):
                self.NumCompte = num_compte
                self.CodeClient = code_client
                self.NumCarte = num_carte
                self.CodeSecret = code_secret
                self.DateExpiration = date_expiration
                self.EtatCarte = etat_carte

            def ajouter_carte(self):
                dab_db.ajouter_carte(self.NumCompte, self.CodeClient, self.NumCarte,
                                     self.CodeSecret, self.DateExpiration, self.EtatCarte)

            def blouquer_carte(self, num_carte):
                self.NumCarte = num_carte
                self.EtatCarte = False
                dab_db.change_etat(self.EtatCarte, self.NumCarte)

            def supprimer_carte(self, num_carte):
                self.NumCarte = num_carte
                dab_db.supprimer_carte(self.NumCarte)

            def deblouquer_cart(self, num_carte):
                self.NumCarte = num_carte
                self.EtatCarte = True
                dab_db.change_etat(self.EtatCarte, self.NumCarte)

            def modifier_code_secret(self, num_carte,  code):
                self.NumCarte = num_carte
                self.CodeSecret = code
                dab_db.change_code(self.CodeSecret, self.NumCarte)

# TODO: public and private
