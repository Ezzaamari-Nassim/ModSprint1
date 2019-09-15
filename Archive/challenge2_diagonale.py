#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 09:42:40 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt

iD = np.eye(50, dtype=np.uint8)+1

iD2 = np.eye(50, dtype=np.uint8)

iD = iD-iD2-iD2

print iD

R = 255*np.ones((50,50), dtype = np.uint8)
G = 255*np.ones((50,50), dtype = np.uint8)
B = 255*np.ones((50,50), dtype = np.uint8)

R = R*iD
G = G*iD
B = B*iD

rectangle = np.stack((R,G,B), axis = 2)

plt.imshow(rectangle)