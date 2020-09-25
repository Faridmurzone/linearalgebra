#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 20:33:27 2020

@author: fmurzone
"""

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[-1, 3], [2,-2]])
print(A)

vector = np.array([[2], [1]])

def graphVectors(vecs, col, alpha = 1):
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
                   color = col[i],
                   alpha = alpha)
print(A)
print(A.flatten())

graphVectors([vector.flatten()], col="blue")
plt.xlim(-0.5, 3)
plt.ylim(-0.5, 2)
t_vector = A.dot(vector)
graphVectors([vector.flatten(), t_vector.flatten()], col = ["blue", "orange"])
plt.xlim(-0.5, 3)
plt.ylim(-0.5, 2)