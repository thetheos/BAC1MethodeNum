# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 0
#
# Script de test
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 

import matplotlib 
from matplotlib import pyplot as plt

from numpy import *
from math import sqrt
from solveRatio import solveRatio

#
# -1- Test de la fonction solveRatio$
#     Essayer comme argument phi = 0.5 :-)
#

phi = (1 + sqrt(5.0)) / 2


x = solveRatio(phi)
print("Solution with phi = %.6f is given by : \n  " % phi,end='')
print(x)

#
# -2- Un petit design moderniste :-)
#     Typiquement, le genre de profil de fenêtre que Lecorbusier utilisait !
#

X = array([0,x[0],x[0],0,0]) + x[1]
Y = array([0,0,x[1],x[1],0])

matplotlib.rcParams['toolbar'] = 'None'
plt.rcParams['figure.facecolor'] = 'moccasin'
plt.axis('equal')
plt.axis('off')
plt.text(0.5,-0.0625*phi,'$\phi = %.6f$' % phi) 
plt.plot([0,phi,phi,0,0,1,1],[0,0,1,1,0,0,1],'-b')
plt.plot(X,Y,'-r')
plt.plot(Y,X,'-r')
plt.show()
