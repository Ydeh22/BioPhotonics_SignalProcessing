## import packages
import os
import numpy as np
import matplotlib.pyplot as plt

#%%


def sensing_area(F):
    A=plt.imread(F)
    A0=A[:,:,2]
    return A0[A.shape[0]::-1,:] ## not sure about this line

def Z(mtrx):
    S=plt.imread(mtrx)
    R = S[S.shape[0]::-1,:,0]
    G = S[S.shape[0]::-1,:,1]
    B = S[S.shape[0]::-1,:,2]
    z=(G-R)/(G+R)
    return S,R,G,B,z 

def quick_plot(mtrx):
    fig = plt.figure(figsize=(6, 3.2))
    ax = fig.add_subplot(111)
    ax.set_title('colorMap')
    plt.imshow(mtrx)
    ax.set_aspect('equal')
    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)
    plt.colorbar(orientation='vertical')
    return plt.show()
#%%
nx=1
ny=5
g=[52,33]
s=20
dx=15
dy=118
#%%
S,R,G,B,z=Z('water001.tif')
me=[]
sd=[]
for n in range(ny):
        yy=np.round(np.arange(g[1]+n*dy,g[1]+n*dy+s,1))
        for m in range(nx):
            xx=np.round(np.arange(g[0]+m*dx,g[0]+m*dx+s,1))
            H=z[xx:,yy:]
            np.array(me.append(np.mean(H)))
            np.array(sd.append(np.std(H)))
            

        
