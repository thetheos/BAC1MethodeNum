from numpy import *

def function_list(u):
    return [10*u[1] -10*u[0], 28*u[0] - u[1] - u[0]*u[2], u[0]*u[1] -8/3 * u[2]]

def lorenz(Xstart,Xend,Ustart,n):
    X,h = linspace(Xstart,Xend,n+1,retstep=True)
    U_LIST = zeros((n+1,3))
    for pos,i in enumerate(X):
        K1 = array(function_list(Ustart))
        K2 = array(function_list(Ustart+ h/2 * K1))
        K3 = array(function_list(Ustart + h/2 * K2))
        K4 = array(function_list(Ustart + h * K3))
        U = Ustart + h/6 * (K1+ 2* K2 + 2*K3 +K4)
        U_LIST[pos][0] = U[0]
        U_LIST[pos][1] = U[1]
        U_LIST[pos][2] = U[2]
        Ustart = U
        
    print(U_LIST.shape)
    return X,U_LIST