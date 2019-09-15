#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 14:26:26 2019

@author: nguyent
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

tabBool = np.arange(0,50)
tabBool =tabBool%10 < 5

im = np.zeros((50,100,3), dtype=np.uint8)
im[tabBool]=255

im = np.rot90(im)

plt.imshow(im)
mpg.imsave('Flag/Challenge1bis.png', im)