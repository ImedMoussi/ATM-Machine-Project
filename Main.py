# Imports
# import time
# from datetime import datetime
import re  # Regular Expresion
# import os
# import sys
# import numpy as np
# import pandas as pd
from __MiniProjet import classes, dab_db


def name_request():
    names = [i[1] for i in dab_db.clients_info()]
    while True:
        name = input("->\tDonner le nom & le prénom du client: ")
        if name not in names:
            print(f"\t- Le client -{name}- n'existe pas")
            continue
        return name


def card(client_name):
    code_client = dab_db.client(client_name)[0]
    num_compte = dab_db.compte(code_client)[0]
    c = classes.Client.Compte.Carte(num_compte, code_client)

    print("\t1. Ajouter une carte\n"
          "\t2. Supprimer une carte\n"
          "\t3. Bloquer une carte\n"
          "\t4. Debloquer une carte\n"
          "\t5. Modifier le code secret\n"
          "\t6. Menu principal\n")

    while True:
        choix = input("->\tChoisissez l'option: ")
        if choix == "1":  # ----------------------------------------------
            c.ajouter_carte(num_compte, code_client)
            print(f'{"" :-^60}\n'
                  f'\t- Une carte a été ajoutée au compte: -{num_compte}-.\n'
                  f'\t- Numéro de carte:\t{c.NumCarte}.\n'
                  f'\t- Code secret:\t{c.CodeSecret}.\n'
                  f'{"" :-^60}\n')
            card(client_name)
        if choix == "2":  # ----------------------------------------------
            print(f'{"Supprimer une carte" :-^60}')
            num_cartes = [i[2] for i in dab_db.cards_info()]
            while True:
                num_carte = input("- Donner le numéro de carte: ")
                if num_carte not in num_cartes:
                    print("- La carte n'existe pas")
                    continue
                c.supprimer_carte(num_carte)
                print(f'{"Opération réussie" :-^60}')
                card(client_name)


def account(client_name):
    code_client = dab_db.client(client_name)[0]
    try:
        num_compte = dab_db.compte(code_client)[0]
        solde = dab_db.compte(code_client)[2]
    except:
        num_compte = None
        solde = 0.00

    c = classes.Client.Compte(code_client, num_compte, solde)
    while True:
        if c.NumCompte is None:
            print(f"\n-Le client -{client_name}- n'a pas un compte:\n"
                  "\t1. Ajouter un compte\n"
                  "\t2. Menu principal\n")
            choix = input("->\tChoisissez l'option: ")
            if choix == "1":  # --------------------------------------------------
                c.ajouter_compte(code_client)
                print(f'\n{"" :-^60}\n'
                      f'\t- Un compte a été ajouté au client: -{client_name}-.'
                      f'\n{"" :-^60}')
            elif choix == "2":  # --------------------------------------------------
                print(f'\n{"":=^70}')
                start()

        else:
            print("\n\t1. Retirer de l'argent\n"
                  "\t2. Déposer de l'argent\n"
                  "\t3. Consulter le compte\n"
                  "\t4. Supprimer le compte\n"
                  "\t5. Menu principal\n")
            choix = input("->\tChoisissez l'option: ")
            if choix == "1":  # --------------------------------------------------
                print(f'\n{" Retirer " :-^60}')
                try:
                    montant = float(input("\t- Montant: "))
                except ValueError:
                    print("- Vous devez entrer un nombre")
                    continue
                if montant <= c.consulter_solde():
                    c.debiter(montant)
                    print(f'{"Opération réussie" :-^60}')
                else:
                    print("\t Le montant est superieur au solde")  # TODO: hadi tetbadel
                    print(f'{" Opération échouée " :-^60}')

            elif choix == "2":  # --------------------------------------------------
                print(f'\n{" Déposer " :-^60}')
                try:
                    montant = float(input("- Montant: "))
                except ValueError:
                    print("- Vous devez entrer un nombre")
                    continue
                c.crediter(montant)
                print(f'{" Opération réussie " :-^60}')
            elif choix == "3":  # --------------------------------------------------
                print(f'\n{" Consultation " :-^60}\n'
                      f'\tSolde: {c.consulter_solde():.2f} $'
                      f'\n{"" :-^60}')
            elif choix == "4":  # --------------------------------------------------
                c.supprimer_compte(code_client)
                print(f'\n{"" :-^60}\n'
                      f'\t- Le compte de -{client_name}- a été supprimé.'
                      f'\n{"" :-^60}')
                account(client_name)
            elif choix == "5":  # --------------------------------------------------
                print(f'\n{"":=^70}')
                start()


