#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 07:28:02 2020

@author: fmurzone
"""
import numpy as np

# ¿Las matrices singulares tienen inversa?
- MAL Si y A.dot(A.T) devuelve la identidad.
-Si, es una matriz cuadrada y ...

# Un sistema de ecuaciones lineales con 4 ecuaciones y 4 incógnitas, que tiene solución, se puede representar en su forma matricial por
- 1 matriz A de 4x4 1 vector x de dimension 4 1 vector b de dimension 4

# Dadas A y B, tal que A.dot(B) está definido, entonces al transponer(A.dot(B)) siempre es igual a:
- B.dot(A.T)
- 
A = np.array([[1,2], [3,4]])
B = np.array(([2,3], [4,5]))
C = A.dot(B).T
print(C)
D = A.dot(B.T)
print(D)
E = B.T.dot(A)
print(E)
F = A.T.dot(B)
print(F)
G = B.T.dot(A.T)
print(G) # ESTA
# Cuál de estas afirmaciones es VERDADERA respecto al determinante de la Matriz
a = np.array([[1, 0, 0, 0, 0],
[0, 2, 0, 0, 0],
[0, 0, 3, 0, 0],
[0, 0, 0, 4,0],
[0,0,0,0,5]])

- La suma de los elementos de la diagonal da 15. La determinante es 15.

# MAL Cuando tengo dos matrices A y B, con A de dimensiones (3,2) y B (2,3), entonces con respecto al producto interno:
- En este caso siempre puedo calcular el producto interno, y da el mismo resultado hacer A.dot(B) y B.dot(A)
A = np.array([[1,2,3], [4,5,6]])
B = np.array([[1,2], [3,4], [5,6]])
C = A.dot(B)
D = B.dot(A)
print(C, D) # Puedo pero da distinto.
# BIEN Si estoy en un espacio de dimensión 3 y tengo una matriz, ¿Cuántas filas / columnas ortogonales puedo tener como máximo?
3 vectores ortonormales (filas o columnas), porque cuando quiera tener un vector más ortonormal a todos los que ya tengo no será posible lograrlo con esa cantidad de dimensiones.

# BIEN ¿Cuánto da la norma 0 (cero) del vector [-50,-25,0,25,100,-300]?
vector =  np.array([-50,-25,0,25,100,-300])
np.linalg.norm(vector) # 322.1

# Un sistema de ecuaciones lineales en R2 tiene infinitas soluciones cuando:
- MAL Cuando el sistema tiene mas restricciones que incognitas (grados de libertad) - Sobredeterminado
- Todas las ecuaciones forman parte de la misma recta
# ¿Cuánto da la norma del vector [1/2,1/2,1/2,1/2]? Observación: la norma que vimos durante la clase es la norma 2
vector = np.array([1/2,1/2,1/2,1/2])
np.linalg.norm(vector, ord=2) # Da 1
 
# ¿Son ortogonales los vectores v = [7,-7,3], u=[1,1,0] y w=[0,0,1]?
v = np.array([7,-7,3])
u = np.array([1,1,0])
w = np.array([0,0,1])
result = v.dot(u.T)
print(result)
result2 = u.dot(w.T)
print(result2)
result3 = v.dot(w.T)
print(result3)
MAL - Por lo tanto si son ortogonales.
- No porque no todas las combinaciones dan 0
# BIEN Sumar la matriz [[1 3] [5 6]] con el escalar 3 (matriz+escalar) da lo mismo que hacer:
matriz = np.array([[1, 3],[5, 6]])
result = matriz + 3
print(result) # 4,5 y 8,9
---- Es matriz + vector con vector = np.array([[3], [3]])

# BIEN ¿Es importante definir funciones auxiliares que estén fuera de nuestro código principal?
- Es importante porque simplifica el mantenimiento y ahorramos tiempo.

# BIEN Para calcular la dimensión de un tensor debo usar la instrucción/atributo
tensor = np.array([[[1, 3],[5, 6]],[[1, 3],[5, 6]]])
tensor.shape

# BIEN ¿Qué código debo usar para crear un vector con los elementos 2 y 3 ([2,3])?
np.array([2,3])

# BIEN El producto interno de una matriz de dimensiones (3,2) y un vector de dimensión (2, ) nos devuelve:
matriz = np.array([[3,1], [3,2], [1,3]])
vector = [2,3]
matriz.dot(vector) # (3,)

# BIEN Transponer la matriz [[1, 2, 3, 4] [5, 6, 7, 8] [9,10, 11,12]] da como resultado:
matrix = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9,10, 11,12]])
matrix.T

[[ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]
 [ 4  8 12]]

# BIEN ¿El producto interno es conmutativo? O sea si tengo A y B matrices, tal que es posible calcular el producto interno, hacer A.dot(B) siempre es lo mismo que hacer B.dot(A)?
- No, solamente en casos particulares podria ser el mismo

# BIEN ¿Cómo puedo comprobar si una matriz A es simétrica?
- A == A.T

# BIEN Que angulas forman
- 90 grados, porque norma_v1 * norma_v2 * np.cos(np.deg2rad(90)) da 0

# BIEN Cuando calculo la dimensión del escalar 3.1 con el comando escalar.shape, ¿qué respuesta obtengo?
float object has no attribute shape


# BIEN Dado el sistema de ecuaciones lineales y = 7x+2 y = 3x+5 ¿Cuál es la solución del sistema?
x = 3/4

#¿Cómo debo representar el escalar 5 según la definición matemática con Python? 
escalar = 5
