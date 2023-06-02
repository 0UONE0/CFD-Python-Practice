import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


#Set up the grid

nx = 81
ny = 81
dx = 2/(nx-1)
dy = 2/(ny-1)
nt = 100
c = 1
sigma = .2
dt = sigma*dx

x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,2,ny)

u = numpy.ones((ny,nx)) #ny is number of rows, and nx is the number of columns.
un = numpy.ones((ny,nx))

#IC

u[int(0.5/dy):int(1/dy+1),int(0.5/dx):int(1/dx+1)]=2

#Plot ICs

##fig = plt.figure(figsize=(11,7),dpi=100)
##ax = plt.axes(projection='3d')
##X,Y = numpy.meshgrid(x,y)
##surf = ax.plot_surface(X,Y,u[:],cmap=cm.viridis)
##ax.set_xlabel('X')
##ax.set_ylabel('Y')
##ax.set_zlabel('U')
##plt.show()

#Implement 2-D convection

for n in range(nt+1):
    un = u.copy()
##    row,col = u.shape
##    for j in range(1,row):
##        for i in range(1,col):
##            u[j,i]=un[j,i] \
##            -c*dt*(un[j,i]-un[j,i-1])/dx \
##            -c*dt*(un[j,i]-un[j-1,i])/dy
##
##            u[0,:] = 1
##            u[-1,:] = 1
##            u[:,0] = 1
##            u[:,-1] = 1
    u[1:,1:] = un[1:,1:]\
               -c*dt/dx*(un[1:,1:]-un[1:,:-1])\
               -c*dt/dy*(un[1:,1:]-un[:-1,1:])
    u[0,:] = 1
    u[-1,:] = 1
    u[:,0] = 1
    u[:,-1] = 1
            
fig = plt.figure(figsize=(11,7),dpi=100)
ax = plt.axes(projection='3d')
X,Y = numpy.meshgrid(x,y)
surf = ax.plot_surface(X,Y,u[:],cmap=cm.viridis)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('U')
plt.show()
