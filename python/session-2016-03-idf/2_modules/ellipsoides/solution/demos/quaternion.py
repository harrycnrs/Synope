from __future__ import print_function
import pySynope
import math

print(pySynope.rotate_using_complex(math.pi/4, [1, 0]))  
print(pySynope.rotate_using_quaternion(math.pi/4, [0, 0, 1], [1, 0, 0]))