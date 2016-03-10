# coding: utf8
import math

from ..linspace import linspace
from ..utils import c, s

# """
# Renvoie les coordonnées de la superellipse.
#
# x = rx c(theta, 2/m)
# y = ry s(theta, 2/m)
#
# où 
#
# c(theta, m) = sign(cos(theta))|cos(theta)|**m
# s(theta, m) = sign(sin(theta))|sin(theta)|**m
#
# Paramètres
# ==========
#
# n : nombre de points de discrétisation en theta
#
# rx : rayon suivant x
#
# ry : rayon suivant y
#
# m : puissance dans l'expression de la superellipse.
#
# Sortie
# ======
#
# les coordonnées de la superellipse.
#
# """
def superellipse(n, rx, ry, m):
  phi_list = linspace(0., 2.*math.pi, n)
  x = []
  y = []
  for phi in phi_list:
    x.append(rx*c(phi, 2./m))
    y.append(ry*s(phi, 2./m))
  return x, y