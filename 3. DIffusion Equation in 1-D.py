import numpy
import matplotlib.pyplot as plt
import time,sys


#Set up grid

nx = 41
dx = 2/(nx-1)
nt = 20
nu = 0.3
sigma = 0.2
dt = sigma*dx**2/nu

#Set up IC

u = numpy.ones(nx)
u[int(0.5/dx) : int((1/dx)+1)] = 2

#plt.plot(numpy.linspace(0,2,nx),u)
#plt.show()

un = numpy.ones(nx)

#Implement diffusion

for n in range(nt):
    un = u.copy()
    for i in range(1,nx-1):
        u[i] = un[i] + (nu*dt/dx**2)*(un[i+1]-2*u[i]+u[i-1])

plt.plot(numpy.linspace(0,2,nx),u)
plt.show()
