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