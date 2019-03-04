from numpy import *
import matplotlib.pyplot as plt
from timeit import default_timer as timer


def tic():
    global startTime
    startTime = timer()

# =========================================================================
 
def toc(message = ''):
    global startTime
    stopTime = timer()
    if message:
        message = ' (' + message + ')' ;
    print("Elapsed time is %.6f seconds %s" % ((stopTime - startTime),message) )
    startTime = 0

def spline(x,h,U):
    n = size(U); X = arange(0,n+1)*h
    print(size(U))
    print(size(X))
    i = zeros(len(x),dtype=int)
    i = searchsorted(X[1:], x) #
    
    U = append(U,U[0])
   
    test_ar = ones(n, dtype=int)
    A = diag(test_ar*4) + diag(test_ar[1:], 1) + diag(test_ar[1:], -1)
    A[-1,0] = 1
    A[0,-1] = 1
    
    print(A)

    b = zeros(n, dtype=int)
    small_index = arange(0,n)
    
    #b = array([0])
    b = U[small_index+1] - 2 * U[small_index] + U[small_index-1]
    b = append(b, U[0] - 2 * U[-1] + U[small_index[-2]] )
    print(b)
    #[0] = 0
    b=U[range(-1,n-1)]-2*U[0:n]+U[append(arange(1,n),[0])]
    print(b)


    
    
    DU = linalg.solve(((h*h)/6)*A, b)
    
    #uh = ( ((DU[i]/(6*h)) * diff_1 * diff_1 * diff_1) + (DU[i+1]/(6*h) * diff_2 * diff_2 * diff_2) + (U[i]/h - DU[i]*h/6)*diff_1 + (U[i+1]/h - DU[i+1]*h/6)*diff_2 ) 
    
    
    diff_1 = X[i+1] - x
    diff_2 = x - X[i]
    
    uh = ( ((DU[i]/(6*h)) * diff_1 * diff_1 * diff_1) + (DU[i+1]/(6*h) * diff_2 * diff_2 * diff_2) + (U[i]/h - DU[i]*h/6)*diff_1 + (U[i+1]/h - DU[i+1]*h/6)*diff_2 ) 
    
    return uh

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
    

n = 4;
h = 3*pi/(2*(n+1));
T = arange(0,3*pi/2,h)
X = cos(T); Y = sin(T)
 
fig = plt.figure()
plt.plot(X,Y,'.r',markersize=10)
t = linspace(0,2*pi,100)
plt.plot(cos(t),sin(t),'--r')
 
t = linspace(0,3*pi/2,100)

tic()
plt.plot(spline(t,h,X),spline(t,h,Y),'-b')
toc()

plt.axis("equal"); plt.axis("off")
plt.show()
