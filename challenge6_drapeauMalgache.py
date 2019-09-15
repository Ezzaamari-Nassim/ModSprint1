#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:18:54 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((400,600,3), dtype=np.uint8)

im[:,:] = 255

im[0:200,200:600:1,0] = 255
im[0:200,200:600:1,1] = 0
im[0:200,200:600:1,2] = 0

im[200:400,200:600:1,0] = 0
im[200:400,200:600:1,1] = 255
im[200:400,200:600:1,2] = 0


plt.imshow(im)
mpg.imsave('Flag/DrapeauMalgache.png', im)