#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 21:11:27 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

largeur = 800
longueur = 500#int(largeur * 5/8)

c = int(longueur/2)

im = np.zeros((longueur,largeur,3), dtype=np.uint8)

im[0:c,:] = 255

im[c:2*c,:] = [255,0,0]


I, J = np.meshgrid(\
                    np.arange(500, dtype=np.int64),\
                    np.arange(800, dtype = np.int64),\
                    indexing = 'ij')

im[np.logical_and(I >= J, I <= 500 - J)] = np.array([0, 0, 255], dtype = np.uint8)

plt.imshow(im)
mpg.imsave('Flag/DrapeauTcheque.png', im)