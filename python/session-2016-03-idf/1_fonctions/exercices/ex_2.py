#!/usr/bin/env python
# coding=UTF-8




# Exercice 2.1 fonctions mul(a, b), div(a, b), add(a, b) et sub(a, b)

# Exercice 2.2 fonctions divInfinityOnZeroTest(a, b) et divInfinityOnZeroException(a, b)
# fonction divInfinityOnZeroTest
	# utiliser la fonction float("inf") (-float("inf")) pour représenter +∞ et -∞ ;
	# si b est égal à 0, retourner +∞ ou -∞.
# fonction divInfinityOnZeroException
	# utiliser la fonction float("inf") (-float("inf")) pour représenter +∞ et -∞ ;
	# exécuter la division sans conditions ;
	# récupérer l'exception ZeroDivisionError et retourner alors +∞ ou -∞.





#*****************************************************************************#
#*****************************************************************************#
#***                             Vérifications                             ***#
#*****************************************************************************#
#*****************************************************************************#


print("Exercice 2.1")
try:
	print('  1 * 3 = ', mul(1, 3))
except NameError:
	print("La fonction mul() n'est pas définie")
try:
	print("  1 / 3 = ", div(1, 3))
except NameError:
	print("La fonction div() n'est pas définie")
try:
	print("  1 + 3 = ", add(1, 3))
except NameError:
	print("La fonction add() n'est pas définie")
try:
	print("  1 - 3 = ", sub(1, 3))
except NameError:
	print("La fonction sub() n'est pas définie")
try:
	print("  (1 + 3) * 11 + 1 - 3 = ", add(mul(add(1, 3), 11), sub(1, 3)))
except NameError:
	print("Il manque une des fonctions add, mul ou sub")

print("Exercice 2.2")
try:
	print("  +1 / 0 = ", divInfinityOnZeroTest(+1, 0))
	print("  -1 / 0 = ", divInfinityOnZeroTest(-1, 0))
except NameError:
	print("La fonction divInfinityOnZeroTest() n'est pas définie")
try:
	print("  +1 / 0 = ", divInfinityOnZeroException(+1, 0))
	print("  -1 / 0 = ", divInfinityOnZeroException(-1, 0))
except NameError:
	print("La fonction divInfinityOnZeroException() n'est pas définie")
