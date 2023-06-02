import numpy
import matplotlib.pyplot as plt
import time,sys

#Set up grid

nx = 41
dx = 2/(nx-1)
nt = 25
dt = 0.025

#Set up initial condition

u = numpy.ones(nx)
u[int((0.5/dx)):int((1/dx) + 1)] = 2

un = numpy.ones(nx) #temporay u to store previous values

#plt.plot(numpy.linspace(0,2,nx),u)
#plt.show()

#Implement nonlinear convection

for n in range(nt):
    un = u.copy()
    for i in range(1,nx):
        u[i] = un[i] - (un[i]*dt/dx) * (un[i] - un[i-1])
    plt.plot(numpy.linspace(0,2,nx),u)

#Plot
        
plt.plot(numpy.linspace(0,2,nx),u)
plt.show()
