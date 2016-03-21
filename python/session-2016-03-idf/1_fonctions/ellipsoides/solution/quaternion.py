# coding: utf8
from __future__ import print_function
import math

def hamilton_product(q1, q2):
  return  [ q1[0]*q2[0] - q1[1]*q2[1] - q1[2]*q2[2] - q1[3]*q2[3],
            q1[0]*q2[1] + q1[1]*q2[0] + q1[2]*q2[3] - q1[3]*q2[2],
            q1[0]*q2[2] - q1[1]*q2[3] + q1[2]*q2[0] + q1[3]*q2[1],
            q1[0]*q2[3] + q1[1]*q2[2] - q1[2]*q2[1] + q1[3]*q2[0]]
  
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

  return hamilton_product([w, x, y, z], hamilton_product([0] + pos, [w, -x, -y, -z]))[1:]


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


# """
# demonstration code
# """

print(rotate_using_complex(math.pi/4, [1, 0]))  
print(rotate_using_quaternion(math.pi/4, [0, 0, 1], [1, 0, 0]))
print(rotate_using_quaternion_1(math.pi/4, [0, 0, 1], [1, 0, 0]))
