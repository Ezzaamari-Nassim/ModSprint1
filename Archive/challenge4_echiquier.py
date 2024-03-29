#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:21:59 2019

@author: nguyent
"""

import numpy as np
import matplotlib.pyplot as plt

R = np.ones((8,8), dtype = np.uint8)*255
G = np.ones((8,8), dtype = np.uint8)*255
B = np.ones((8,8), dtype = np.uint8)*255

carreBlanc = np.stack ((R,G,B), axis = 2)

R = np.ones((8,8), dtype = np.uint8)*0
G = np.ones((8,8), dtype = np.uint8)*0
B = np.ones((8,8), dtype = np.uint8)*0

carreNoir = np.stack ((R,G,B), axis = 2)

motifG = np.concatenate((carreBlanc,carreNoir), axis = 0)

motifD = np.concatenate((carreNoir,carreBlanc), axis = 0)
#axis = 0 signifie mettre sous l'autre

motif = np.concatenate((motifG,motifD), axis = 1)
#axis = 1 signifie mettre côte à côte

grandMotif = np.concatenate((motif,motif), axis = 1)

ligne = np.concatenate((grandMotif,grandMotif), axis = 1)

demiEchiquier = np.concatenate((ligne,ligne), axis = 0)

echiquier = np.concatenate((demiEchiquier,demiEchiquier), axis = 0)

plt.imshow(echiquier)