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

