from __future__ import print_function
import pySynope
import matplotlib.pyplot as plt

c = pySynope.Circle(10, 1)
x, y = c.surface_with_square()
plt.plot(x, y, '.')
plt.show()

c = pySynope.Superellipse(100, 1, 1, 100)
x, y = c.surface()
plt.plot(x, y, '.')
plt.show()