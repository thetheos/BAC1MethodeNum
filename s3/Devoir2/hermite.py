
import matplotlib
from matplotlib import pyplot as plt
from numpy import *

def hermite(x, X, U, dU):
    i = zeros(len(x),dtype=int)
    for j in range(1,len(X)-1):    
        i[X[j]<=x] = j #Permet de donner le bon interval de X pour une valeur de x,
    return U[i] + (x-X[i])*(dU[i] + (x-X[i])*(((3*(U[i+1]-U[i])/(X[i+1]-X[i])**2) - ((dU[i+1] + 2*dU[i])/(X[i+1]-X[i]))) + ((-2*(U[i+1]-U[i])/(X[i+1]-X[i])**3) + ((dU[i+1] + dU[i])/((X[i+1]-X[i])**2)))*(x-X[i])))

