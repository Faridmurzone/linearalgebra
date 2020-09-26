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