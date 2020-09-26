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

# Eigen vectors
# Autovectores: Al aplicar una transformación no se ve modificado.
# Puede tener una longitud distinta, multiplicado por un autovalor.

orange_light = '#FF9A13'
blue_light = '#1190FF'

X = np.array([[3,2], [4,1]])
v = np.array([[1], [1]])
u = X.dot(v)
print(u)

graphVectors([u.flatten(), v.flatten()], col=[blue_light, orange_light])
plt.xlim(-1,10)
plt.ylim(-1,10)

# Calcular autovalores y autovectores
print(np.linalg.eig(X))
autovalor, autovector = np.linalg.eig(X)
print(autovector[:,0])

v = np.array([[-1], [2]])
Xv = X.dot(v)
v_np = autovector[:,0]
graphVectors([Xv.flatten(), v.flatten(), v_np], col=["green", "orange", "blue"])
plt.xlim(-3, 5)
plt.ylim(-3, 5)

# Descomposición de matrices.
# A = autovectores * diag(autovalores) * inv_autovectores
# A = [autovectores] [[delta1,0], [0, delta2]] [autovectores]**-1
A = np.array([[3,2],  [4,1]])
autovalores, autovectores = np.linalg.eig(A)

A_calc = autovectores.dot(np.diag(autovalores)).dot(np.linalg.inv(autovectores))
# Matriz tiene que ser cuadrada

print(A_calc) # Devuelve la misma matriz (fue decompuesta)


# Descomposición de una matriz no cuadrada (SVD
# DEscomposición en valores singulares
A = np.array([[1,2,3], [3,4,5]])
U, D, V = np.linalg.svd(A)
# U -> Vectores izquierdos singulares
# D -> Vectores derechos singulares
# V -> Diagonal con todos los valores singulares
# U y V son ortonormales

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
    
    graphVectors([u1, v1], col=[vectorCol[0], vectorCol[1]])
    plt.plot(x1, y1, 'green', alpha = 0.7)
    plt.plot(x1_neg, y1_neg, 'green', alpha = 0.7)

A = np.array([[3,7], [5,2]])
print(A)

print('Circulo unitario:')
graphMatrix(np.array([[1,0], [0,1]]))
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

print('Circulo unitario transformado:')
graphMatrix(A)
plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()

# Aplicacion de matrices D V U y su efecto en la transformacion

U, D, V = np.linalg.svd(A)
print("Primer rotacion (V):")
graphMatrix(V)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()

print("Escala (D):")
graphMatrix(np.diag(D).dot(V))
plt.xlim(-8.5, 8.5)
plt.ylim(-8.5, 8.5)
plt.show()

print("Segunda rotacion (U):")
graphMatrix(U.dot(np.diag(D).dot(V)))
plt.xlim(-7.5, 7.5)
plt.ylim(-7.5, 7.5)
plt.show()

# La segunda rotacion nos propone la misma transformación que el circulo unitario transformado (A)


# Interpretar valores singulares.
print(D[0])
print(D[1])

u1 = [D[0] * U[0,0], D[0]*U[0,1]]
v1 = [D[1]*U[1,0], D[1]*U[1,1]]
print([A[0,0], A[1,0]])
print(u1)
print([A[0,1], A[1,1]])

graphMatrix(A)
graphVectors([u1,v1], col=['blue', 'red'])
plt.text(3,5, r"$u_1$", size=18)
plt.text(7,2, r"$v_1$", size=18)
plt.text(-5,-4, r"$D(u_1)$", size=18)
plt.text(-4,1, r"$D(v_1)$", size=18)

plt.xlim(-8,8)
plt.ylim(-8,8)
plt.show()
# La matriz D está compuesta por la diagonal con lo valores singulares lambdas.
