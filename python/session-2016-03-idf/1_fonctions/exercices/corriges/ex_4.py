#!/usr/bin/env python
# coding=UTF-8

# Dictionnaire de conversion de devises
DEVISES = {
	'€':{ '€':1.00, '$':1.25, '£':0.80 },
	'$':{ '€':0.80, '$':1.00, '£':0.64 },
	'£':{ '€':1.25, '$':1.56, '£':1.00 }
}

def conversionDeDevise(valeur, deviseValeur, deviseRetour):
	"""Convertit la "valeur" exprimée en "deviseValeur" vers la devise "deviseRetour", arrondi a deux chiffres après la virgule.

	Args :
	valeur(float)     -- la valeur à convertir ;
	deviseValeur(str) -- la devise de la valeur à convertir ;
	deviseRetour(str) -- la devise attendue par l'appeleur de cette fonction.
        Returns :
	float : la "valeur" exprimée en "deviseRetour"
	"""
	return round(DEVISES[deviseValeur][deviseRetour] * valeur, 2)

def lectureLigne(ligne):
	"""Lit une ligne du fichier csv sous forme d'un tuple (Libellé,Auteur,Prix,Devise)

	Args :
	ligne(str) -- une ligne du fichier csv
        Returns :
	tuple : un tuple (Libellé:str,Auteur:str,Prix:float,Devise:str)
	"""
	# indices:
	#	- dans ipython taper help(str) et regarder la documentation de la méthode "split" ;
	#	- dans ipython taper help(str) et regarder la documentation de la méthode "strip".
	return ligne.split(',')[0].strip(), ligne.split(',')[1].strip(), float(ligne.split(',')[2].strip()), ligne.split(',')[3].strip()

def lectureCSV(chemin, avecEntete=False):
	"""Lit le fichier csv qui se trouve dans "chemin" et le convertit en une liste de tuples (Libellé,Auteur,Prix,Devise).

	Args:
	chemin(str) -- le chemin vers le fichier csv.
        Returns:
	list: une liste des tuples (Libellé,Auteur,Prix,Devise) contenus dans le fichier csv, cette liste n'inclut pas l'entête.
	"""
	f = open(chemin, mode='r')
	resultat = []
	if avecEntete:
		f.readline()
	# lecture du fichier ligne par ligne
	for ligne in f:
		resultat.append(lectureLigne(ligne))
	f.close()
	return resultat

def conversionDonnees(donnees, deviseRetour):
	"""Convertit une liste de tuples (Libellé,Auteur,Prix,Devise) en liste de tuples (Libellé,Auteur,Prix,deviseRetour).

	Args :
	donnees(list)     -- une liste des tuples (Libellé,Auteur,Prix,Devise) ;
	deviseRetour(str) -- la devise attendue pour toutes les cases de la liste de retour.
        Returns :
	list : une liste des tuples (Libellé,Auteur,Prix,deviseRetour).
	"""
	for index in range(len(donnees)):
                donnees[index] = donnees[index][0], donnees[index][1], conversionDeDevise(donnees[index][2], donnees[index][3], deviseRetour), deviseRetour
                # pour plus de lisibilité, on aurait pu utiliser une variable intermédiaire
		#bouquin = donnees[index]
		#donnees[index] = bouquin[0], bouquin[1], conversionDeDevise(bouquin[2], bouquin[3], deviseRetour), deviseRetour
	return donnees

def ecritureCSV(chemin, donnees):
	"""Crée un fichier csv dans "chemin" (et l'écrase s'il existe déjà) et écrit les "donnees" au format csv.

	Args :
		chemin(str)   -- le chemin vers le nouveau fichier csv ;
		donnees(list) -- une liste des tuples (Libellé,Auteur,Prix,Devise).
	"""
	f = open(chemin, mode='w+')
	for bouquin in donnees:
		f.write(bouquin[0] + "," + bouquin[1] + "," + str(bouquin[2]) + "," + bouquin[3] + "\n")
	f.close()


#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#

