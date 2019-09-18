# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 00:20:41 2019

@author: xd
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

largeur = 100
longueur = 100

largeur = largeur * 2
longueur = longueur * 3

im = np.zeros((largeur,longueur,3), dtype=np.uint8)

im[:,:] = [0,0,128]
im[90:110,]=255
im[:,140:160]=255
im[0:90,0:140] = [200, 0, 0]
im[110:,160:,] = [200, 0, 0]

im = np.fliplr(im)

plt.imshow(im)
mpg.imsave('Flag/DrapeauDominicain.png', im)

