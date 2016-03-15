# -*- coding: utf-8 -*-

from calculatrice import CalculatriceEtendue
import os
import copyreg, copy, pickle #python3

nom_fichier = 'main.pkl'
if os.path.exists(nom_fichier):
    fichier = open(nom_fichier,'rb')
    calc = pickle.load(fichier)
    fichier.close()
else:
    calc = CalculatriceEtendue()

print("calc 5")
ligne=input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne=input(">>> ")
    
fichier = open(nom_fichier,'wb')
pickle.dump(calc, fichier)
fichier.close()

