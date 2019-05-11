
from scipy.linalg import norm
from scipy.linalg import solve

def laddersIterate(geometry, v):
    a= geometry[0]; b = geometry[1]; c = geometry[2]; y = v[1]; x = v[0]
    f1 = a**2 * x**2 - (x**2 + c**2)*(x+y)**2
    f2 = b**2 * y**2 - (y**2 + c**2)*(x+y)**2
    df1dx = 2*a**2*x - 2*(x+y)*(x**2 + c**2) - 2*x*(x+y)**2
    df1dy = -2*(x+y)*(x**2 + c**2)
    df2dx = -2*(y**2 + c**2)*(x+y)
    df2dy = 2* b**2 *y -2*(x+y)*(y**2 +c**2) - 2 * y* (x+y)**2
    jacc_matrix = [[df1dx, df1dy], [df2dx, df2dy]]
    b = [f1,f2]
    dx = solve(jacc_matrix, b)
    v =  v - dx 
    return v
    
def laddersSolve(geometry,tol,nmax):
    a= geometry[0]; b = geometry[1]; c = geometry[2]
    if a==b and c ==b:
        return [-1,-1]
    delta = tol+1
    n = 0
    x = [(b-c)/2,(a-c)/2]
    while (norm(delta) > tol and n < nmax):
        xold = x
        x = laddersIterate(geometry,xold)
        delta = x-xold; n = n+1
        print(" Estimated error %9.2e at iteration %d : " % (norm(delta),n),x)
    if norm(delta) > tol * 1e5:
        return [-1,-1]
    return x