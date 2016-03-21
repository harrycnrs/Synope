from __future__ import print_function
import math
import pySynope

s = pySynope.Superellipse(10, 1, 1, 2)
print(s.area)

c = pySynope.Circle(10, 1)
print(c.area)
print(c.perimeter)

s = pySynope.Superellipsoid(10, 1, 1, 1, 2, 2)
print(s.volume, 4./3*math.pi)

s = pySynope.Sphere(10, 1)
print(s.volume, 4./3*math.pi)
