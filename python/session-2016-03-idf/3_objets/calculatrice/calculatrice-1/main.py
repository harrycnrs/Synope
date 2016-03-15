# -*- coding: utf-8 -*-

from calculatrice import Calculatrice

calc = Calculatrice()
calc.init()

print()
ligne = input(">>> ")
while ligne!='OFF':
    calc.calcule(ligne)
    ligne= input(">>> ")
