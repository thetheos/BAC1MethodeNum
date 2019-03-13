

from numpy import *
import matplotlib.pyplot as plt

def trapezeEasy(f,a,b,n):
    
    i = linspace(a,b,int(n))
    U = f(i)
    h = i[2] - i[1]
    I = h/2 * (U[0] + U[-1] + 2 * sum(U[1:-1]))
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

def optimize_fun(f,a,b,n,nmax,tol):
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
    
def u(x):
    return cos(x)
  
a = 0
b = pi/2
n = 10
 
I = trapezeEasy(u,a,b,n)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Number of intervals = %d" % n)
print("\n")


I,n,errorEst = optimize_fun(u,a,b,n,200000,1e-12)
errorExact = abs(1.0 - I)
print(" ======= Integral of sinus between 0 and pi/2 = %21.14e " % I)
print("  True error = %14.7e" % errorExact)
print("  Est. error = %14.7e" % errorEst)
print("  Number of intervals = %d" % n)

n=10


I,n,errorEst = trapezeFun(u,a,b,n,200000,1e-12)
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

