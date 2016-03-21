import numpy as np

def spe_cos(w, m):
    cosw = np.cos(w)
    return np.sign(cosw)*np.abs(cosw)**m

def spe_sin(w, m):
    sinw = np.sin(w)
    return np.sign(sinw)*np.abs(sinw)**m
    