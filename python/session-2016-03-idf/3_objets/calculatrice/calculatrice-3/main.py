# -*- coding: utf-8 -*-

from calculatrice import Calculatrice

calc = Calculatrice()

print("calc 3")
ligne = input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne = input(">>> ")
