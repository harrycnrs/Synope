# -*- coding: utf-8 -*-

from analyseur import Expression
import operateurs
import math

class Calculatrice(object):

    def __init__(self):
        self.__res = 0
        
    def getres(self) :
        return self.__res

    def __call__(self,chaine):
        expr = Expression(chaine)
        print(expr)
        for op, num in expr:
            if op=='=':
                self.__res = num
            else:
                self.__res = operateurs.operations[op](self.__res,num)
        print(self.__res)

class CalculatriceEtendue(Calculatrice):

    def __call__(self,chaine):
        if chaine=="inv":
            chaine = "%f" % (1./self.getres())
        elif chaine=="sqrt":
            chaine = "%f" % math.sqrt(self.getres())
        super(CalculatriceEtendue,self).__call__(chaine)

        
