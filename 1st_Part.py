from __MiniProjet import functions as fct
from __MiniProjet.classes import *
import re


def card():  # ==============================================================================================
    print("\t1. Ajouter une carte\n"
          "\t2. Supprimer une carte\n"
          "\t3. Bloquer une carte\n"
          "\t4. Debloquer une carte\n"
          "\t5. Modifier le code secret\n"
          "\t6. Menu principal\n")

    while True:
        choix = input("-> Choisissez l'option: ")
        if choix == "1":  # Ajouter carte _________________________________________________________
            code_client = fct.client_code_request()
            try:
                num_compte = db.compte_info(code_client)[0]
                num_carte = fct.generate_card_number()
                code_secret = fct.generate_secret_code()
                date_exp = fct.exp_date()

                cart = Client.Compte.Carte(num_compte, code_client, num_carte, code_secret, date_exp)
                cart.ajouter_carte()
            except:  # C'est le client n'a pas un compte
                account(code_client)
            else:
                print(f'\n{" Ajouter une carte " :-^60}\n'
                      f'- Une carte a été ajoutée au compte -{num_compte}-:\n'
                      f'\t- Numéro de la carte: |{cart.NumCarte}|\n'
                      f'\t- Code PIN: |{cart.CodeSecret}|\n'
                      f"\t- Date d'expiration: {cart.DateExpiration}\n"
                      f'{"" :-^60}\n')
            card()

        elif choix in ["2", "3", "4", "5"]:
            num_carte = fct.num_card_request()
            card_info = db.carte_info(num_carte)
            num_compte = card_info[0]
            code_client = card_info[1]
            code_secret = card_info[3]
            date_exp = card_info[4]
            etat_carte = card_info[5]

            cart = Client.Compte.Carte(num_compte, code_client, num_carte, code_secret, date_exp, etat_carte)
            if choix == "2":  # Supprimer carte ___________________________________________________
                print(f'\n{" Supprimer une carte " :-^60}')
                cart.supprimer_carte(num_carte)
                print(f'\t-La carte |{num_carte}| a été supprimée.\n'
                      f'{" Opération réussie " :-^60}\n')
                card()

            elif choix == "3":  # Bloquer carte __________________________________________________
                print(f'\n{" Bloquer une carte " :-^60}')
                if not cart.EtatCarte:
                    print(f'\t- La carte est déjà bloqué\n{"" :-^60}')
                else:
                    cart.bloquer_carte(num_carte)
                    print(f'\t- La carte a été bloquée\n'
                          f'{" Opération réussie " :-^60}\n')
                card()

            elif choix == "4":  # Débloquer carte ________________________________________________
                print(f'\n{" Débloquer une carte " :-^60}')
                if cart.EtatCarte:
                    print(f'\t- La carte est déjà débloqué\n{"" :-^60}\n')
                else:
                    cart.debloquer_cart(num_carte)
                    print(f'\t- La carte a été débloquée\n'
                          f'{" Opération réussie " :-^60}\n')
                card()

            elif choix == "5":  # Modifier code ___________________________________________________
                print(f'\n{" Modifier le code secret " :-^60}')
                while True:
                    secret_code = input("-> Le code secret actual: ")
                    if secret_code != str(code_secret):
                        print("\t- Le code secret incorrect.\n")
                        continue
                    else:
                        codes = [str(i[3]) for i in db.cards()]
                        while True:
                            new_code = input("-> Le nouveau code (4 chiffres): ")
                            if new_code in codes or not re.search(r'^\d{4}$', new_code):
                                print("- Tapez un autre code SVP.\n")
                                continue
                            cart.modifier_code_secret(num_carte, int(new_code))
                            print(f'{" Opération réussie " :-^60}\n')
                            break
                        card()

        elif choix == "6":  # Menu principal ______________________________________________________
            print(f'\n{"":=^70}')
            start()


def account(code_client):  # ===============================================================================
    client_name = db.client_info(code_client)[1]
    try:  # Le client a un compte
        num_compte = db.compte_info(code_client)[0]
        solde = db.compte_info(code_client)[2]
    except:  # Le client n'a pas un compte
        num_compte = None
        solde = 0

    cmpt = Client.Compte(code_client, num_compte, solde)
    while True:
        if cmpt.NumCompte is not None:
            print(f"\n-> Client -{client_name}- :\n"
                  "\t1. Retirer de l'argent\n"
                  "\t2. Déposer de l'argent\n"
                  "\t3. Consulter le solde\n"
                  "\t4. Supprimer le compte\n"
                  "\t5. Menu principal\n")
            choix = input("-> Choisissez l'option: ")

            if choix == "1":  # Retirer ___________________________________________________________
                print(f'\n{" Retirer " :-^60}')
                while True:
                    try:
                        montant = float(input("- Montant: "))
                    except ValueError:
                        print("\t- Tapez un montant SVP.")
                        continue
                    if montant > cmpt.consulter_solde():
                        print('\t-> Le montant est supérieur au solde.\n'
                              f'{" Opération échouée " :-^60}')
                    else:
                        cmpt.debiter(montant)
                        print(f'\t-> Le solde maintenant est: {cmpt.Solde:.2f} £\n'
                              f'{" Opération réussie " :-^60}')
                    break

            elif choix == "2":  # Déposer _________________________________________________________
                print(f'\n{" Déposer " :-^60}')
                while True:
                    try:
                        montant = float(input("- Montant: "))
                    except ValueError:
                        print("\t- Tapez un montant SVP.")
                        continue
                    else:
                        cmpt.crediter(montant)
                        break
                print(f'\t-> Le solde maintenant est: {cmpt.Solde:.2f} £\n'
                      f'{" Opération réussie " :-^60}')

            elif choix == "3":  # Consulter _______________________________________________________
                solde = cmpt.consulter_solde()
                print(f'\n{" Consultation " :-^60}\n'
                      f'\tSolde: {solde:.2f} £'
                      f'\n{"" :-^60}')

            elif choix == "4":  # Supprimer _______________________________________________________
                print(f'\n{" Supprimer le compte" :-^60}'
                      f'\n- Le compte N°: {cmpt.NumCompte} de -{client_name}- a été supprimé.'
                      f'\n{" Opération réussie " :-^60}')
                cmpt.supprimer_compte()
                start()

            elif choix == "5":  # Menu principal __________________________________________________
                print(f'\n{"":=^70}')
                start()

        else:
            print(f"\n-Le client -{client_name}- n'a pas un compte:\n"
                  "\t1. Ajouter un compte\n"
                  "\t2. Menu principal\n")
            choix = input("-> Choisissez l'option: ")

            if choix == "1":  # Ajouter compte _________________________________________________
                num_compte = fct.generate_account_number()
                cmpt.ajouter_compte(num_compte)
                print(f'\n{"" :-^60}'
                      f'\n- Le compte N°: {num_compte} a été ajouté au client: -{client_name}-.'
                      f'\n{"" :-^60}')
                start()

            elif choix == "2":  # Menu principal __________________________________________________
                print(f'\n{"":=^70}')
                start()


