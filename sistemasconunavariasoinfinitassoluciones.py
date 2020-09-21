#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 07:44:22 2020

@author: fmurzone
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6,6)

y_1 = 3*x+5
y_2 = -x+3
y_3 = 2*x + 1

plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.axvline(x=0, color="grey")
plt.axhline(y=0, color="grey")

plt.show()
# Sistema sobredeterminado

x = np.arange(-6,6)
y_2 = -1*x+3
y_2 = 2*x+1

plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.axvline(x=0, color="grey")
plt.axhline(y=0, color="grey")

plt.show()
# Sistema con una solucion