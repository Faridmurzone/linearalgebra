#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 09:56:28 2020

@author: fmurzone
"""

import numpy as np

scalar = 1.2345
vector = np.array([2,3])
matrix = np.array([[1,2], [2,3], [3,4]])

A = matrix * vector # Cross product 
B = matrix.dot(vector) # Dot product

print(A)
print(B)

# Alternative for Dot product:
C = np.dot(matrix, vector)

D = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
E = np.array([[1, 2], [3, 4], [5, 6]])
F = D.dot(E)
# The rows of the first matrix and the columns of the second most be equal or:
G = E.dot(D) # undefined

# Props:
# Asociativa: A(BC) = (AB)C
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[2,3,1],[1,5,2],[1,8,9]])
C = np.array([[1,3,3],[5,5,1],[3,1,2]])
ABC = A.dot(B.dot(C))
CBA = C.dot(B.dot(A))
print(ABC==CBA)
#Distributiva
# A(B+C) = (AB)+C
D = A.dot(B+C)
E = (A.dot(B))+(A.dot(C))
print(D==E)


# Transposición:
# (AB)**t = (A**t)(B**t)
# ((AB)**t)**t = AB
A = np.array([[1,3],[4,6],[8,9]])
B = np.array([[1,2], [3,4]])
print(A)
AB_t = A.dot(B).T
print(AB_t)
B_tA_t = B.T.dot(A.T)
print(B_tA_t)
print(AB_t == B_tA_t)