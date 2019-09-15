#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:07:42 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((400,600,3), dtype=np.uint8)

im[:,0:200:1,0] = 5 #R
im[:,0:200:1,1] = 20 #V
im[:,0:200:1,2] = 64 #B

im[:,200:400:1,0] = 255
im[:,200:400:1,1] = 255
im[:,200:400:1,2] = 255

im[:,400:600:1,0] = 236
im[:,400:600:1,1] = 25
im[:,400:600:1,2] = 32

plt.imshow(im)
mpg.imsave('Flag/DrapeauFrancais.png', im)