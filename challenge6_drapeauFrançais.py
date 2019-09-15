#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:07:42 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

largeur = 600
longueur = int(largeur * 2/3)

c = int(largeur * 1/3)

print(longueur)

im = np.zeros((longueur,largeur,3), dtype=np.uint8)

im[:,0:c:1] = [5,20,64]
im[:,c:2*c:1] = [255,255,255]
im[:,2*c:3*c:1] = [236,25,32]

plt.imshow(im)
mpg.imsave('Flag/DrapeauFrancais.png', im)