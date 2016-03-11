# coding: utf8
from __future__ import print_function
import math

__all__ = ['rotate_using_quaternion', 'rotate_using_complex']

# """
# rotation 3D d'une position à l'aide d'une représentation quaternion.
#
# Paramètres
# ==========
#
# angle : radians
# 
# axe : liste de taille 3
#       axe de rotation
#
# pos : liste de taille 3
#       point à faire tourner
#
# Sortie
# ======
#
# la position tournée
#
# """
def rotate_using_quaternion(angle, axe, pos):
  if len(axe) != 3:
    print("La taille de axes doit être de 3\n")
    return

  if len(pos) != 3:
    print("La taille de pos doit être de 3\n")
    return

  x = math.sin(angle/2)*axe[0]
  y = math.sin(angle/2)*axe[1]
  z = math.sin(angle/2)*axe[2]
  w = math.cos(angle/2)
  return [(1-2*y*y-2*z*z)*pos[0] +   (2*x*y-2*z*w)*pos[1] +   (2*x*z+2*y*w)*pos[2],
            (2*x*y+2*z*w)*pos[0] + (1-2*x*x-2*z*z)*pos[1] +   (2*y*z-2*x*w)*pos[2],
            (2*x*z-2*y*w)*pos[0] +   (2*y*z+2*x*w)*pos[1] + (1-2*x*x-2*y*y)*pos[2]]

# """
# rotation 2D d'une position à l'aide d'une représentation complexe.
#
# Paramètres
# ==========
#
# angle: radians
#
# pos : liste de taille 2
#       point à faire tourner
#
# Sortie
# ======
#
# la position tournée
#
# """
def rotate_using_complex(angle, pos):
  if len(pos) != 2:
    print("La taille de pos doit être de 2\n")
    return
  x = math.cos(angle)
  y = math.sin(angle)
  return [x*pos[0] - y*pos[1], x*pos[1] + y*pos[0]] 

if __name__ == '__main__':
  print(rotate_using_complex(math.pi/4, [1, 0]))  
  print(rotate_using_quaternion(math.pi/4, [0, 0, 1], [1, 0, 0]))