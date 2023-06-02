import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#Set up the grid
nx = 31
dx = 2/(nx-1)
ny = 31
dy = 2/(ny-1)
nt = 17
nu = .05
sigma = .25
dt = sigma*dx*dy/nu

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

#Define a funcion
def diffusion(nt):
    u = numpy.ones((ny,nx))
    un = numpy.ones((ny,nx))

    #Set up IC
    u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)] = 2

###Plot IC
##fig = plt.figure(figsize=(11,7),dpi=100)
##ax = plt.axes(projection='3d')
##X,Y = numpy.meshgrid(x,y)
##ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=1,cstride=1,linewidth=0,antialiased=False)
##ax.set_xlim(0,2)
##ax.set_ylim(0,2)
##ax.set_zlim(1,2.5)
##ax.set_xlabel('$x$')
##ax.set_ylabel('$y$')
##ax.set_zlabel('$u$')
##plt.show()

    #Implement 2D diffusion
    for n in range(1,nt+1):
        un = u.copy()
##      for j in range(1,ny-1):
##          for i in range(1,nx-1):
##              u[j,i] = un[j,i]\
##                      +nu*dt/dx**2*(un[j,i+1]-2*un[j,i]+un[j,i-1])\
##                      +nu*dt/dy**2*(un[j+1,i]-2*un[j,i]+un[j-1,i])
##
##              u[:,0]=1
##              u[:,-1]=1
##              u[0,:]=1
##              u[-1,:]=1
        u[1:-1,1:-1] = un[1:-1,1:-1]\
                   +nu*dt/dx**2*(un[1:-1,2:]-2*un[1:-1,1:-1]+un[1:-1,0:-2])\
                   +nu*dt/dy**2*(un[2:,1:-1]-2*un[1:-1,1:-1]+un[0:-2,1:-1])
    
        u[:,0]=1
        u[:,-1]=1
        u[0,:]=1
        u[-1,:]=1
    
#Plot

    fig = plt.figure(figsize=(11,7),dpi=100)
    ax = plt.axes(projection='3d')
    X,Y = numpy.meshgrid(x,y)
    ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=1,cstride=1,linewidth=0,antialiased=False)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$u$')
    ax.set_xlim(0,2)
    ax.set_ylim(0,2)
    ax.set_zlim(1,2.5)
    plt.show()
