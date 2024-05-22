#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  3 15:00:42 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
Q1=80/60
D=5.38
S=(np.pi*D**2)/4
h_experiments=np.arange(0, 7.8, 0.078)
t_exp=np.arange(0,97,0.97)
h_teorique=Q1*t_exp/S
Q_exp=S*np.tan((90-22.989)*np.pi/180)*2.6*60/105
print(Q_exp)
plt.figure()
plt.plot(t_exp, h_experiments, label='measuré')
plt.plot(t_exp, h_teorique, label='theorie')
plt.legend()
plt.show()






