#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 21:32:22 2020

@author: fmurzone
"""
import numpy as np
import matplotlib.pyplot as plt
import sklearn.datasets
import pandas as pd
# Por cada variable en el conjunto de datos hara falta exponencialmente mas muestras para tener el mismo rigor.


np.random.seed(42)

x = 3*np.random.rand(200)
y = 20*x + 2*np.random.rand(200)

x = x.reshape(200, 1)
y = y.reshape(200, 1)

xy = np.hstack([x, y])
plt.show()

xy_centrado = xy - np.mean(xy, axis = 0)

plt.plot(xy_centrado[:,0], xy_centrado[:,1], '.')
plt.show()

autovalores, autovectores = np.linalg.eig(xy_centrado.T.dot(xy_centrado))
print(autovectores)
# Estos autovectores estan relacionados con la dirección de la disperción

xy_new = autovectores.T.dot(xy_centrado.T)
print(xy_new)
# El PCA (Analisis de componentes principales) se usa mucho para reducir la cantidad de dimensiones con las que estamos trabajando
# Muchas veces nuestro conjunto de datos es muy grande y es necesario reducirlo al menos en un 20%, dejando el 80% de datos mas significativo.
# Uso en imagenes:
data= sklearn.datasets.fetch_olivetti_faces()
imagen_1 = data.data[0].reshape(64, 64)
imagen_2 = data.data[1].reshape(64, 64)
plt.imshow(data.data[5].reshape(64,64), cmap='gray')





