# -*- coding: utf-8 -*-

import pySynope
import utils

x, y = pySynope.superellipse(5, 1, 1, 2)
print("superellipse(5, 1, 1, 2)")
print(utils.myformat(x))
print(utils.myformat(y))

x, y, z = pySynope.superellipsoid(4, 1, 1, 1, 2, 2)
print("superellipsoid(4, 1, 1, 1, 2, 2)")
print(utils.myformat2d(x))
print(utils.myformat2d(y))
print(utils.myformat2d(z))
