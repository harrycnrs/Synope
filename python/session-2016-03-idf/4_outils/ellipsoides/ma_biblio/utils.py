import math

def c(w, m):
  cosw = math.cos(w)
  return math.copysign(abs(cosw)**m, cosw)

def s(w, m):
  sinw = math.sin(w)
  return math.copysign(abs(sinw)**m, sinw)