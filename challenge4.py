#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:03:06 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((80,80,3), dtype=np.uint8)

a = np.arange(0,80)%20 < 10
b = np.arange(0,80)%20 < 10

A, B = np.meshgrid(a,b)
im[A == B] = 255

plt.imshow(im)
mpg.imsave('Flag/Challenge4.png', im)