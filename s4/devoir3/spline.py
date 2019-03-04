from numpy import *

def spline(x, h, U):
    n = size(U); X = arange(0,n+1)*h

    #Création de la liste
    i = searchsorted(X[1:], x)
    
    #Création de la matrice
    diag_line = ones(n, dtype=int)
    A = diag(diag_line*4) + diag(diag_line[1:], -1) + diag(diag_line[1:], 1)
    A[0,-1] = 1
    A[-1,0] = 1
   
    #creation du vecteur b
    b_index = {0: append(arange(1,n), [0]), 1: arange(0,n), 2: arange(-1,n-1)}
    b = U[b_index[0]] -2*U[b_index[1]] + U[b_index[2]]
    
    #Resolution de l'équation
    DU = linalg.solve(((h*h)/6)*A, b)

    U = append(U, U[0])
    DU = append(DU, DU[0])
    
    diff_1 = X[i+1] - x
    diff_2 = x - X[i]
    
    
    uh = diff_1 * (DU[i]/6 * ((diff_1 * diff_1)/h - h) + U[i]/h) + diff_2*( (DU[i+1]/6)*((diff_2*diff_2)/h - h) + U[i+1]/h )
    
    return uh