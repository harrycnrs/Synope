# -*- coding: utf-8 -*-


import re
import copy


class Expression(object):

    __slots__ = [ '__opList', '__numList' ]
    
    __parse_op = re.compile(r'[-+*/]')
    __parse_num = re.compile(r'[^-+*/]+')

    __PI = 3.1416
    
    @staticmethod
    def pi():
        return Expression.__PI

    def __init__(self,chaine):
     
        self.__opList = self.__parse_op.findall(chaine)
        self.__numList = self.__parse_num.findall(chaine)
    
        if len(self.__opList) != len(self.__numList):
            self.__opList.insert(0, '=')

        def numMap(num):
            if num=='PI':
                return Expression.pi()
            else:
                return float(num)
            
        self.__numList = list(map(numMap,self.__numList))

    def __str__(self):
        return "( %s %s )" % (self.__opList,self.__numList)

    def __getitem__(self,index):
        return self.__opList[index],self.__numList[index]

    def __add__(self,other):
        res = copy.deepcopy(self)
        res.__opList.extend(other.__opList)
        res.__numList.extend(other.__numList)
        return res

    def __eq__(self,other): 
        return ( self.__opList==other.__opList ) and ( self.__numList==other.__numList )
        
    def __ne__(self,other): 
        return not ( self==other )

    
if __name__ == "__main__":
    expr1 = Expression("+1+2")
    expr2 = Expression("+3+4")
    expr3 = expr1+expr2
    expr4 = Expression("+1+2+3+4")
    print(expr3)
    print(expr4)
    if (expr3==expr4):
        print("Concatenation et comparaison OK")
    else:
        print("PROBLEME de concatenation et comparaison")
    if (expr3!=expr4):
        print("PROBLEME de concatenation et comparaison")
    else:
        print("Concatenation et comparaison OK")
