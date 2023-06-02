import numpy
import sympy
from sympy import init_printing
init_printing(use_latex=True)
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
import time,sys

#Burgers' equation
x,nu,t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+sympy.exp(-(x-4*t-2*sympy.pi)**2/(4*nu*(t+1)))
phiprime = phi.diff(x)
u = -2*nu*(phiprime/phi) + 4
#print(u)
ufunc = lambdify((t,x,nu),u)
#print(ufunc(1,4,3))
#Set up the grid

nx = 101
dx= 2*numpy.pi/(nx-1)
nt = 100
nu = 0.07
dt = dx*nu

x = numpy.linspace(0,2*numpy.pi,nx)
un = numpy.empty(nx)
t=0

u=numpy.asarray([ufunc(t,x0,nu) for x0 in x])



#plt.figure(figsize=(11,7),dpi=100)
#plt.plot(x,u,marker='o',lw=2)
#plt.xlim([0,2*numpy.pi])
#plt.ylim([0,10])
#plt.show()

#Implement

for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i]-un[i]*dt*(un[i]-un[i-1])/dx + nu*dt*(un[i+1]-2*un[i]+un[i-1])/dx**2
    u[0]=un[0]-un[0]*dt*(un[0]-un[-2])/dx + nu*dt*(un[1]-2*un[0]+un[-2])/dx**2
    u[-1]=u[0]

u_analytical=numpy.asarray([ufunc(nt*dt,xi,nu)for xi in x])

#Plot

plt.figure(figsize=(11,7),dpi=100)
plt.plot(x,u,marker='o',lw=2, label='Computational')
plt.plot(x,u_analytical,label='Analytical')
plt.xlim([0,2*numpy.pi])
plt.ylim([0,10])
plt.legend()
plt.show()
