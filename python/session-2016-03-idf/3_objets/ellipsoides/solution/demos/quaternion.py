# -*- coding: utf-8 -*-

from pySynope import Point3d, Quaternion
import utils
import math

q = Quaternion(math.pi/4)
print(q)

pos = Quaternion(Point3d(1, 0, 0))
q2 = q*q
pos = (q2*pos*q2.conjugate()).point()
print(pos)  
