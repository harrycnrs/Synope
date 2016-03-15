# -*- coding: utf-8 -*-

import operateurs
from analyseur import analyse

class Calculatrice(object):

    def init(self):
        self.__res = 0

    def calcule(self,chaine):
        expression = analyse(chaine)
        expression.display()
        for op, num in expression.paires():
            if op=='=':
                self.__res = num
            else:
                fct = operateurs.operations[op]
                self.__res = fct(self.__res,num)
        print(self.__res)

        
