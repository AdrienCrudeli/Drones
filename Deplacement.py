#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:59:11 2025

@author: adrien
"""
import numpy as np

def Z(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][2]+=valeures
        
    return(a_coordonnéesInitiales)

def X(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][0]+=valeures
        
    return(a_coordonnéesInitiales)

def Y(a_coordonnéesInitiales,valeures):

    for i in range(len(a_coordonnéesInitiales)):
        a_coordonnéesInitiales[i][1]+=valeures
        
    return(a_coordonnéesInitiales)
        
def rotX(a_coordonnéesInitiales,angle):
    coordonnéesFinales=[]
    for i in range(len(a_coordonnéesInitiales)):
        pivot=[]
        x=a_coordonnéesInitiales[i][0]
        y=np.cos(angle)*a_coordonnéesInitiales[i][1]+np.sin(angle)*a_coordonnéesInitiales[i][2]
        z=np.cos(angle)*a_coordonnéesInitiales[i][2]-np.sin(angle)*a_coordonnéesInitiales[i][1]
        pivot+=[x,y,z]
        coordonnéesFinales+=[pivot]
    
    return(coordonnéesFinales)
        
def rotY(a_coordonnéesInitiales,angle):
    coordonnéesFinales=[]
    for i in range(len(a_coordonnéesInitiales)):
        pivot=[]
        x=np.cos(angle)*a_coordonnéesInitiales[i][0]-np.sin(angle)*a_coordonnéesInitiales[i][2]
        y=a_coordonnéesInitiales[i][1]
        z=np.cos(angle)*a_coordonnéesInitiales[i][2]+np.sin(angle)*a_coordonnéesInitiales[i][0]
        pivot+=[x,y,z]
        coordonnéesFinales+=[pivot]
    
    return(coordonnéesFinales)


        
def rotZ(a_coordonnéesInitiales,angle):
    coordonnéesFinales=[]
    for i in range(len(a_coordonnéesInitiales)):
        pivot=[]
        x=np.cos(angle)*a_coordonnéesInitiales[i][0]+np.sin(angle)*a_coordonnéesInitiales[i][1]
        y=np.cos(angle)*a_coordonnéesInitiales[i][1]-np.sin(angle)*a_coordonnéesInitiales[i][0]
        z=a_coordonnéesInitiales[i][2]
        pivot+=[x,y,z]
        coordonnéesFinales+=[pivot]
    
    return(coordonnéesFinales)
        

