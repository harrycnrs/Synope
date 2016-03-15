# -*- coding: utf-8 -*-

import operateurs
from analyseur import Expression

class Calculatrice(object):

    def __init__(self):
        self.__res = 0

    def __call__(self,chaine):
        expr = Expression(chaine)
        print(expr)
        for op, num in expr:
            if op=='=':
                self.__res = num
            else:
                self.__res = operateurs.operations[op](self.__res,num)
        print(self.__res)

        
