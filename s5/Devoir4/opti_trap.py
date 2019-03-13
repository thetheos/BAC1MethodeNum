

from numpy import *
import matplotlib.pyplot as plt

def trapezeEasy(f,a,b,n):
    i = linspace(a,b,n+1)
    print(i.shape)
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
        print(abs(I2-I1))
    return I2,n,abs(I2-I1) 


def u(x):
    return cos(x)
  
a = 0
b = 1.57
n = 10
 
I = trapezeEasy(u,a,b,n)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Number of intervals = %d" % n)
print("\n")


I,n,errorEst = trapezeFun(u,a,b,n,2000,1e-6)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Est. error = %14.7e" % errorEst)
print("  Number of intervals = %d" % n)


 
 
 
plt.figure("Discovering the trapezoids integration rule :-)")
x = [a,b]
plt.plot(x,u(x),'.k',markersize=5) 
x = linspace(a,b,200)
plt.fill(append(x,[0]),append(u(x),[0]),'xkcd:sky blue')
x = linspace(-pi/2,pi,300)
plt.plot(x,u(x),'-k')
plt.title('Integrating sinus between 0 and pi/2')
plt.gca().axhline(y=0,color='k',linewidth=1.0)
plt.text(0.1,0.1,"I = %6.4f" % I,fontsize=12)
plt.show()

