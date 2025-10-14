# -*- coding: utf-8 -*-

###############################################################################
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Essaim Drone!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!#
###############################################################################
"""Importations"""

import matplotlib.pyplot as plt
import numpy as np


"""Variables"""

#Dimensions des drones



"""Fonctions"""

def Répartition(a_NbDrones=int,a_Circonférence=float):
    
    #Premières variables pre boucle
    
    StockageDesCoordonnées=[[0,0]] #Création du point central
    NombreDeRotation=1  #Initialisation des répétitions hexagonales
    NombreDeDronePlacé=1 #suivi du nombre de drone
    
    #Boucle principale
    
    while NombreDeDronePlacé<a_NbDrones:
        
        # Variables post boucle
        
        PointsMilieux=[] #Variables pour stocké les points dans les segments
        # Comptage drone
        
        if NombreDeDronePlacé>=a_NbDrones :#
            break #
        else: #
            NombreDeDronePlacé+=1 # 
            
            StockageDesCoordonnées+=[[0,NombreDeRotation*a_Circonférence]] #stock des points et initialisation du vecteur tournant
        pivot=[0,NombreDeRotation*a_Circonférence] #mise en mémoire du vecteur tournant
        
       
        
            
        Vecteur=[StockageDesCoordonnées[len(StockageDesCoordonnées)-1][0]-StockageDesCoordonnées[0][0],
                 StockageDesCoordonnées[len(StockageDesCoordonnées)-1][1]-StockageDesCoordonnées[0][1]]
        
        #Boucle pour chaque face
        
        for i in range(1,6):
            
            # Comptage drone

            if NombreDeDronePlacé>=a_NbDrones :
                break
            else:
                NombreDeDronePlacé+=1 

                StockageDesCoordonnées+=[RotationVect(i*np.pi/3,Vecteur)] #Ajout du vecteur tourné
                
                
            #Boucle pour nombre de point dans les segments
            
            for j in range(1,NombreDeRotation): #Nombre de point par face augmente avec la rotation, cad 1ere rotation, 0 pts, 2eme, 1pts, 3eme ,2pts ...
                
                # Comptage drone
                
                if NombreDeDronePlacé>=a_NbDrones :
                    break
                elif NombreDeRotation>1:
                    
                    
                    if i == 5: #Pour placé le dernier point
                        NombreDeDronePlacé+=1 
                        PointsMilieux+=[[((j)*(StockageDesCoordonnées[len(StockageDesCoordonnées)-1][0]-pivot[0])/NombreDeRotation)+pivot[0],
                                         ((j)*(StockageDesCoordonnées[len(StockageDesCoordonnées)-1][1]-pivot[1])/NombreDeRotation)+pivot[1]]]
                        
                    #Placage des points
                if NombreDeDronePlacé>=a_NbDrones :
                    break
                elif NombreDeRotation>1:
                    NombreDeDronePlacé+=1 
                    PointsMilieux+=[[((j)*(StockageDesCoordonnées[len(StockageDesCoordonnées)-1][0]-StockageDesCoordonnées[len(StockageDesCoordonnées)-2][0])/NombreDeRotation)+StockageDesCoordonnées[len(StockageDesCoordonnées)-2][0],
                                     ((j)*(StockageDesCoordonnées[len(StockageDesCoordonnées)-1][1]-StockageDesCoordonnées[len(StockageDesCoordonnées)-2][1])/NombreDeRotation)+StockageDesCoordonnées[len(StockageDesCoordonnées)-2][1]]]

        StockageDesCoordonnées+=PointsMilieux
        NombreDeRotation+=1

    return(StockageDesCoordonnées)
    
def RotationVect(a_angle=float,a_vect=list): #fonction pour rotater un vecteur
    return([a_vect[0]*np.cos(a_angle)-a_vect[1]*np.sin(a_angle),a_vect[1]*np.cos(a_angle)+a_vect[0]*np.sin(a_angle)])
        
def Rendu(a_données=list): #Fonction pour le rendu

    for i in range(len(a_données)):
        if i==0:
            plt.plot(a_données[i][0],a_données[i][1],"xb")
        else:
            plt.plot(a_données[i][0],a_données[i][1],"xr")
        

                     
        