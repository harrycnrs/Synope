# -*- coding: utf-8 -*-

import pySynope
import utils
import math

pos = [1, 0]
pos = pySynope.rotate_using_complex(math.pi/4, pos)
pos = pySynope.rotate_using_complex(math.pi/4, pos)

print(utils.myformat(pos))  

pos = [1, 0, 0]
pos = pySynope.rotate_using_quaternion(math.pi/4, [0, 0, 1], pos)
pos = pySynope.rotate_using_quaternion(math.pi/4, [0, 0, 1], pos)

print(utils.myformat(pos))  
