# coding: utf8
import math

from ..linspace import linspace
from ..utils import spe_cos, spe_sin

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
  x = []
  y = []
  for theta in linspace(0., 2.*math.pi, n):
    x.append(rx*spe_cos(theta, 2./m))
    y.append(ry*spe_sin(theta, 2./m))
  return x, y
  
def superellipse_area(rx, ry, m):
  r = 1./m
  return 4**(1-r)*rx*ry*math.sqrt(math.pi)*math.gamma(1+r)/math.gamma(.5+r)
