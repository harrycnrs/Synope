# coding: utf8
import math

from ..linspace import linspace
from ..utils import spe_cos, spe_sin

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
  x = []
  y = []
  z = []
  for theta in linspace(-math.pi, math.pi, n):
    x.append([])
    y.append([])
    z.append([])
    for phi in linspace(-.5*math.pi, .5*math.pi, n):
      x[-1].append(rx*spe_cos(phi, 2./m1)*spe_cos(theta, 2./m2))
      y[-1].append(ry*spe_cos(phi, 2./m1)*spe_sin(theta, 2./m2))
      z[-1].append(rz*spe_sin(phi, 2./m1))
  return x, y, z

def beta_func(r, t):
  return math.gamma(r)*math.gamma(t)/math.gamma(r+t)

def superellipsoid_volume(rx, ry, rz, m1, m2):
  r = 1./m1
  t = 1./m2
  return 8./3.*rx*ry*rz*r*t*beta_func(r, r)*beta_func(2*t, t)
