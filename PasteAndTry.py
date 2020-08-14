# import csv

# # Remplir la table "Client":
# with open("Clients.csv", "r") as clnt:
#     for i in csv.DictReader(clnt):
#         values = [list(i.values())]
#         cur.executemany(""" INSERT INTO Client VALUES (?, ?, ?, ?, ?) """, values)
#
# # Remplir la table "Compte":
# with open("Comptes.csv", "r") as cmpt:
#     for i in csv.DictReader(cmpt):
#         values = [list(i.values())]
#         cur.executemany(""" INSERT INTO Compte VALUES (?, ?, ?) """, values)
#
# # Remplir la table "Carte":
# with open("Cartes.csv", "r") as Crt:
#     for i in csv.DictReader(Crt):
#         values = tuple(list(i.values()))
#         cur.executemany(""" INSERT INTO Carte VALUES (?, ?, ?, ?, ?, ?) """, values)

from __MiniProjet import dab_db


def account_info_reqeust():
    accounts_no = [i[0] for i in dab_db.accounts()]
    print(accounts_no)
    while True:
        account_no = input("->\tDonner le No du compte: ")
        if account_no not in accounts_no:
            print("\t-Numéro de compte incorrecte")
            continue
        break
    while True:
        code = int(input("->\tDonner le code secret: "))
        if code != dab_db.secret_code(accounts_no):
            print("\t-Code secret incorrecte")
            continue
        break
    return accounts_no, code

print(account_info_reqeust())
