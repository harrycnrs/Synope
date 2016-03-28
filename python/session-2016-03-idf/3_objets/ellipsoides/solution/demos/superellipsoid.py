
import pySynope
import utils
import math

print("superellipsoid(1, 1, 1, 2, 2) cloud(4)")
se = pySynope.Superellipsoid(1, 1, 1, 2, 2)
x, y, z = se.cloud(4)
print(utils.myformat2d(x))
print(utils.myformat2d(y))
print(utils.myformat2d(z))

print("volumes")
print(se.volume, 4./3*math.pi)
sphere = pySynope.Sphere(1)
print(sphere.volume, 4./3*math.pi)
