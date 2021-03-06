from __MiniProjet import data_base as db
from datetime import datetime
import numpy as np


def client_code_request():
    """This function return a client code before it check if this code is already exist in my data base"""
    codes = [i[0] for i in db.clients()]
    while True:
        code = input("- Donner le code client: ")
        if code not in codes:
            print(f"\t-> Le client -{code}- n'existe pas.\n")
            continue
        return code


def num_card_request():
    """This function return a number card before it check if this number is already exist in my data base"""
    num_cartes = [i[2] for i in db.cards()]
    while True:
        num_carte = input("- Le numéro de carte: ")
        if num_carte not in num_cartes:
            print("\t-> Cette carte n'existe pas.\n")
            continue
        return num_carte


def generate_client_code():
    """This function generate a new and UNIQUE client code"""
    while True:
        code = str(np.random.randint(1, 99999)).ljust(5, "0")
        codes = [i[0] for i in db.clients()]
        if code in codes:
            continue
        return code


def generate_account_number():
    """This function generate a new and UNIQUE account number"""
    accounts = [int(i[0]) for i in db.accounts()]
    num_compte = 1
    while True:
        if num_compte in accounts:
            num_compte += 1
            continue
        return str(num_compte).rjust(5, "0")


def generate_card_number():
    """This function generate a new and UNIQUE card number"""
    lst = list()
    while True:
        for i in range(4):
            s = str(np.random.randint(1, 9999)).ljust(4, '0')
            lst.append(s)
        num = '-'.join(lst)
        num_cartes = [i[2] for i in db.cards()]
        if num in num_cartes:
            continue
        return num


def generate_secret_code():
    """This function generate a new and UNIQUE code PIN"""
    while True:
        code = int(str(np.random.randint(1, 9999)).ljust(4, "0"))
        codes = [i[3] for i in db.cards()]
        if code in codes:
            continue
        return code


def exp_date():
    """This function return today date + 4 years"""
    dt = datetime.now()
    dt = dt.replace(year=dt.year + 4)
    return dt.date()
