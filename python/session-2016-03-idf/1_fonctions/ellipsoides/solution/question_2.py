# coding: utf-8

# """
# Affiche une liste de points espacés de manière
# régulière pour un intervalle donné.
#
# Paramètres
# ==========
#
# begin : borne inférieure de l'intervalle
# end : borne supérieure de l'intervalle
# n : nombre de points
#
# Sortie
# ======
#
# None
#
# """

def linspace(begin, end, n):
  if (begin>end):
    print('ERROR: begin>end')
    return
  step = (end - begin)/(n-1)
  for i in range(n):
    print(begin + i*step)

linspace(0,1,10)
linspace(1,0,10)
