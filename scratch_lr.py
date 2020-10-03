#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 07:50:02 2020

@author: fmurzone
"""

# y = b₀ + b₁x
# b₁ = Σ(x-m_x)(y-m_y) / Σ(x - m_x)**2 -> Donde m_ es promedio de...

import numpy as np
import matplotlib.pyplot as plt

# Estimate b0 and b1
def estimate_b0_b1(x, y):
    n = np.size(x)
    # obtain means
    m_x, m_y = np.mean(x), np.mean(y)
    
    # get sumayory of XY and sum XX
    sumatory_xy = np.sum((x-m_x)*(y-m_y))
    sumatory_xx = np.sum(x*(x-m_y))
    
    # regression coeficients
    b_1 = sumatory_xy / sumatory_xx
    b_0 = m_y - b_1 * m_x 
    
    return(b_0, b_1)

# Graph function
def plot_regression(x, y, b):
    plt.scatter(x, y, color="r", marker = "o", s=30)
    y_pred = b[0] + b[1]*x
    plt.plot(x, y_pred, color="b")
    plt.xlabel('X - Var independiente')
    plt.ylabel('Y - Var Dependiente')
    plt.show()
    
def main():
    x = np.array([1,5,2,3,6,7])
    y = np.array([1,2,3,4,5,6])
    b = estimate_b0_b1(x, y)
    print(f'b0 = {b[0]}, b1 = {b[1]}')
    plot_regression(x,y,b)
    
if __name__ == "__main__":
    main()