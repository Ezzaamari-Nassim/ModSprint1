#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:30:55 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt

R = 255 * np.ones((100,5), dtype = np.uint8)
G = 255 * np.ones((100,5), dtype = np.uint8)
B = 255 * np.ones((100,5), dtype = np.uint8)

R1 = 0 * np.ones((100,5), dtype = np.uint8)
G1 = 0 * np.ones((100,5), dtype = np.uint8)
B1 = 0 * np.ones((100,5), dtype = np.uint8)

rectangle = np.stack((R,G,B), axis = 2)
rectangle1 = np.stack((R1,G1,B1), axis = 2)

motif = np.concatenate((rectangle, rectangle1), axis = 1)

petitDrapeau = np.concatenate((motif, motif), axis = 1)

moyenDrapeau = np.concatenate((petitDrapeau, petitDrapeau), axis = 1)

drapeau = np.concatenate((moyenDrapeau, motif), axis = 1)

plt.imshow(drapeau)