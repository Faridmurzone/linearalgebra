#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:05:01 2020

@author: fmurzone
"""

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargamos informacion de wines
wines = datasets.load_wine()

# Separamos nuestra dataset
X_wines = wines.data
Y_wines = wines.target

# Llevo los datos a una estructura de DataFrame
xw = pd.DataFrame(X_wines, columns = ['Alcohol', 'Malic Acid', 'Ash', 'Alcalinity of Ash', 'Magnesium', 
                                      'Total Phenols', 'Flavanoids', 'Nonflavanoid Phenols', 'Proanthocyanins', 
                                      'Colour Intensity', 'Hue', 'OD280/OD315 of diluted wines', 'Proline'])
yw = pd.DataFrame(Y_wines, columns = ['Target'])
xw.head(5)

# Ploteo para encontrar el numero de clusters de acuerdo a 
# metodo del codo
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, max_iter=1000, random_state=0)
    kmeans.fit(xw)
    yw_kmeans = kmeans.predict(xw)
    wcss.append(kmeans.inertia_)
    accuracy =  metrics.adjusted_rand_score(Y_wines, yw_kmeans)
    print(f'numero de n_clusters: {i} accurracy {accuracy}')
plt.plot(range(1, 11), wcss)
plt.title('ELBOW METHOD')
plt.xlabel('NUMBER OF CLUSTERS')
plt.ylabel('WCSS')
plt.show()

# Aplico el modelo de KMeans
modelw = KMeans(n_clusters = 3, max_iter = 1000)
modelw.fit(xw)
yw_labels = modelw.labels_
yw_kmeans = modelw.predict(xw)
print('predicciones ', yw_kmeans)
yw_kmeans_df = pd.DataFrame(yw_kmeans, columns = ['Prediction'])

# Precisión del modelo
accuracyw =  metrics.adjusted_rand_score(Y_wines, yw_kmeans)
print(accuracyw)

# Concateno el dataset de entrada con el de la prediccion
Z = pd.concat([xw, yw_kmeans_df],axis=1)

# Grafico para ver relación de las features con respecto a las 
# valores de la predicción, poniendo color según (0,1,2) 
# considerando las tres clases.
sns.pairplot(Z, hue = 'Prediction')