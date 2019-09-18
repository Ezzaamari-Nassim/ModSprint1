#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:58:11 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpg

im = np.zeros((200,300,3), dtype=np.uint8)

im[:] = 255

I, J = np.meshgrid(\
                    np.arange(200, dtype=np.int64),\
                    np.arange(300, dtype = np.int64),\
                    indexing = 'ij')
centreCercleX = 100
centreCercleY = 150
rayonCercle = 4000

#Utilisation de Pythagore : a²+b² = c²
#Merci JF
im[(I-centreCercleX)**2 + (J-centreCercleY)**2 <= rayonCercle]= \
np.array([255, 0, 0], dtype = np.uint8)

plt.imshow(im)
mpg.imsave('Flag/DrapeauJaponais.png', im)