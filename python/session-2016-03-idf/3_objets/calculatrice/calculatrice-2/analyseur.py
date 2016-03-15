# -*- coding: utf-8 -*-


import re
import copy

parse_op = re.compile(r'[-+*/]')
parse_num = re.compile(r'[^-+*/]+')    

class Expression(object):
    
    def __init__(self,chaine):
     
        self.__opList = parse_op.findall(chaine)
        self.__numList = list(map(float,parse_num.findall(chaine)))
    
        if len(self.__opList) != len(self.__numList):
            self.__opList.insert(0, '=')

    def __str__(self):
        return "( %s %s )" % (self.__opList,self.__numList)

    def __getitem__(self,index):
        return self.__opList[index],self.__numList[index]


    
