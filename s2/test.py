
import numpy as np 
import matplotlib
from matplotlib import pyplot as plt

def interpolation(X, U, x):
    """
    Process an interpolation fitting the points (X, U).
    Return the interpollated image of x
    """
    k = np.arange(-(len(X)-1)/2, (len(X)-1)/2 + 1)      #Create an array from -n to n
    fun_matrix = np.array([[np.exp(np.complex(0,i * x_val)) for i in k] for x_val in X ])       #Create the base function matrix
    coef_vector = np.linalg.solve(fun_matrix, U)        #Solve the system to find the coefficient
    matrix_to_fit = np.array([[np.exp(np.complex(0,i * x_val)) for i in k] for x_val in x ])        #base function matrix evaluated at the points we want to fit
    interpol_val = matrix_to_fit @ coef_vector      #Matrix product to get the interpolated points
    interpol_val = interpol_val.real        #Extract the real part of the complex numbers
    return interpol_val

from matplotlib import pyplot as plt
from numpy import *
n = 4
m = 100
x = (2*pi/(m))*arange(0,m+1)
X = (2*pi/(2*n+1))*arange(0,2*n+1)

functions = [lambda x : x*(x-2*pi)*exp(-x),
            lambda x : sin(x)+sin(5*x),
            lambda x : sign(x-2)]

for u in functions:
    plt.figure()
    plt.plot(x,u(x),'-b',label='Fontion u')
    U = u(X)
    uh = polyval(polyfit(X,U,len(X)-1),x)
    plt.plot(x,uh,'-g',label='Interpolation polynomiale')
    uh = interpolation(X,U,x)
    plt.plot(x,uh,'-r',label='Interpolation trigonometrique')
    plt.plot(X,U,'ob')
    plt.xlim((-0.2,2*pi+0.2)); plt.ylim((-3,3))
    plt.title('Interpolation trigonometrique : 2n+1 = %d ' % len(X))
    plt.legend(loc='upper right')

plt.show()


