#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:33:46 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt

R = np.ones((60,1), dtype = np.uint8)*0
G = np.ones((60,1), dtype = np.uint8)*0
B = np.ones((60,1), dtype = np.uint8)*0

image = np.stack ((R,G,B), axis = 2)
"""
#####
R = np.ones((5,1), dtype = np.uint8)*50
G = np.ones((5,1), dtype = np.uint8)*50
B = np.ones((5,1), dtype = np.uint8)*50

uniqueColone = np.stack ((R,G,B), axis = 2)

image = np.concatenate((image,uniqueColone), axis = 1)
#######

#####
R = np.ones((5,1), dtype = np.uint8)*100
G = np.ones((5,1), dtype = np.uint8)*100
B = np.ones((5,1), dtype = np.uint8)*100

uniqueColone = np.stack ((R,G,B), axis = 2)

image = np.concatenate((image,uniqueColone), axis = 1)
#######
"""
for niveauDeGris in np.arange(256): #0->255 256 niveaux de gris
    R = np.ones((60,1), dtype = np.uint8)*niveauDeGris#60x1 de large
    G = np.ones((60,1), dtype = np.uint8)*niveauDeGris
    B = np.ones((60,1), dtype = np.uint8)*niveauDeGris
    
    uniqueColone = np.stack ((R,G,B), axis = 2)
    
    image = np.concatenate((image,uniqueColone), axis = 1)



print image
"""
for niveauDeGris in np.arange(2): #0->255 256 niveaux de gris
    R = np.ones((60,1), dtype = np.uint8)*niveauDeGris#60x1 de large
    G = np.ones((60,1), dtype = np.uint8)*niveauDeGris
    B = np.ones((60,1), dtype = np.uint8)*niveauDeGris
    
    uniqueColone = np.stack ((R,G,B), axis = 2)
    
    image = np.concatenate((image,uniqueColone), axis = 1)
    
    #print uniqueColone"""

plt.imshow(image)