from numpy import *
from math  import factorial
from numpy.linalg import solve

eps = finfo('float').eps
 
def doublePrime(alpha):

    n = len(alpha)
    b = zeros(n)
    
    b[2] = 1
    
    A = empty((n,n))
    for i in range(n):
        A[i] = ((alpha)**i)/factorial(i)
    
    beta = solve(A,b)
    E = sum(abs(dot(A,beta) - b)) * dot(abs(beta), abs(alpha**n)) 
    
    print(beta)
    if abs((dot(beta,alpha**n)))<=E: 
        factor = factorial(n+1)/(dot(beta,alpha**(n+1)))
        order = n-1
    else:
        factor = factorial(n)/(dot(beta,alpha**(n)))
        order = n-2

    return beta,factor,order