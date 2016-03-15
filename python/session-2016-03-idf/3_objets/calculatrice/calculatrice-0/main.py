# -*- coding: utf-8 -*-

from calculatrice import calcule

print()
ligne=input(">>> ")
while ligne!='OFF':
    calcule(ligne)
    ligne=input(">>> ")
