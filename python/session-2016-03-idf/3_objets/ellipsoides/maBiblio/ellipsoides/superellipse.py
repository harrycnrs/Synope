# coding: utf8
import math

from ..linspace import linspace
from ..utils import c, s

# """
# définit une superellipse.
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
# Attributs
# =========
# n : nombre de points de discrétisation en theta
#
# rx : rayon suivant x
#
# ry : rayon suivant y
#
# m : puissance dans l'expression de la superellipse.
#
# Méthodes
# ========
#
# surface: renvoie les points de la surface.
#
# area: renvoie l'aire.    
# 
# """
class Superellipse(object):

  def __init__(self, n, rx, ry, m):
    self.n = n
    self.rx = rx
    self.ry = ry
    self.m = m

  def surface(self):
    phi_list = linspace(0., 2.*math.pi, self.n)
    x = []
    y = []
    for phi in phi_list:
      x.append(self.rx*c(phi, 2./self.m))
      y.append(self.ry*s(phi, 2./self.m))
    return x, y

  @property
  def area(self):
    r = 1./self.m
    return 4**(1-r)*self.rx*self.ry*math.sqrt(math.pi)*math.gamma(1+r)/math.gamma(.5+r)

class Circle(Superellipse):
  def __init__(self, n, r):
    super(Circle, self).__init__(n, r, r, 2)

  @property
  def perimeter(self):
    return 2*math.pi*self.rx
    
