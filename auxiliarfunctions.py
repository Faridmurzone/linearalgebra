#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:38:35 2020

@author: fmurzone
"""
import numpy as np
import matplotlib.pyplot as plt

def graphVectors(vecs, cols, alpha = 1):
    plt.axvline(x = 0, color = "grey", zorder = 0)
    plt.axhline(y = 0, color = "grey", zorder= 0)
    for i in range(len(vecs)):
        x = np.concatenate([[0,0], vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles = 'xy',
                   scale_units = 'xy',
                   scale = 1, 
                   alpha = alpha)
        

def graphMatrix(matrix, vectorCol=['red', 'blue']):
    # circulo unitario
    x = np.linspace(-1,1,100000)
    y = np.sqrt(1-(x**2))
    
    # circulo unitario transformado
    x1 = matrix[0,0]*x + matrix[0,1]*y
    y1 = matrix[1,0]*x + matrix[1,1]*y
    x1_neg = matrix[0,0]*x - matrix[0,1]*y
    y1_neg = matrix[1,0]*x - matrix[1,1]*y
    
    
    # vectores
    u1 = [matrix[0,0], matrix[1,0]]
    v1 = [matrix[0,1], matrix[1,1]]
    
    graphVectores([u1, v1], col=[vectorCol[0], vectorCol[1]])
    plt.plot(x1, y1, 'green', alpha = 0.7)
    plt.plot(x1_neg, y1_neg, 'green', alpha = 0.7)

