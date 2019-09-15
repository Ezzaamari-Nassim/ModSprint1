#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:44:28 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((60,256,3), dtype=np.uint8)
#im[:,0:256:1] = np.linspace(0,255,256)
im[:,0:100,2] = 255
#print(np.linspace(0,255,256))
plt.imshow(im)
mpg.imsave('Flag/Challenge3.png', im)