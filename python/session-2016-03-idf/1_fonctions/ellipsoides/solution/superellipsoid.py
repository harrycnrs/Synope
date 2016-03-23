# coding: utf8
from __future__ import print_function
from six.moves import range
# coding: utf-8

import math

# """
# Renvoie une liste de points espacés de manière régulière
# pour un intervalle donné.
#
# Paramètres
# ==========
#
# begin : borne inférieure de l'intervalle
#
# end : borne supérieure de l'intervalle
#
# n : nombre de points
#
# Sortie
# ======
#
# Renvoie la liste des points de discrétisation.
#
# """
def linspace(begin, end, n):
  h = (end - begin)/(n-1)
  return [begin + i*h for i in range(n)]

def spe_cos(w, m):
  cosw = math.cos(w)
  return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
  sinw = math.sin(w)
  return math.copysign(abs(sinw)**m, sinw)

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
    x.append(rx*spe_cos(phi, 2./m))
    y.append(ry*spe_sin(phi, 2./m))
  return x, y

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
      x[-1].append(rx*spe_cos(phi, 2./m1)*spe_cos(beta, 2./m2))
      y[-1].append(ry*spe_cos(phi, 2./m1)*spe_sin(beta, 2./m2))
      z[-1].append(rz*spe_sin(phi, 2./m1))
  return x, y, z


# """
# demonstration code
# """

print("superellipse(10, 1, 1, 2)")
x, y = superellipse(5, 1, 1, 2)
print(x)
print(y)

print("superellipsoid(10, 1, 1, 1, 2, 2)")
x, y, z = superellipsoid(10, 1, 1, 1, 2, 2)
print(x)
print(y)
print(z)
