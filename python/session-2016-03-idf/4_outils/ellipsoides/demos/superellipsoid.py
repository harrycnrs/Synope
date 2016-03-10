from __future__ import print_function
import math
import ma_biblio

s = ma_biblio.Superellipse(10, 1, 1, 2)
print(s.area)

c = ma_biblio.Circle(10, 1)
print(c.area)
print(c.perimeter)

s = ma_biblio.Superellipsoid(10, 1, 1, 1, 2, 2)
print(s.volume, 4./3*math.pi)

s = ma_biblio.Sphere(10, 1)
print(s.volume, 4./3*math.pi)
