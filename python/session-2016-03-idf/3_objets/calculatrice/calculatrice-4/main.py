# -*- coding: utf-8 -*-

from calculatrice import CalculatriceEtendue

calc = CalculatriceEtendue()

print("calc 4")
ligne = input(">>> ")
while ligne!='OFF':
    calc(ligne)
    ligne = input(">>> ")
