# coding: utf8
"""
Fonctions utilisées dans la création des

- superellipses
- superellipsoides

"""

import math

def spe_cos(theta, epow):
    """
    calcule sign(cos(theta))|cos(theta)|^epow
    """
    cosw = math.cos(theta)
    return math.copysign(abs(cosw)**epow, cosw)

def spe_sin(theta, epow):
    """
    calcule sign(sin(theta))|sin(theta)|^epow
    """
    sinw = math.sin(theta)
    return math.copysign(abs(sinw)**epow, sinw)
