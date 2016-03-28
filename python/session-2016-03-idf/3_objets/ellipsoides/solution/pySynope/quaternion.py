# coding: utf8

from .point3d import Point3d
import math

def hamilton_product(q1, q2):
  return  [ q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
            q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
            q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
            q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]]

class Quaternion:
    
  def __init__(self, *args):
    if len(args)<1:
      raise RuntimeError("not enough arguments")
    if len(args)>2:
      raise RuntimeError("too much arguments")
    if isinstance(args[0],Point3d):
      self.w = 0
      self.coords = args[0]
      if len(args)>1:
        raise RunTimeError("too much arguments")
    elif isinstance(args[0],float):
      angle = args[0]
      if len(args)==1:
        axe = Point3d(0,0,1)
      else:
        if not isinstance(args[0],Point3d):
          raise RunTimeError("wrong second argument")
        axe = args[1]
      self.w = math.cos(angle/2)
      self.coords = axe*math.sin(angle/2)
    elif len(args[0])==4:
      self.w = args[0][0]
      self.coords = Point3d(args[0][1],args[0][2],args[0][3])
    else:
      raise RuntimeError("wrong first argument")
    
  @property
  def w(self):
    return self.__w

  @w.setter
  def w(self, value):
    self.__w = value

  @property
  def x(self):
    return self.coords.x

  @x.setter
  def x(self, value):
    self.coords.x = value

  @property
  def y(self):
    return self.coords.y

  @y.setter
  def y(self, value):
    self.coords.y = value

  @property
  def z(self):
    return self.coords.z

  @z.setter
  def z(self, value):
    self.coords.z = value

  def point(self):
    if self.w!= 0:
        raise ValueError('w should be 0')
    return self.coords

  def __add__(self, q):
    return Quaternion((self.w + q.w, self.x + q.x, self.y + q.y, self.z + q.z))

  def __sub__(self, q):
    return Quaternion((self.w - q.w, self.x - q.x, self.y - q.y, self.z - q.z))

  def __mul__(self, q):
    return Quaternion(hamilton_product([self.w, self.x, self.y, self.z],
      [q.w, q.x, q.y, q.z]))
  
  def conjugate(self):
    return Quaternion((self.w, -self.x, -self.y, -self.z))

  def __str__(self):
    return '({:+.2f} {:+.2f}i {:+.2f}j {:+.2f}k)'.format(self.w,self.x,self.y,self.z)

  def __repr__(self):
    return __str__(self)

