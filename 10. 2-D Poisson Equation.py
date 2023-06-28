import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def plot2D(x,y,p):
    fig = plt.figure(figsize=(11,7),dpi=100)
    ax = plt.axes(projection='3d')
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,p,rstride=1,cstride=1,cmap=cm.viridis,
                           linewidth=0,antialiased=False)
    ax.set_xlim(0,2)
    ax.set_ylim(0,1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$p$')
    ax.view_init(30,225)
    
#Set up the grid
nx = 50
ny = 50
nt = 100
xmin = 0
xmax = 2
ymin = 0
ymax = 1

dx = (xmax-xmin)/(nx-1)
dy = (ymax-ymin)/(ny-1)

#IC
p = np.zeros((ny,nx))
pn = np.zeros((ny,nx))
b = np.zeros((ny,nx))
x = np.linspace(xmin,xmax,nx)
y = np.linspace(ymin,ymax,ny)
#Source
b[int(ny/4),int(nx/4)]=100
b[int(3*ny/4),int(3*nx/4)]=-100

###Compute using for loop
##for n in range(nt+1):
##    pn=p.copy()
##
##    p[1:-1,1:-1] = ((dy**2*(pn[1:-1,2:]+pn[1:-1,0:-2]))\
##               +(dx**2*(pn[2:,1:-1]+pn[0:-2,1:-1]))\
##               -(dy**2*dx**2*b[1:-1,1:-1]))\
##               /(2*(dy**2+dx**2))
##    p[:,0]=0
##    p[:,-1]=0
##    p[0,:]=0
##    p[-1,:]=0

#Compute using function       
def poisson2D(p,dx,dy,nt,b):
    for n in range(nt+1):
        pn = p.copy()

        p[1:-1,1:-1] = ((dy**2*(pn[1:-1,2:]+pn[1:-1,0:-2]))\
                       +(dx**2*(pn[2:,1:-1]+pn[0:-2,1:-1]))\
                       -(dy**2*dx**2*b[1:-1,1:-1]))\
                       /(2*(dx**2+dy**2))

        p[:,0]=0
        p[:,-1]=0
        p[0,:]=0
        p[-1,:]=0
    return p
