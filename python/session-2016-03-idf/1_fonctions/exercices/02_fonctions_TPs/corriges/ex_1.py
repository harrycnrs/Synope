#!/usr/bin/env python
# coding=UTF-8


def afficheBonjour():
	print("Bonjour")

def afficheBonjourA(nom, prenom):
	print("Bonjour {} {}".format(prenom, nom))



print("**Le résultat attendu est :\nBonjour")
print("->Votre résultat :")
try:
	afficheBonjour()
except NameError:
	print("La fonction afficheBonjour() n'est pas définie")

print("\n**Le résultat attendu est :\nBonjour Henry Salvador")
print("->Votre résultat :")
try:
	afficheBonjourA("Salvador", "Henry")
except NameError:
	print("La fonction afficheBonjourA() n'est pas définie")


