:atm: Distributeur Automatique de Billets (DAB) :credit_card:
==============================================================
#### Application en python pour saisir et consulter des données des clients, comptes et cartes.

## <ins>Instructions pour l’exécution du programme:</ins> :arrow_forward:
- [Télécharger](https://www.python.org/downloads/) et installer python 3.x 
- Installer un IDE (Pycharm, VS Code, Sublime Text, Atom ...) 
- Télécharger puis déziper le **Mini_Projet.zip** :open_file_folder:
- Pour le code de dévloppeur (Back-End), ouvrez le fichier **1st_part.py**
- Pour l'interface graphique (Front_end), ouvrez le fichier **2nd_part.py** 


## <ins>Le développeur:</ins> :bust_in_silhouette:
**- Nom & Prénom:** MOUSSI Imed <br>
**- Spécialité:** Mécatronique<br>
**- GitHub:** https://github.com/ImedMoussi<br>
**- Email:** i_moussi@enst.dz

## <ins>La date:</ins> :date:
De **06-07-2020** à **06-09-2020**

## <ins>Pour tester:</ins> :pencil:
Code Client | Nom & Prénom | N° Compte | Solde | N° Carte | Code PIN | Etat Carte
------------ | ------------- | ------------ | ------------- | ------------ | ------------- | ------------- |
10101 | Moussi Imed | 00001 | 5200 | 1010-1010-1010-1010<br>2020-2020-2020-2020<br>3030-3030-3030-3030| 1111<br>2222<br>3333 | Valide<br>Invalide<br>Valide |
20202 | Moussi Halim | 00002 | 3500 | 4175-0070-7708-6904 | 5004 | Invalide |
30303 | Moussi Raouf | 00003 | 2200 | 4508-1285-8235-4633<br>4175-0020-0047-3725 | 2557<br>1303 | Invalide<br>Valide |


## <ins>Déscription:</ins> :pencil:<br>

### <ins>Les fichiers.py:</ins>
1. **<ins>data_base:</ins>** La creation de et la connection avec la base de données.<br>
2. **<ins>classes:</ins>** Les classes (Client, Compte, Carte), et leurs méthodes.<br>
3. **<ins>functions:</ins>** Des Fonctions auxiliaires.<br>
4. **<ins>1sr_part:</ins>** Le programme principal.<br>
5. **<ins>2nd_part</ins>** le programme de l'interface graphique.

### <ins>Les Modules utilisés:</ins>
- sqlite3
- read_csv from pandas
- re (Regular Expression)
- datetime from datetime
- numpy

### <ins>Partie 1:</ins> 
Via le console:
> Client:
>> - Ajouter un client.<br>
>> - Afficher les détails d'un client<br>

> Compte:
>> - Retirer de l'argent<br>
>> - Déposer de l'argent<br>
>> - Consulter le solde<br>
>> - Ajouter un compte<br>
>> - Supprimer un compte<br>

> Carte:
>> - Ajouter une carte<br>
>> - Supprimer une carte<br>
>> - Bloquer une carte<br>
>> - Debloquer une carte<br>
>> - Modifier le code secret<br>

### <ins>Partie 2:</ins>
Interface graphique:
> - Entrer le numéro de carte<br>
> - Entrer le code PIN<br>
> - Consulter le solde<br>
> - Retirer de l'argent<br>
