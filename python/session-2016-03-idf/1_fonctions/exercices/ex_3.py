#!/usr/bin/env python
# coding=UTF-8
import random, math

LIST_DATA = [ 4.1, 9, 0, "coucou", -1000, 1000, [ 0, 1], "42", -float("inf"), 18, -49, -4999.0, -455, float("inf"), -541, 9999.9, float("nan") ]
LIST_DATA.extend(4.2 * random.randint(-1000,1000) for r in range(20))
print(LIST_DATA)

# Exercice 3.1: Filtrage de données de type liste
# écrire un filtre de type lamda qui sélectionne les données de types entières et flottantes
LIST_DATA1 = LIST_DATA

# Exercice 3.2: Filtrage de données de type liste
# écrire un filtre de type lamda qui sélectionne les données comprises entre [-1000 et 1000[
LIST_DATA2 = LIST_DATA1

# Exercice 3.3: "Mappage" de données de type liste
# écrire un map de type lamda qui transforme les données en valeur absolues
LIST_DATA3 = LIST_DATA2

# Exercice 3.4: "Réduction" de données de type liste
# écrire un reduce de type lamda qui calcule la multiplication des données tronquées en entier (0 doit être traité comme 1)
DATA4 = LIST_DATA3

# Exercice 3.5: Filtrage de données de type chaine
# écrire un filtre de type lamda qui sélectionne les caractères entre 'e' et 'n' et également entre 'E' et 'N'
CHAINE = "abcd0ef9ghij8klmA5BCD7EFG6HIJK4LMNO3PQR2STU1VWXYZnopqrstuvwxyz"
CHAINE5 = CHAINE


#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#


print("\nVérifications exercice 3.1")
erreurDetecte = False
print(LIST_DATA1)
if (type(LIST_DATA1) != type(LIST_DATA)):
        erreurDetecte = True
        print("L'objet retourné n'est pas une liste")
else:
        for e in LIST_DATA1:
	        if not (isinstance(e, int) or isinstance(e, float)):
		        print("  - ", e, "n'est ni entier ni flotant")
		        erreurDetecte = True
if erreurDetecte:
	print("Vous devez corriger vos erreurs.")
else:
	print("Bravo, le filtre semble fonctionner correctement.")

print("\nVérifications exercice 3.2")
print(LIST_DATA2)
erreurDetecte = False
if (type(LIST_DATA2) != type(LIST_DATA)):
        erreurDetecte = True
        print("L'objet retourné n'est pas une liste")
else:
        for e in LIST_DATA2:
	        if isinstance(e, int) or isinstance(e, float):
		        if math.isnan(e) or e >= 1000 or e < -1000:
			        print("  - ", e, "n'est pas dans l'interval [-1000..1000[")
			        erreurDetecte = True
if erreurDetecte:
	print("Vous devez corriger vos erreurs.")
else:
	print("Bravo, le filtre semble fonctionner correctement.")

print("\nVérifications exercice 3.3")
print(LIST_DATA3)
erreurDetecte = False
if (type(LIST_DATA3) != type(LIST_DATA)):
        erreurDetecte = True
        print("L'objet retourné n'est pas une liste")
else:
        for e in LIST_DATA3:
	        if isinstance(e, int) or isinstance(e, float):
		        if (not math.isnan(e)) and (-1000<e<=1000):
			        if e < 0:
				        print("  - ", e, "n'est pas >= 0")
				        erreurDetecte = True
if erreurDetecte:
	print("Vous devez corriger vos erreurs.")
else:
	print("Bravo, le map semble fonctionner correctement.")

print("\nVérifications exercice 3.4")
print(DATA4)
verif = 1
if (type(DATA4) != type(int)):
        erreurDetecte = True
        print("L'objet retourné n'est pas un entier")
else:
        for e in LIST_DATA3:
	        if (isinstance(e, int) or isinstance(e, float)) and (not math.isnan(e)) and (0<=e<=1000):
		        e = int(e)
		        verif = verif * 1 if (e == 0) else e
if DATA4 != verif:
	print("Vous devez corriger vos erreurs.")
else:
	print("Bravo, la réduction semble fonctionner correctement.")

print("\nVérifications exercice 3.5")
print(CHAINE5)
if CHAINE5 == 'efghijklmEFGHIJKLMNn':
	print("Bravo, le filtre semble fonctionner correctement.")
else:
	print("Vous devez corriger vos erreurs.")
