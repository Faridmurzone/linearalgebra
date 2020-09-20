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

# Dims

print(vector.shape)
len(vector)
print(matrix.shape)
len(matrix.shape)
print(matrix.size)
print(tensor.shape)
print(tensor.size)


A = matrix
B = matrix.T
C = A + B # Error because of dims

A = np.array([[1,2], [3,4], [5,6]])
B = np.array([[6,5], [4,3], [2,1]])
C = A + B
print(C)

# Broadcasting
D = matrix + scalar
print(D)

E = A + [1,2]
print(E)
