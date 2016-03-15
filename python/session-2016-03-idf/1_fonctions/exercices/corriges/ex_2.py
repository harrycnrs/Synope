#!/usr/bin/env python
# coding=UTF-8

def mul(a, b):
	return a * b

def div(a, b):
	return a / b

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def divInfinityOnZeroTest(a, b):
	if b == 0:
		return float("inf") if a > 0 else -float("inf")
	return div(a, b)
def divInfinityOnZeroException(a, b):
	try:
		return div(a, b)
	except ZeroDivisionError:
		return float("inf") if a > 0 else -float("inf")


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
