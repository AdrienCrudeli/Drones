#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 16:21:34 2025

@author: adrien
"""
import CreateDrone as init
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d import Axes3D
import Deplacement as moov
import time as t
from PIL import Image

def ExtractingCoordinates(a_coordonnées):
    Taille=len(a_coordonnées[0])
    Splitted=[]
    for i in range(Taille):
        Splitted+=[[]]
    
    for i in range(len(a_coordonnées)):
        for j in range(Taille):
            Splitted[j]+=[a_coordonnées[i][j]]

    return(Splitted)


def generate(initial_coords, target_coords, progression, a_CirconférenceDrones, dimx1, dimx2, dimy1, dimy2, dimz1, dimz2, frame_offset=0):
    """
    Génère une animation entre deux positions de drones
    
    Args:
        initial_coords : position initiale des drones
        target_coords : position cible des drones
        progression : nombre entre 0 et 1 indiquant la progression entre les positions
        a_CirconférenceDrones : taille des points représentant les drones
        dimx1, dimx2, dimy1, dimy2, dimz1, dimz2 : limites de l'espace de vol
        frame_offset : décalage pour la numérotation des frames
    """
    frame_name = f"f{frame_offset:06d}.png"  # Format avec padding de zéros
    ListeAAfficher = []
    
    # Interpolation linéaire entre les positions initiales et cibles
    for init, target in zip(initial_coords, target_coords):
        pos = []
        for i in range(3):  # Pour chaque dimension (x, y, z)
            pos.append(init[i] + (target[i] - init[i]) * progression)
        ListeAAfficher.append(pos)
    
    # Extraction des coordonnées pour l'affichage
    Extract = ExtractingCoordinates(ListeAAfficher)
    
    x1,y1,z1 = Extract[0],Extract[1],Extract[2]
    
    # Génère une frame avec les positions interpolées
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(dimx1,dimx2)
    ax.set_ylim(dimy1,dimy2)
    ax.set_zlim(dimz1,dimz2)    
    
    # Ajoute des axes pour mieux visualiser
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.grid(True)
    ax.scatter(x1, y1, z1, c='g', s=a_CirconférenceDrones, alpha=0.6)
    
    # Ajoute un titre montrant la progression
    ax.set_title(f'Progression: {int(progression * 100)}%')
    
    plt.savefig(frame_name, bbox_inches='tight', dpi=100)
    plt.close('all')
   
    
    
    
    
    
    
    
    
    
    