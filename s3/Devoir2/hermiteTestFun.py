# -------------------------------------------------------------------------
#
# PYTHON for DUMMIES 18-19
# Problème 2
#
# Script de test un peu plus rigolo
# Pour introduite un point : faire un clic sur la figure
# Un double clic permet d'obtenir le calcul de la courbe d'Hermite
#
#  Vincent Legat
#
# -------------------------------------------------------------------------
# 

import matplotlib
from matplotlib import pyplot as plt
from numpy import *

# ====================== callback pour les événements avec la souris ======
#
#  Observer la gestion distincte du clic simple et double :-)
#  Apres un evenement, on redessine la figure avec draw()
#

def hermite(x, X, U, dU):
    i = zeros(len(x),dtype=int)
    for j in range(1,len(X)-1):    
        i[X[j]<=x] = j #Permet de donner le bon interval de X pour une valeur de x,
    return U[i] + (x-X[i])*(dU[i] + (x-X[i])*(((3*(U[i+1]-U[i])/(X[i+1]-X[i])**2) - ((dU[i+1] + 2*dU[i])/(X[i+1]-X[i]))) + ((-2*(U[i+1]-U[i])/(X[i+1]-X[i])**3) + ((dU[i+1] + dU[i])/((X[i+1]-X[i])**2)))*(x-X[i])))




"""  
    A = (3*(U[i+1]-U[i])/(X[i+1]-X[i])**2) - ((dU[i+1] + 2*dU[i])/(X[i+1]-X[i])) 
    B = (-2*(U[i+1]-U[i])/(X[i+1]-X[i])**3) + ((dU[i+1] + dU[i])/((X[i+1]-X[i])**2)) 
    uh = U[i] + (x-X[i])*(dU[i] + (x-X[i])*(A + B*(x-X[i])))

    return uh
"""
def mouse(event):
  global X,Y,n
  if (event.dblclick):
    X  = append(X,[X[0]])
    Y  = append(Y,[Y[0]])
    dX = array([X[1]-X[n-1],*(X[2:n+1]-X[0:n-1]),X[1]-X[n-1]])
    dY = array([Y[1]-Y[n-1],*(Y[2:n+1]-Y[0:n-1]),Y[1]-Y[n-1]])
    T  = arange(0,n+1)
    t  = arange(0,n+0.001,0.001)
    x  = hermite(t,T,X,dX)
    y  = hermite(t,T,Y,dY)
    plt.plot(x,y,'-b')
    X,Y = [],[]; n = 0
  else :    
    x = event.xdata 
    y = event.ydata
    if (x != None and y != None) :
      n = n + 1
      X = append(X,[x])
      Y = append(Y,[y])
      print("New data : " + str(x) + "," + str(y))
      plt.plot([x],[y],'.r',markersize=10)
  fig.canvas.draw()


# ============================= mainProgram ===============================
 
matplotlib.rcParams['toolbar'] = 'None'
matplotlib.rcParams['lines.linewidth'] = 1
plt.rcParams['figure.facecolor'] = 'silver'

X,Y = [],[]; n = 0   
fig = plt.figure("Hermite interpolation")
fig.canvas.mpl_connect('button_press_event',mouse)
plt.ylim((0,1)); plt.xlim((0,1.3)); plt.axis("off")

plt.show()



