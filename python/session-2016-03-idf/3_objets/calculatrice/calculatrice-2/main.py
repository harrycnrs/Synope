# -*- coding: utf-8 -*-

from calculatrice import Calculatrice

calc = Calculatrice()

print()
ligne = input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne = input(">>> ")