def client():
    print('\t1. Ajouter un client\n'
          '\t2. Afficher les détails d\'un client\n'
          '\t3. Menu principal\n')
    while True:
        choix = input("->\tChoisissez l'option: ")
        if choix == "1":  # -------------------------------------------------
            print(f'\n{" Ajouter un client ":-^60}')
            while True:
                nom_prenom = input("- Nom et Prénom: ")
                names = [i[1] for i in dab_db.clients_info()]
                if not nom_prenom:
                    continue
                elif nom_prenom in names:
                    print("\t- Le client est déja existé")
                    continue
                break
            while True:
                code_agence = input("- Code d'agence (3 chiffres): ")
                if not re.search(r'^\d{3}$', code_agence):
                    continue
                break
            while True:
                tel = input("- Telephone: ")
                if not re.search(r'^[0-9]+$', tel):
                    continue
                break
            while True:
                email = input("- Email (..@..): ")
                if not re.search(r'\S+@\S+', email):
                    continue
                break

            c = classes.Client()
            c.ajouter_client(nom_prenom, code_agence, tel, email)
            print(f'{" Opération terminée ":-^60}\n')
            # TODO: hadi fiha luch
            c.Compte(c.CodeClient).ajouter_compte(c.CodeClient)
            print(f'{"" :-^60}\n'
                  f'\t- Un compte a été ajouté au client: -{nom_prenom}-.'
                  f'\n{"" :-^60}\n')
            client()
        elif choix == "2":  # --------------------------------------------------
            name = name_request()
            info = dab_db.client(name)
            num = dab_db.compte(info[0])
            print(num)
            print(f'\n{" Client Info ":-^60}\n'
                  f'\tCode client: {info[0]}\n'
                  f'\tNom & Prénom: {info[1]}\n'
                  f'\tCode agence: {info[2]}\n'
                  f'\tTelephone: {info[3]}\n'
                  f'\tEmail: {info[4]}\n'
                  f'{"":-^60}\n')
            client()
        elif choix == "3":  # ---------------------------------------------------
            print(f'\n{"":=^70}')
            start()


def start():
    print("\n- Bienvenue dans le menu principal, Vous pouvez choisir l'une des options suivantes:\n"
          "\t1. Client\n"
          "\t2. Compte\n"
          "\t3. Carte\n"
          "\t4. Quitter\n")
    while True:
        choix = input("->\tChoisissez l'option: ")
        if choix == "1":
            print(f'\n{" Client ":=^70}')
            client()
        elif choix == "2":
            print(f'\n{" Compte ":=^70}\n')
            client_name = name_request()
            account(client_name)
        elif choix == "3":
            print(f'\n{" Carte ":=^70}\n')
            client_name = name_request()
            card(client_name)
        elif choix == "4":
            print(f'\n{"_ MERCI _":*^80}')
            exit()


if __name__ == '__main__':
    print(f'{"_ BIENVENUE _":*^80}')
    start()


# TODO: un compte ykon 3ando plz carte ... w kifeh t9asem swared bin lesz cartes ...
# TODO: lazem n3awed nkhamem comment fonctionne le programme d'une maniere logique
# sinarko