def client():  # ============================================================================================
    print("\t1. Ajouter un client\n"
          "\t2. Afficher les informations d'un client\n"
          "\t3. Menu principal\n")
    while True:
        choix = input("-> Choisissez l'option: ")

        if choix == "1":  # Ajouter client ________________________________________________________
            print(f'\n{" Ajouter un client ":-^60}')
            code_client = fct.generate_client_code()
            while True:  # Nom & Prénom -------------------------------------------------
                nom_prenom = input("- Nom et Prénom: ").title()
                names = [i[1] for i in db.clients()]
                if re.search(r'^\d*$', nom_prenom) or nom_prenom.isspace():
                    continue
                elif nom_prenom in (name.title() for name in names):
                    print(f"\t- Le client -{nom_prenom}- est déja existé."
                          f'\n{"":-^60}\n')
                    client()
                break
            while True:  # Code d'agence ------------------------------------------------
                code_agence = input("- Code d'agence (3 chiffres): ")
                if not re.search(r'^\d{3}$', code_agence):
                    continue
                break
            while True:  # Telephone ----------------------------------------------------
                tel = input("- Téléphone: ")
                if not re.search(r'^[0-9]+$', tel):
                    continue
                break
            while True:  # Email --------------------------------------------------------
                email = input("- Email: ")
                if not re.search(r'\S+@\S+', email):
                    continue
                break

            clnt = Client(code_client, nom_prenom, int(code_agence), tel, email)
            clnt.ajouter_client()
            print(f'{" Opération terminée ":-^60}\n')
            # Lorsqu'un client est ajouté, un compte et une carte sont automatiquement ajouté.
            # Compte: -------------------------------------
            cmpt = clnt.Compte(code_client)
            num_compte = fct.generate_account_number()
            cmpt.ajouter_compte(num_compte)
            # Carte: --------------------------------------
            num_carte = fct.generate_card_number()
            code_secret = fct.generate_secret_code()
            date_exp = fct.exp_date()
            cart = cmpt.Carte(num_compte, code_client, num_carte, code_secret, date_exp)
            cart.ajouter_carte()

            print(f'{"" :-^60}\n'
                  f'- Le Client: {nom_prenom}\n'
                  f'- Code Client: -{code_client}-\n'
                  f'- N° Compte: -{num_compte}-\n'
                  f'- N° Carte: |{cart.NumCarte}|\n'
                  f'- Code PIN: |{cart.CodeSecret}|\n'
                  f'{"" :-^60}\n')
            client()

        elif choix == "2":  # Afficher détails ____________________________________________________
            code_client = fct.client_code_request()
            client_info = db.client_info(code_client)
            print(f'\n{" Client Info ":-^60}\n'
                  f'\tCode client: {client_info[0]}\n'
                  f'\tNom & Prénom: {client_info[1]}\n'
                  f'\tCode agence: {client_info[2]}\n'
                  f'\tTelephone: {client_info[3]}\n'
                  f'\tEmail: {client_info[4]}\n'
                  f'{"":-^60}\n')
            client()

        elif choix == "3":  # Menu principal ______________________________________________________
            print(f'\n{"":=^70}')
            start()


def start():
    print("\nBienvenue dans le menu, Vous pouvez choisir l'une des options suivantes:\n"
          "\t1. Client\n"
          "\t2. Compte\n"
          "\t3. Carte\n"
          "\t4. Quitter\n")
    while True:
        choix = input("-> Choisissez l'option: ")
        if choix == "1":
            print(f'{" Client ":=^70}\n')
            client()
        elif choix == "2":
            print(f'{" Compte ":=^70}\n')
            client_code = fct.client_code_request()
            account(client_code)
        elif choix == "3":
            print(f'{" Carte ":=^70}\n')
            card()
        elif choix == "4":
            print(f'\n{" MERCI ":*^80}')
            exit()


if __name__ == '__main__':
    print(f'\n{" BIENVENUE ":*^80}')
    start()
