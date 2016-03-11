from __future__ import print_function
import math
import maBiblio

s = maBiblio.Superellipse(10, 1, 1, 2)
print(s.area)

c = maBiblio.Circle(10, 1)
print(c.area)
print(c.perimeter)

s = maBiblio.Superellipsoid(10, 1, 1, 1, 2, 2)
print(s.volume, 4./3*math.pi)

s = maBiblio.Sphere(10, 1)
print(s.volume, 4./3*math.pi)
