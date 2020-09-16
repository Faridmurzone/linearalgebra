#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 08:35:12 2020

@author: fmurzone
"""
import numpy as np
import matplotlib.pyplot as plt
scalar = 5.678
print(scalar)

scalar_python = True
print(type(scalar_python), type(scalar))

# Scalar / Vector / Matrix / Tensor
vector = np.array([1,2,3,4])
matrix = np.array([[1,2,3,4], [1,4,2,5], [7,5,2,3]])
tensor = np.array([
    [[255,0,0],[0,255,0],[0,0,255]],
    [[0,0,0],[0,0,0],[0,0,0]],
    [[255,255,255],[255,255,255],[255,255,255]],
    [[128,128,128],[128,128,128],[128,128,128]]
])
print(vector)
print(matrix)
print(tensor)

# Ploting the tensor data as colors
plt.imshow(tensor, interpolation="nearest")
plt.show()