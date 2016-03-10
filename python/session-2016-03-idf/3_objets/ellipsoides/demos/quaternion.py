from __future__ import print_function
import maBiblio
import math

q = maBiblio.Quaternion()
print(q)

q.set_angle(math.pi/4)
q.normalize()
print(q)

print((q*q).rotate([1, 0, 0]))
