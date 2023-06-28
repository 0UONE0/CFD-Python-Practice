import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot2D(x,y,p):
    fig = plt.figure(figsize=(11,7),dpi=100)
    ax = plt.axes(projection='3d')
    X,Y = numpy.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p,rstride=1,cstride=1,cmap=cm.viridis,
                           linewidth=0,antialiased=False)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0,2)
    ax.set_ylim(0,1)
    ax.view_init(30,225)

def laplace2d(p,y,dx,dy,llnorm_target):
    llnorm = 1
    pn = numpy.empty_like(p)

    while llnorm > llnorm_target:
        pn = p.copy()
        p[1:-1,1:-1]=(dy**2*(pn[1:-1,2:]+pn[1:-1,0:-2])\
                      +dx**2*(pn[2:,1:-1]+pn[0:-2,1:-1]))\
                      /(2*(dx**2+dy**2))

        #BC
        p[:,0]=0
        p[:,-1]=y
        p[0,:]=p[1,:]
        p[-1,:]=p[-2,:]

        llnorm = numpy.sum(numpy.abs(p)-numpy.abs(pn))/numpy.sum(numpy.abs(pn))
        
    return p

#Set up the grid
nx = 31
ny = 31
c = 1
dx = 2/(nx-1)
dy = 1/(ny-1)

#IC
p = numpy.zeros((nx,ny))
x = numpy.linspace(0,2,nx)
y = numpy.linspace(0,1,ny)

#BC
p[:,0]=0 #p=0 @ x=0
p[:,-1]=y #p=y @ x=2
p[0,:]=p[1,:] #dp/dy=0 @ y=0
p[-1,:]=p[-2,:] #dp/dy=0 @ y=1
