#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 17:55:46 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

R = np.ones((5*10,16*10), dtype = np.uint8)*255
G = np.ones((5*10,16*10), dtype = np.uint8)*255
B = np.ones((5*10,16*10), dtype = np.uint8)*255

rectBlanc = np.stack ((R,G,B), axis = 2)

R = np.ones((5*10,16*10), dtype = np.uint8)*227
G = np.ones((5*10,16*10), dtype = np.uint8)*66
B = np.ones((5*10,16*10), dtype = np.uint8)*52

rectRouge = np.stack ((R,G,B), axis = 2)

drapeau = np.concatenate((rectBlanc,rectRouge), axis = 0)

plt.imshow(drapeau)

mpg.imsave('polandFlag.png', drapeau)