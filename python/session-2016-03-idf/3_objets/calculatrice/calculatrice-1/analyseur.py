# -*- coding: utf-8 -*-


import re


class Expression(object):
      
    def init(self,opList,numList):
        self.__opList = opList
        self.__numList = list(map(float, numList))

    def display(self):
        print ("( %s %s )" % (self.__opList,self.__numList))

    def paires(self):
        return zip(self.__opList,self.__numList)

        
parse_op = re.compile(r'[-+*/]')
parse_num = re.compile(r'[^-+*/]+')
    
def analyse(s):

    opList = parse_op.findall(s)
    numList = parse_num.findall(s)
    
    if len(opList) != len(numList):
        opList.insert(0, '=')

    expr = Expression()
    expr.init(opList,numList)
    
    return expr
    
