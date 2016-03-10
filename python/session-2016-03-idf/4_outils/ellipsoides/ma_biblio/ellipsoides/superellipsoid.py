# coding: utf8
import math

from ..linspace import linspace
from ..utils import c, s

def beta_func(r, t):
  return math.gamma(r)*math.gamma(t)/math.gamma(r+t)

class Superellipsoid(object):
  """
  Définit une superellipsoid.

  x = rx c(theta, 2/m1) c(phi, 2/m2)
  y = ry s(theta, 2/m1) c(phi, 2/m2)
  y = rz s(phi, 2/m2)

  où
  c(theta, m) = sign(cos(theta))|cos(theta)|**m
  s(theta, m) = sign(sin(theta))|sin(theta)|**m

  Paramètres
  ==========

  n : nombre de points de discrétisation en theta et en phi

  rx : rayon suivant x

  ry : rayon suivant y

  rz : rayon suivant z

  m : puissance dans l'expression de la superellipse.

  Attributs
  =========

  n : nombre de points de discrétisation en theta et en phi

  rx : rayon suivant x

  ry : rayon suivant y

  rz : rayon suivant z

  m : puissance dans l'expression de la superellipse.

  Méthodes
  ========

  surface : renvoie le nuage de points de la surface.

  volume : renvoie le volume de la superellipsoide.
  """
  def __init__(self, n, rx, ry, rz, m1, m2):
    self.n = n
    self.rx = rx
    self.ry = ry
    self.rz = rz
    self.m1 = m1
    self.m2 = m2

  def surface(self):
    phi_list = linspace(-.5*math.pi, .5*math.pi, self.n)
    beta_list = linspace(-math.pi, math.pi, self.n)

    x = []
    y = []
    z = []
    for beta in beta_list:
      x.append([])
      y.append([])
      z.append([])
      for phi in phi_list:
        x[-1].append(self.rx*c(phi, 2./self.m1)*c(beta, 2./self.m2))
        y[-1].append(self.ry*c(phi, 2./self.m1)*s(beta, 2./self.m2))
        z[-1].append(self.rz*s(phi, 2./self.m1))
    return x, y, z

  @property
  def volume(self):
    r = 1./self.m1
    t = 1./self.m2
    return 8./3.*self.rx*self.ry*self.rz*r*t*beta_func(r, r)*beta_func(2*t, t)

class Sphere(Superellipsoid):
  def __init__(self, n, r):
    super(Sphere, self).__init__(n, r, r, r, 2, 2)

  @property
  def area(self):
    return 4*math.pi*self.rx**2