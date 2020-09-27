#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 09:08:20 2020

@author: fmurzone
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plt.style.use('classic')

image = Image.open('./Desktop/nani.jpeg')

plt.imshow(image)

image_gr = image.convert('LA')
print(image_gr)

image_mat = np.array(list(image_gr.getdata(band=0)), float)

print(image_mat)
image_mat.shape = (image_gr.size[1], image_gr.size[0])

print(image_mat.shape)
plt.imshow(image_mat, cmap = 'gray')

np.max(image_mat)
np.min(image_mat)

U, D, V = np.linalg.svd(image_mat)

print(image_mat.shape)
print(U.shape)
print(D.shape)
print(V.shape)

img_recons = np.matrix(U[:,:1]) * np.diag(D[:1]) * np.matrix(V[:1, :])
plt.imshow(img_recons, cmap='gray')

'''
la compresión de imágenes por SVD hace uso de que muy pocos de los valores singulares realmente representan información.
Los valores singulares se guardan de forma ordenada.
'''

i = 50 # Cantidad de valores singulares
img_recons = np.matrix(U[:,:i]) * np.diag(D[:i]) * np.matrix(V[:i, :])
plt.imshow(img_recons, cmap='gray')

# Calcular la inversa cuando no existe
# Pseudo inversa de Moore Penrose
# La pseudo inversa de Moore Penrose es una aplicación directa de SVD, que nos permite resolver en determinados momentos sistemas de ecuaciones lineales con múltiples soluciones.
# A * x = b
# ƎA**-1 => x = A**-1 * b
# A * A_pse ≈ Identidad
# A_pre = V * D_pse
np.set_printoptions(supress=True)

A = np.array([[2,3], [5,7], [11,13]])
U, D, V = np.linalg.svd(A)
print(U)
print(D)
print(V)

D_pse = np.zeros((A.shape[0], A.shape[1])).T
print(D_pse[:D.shape[0], :D.shape[0]])
print(np.linalg.inv(np.diag(D)))
D_pse[:D.shape[0], :D.shape[0]] = np.linalg.inv(np.diag(D))
print(D_pse)

D_pse = V.T.dot(D_pse).dot(U.T)
print(D_pse)
A_pse_calc = np.linalg.pinv(A)
print(A_pse_calc)

print(D_pse.dot(A))

# ==============================
# Pseudo inversa para un sistema sobredeterminado

x = np.linspace(-5,5, 1000)
y_1 = -4*x+3
y_2 = 2*x+5
y_3 = -3*x+1

matriz = np.array([[4,1], [-2,1], [3,1]])
print(matriz)

matriz_pse = np.linalg.pinv(matriz)
print(matriz_pse)
b = np.array([[3], [5], [1]])
resultado = matriz_pse.dot(B)
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)
plt.xlim(-3, 3.5)
plt.ylim(-7,7)
plt.scatter(resultado[0], resultado[1])
plt.show()
