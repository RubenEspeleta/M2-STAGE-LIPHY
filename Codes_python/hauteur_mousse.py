#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:30:41 2024

@author: ruben
"""

#### HAUTEUR DE MOUSSE

import matplotlib.pyplot as plt
import numpy as np
slope=1/np.tan(2.345*np.pi/180)
h0=21
max_y=69.838
intersect_x_ymax=(max_y-h0)*50/slope
t=np.arange(0, intersect_x_ymax+1)
h=slope*(t/50)+h0
plt.plot(t,h, '-r', label='h(t)')
plt.title('Hauteur colonne 3D debit 80 ml/min aiguille hydrophobe', fontsize=10)
plt.xlabel('timestep t/50 s')
plt.ylabel('h(t) (cm)')
plt.grid(True)
plt.legend()
plt.show()