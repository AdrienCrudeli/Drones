#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme principal pour l'animation des drones
Ce script permet de générer une animation du mouvement des drones
et de la sauvegarder au format GIF.
"""

import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from copy import deepcopy
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d import Axes3D
import Deplacement as moov
import Animation as anim
import CreateDrone as init
from PIL import Image
import os
import sys

# Paramètres de l'animation
pas = 50  # Nombre d'images entre chaque position pour une animation fluide
NbDrones = 50  # Nombre de drones
TaillesDronesX = 10  # Taille des drones en X
TaillesDronesY = 10  # Taille des drones en Y
CirconférenceDrones = max(TaillesDronesY, TaillesDronesX)

# Dimensions de l'espace de vol
dimx1, dimx2 = -50, 50
dimy1, dimy2 = -50, 50
dimz1, dimz2 = -50, 50

# Configuration de matplotlib pour de meilleures performances
plt.style.use('fast')

class Arrow3D(FancyArrowPatch):
    """Classe pour créer des flèches en 3D"""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0,0), (0,0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))
        return np.min(zs)

def generate_animation(interactive=True):
    """
    Génère l'animation des drones avec interaction utilisateur
    
    Args:
        interactive (bool): Si True, demande à l'utilisateur les paramètres de mouvement
    """
    # Obtenir les positions initiales
    a_coordonnées = init.Répartition(NbDrones, CirconférenceDrones)
    positions = [deepcopy([coord + [0] for coord in a_coordonnées])]  # Conversion en 3D
    
    # Historique des trajectoires pour le rendu final
    all_trajectories = []
    
    # Configuration de l'affichage
    fig = plt.figure(figsize=(10, 8))
    ax = plt.axes(projection='3d')
    ax.grid(True)
    
    # Extraire les coordonnées initiales
    coords = anim.ExtractingCoordinates(positions[0])
    x1, y1, z1 = coords[0], coords[1], coords[2]
    ax.scatter(x1, y1, z1, c='g', s=CirconférenceDrones, label='Position initiale')
    
    if interactive:
        while True:
            try:
                # Demander les paramètres de mouvement
                print("\nEntrez les paramètres de mouvement (Enter pour terminer):")
                xinput = input('Translation x = ')
                if not xinput:  # Si l'utilisateur appuie sur Enter sans rien entrer
                    break
                    
                xinput = float(xinput)
                yinput = float(input('Translation y = '))
                zinput = float(input('Translation z = '))
                rotxinput = float(input('Rotation x (degrés) = ')) * np.pi/180
                rotyinput = float(input('Rotation y (degrés) = ')) * np.pi/180
                rotzinput = float(input('Rotation z (degrés) = ')) * np.pi/180
                
                # Calculer la nouvelle position
                nouvelle_pos = moov.rotY(
                    moov.rotZ(
                        moov.rotX(
                            moov.Z(
                                moov.Y(
                                    moov.X(deepcopy(positions[-1]), xinput),
                                yinput),
                            zinput),
                        rotxinput),
                    rotzinput),
                rotyinput)
                
                # Ajouter la nouvelle position
                positions.append(deepcopy(nouvelle_pos))
                
                # Visualiser le mouvement
                coords_new = anim.ExtractingCoordinates(nouvelle_pos)
                x2, y2, z2 = coords_new[0], coords_new[1], coords_new[2]
                
                # Sauvegarder la trajectoire pour le rendu final
                trajectory = {
                    'start': (x1, y1, z1),
                    'end': (x2, y2, z2)
                }
                all_trajectories.append(trajectory)
                
                # Dessiner les flèches de mouvement pour la visualisation en temps réel
                arrow_props = dict(mutation_scale=10, arrowstyle='->', color='purple', shrinkA=0, shrinkB=0)
                for i in range(len(x1)):
                    arrow = Arrow3D([x1[i],x2[i]], [y1[i],y2[i]], [z1[i],z2[i]], **arrow_props)
                    ax.add_artist(arrow)
                
                ax.scatter(x2, y2, z2, c='b', s=CirconférenceDrones)
                plt.draw()
                plt.pause(0.1)
                
                # Mettre à jour les positions courantes
                x1, y1, z1 = x2, y2, z2
                
            except ValueError as e:
                print(f"Erreur de saisie: {e}")
                continue
            except KeyboardInterrupt:
                print("\nAnimation interrompue par l'utilisateur")
                break
    
    # Créer le rendu final avec toutes les trajectoires
    plt.close()  # Fermer la fenêtre interactive
    
    # Créer une nouvelle figure pour le rendu final
    fig_final = plt.figure(figsize=(12, 10))
    ax_final = fig_final.add_subplot(111, projection='3d')
    ax_final.grid(True)
    
    # Afficher la position initiale
    coords_init = anim.ExtractingCoordinates(positions[0])
    ax_final.scatter(coords_init[0], coords_init[1], coords_init[2], 
                    c='g', s=CirconférenceDrones, label='Position initiale')
    
    # Afficher la position finale
    coords_final = anim.ExtractingCoordinates(positions[-1])
    ax_final.scatter(coords_final[0], coords_final[1], coords_final[2], 
                    c='r', s=CirconférenceDrones, label='Position finale')
    
    # Tracer toutes les trajectoires
    arrow_props = dict(mutation_scale=10, arrowstyle='->', color='purple', shrinkA=0, shrinkB=0)
    for traj in all_trajectories:
        x1, y1, z1 = traj['start']
        x2, y2, z2 = traj['end']
        for i in range(len(x1)):
            arrow = Arrow3D([x1[i],x2[i]], [y1[i],y2[i]], [z1[i],z2[i]], **arrow_props)
            ax_final.add_artist(arrow)
    
    ax_final.set_xlabel('X')
    ax_final.set_ylabel('Y')
    ax_final.set_zlabel('Z')
    ax_final.legend()
    
    # Sauvegarder le rendu final
    plt.savefig('ExempleDeRendus.png', bbox_inches='tight', dpi=150)
    plt.close()
    
    # Générer l'animation
    print("\nGénération de l'animation...")
    for i in range(len(positions) - 1):
        pos_actuelle = positions[i]
        pos_suivante = positions[i + 1]
        
        for j in range(pas):
            frame_num = i * pas + j
            # Utiliser un format de numérotation avec padding
            frame_name = f"frame_{frame_num:06d}"  # 6 chiffres avec padding de zéros
            anim.generate(pos_actuelle, pos_suivante, j/pas,
                         CirconférenceDrones,
                         dimx1, dimx2, dimy1, dimy2, dimz1, dimz2,
                         frame_num)
        print(f"Transition {i+1}/{len(positions)-1} complétée")
    
    create_gif()

def create_gif(duration=0.1):
    """Crée un GIF à partir des images générées"""
    try:
        # Liste tous les fichiers PNG dans le dossier
        png_files = [f for f in os.listdir() if f.startswith('f') and f.endswith('.png')]
        # Trier les fichiers par numéro de frame
        png_files.sort(key=lambda x: int(x.split('f')[1].split('.')[0]))
        
        if not png_files:
            print("Aucune image trouvée pour créer le GIF")
            return
        
        print(f"Création du GIF à partir de {len(png_files)} images...")
        
        # Crée le GIF
        frames = []
        for png_file in png_files:
            frame = Image.open(png_file)
            frames.append(frame)
        
        # Sauvegarde le GIF avec optimisation pour une meilleure qualité
        frames[0].save('Drones.gif',
                      save_all=True,
                      append_images=frames[1:],
                      duration=duration*1000,  # PIL utilise des millisecondes
                      loop=0,
                      optimize=False)
        
        print("GIF 'Drones.gif' créé avec succès!")
        
        # Nettoyage des fichiers PNG
        for png_file in png_files:
            os.remove(png_file)
            
    except Exception as e:
        print(f"Erreur lors de la création du GIF: {str(e)}")

def main():
    """Fonction principale"""
    try:
        print("Début de la génération de l'animation...")
        generate_animation(interactive=True)
        print("Processus terminé!")
    except KeyboardInterrupt:
        print("\nProcessus interrompu par l'utilisateur")
    except Exception as e:
        print(f"Une erreur est survenue: {str(e)}")

if __name__ == "__main__":
    main()