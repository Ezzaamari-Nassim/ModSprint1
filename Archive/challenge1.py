# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
"""
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpg

R = 0 * np.ones((5,100), dtype = np.uint8)
G = 0 * np.ones((5,100), dtype = np.uint8)
B = 0 * np.ones((5,100), dtype = np.uint8)

R1 = 255 * np.ones((5,100), dtype = np.uint8)
G1 = 255 * np.ones((5,100), dtype = np.uint8)
B1 = 255 * np.ones((5,100), dtype = np.uint8)

rectangle = np.stack ((R,G,B), axis = 2)
rectangle1 = np.stack ((R1,G1,B1), axis = 2)

bande = np.concatenate((rectangle, rectangle1), axis = 0)

petiDrapeau = np.concatenate((bande, bande), axis = 0)

grandDrapeau = np.concatenate((petiDrapeau, petiDrapeau), axis = 0)

drapeau = np.concatenate((grandDrapeau, bande), axis = 0)

plt.imshow(drapeau)