# Exercice 4.1: Conversion de devises
#	- Compléter la fonction conversionDeDevise grâce au dictionnaire "DEVISES".
# Vérification (non exhaustive) des spécifications de la fonction conversionDeDevise.
print("\nVérifications exercice 4.1")
try:
	erreurDetecte = False
	if conversionDeDevise(1., u"€", u"€") != 1.:
		print(" - Erreur de conversion € => €")
		erreurDetecte = True
	if conversionDeDevise(1., u"€", u"$") != 1.25:
		print(" - Erreur de conversion € => $")
		erreurDetecte = True
	if conversionDeDevise(1., u"£", u"$") != 1.56:
		print(" - Erreur de conversion £ => $")
		erreurDetecte = True
	if conversionDeDevise(1., u"$", u"€") != .8:
		print(" - Erreur de conversion $ => €")
		erreurDetecte = True

	if erreurDetecte:
		print("Vous devez corriger vos erreurs.")
	else:
		print("Bravo, la conversion semble fonctionner correctement.")
except BaseException as e:
	print(e)



# Exercice 4.2: Transformation d'un texte vers une structure de données.
#	- Compléter la fonction lectureLigne.
# Vérification (non exhaustive) des spécifications de la fonction lectureLigne.
print("\nVérifications exercice 4.2")
try:
	erreurDetecte = False
	attendu = 'abcd', 'efg h', 42.0, '$'
	obtenu  = lectureLigne(u"abcd,efg h,42.0,$")
	if obtenu != attendu or not isinstance(obtenu[2], float):
		print("erreur, obtenu:", obtenu, ", attendu:", attendu)
		erreurDetecte = True
	attendu = 'abcd', 'efg h', 4.2, '€'
	obtenu  = lectureLigne(u"abcd  ,efg h, 4.2, €")
	if obtenu != attendu or not isinstance(obtenu[2], float):
		print("erreur, obtenu:", obtenu, ", attendu:", attendu)
		erreurDetecte = True

	if erreurDetecte:
		print("Vous devez corriger vos erreurs.")
	else:
		print("Bravo, la conversion d'une ligne semble fonctionner correctement.")
except BaseException as e:
	print(e)


# Exercice 4.3: Lecture d'un fichier.
#	- Compléter la fonction lectureCSV
# Vérification (non exhaustive) des spécifications de la fonction lectureCSV.
print("\nVérifications exercice 4.3")
try:
        donnees = lectureCSV('data_3_v0.csv')
        attendu = 'Python Pocket Reference 5ed', 'Mark Lutz', 12.62, '€'
        if donnees[1] == attendu:
	        print("Bravo, la lecture de fichier semble fonctionner correctement.")
        else:
	        print("Vous devez corriger vos erreurs.")
except BaseException as e:
        print(e)

# Exercice 4.4: Gestion de l'entête.
#	- Modifier la fonction lectureCSV de telle façon qu'elle ignore la ligne
#   d'entête lorsque la variable avecEntete est True.
# Vérification (non exhaustive) des spécifications de la fonction lectureCSV.
print("\nVérifications exercice 4.4")
try:
	attendu = 'Python Pocket Reference 5ed', 'Mark Lutz', 12.62, '€'
	donnees = lectureCSV('data_3_v1.csv', True)
	codeCorrect = (donnees[1] == attendu)
	if not codeCorrect:
		print("Vous devez corriger vos erreurs.")
	else:
		print("Bravo, la lecture de fichier avec entête semble fonctionner correctement.")
except BaseException as e:
	print(e)


# Exercice 4.5: Conversion en €
#	- Compléter la fonction conversionDonnees en modifiant les données pour que toutes les lignes soient en €.
print("\nVérifications exercice 4.5")
try:
	erreurDetecte = True
	donnees2 = conversionDonnees(donnees, '€')
	attendu = 'Python 3', 'Sébastien CHAZALLET', 38.89, '€'
	if donnees2[2] == attendu:
		print("Bravo, la conversion des données semble fonctionner correctement.")
		if donnees2 is donnees:
			erreurDetecte = False
		else:
			print(" ! Cependant la modification doit être faite en place.")
	if erreurDetecte:
		print("Vous devez corriger vos erreurs.")
except BaseException as e:
	print(e)


# Exercie 4.6: Écriture d'un fichier
#	- Compléter la fonction ecritureCSV
print("\nVérifications exercice 4.6")
try:
	ecritureCSV('data_out.csv', donnees)
	donneesTest = lectureCSV('data_out.csv')
	if donnees == donneesTest:
		print("Bravo, l'écriture de fichier semble fonctionner correctement.")
	else:
		print("Vous devez corriger vos erreurs.")
except BaseException as e:
	print(e)

print(donnees)
