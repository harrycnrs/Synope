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
        print ("Concatenation et comparaison OK")
    else:
        print("PROBLEME de concatenation et comparaison")
    if (expr3!=expr4):
        print("PROBLEME de concatenation et comparaison")
    else:
        print("Concatenation et comparaison OK")
    
