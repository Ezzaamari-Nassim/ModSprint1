#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:38:44 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg


I, J = np.meshgrid(\
                    np.arange(50, dtype=np.int64),\
                    np.arange(50, dtype = np.int64),\
                    indexing = 'ij')

tabBool = np.arange(0,50)
tabBool =tabBool%10 < 5

im = np.ones((50,50,3), dtype=np.uint8)*255
im[I == J]=0

plt.imshow(im)
mpg.imsave('Flag/Challenge2.png', im)

print(I)
print(J)