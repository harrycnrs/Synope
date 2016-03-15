#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  01_Intro_exo_final.py
#  
#  Copyright 2016  <pi@raspberrypi>
#  version bonus

"""
Created on Wed Nov 26 22:31:38 2014
Update on Sun Jan 24 12:32:11 CET 2016

Écrivez un programme qui convertisse en degrés Celsius une température 
exprimée au départ en degrés Fahrenheit, ou l’inverse.

La formule de conversion est : TF = TC × 1,8 + 32
TF : température en degré Farenheit
TC : température en degré Celsius

@author: chalgand
@revision : fmendes
"""

goodAnswer=False
while goodAnswer==False:
    print( "Dans quel sens voulez-vous faire la conversion ?")
    print( "1 - Degré Celsius    vers  Degré Farenheit")
    print( "2 - Degré Farenheit  vers  Degré Celsius")
    answer = input()
    print(answer)
    try:
        answer = int(answer)
    except:
        print("Erreur de typage (casting error)")
        #pass #Voir l'autre cast
    if type(answer)==int and (answer == 1 or answer == 2):
        goodAnswer=True
        print(answer)

print("Vous avez choisi la conversion : " + \
    ("Degré Celsius vers Degré Farenheit" if answer==1 \
    else "Degré Farenheit  vers  Degré Celsius"))

temp = "une mauvaise température"
while type(temp)!=float:
    temp = input("Veuillez entrer la température à convertir : ")
    try:
        temp = int(temp)
    except:
        pass

if answer == 1:
    print temp, " degré Celsius = ", temp*1.8+32," degré Farenheit"
else:
    print temp, " degré Farenheit = ", (temp-32)/1.8," degré Celsius"

