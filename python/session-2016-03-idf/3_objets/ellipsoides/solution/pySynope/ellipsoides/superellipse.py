# coding: utf8

import math

from ..linspace import linspace
from ..utils import spe_cos, spe_sin

class Superellipse:
  """
  Définit une superellipse.

  x = rx c(theta, 2/m)
  y = ry s(theta, 2/m)

  où 

  c(theta, m) = sign(cos(theta))|cos(theta)|**m
  s(theta, m) = sign(sin(theta))|sin(theta)|**m
  
  Attributs
  =========

  rx : rayon suivant x

  ry : rayon suivant y

  m : puissance dans l'expression de la superellipse.

  Méthodes
  ========

  surface: renvoie les points de la surface.

  area: renvoie l'aire.    
  
  """

  def __init__(self, rx, ry, m):
    self.rx = rx
    self.ry = ry
    self.m = m

  # n : nombre de points de discrétisation en theta
  def cloud(self, n):
    x = []
    y = []
    for theta in linspace(0., 2.*math.pi, n):
      x.append(self.rx*spe_cos(theta, 2./self.m))
      y.append(self.ry*spe_sin(theta, 2./self.m))
    return x, y

  @property
  def area(self):
    r = 1./self.m
    return 4**(1-r)*self.rx*self.ry*math.sqrt(math.pi)*math.gamma(1+r)/math.gamma(.5+r)

class Circle(Superellipse):
  def __init__(self, r):
    super().__init__(r, r, 2)

  @property
  def perimeter(self):
    return 2*math.pi*self.rx
    
    

