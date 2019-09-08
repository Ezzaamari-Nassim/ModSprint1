#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 18:14:22 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

R = np.ones((2*100,1*100), dtype = np.uint8)*0
G = np.ones((2*100,1*100), dtype = np.uint8)*0
B = np.ones((2*100,1*100), dtype = np.uint8)*255

rectBle = np.stack ((R,G,B), axis = 2)

R = np.ones((2*100,1*100), dtype = np.uint8)*255
G = np.ones((2*100,1*100), dtype = np.uint8)*255
B = np.ones((2*100,1*100), dtype = np.uint8)*255

rectBla = np.stack ((R,G,B), axis = 2)

motif = np.concatenate((rectBle,rectBla), axis = 1)

R = np.ones((2*100,1*100), dtype = np.uint8)*255
G = np.ones((2*100,1*100), dtype = np.uint8)*0
B = np.ones((2*100,1*100), dtype = np.uint8)*0

rectRed = np.stack ((R,G,B), axis = 2)

drapeau = np.concatenate((motif,rectRed), axis = 1)


plt.imshow(drapeau)

mpg.imsave('frenchFlag.png', drapeau)