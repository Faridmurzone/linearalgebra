#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:29:18 2020

@author: fmurzone
"""

import numpy as np

identity = np.eye(5)
print(identity)

vector = np.array([[2], [3], [5], [7], [9]])
print(identity.dot(vector))

A = np.array([[1,0,1], [0,1,1], [-1,1,1]])
print(A)

inverse_A = np.linalg.inv(A)
print(inverse)

print(A.dot(inverse_A))

singular = np.array([[1,1], [1,1]])
print(singular)

print(np.linalg.inv(singular))