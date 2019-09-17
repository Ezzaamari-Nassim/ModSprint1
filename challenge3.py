#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:44:28 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

x = np.arange(0,256)
y = np.arange(0,60)

X, Y = np.meshgrid(x,y)

im = np.stack((X,X,X), axis = 2)

plt.imshow(im)
mpg.imsave('Flag/Challenge3.png', im)