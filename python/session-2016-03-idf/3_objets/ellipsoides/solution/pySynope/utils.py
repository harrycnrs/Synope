import math

def spe_cos(w, m):
    cosw = math.cos(w)
    return math.copysign(abs(cosw)**m, cosw)

def spe_sin(w, m):
    sinw = math.sin(w)
    return math.copysign(abs(sinw)**m, sinw)
    

