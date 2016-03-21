# coding: utf8
import numpy as np

from ..utils import spe_cos, spe_sin

class Superellipse(object):
  """
  définit une superellipse.

  x = rx c(theta, 2/m)
  y = ry s(theta, 2/m)

  où 

  c(theta, m) = sign(cos(theta))|cos(theta)|**m
  s(theta, m) = sign(sin(theta))|sin(theta)|**m
  
  Paramètres
  ==========

  n : nombre de points de discrétisation en theta

  rx : rayon suivant x

  ry : rayon suivant y

  m : puissance dans l'expression de la superellipse.

  Attributs
  =========
  n : nombre de points de discrétisation en theta

  rx : rayon suivant x

  ry : rayon suivant y

  m : puissance dans l'expression de la superellipse.

  Méthodes
  ========

  surface: renvoie les points de la surface.

  area: renvoie l'aire.    
  
  """

  def __init__(self, n, rx, ry, m):
    self.n = n
    self.rx = rx
    self.ry = ry
    self.m = m

  def surface(self):
    phi = np.linspace(0., 2.*np.pi, self.n)
    return self.rx*spe_cos(phi, 2./self.m), self.ry*spe_sin(phi, 2./self.m)

  def surface_with_square(self):
    n = self.n
    x = np.concatenate((np.linspace(-1, 1., n), np.ones(n-2), np.linspace(1, -1., n), -np.ones(n-2)))
    y = np.concatenate((-np.ones(n-1), np.linspace(-1, 1., n), np.ones(n-2), np.linspace(1, -1., n-1, endpoint=False)))
    return x*self.rx*(1. - .5*np.abs(y)**self.m)**(1./self.m),  y*self.ry*(1. - .5*np.abs(x)**self.m)**(1./self.m)

  @property
  def area(self):
    r = 1./self.m
    return 4**(1-r)*self.rx*self.ry*math.sqrt(np.pi)*math.gamma(1+r)/math.gamma(.5+r)

class Circle(Superellipse):
  def __init__(self, n, r):
    super(Circle, self).__init__(n, r, r, 2)

  @property
  def perimeter(self):
    return 2*np.pi*self.rx