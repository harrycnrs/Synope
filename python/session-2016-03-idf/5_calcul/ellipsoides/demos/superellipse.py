from __future__ import print_function
import ma_biblio
import matplotlib.pyplot as plt

c = ma_biblio.Circle(10, 1)
x, y = c.surface_with_square()
plt.plot(x, y, '.')
plt.show()

c = ma_biblio.Superellipse(10, 1, 1, 1)
x, y = c.surface_with_square()
plt.plot(x, y, '.')
plt.show()