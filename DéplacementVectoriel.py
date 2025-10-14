#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import CreateDrone as local
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d import Axes3D

NbDrones=100
TaillesDronesX=10
TaillesDronesY=10
CirconférenceDrones=max(TaillesDronesY,TaillesDronesX)
a_coordonnées=local.Répartition(NbDrones,CirconférenceDrones)

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

        return np.min(zs)

def TwoDimensionToThree (a_coordonnées):
    ThreeDimension=[]
    for i in range(len(a_coordonnées)):
        ThreeDimension+=[a_coordonnées[i]+[0]]
    return(ThreeDimension)

def ExtractingCoordinates(a_coordonnées):
    Taille=len(a_coordonnées[0])
    Splitted=[]
    for i in range(Taille):
        Splitted+=[[]]
    
    for i in range(len(a_coordonnées)):
        for j in range(Taille):
            Splitted[j]+=[a_coordonnées[i][j]]

    return(Splitted)

def Distance(pointsA,pointsM):
    SquareSum=0
    AM=[]
    for i in range(len(pointsA)):
        AM+=[[]]
        AM[i]=[pointsM[i]-pointsA[i]]
    for i in range(len(AM)):
  
        SquareSum+=AM[i][0]**2
    return(np.sqrt(SquareSum))
    
def Tri(liste):
    pivot=liste[0]
    a=0
    for i in range(1,len(liste)):
        if pivot>liste[i]:
            pivot=liste[i]
            a=i
            
    return(a)
def DéplacementZ(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][2]+=valeures
        
    return(a_coordonnéesInitiales)

def DéplacementX(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][0]+=valeures
        
    return(a_coordonnéesInitiales)

def DéplacementY(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][1]+=valeures
        
    return(a_coordonnéesInitiales)
        
def Déplacement(a_coordonnéesInitiales,a_coordonnéesFinales):
    Lien=[]
    coordonnéesInitiales=deepcopy(a_coordonnéesInitiales)
    for i in range(len(coordonnéesInitiales)):
        distance=[]
        for j in range(len(a_coordonnéesFinales)):

            distance+=[Distance(coordonnéesInitiales[i],a_coordonnéesFinales[j])]
        PPélément=Tri(distance)
        Lien+=[[coordonnéesInitiales[i]],a_coordonnéesFinales[PPélément],distance[PPélément]]
        a_coordonnéesFinales.pop(PPélément)
    return(Lien)
        
ToThreeD=TwoDimensionToThree(a_coordonnées)
ToThreeDc=deepcopy(ToThreeD)
EToThreeD=ExtractingCoordinates(ToThreeD)
x1,y1,z1=EToThreeD[0],EToThreeD[1],EToThreeD[2]

Déplacé=DéplacementY(DéplacementZ(DéplacementX(ToThreeDc,50),10),0) #Déplacement
EDéplacé=ExtractingCoordinates(Déplacé)
x2,y2,z2=EDéplacé[0],EDéplacé[1],EDéplacé[2]
Chemin=Déplacement(ToThreeD,Déplacé)
            


ax = plt.axes(projection='3d')
ax.grid()

ax.scatter(x1, y1, z1, c = 'g', s = 50)
ax.scatter(x2, y2, z2, c = 'b', s = 50)

arrow_prop_dict = dict(mutation_scale=10, arrowstyle='->', color='purple', shrinkA=0, shrinkB=0)
for i in range(len(x1)):
    arw = Arrow3D([x1[i],x2[i]],[y1[i],y2[i]],[z1[i],z2[i]], **arrow_prop_dict)
    ax.add_artist(arw)
ax.set_title('3D Scatter Plot')
plt.show()
        

