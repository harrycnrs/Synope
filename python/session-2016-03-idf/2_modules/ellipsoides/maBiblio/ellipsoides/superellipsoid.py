# coding: utf8
import math

from ..linspace import linspace
from ..utils import c, s

# """
# Renvoie les coordonnées de la superellipsoid.
#
# x = rx c(theta, 2/m1) c(phi, 2/m2)
# y = ry s(theta, 2/m1) c(phi, 2/m2)
# y = rz s(phi, 2/m2)
#
# où
# c(theta, m) = sign(cos(theta))|cos(theta)|**m
# s(theta, m) = sign(sin(theta))|sin(theta)|**m
#
# Paramètres
# ==========
#
# n : nombre de points de discrétisation en theta et en phi
#
# rx : rayon suivant x
#
# ry : rayon suivant y
#
# rz : rayon suivant z
#
# m : puissance dans l'expression de la superellipse.
#
# Sortie
# ======
#
# les coordonnées de la superellipse.
#
# """
def superellipsoid(n, rx, ry, rz, m1, m2):
  phi_list = linspace(-.5*math.pi, .5*math.pi, n)
  beta_list = linspace(-math.pi, math.pi, n)

  x = []
  y = []
  z = []
  for beta in beta_list:
    x.append([])
    y.append([])
    z.append([])
    for phi in phi_list:
      x[-1].append(rx*c(phi, 2./m1)*c(beta, 2./m2))
      y[-1].append(ry*c(phi, 2./m1)*s(beta, 2./m2))
      z[-1].append(rz*s(phi, 2./m1))
  return x, y, z

