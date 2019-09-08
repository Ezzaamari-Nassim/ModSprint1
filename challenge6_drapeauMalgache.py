#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:27:03 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

R = np.ones((2*100,1*100), dtype = np.uint8)*255
G = np.ones((2*100,1*100), dtype = np.uint8)*255
B = np.ones((2*100,1*100), dtype = np.uint8)*255
rectBla = np.stack ((R,G,B), axis = 2)

R = np.ones((1*100,2*100), dtype = np.uint8)*255
G = np.ones((1*100,2*100), dtype = np.uint8)*0
B = np.ones((1*100,2*100), dtype = np.uint8)*0
rectRou = np.stack ((R,G,B), axis = 2)

R = np.ones((1*100,2*100), dtype = np.uint8)*0
G = np.ones((1*100,2*100), dtype = np.uint8)*255
B = np.ones((1*100,2*100), dtype = np.uint8)*0
rectVert = np.stack ((R,G,B), axis = 2)

motif = np.concatenate((rectRou,rectVert), axis = 0)

drapeau = np.concatenate((rectBla,motif), axis = 1)


plt.imshow(drapeau)
mpg.imsave('malgacheFlag.png', drapeau)