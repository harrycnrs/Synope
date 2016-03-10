from __future__ import print_function
import ma_biblio
import math

q = ma_biblio.Quaternion()
print(q)

q.set_angle(math.pi/4)
q.normalize()
print(q)

print((q*q).rotate([1, 0, 0]))
