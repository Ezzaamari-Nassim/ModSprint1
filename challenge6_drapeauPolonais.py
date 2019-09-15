#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:02:33 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((500,800,3), dtype=np.uint8)

im[0:250,:] = 255

im[250:500,:,0] = 227
im[250:500,:,1] = 66
im[250:500,:,2] = 52

plt.imshow(im)
mpg.imsave('Flag/DrapeauPolonais.png', im)