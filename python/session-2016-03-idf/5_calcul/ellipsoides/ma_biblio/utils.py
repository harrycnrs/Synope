import numpy as np

def c(w, m):
  cosw = np.cos(w)
  return np.sign(cosw)*np.abs(cosw)**m

def s(w, m):
  sinw = np.sin(w)
  return np.sign(sinw)*np.abs(sinw)**m