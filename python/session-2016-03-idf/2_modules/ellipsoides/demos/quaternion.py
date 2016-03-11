from __future__ import print_function
import maBiblio
import math

print(maBiblio.rotate_using_complex(math.pi/4, [1, 0]))  
print(maBiblio.rotate_using_quaternion(math.pi/4, [0, 0, 1], [1, 0, 0]))