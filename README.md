Distributeur Automatique de Billets (DAB)
==============================================================
#### Application en python pour saisir et consulter des données des clients, comptes et cartes.


## Instructions pour l’exécution du programme:
- [Télécharger](https://www.python.org/downloads/) et installer python 3.x 
- Télécharger et nnstaller un IDE (Pycharm, VS Code, Sublime Text, Atom ...) .
- Télécharger puis déziper le `Mini_Projet.zip`.
- Pour le code de dévloppeur (Back-End), ouvrez le fichier `1st_part.py`.
- Pour l'interface graphique (Front_end), ouvrez le fichier `2nd_part.py`.


## Le développeur:
**- Nom & Prénom:** MOUSSI Imed <br>
**- Spécialité:** Mécatronique <br>
**- GitHub:** https://github.com/ImedMoussi <br>
**- Email:** i_moussi@enst.dz <br>

## La date:
De **06-07-2020** à **06-09-2020**


## Pour tester:
Code Client | Nom & Prénom | N° Compte | Solde | N° Carte | Code PIN | Etat Carte
------ | ------ | ------ | ------ | ------ | ------ | ------ |
10101 | Moussi Imed | 00001 | 5200 | 1010-1010-1010-1010<br>4175-0070-7708-6904<br>4508-1285-8235-4633 | 1111<br>5004<br>2557 | Valide<br>Invalide<br>Valide |
20202 | Moussi Halim | 00002 | 3500 | 2020-2020-2020-2020 | 2222 | Valide |
30303 | Moussi Raouf | 00003 | 2200 | 3030-3030-3030-3030<br>4175-0020-0047-3725 | 3333<br>1303 | Invalide<br>Valide |


## Déscription:<br>

#### Les fichiers.py:
1. **data_base:** La creation de et la connection avec la base de données.<br>
2. **classes:** Les classes (Client, Compte, Carte), et leurs méthodes.<br>
3. **functions:** Des Fonctions auxiliaires.<br>
4. **1sr_part:** Le programme principal.<br>
5. **2nd_part** Le programme de l'interface graphique.

#### Les Modules utilisés:
```python
import sqlite3
from pandas import read_csv
import re  # Regular Expression
from datetime import datetime
import numpy
```

#### Partie 1:
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

#### Partie 2:
Interface graphique:
> - Entrer le numéro de carte<br>
> - Entrer le code PIN<br>
> - Consulter le solde<br>
> - Retirer de l'argent<br>
