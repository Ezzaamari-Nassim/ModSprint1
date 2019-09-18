#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 18:22:01 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((400,800,3), dtype=np.uint8)

im[:] = [0,0,255]

I, J = np.meshgrid(\
                    np.arange(400, dtype=np.int64),\
                    np.arange(800, dtype = np.int64),\
                    indexing = 'ij')

#bande jaune
im[J*17/10 >= 400-I] = np.array([255,255,0], dtype = np.uint8)

#bande rouge
im[J*7/10 >= 400-I] = np.array([255,0,0], dtype = np.uint8)

#bande blanche
im[J*1/4>= 400-I] = np.array([255,255,255], dtype = np.uint8)


#bande verte
im[J*1/9 >= 400-I] = np.array([0, 255, 0], dtype = np.uint8)

plt.imshow(im)
mpg.imsave('Flag/DrapeauSeychellois.png', im)