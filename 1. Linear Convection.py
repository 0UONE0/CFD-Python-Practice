#       numpy is a library that provides
#       a bunch of useful matrix operations akin to MATLAB

#       matplotlib is a 2D plotting library that we will use to plot our results

#       time and sys provide basic timing functions that we'll use to slow down animations for viewing


# Remember: comments in python are denoted by the pound sign
import numpy                # load numpy
import matplotlib.pyplot as plt   #load matplotlib
import time,sys             #load some utilities


#Set up the grid

nx = 41     # 41 nodes in space
dx = 2 / (nx - 1) # delta x for lengh of 2
nt = 25     # 25 time steps
dt = 0.025  # delta t = 0.025
c = 1   # assume the wavespeed is 1


#Set up the Initial Conditions

u = numpy.ones(nx)  # set u = 1 at each node
u[int(0.5 / dx) : int(1 / dx + 1)] = 2    # set u = 2 between 0.5 and 1 as I.C.s. Notice u[a: b] is a<= i <b
print(u)


#Plot the grid with I.C.s

#plt.figure(1)
#plt.plot(numpy.linspace(0,2,nx),u)
#plt.show()

#Implement the discretization

un = numpy.ones(nx)     #set up a temporary array to save new values for the next time step
for n in range(nt):     #loop for time steps
    un = u.copy()   #copy the previous values of u
    for i in range(1,nx): #calculating the values of u skipping the initial condition
        u[i] = un[i] - c * (dt/dx) * (un[i] - un[i-1])


#Plot the u solution
plt.figure(2)
plt.plot(numpy.linspace(0,2,nx),u)
plt.show()
