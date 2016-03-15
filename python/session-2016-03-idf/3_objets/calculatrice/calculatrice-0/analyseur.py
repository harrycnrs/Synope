# -*- coding: utf-8 -*-

import re

parse_op = re.compile(r'[-+*/]')
parse_num = re.compile(r'[^-+*/]+')

def analyse(s):

    opList = parse_op.findall(s)
    numList = list(map(float, parse_num.findall(s)))
    
    if len(opList) != len(numList):
        opList.insert(0, '=')

    return opList, numList
    
