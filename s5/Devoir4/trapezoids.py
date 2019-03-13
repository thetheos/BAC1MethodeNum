from numpy import *


def trapezeEasy(f,a,b,n):
    
    i = linspace(a,b,n)
    U = f(i)
    h = i[2] - i[1]
    I = h/2 * (U[0] + U[-1] + 2 * sum(U[1:-1]))
    return I
""" 
def trapezeFun(f,a,b,n,nmax,tol):
    I1 = trapezeEasy(f,a,b,n)
    n = n*2
    I2 = trapezeEasy(f,a,b,n)
    for i in range(nmax):
        if abs(I2-I1) < tol: 
            print("Tolerance : " + str(tol))
            print("smaller tol " + str(I2))
            return I2, n, abs(I2-I1)
        n = n*2
        I1 = I2
        I2 = trapezeEasy(f,a,b,n)
        
    return I2,n,abs(I2-I1) 
"""
#Optimize function
def trapezeFun(f,a,b,n,nmax,tol):
    real_n_max = int(n * 2 **(round(log2(nmax/n))))
    
    I2 = trapezeEasy(f,a,b,real_n_max)
    real_n_max = real_n_max / 2
    I1 = trapezeEasy(f,a,b,real_n_max)
    
    while abs(I2-I1) < tol:
        print(abs(I2-I1) )
        real_n_max = real_n_max / 2
        I2 = I1
        I1 = trapezeEasy(f,a,b,real_n_max)
    
    return I2,real_n_max*2,abs(I2-I1) 
