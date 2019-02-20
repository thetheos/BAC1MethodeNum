#
# Splines cubiques
# Vincent Legat - 2018
# Ecole Polytechnique de Louvain
#

from numpy import *

n = 21
L = 1
X = linspace(-L,L,n)       ; print(X)  # Pour debugger step by step                 
U = sin(2*pi*X)            ; print(U)  # Pour debugger step by step         

x = linspace(-L,L,10*n)

#
# -1- Acceder aux donnÃ©es d'un tableau
#     Assez proche de la syntaxe de MATLAB
#     Attention : on numÃ©rote Ã  partir de zero en Python
#       X[0:21:2] Python = MATLAB X(1:2:20)
#

print(X)
print(X[:])
print(X[0:10])
print(X[0:21:2])

#
# -2- Une copie et une vue d'un tableau
#     Attention : ceci est diffÃ©rent de MATLAB !
#     =====> beaucoup de bugs vicieux possibles....
#     Y = une vue du mÃªme espace mÃ©moire
#     Z = une vraie copie du mÃ©moire
#

Y = X[0:21:2]
print(Y)
Y[0] = 69;    print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))
X[0] = 456;   print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))
X[0] = -1;    print('X[0] = %3d - Y[0] = %3d' % (X[0],Y[0]))
Z = copy(X)
Z[0] = 69;    print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))
X[0] = 456;   print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))
X[0] = -1;    print('X[0] = %3d - Y[0] = %3d - Z[0] = %3d' % (X[0],Y[0],Z[0]))

#
# -3- Calcul des splines cubiques
#

from scipy.interpolate import CubicSpline as spline

uSpline1 = spline(X[0:10],U[0:10])(x)
uSpline2 = spline(X[0:21:2],U[0:21:2])(x)

#
# -4- Et le joli dessin :-)
#

import matplotlib 
from matplotlib import pyplot as plt

plt.plot(x,uSpline1,'-b',label='spline sur les 10 premiers point')
plt.plot(x,uSpline2,'-r',label='spline sur un point sur deux')
plt.plot(X[0:10],U[0:10],'.r',markersize=20,label='10 premiers points')
plt.plot(X[0:21:2],U[0:21:2],'.b',markersize=10,label='1 point sur 2')


plt.legend(loc='upper right')
plt.show()
