import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#Set up the grid

nx = 101
dx = 2/(nx-1)
ny = 101
dy = 2/(ny-1)
nt = 80
c=1
sigma = .2
dt = sigma*dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx))
v = numpy.ones((ny,nx))
un = numpy.ones((ny,nx))
vn = numpy.ones((ny,nx))

#IC

u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)] = 2
v[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)] = 2

###Plot IC
##
##fig = plt.figure(figsize=(11,7),dpi=100)
##ax = plt.axes(projection='3d')
##X,Y=numpy.meshgrid(x,y)
##ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=2,cstride=2)
##ax.set_xlabel('$x$')
##ax.set_ylabel('$y$')
##ax.set_zlabel('$u$')
##plt.show()

#Implement 2-D Nonlinear convection

for n in range(nt+1):
    un = u.copy()
    vn = v.copy()
##    for j in range(1,ny):
##        for i in range(1,nx):
##            u[j,i] = un[j,i]\
##                     -un[j,i]*c*dt/dx*(un[j,i]-un[j,i-1])\
##                     -vn[j,i]*c*dt/dy*(un[j,i]-un[j-1,i])
##
##            v[j,i] = vn[j,i]\
##                     -un[j,i]*c*dt/dx*(vn[j,i]-vn[j,i-1])\
##                     -vn[j,i]*c*dt/dy*(vn[j,i]-vn[j-1,i])
##            #BCs
##            u[0,:] = 1
##            u[-1,:] = 1
##            u[:,0] = 1
##            u[:,-1] = 1
##            v[0,:] = 1
##            v[-1,:] = 1
##            v[:,0] = 1
##            v[:,-1] = 1
            
            
# Array operations
    u[1:,1:] = un[1:,1:]\
               -un[1:,1:]*c*dt/dx*(un[1:,1:]-un[1:,:-1])\
               -vn[1:,1:]*c*dt/dy*(un[1:,1:]-un[:-1,1:])
    v[1:,1:] = vn[1:,1:]\
               -un[1:,1:]*c*dt/dx*(vn[1:,1:]-vn[1:,:-1])\
               -vn[1:,1:]*c*dt/dy*(vn[1:,1:]-vn[:-1,1:])
    #BCs
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
    v[0,:] = 1
    v[-1,:] = 1
    v[:,0] = 1
    v[:,-1] = 1
            
fig = plt.figure(figsize=(11,7),dpi=100)
ax = plt.axes(projection='3d')
X,Y=numpy.meshgrid(x,y)
ax.plot_surface(X,Y,u,cmap=cm.viridis,rstride=2,cstride=2)
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$u$')
plt.show()
