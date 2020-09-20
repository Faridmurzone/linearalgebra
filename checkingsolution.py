#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 10:22:33 2020

@author: fmurzone
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5)
y_1 = 3*x + 5
y_2 = 2*x + 3
plt.figure()

# Option 1: graphic
plt.plot(x, y_1)
plt.plot(x, y_2)

plt.xlim(-5,5)
plt.ylim(-5,5)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
# Lines are crossing so the solution EXISTS

# Option 2: Build matrix system
A = np.array([[-3,1], [-2,1]])
B = np.array([[5], [3]])

sol = np.array([-2,-1])
print(A.dot(sol)) # == B

