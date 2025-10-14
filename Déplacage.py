#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import CreateDrone as CD
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits import mplot3d

Ordres=[]

NbDrones=100
Longueure=253
Largeur=183
Hauteur=77
Circonférence=max([Longueure,Largeur])
fig = plt.figure()
ax = plt.axes(projection='3d')
distance=10 #test
pas_z=0.1
pas_theta=1
a=1
b=1
c=2

def f(x,y):
    return(np.linspace(0,10,100),np.linspace(0,10,100))


def cylindre(f):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

# Make data
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = 10 *np.cos(u)
    y = 10 *np.sin(u)
    z, U = np.meshgrid(np.linspace(0,10,100), u)
    return(x,y,z)    

cylindre=cylindre(f)


# Plot the surface
ax.plot_surface(cylindre[0],cylindre[1],cylindre[2])

# Set an equal aspect ratio
ax.set_aspect('equal')

plt.show()

            
