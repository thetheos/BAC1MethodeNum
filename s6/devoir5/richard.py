from numpy import *


def trapezeEasy(f,a,b,n):
    i = linspace(a,b,n+1)
    U = f(i)
    h = (b - a)/(n)
    I = h * (U[0]/2 + U[-1]/2 +  sum(U[1:-1]))
    return I

def richard(I0 , I1 , j ):
    A = 2**(2*j)
    return (A*I1 - I0)/(A-1)

def romberg(f,a,b,n,nmax,tol):
    matrix = [[trapezeEasy(f,a,b,n)]]
    print(trapezeEasy(f,a,b,n))
    print(matrix)
    
    error = 1  #matrix[1][0] - matrix[0][0]
    
    i = 1
    n = n * 2
    
    while error > tol and n<nmax:
        matrix.append([])
        matrix[i].append(trapezeEasy(f,a,b,n))
        for it in range(1,i+1):
            matrix[i].append(richard(matrix[i-1][it-1], matrix[i][it-1],it))
        
        error = abs(matrix[i][-1] - matrix[i][-2])
        
        n = n*2
        i += 1
    for elm in matrix:
        print(elm)
    I = matrix[i-1][-1]
    return I,n,error