from numpy import *

def trapezeEasy(f,a,b,n):
    i = linspace(a,b,n+1)
    U = f(i)
    h = (b - a)/(n)
    I = h * (U[0]/2 + U[-1]/2 +  sum(U[1:-1]))
    return I
  
def trapezeFun(f,a,b,n,nmax,tol):
    I1 = trapezeEasy(f,a,b,n)  
    n = n*2
    I2 = trapezeEasy(f,a,b,n)
    while n*2 < nmax:
        if abs(I2-I1) < tol: 
            return I2, n, abs(I2-I1)
        n = n*2
        I1 = I2
        I2 = trapezeEasy(f,a,b,n)
    return I2,n,abs(I2-I1) 
