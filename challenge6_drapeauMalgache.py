#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:18:54 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

largeur = 600
longueur = int(largeur * 2/3)

c = int(longueur * 1/2)

im = np.zeros((longueur,largeur,3), dtype=np.uint8)

im[:,:] = 255

im[0:c,c:c*3:1] = [255,0,0]

im[c:c*2,c:c*3:1] = [0,255,0]


plt.imshow(im)
mpg.imsave('Flag/DrapeauMalgache.png', im)