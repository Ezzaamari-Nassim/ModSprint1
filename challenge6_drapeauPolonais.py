#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:02:33 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

largeur = 800
longueur = int(largeur * 5/8)

c = int(longueur/2)

im = np.zeros((longueur,largeur,3), dtype=np.uint8)

im[0:c,:] = 255

im[c:2*c,:] = [227,66,52]

plt.imshow(im)
mpg.imsave('Flag/DrapeauPolonais.png', im)