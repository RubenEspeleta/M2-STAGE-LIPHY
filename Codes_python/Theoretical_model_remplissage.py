#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 14:56:22 2024

@author: stage
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math
Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A

# t=np.arange(0,20001,1)
# D1=0.000001
# D2=0.000016
# D3=10*D2

# epsilon=(v*t)/0.6
# eta_1=D1/(v*0.6)
# y1=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_1*epsilon)))+(np.exp(1/eta_1)*special.erfc((1+epsilon)/(2*np.sqrt(eta_1*epsilon)))))

# plt.plot(t, y1, 'r-', label='D=0')
# eta_2=D2/(v*0.6)
# y2=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_2*epsilon)))+(np.exp(1/eta_2)*special.erfc((1+epsilon)/(2*np.sqrt(eta_2*epsilon)))))
# plt.plot(t, y2, 'b-', label='D=0.16 cm²/s')

# eta_3=D3/(v*0.6)
# y3=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_3*epsilon)))+(np.exp(1/eta_3)*special.erfc((1+epsilon)/(2*np.sqrt(eta_3*epsilon)))))
# plt.plot(t, y3, 'g-', label='D=1.6 cm²/s')

# plt.xlabel('Time (s)', fontsize=40)
# plt.ylabel('Concentration $CO_2$ (%)', fontsize=40)
# plt.legend(loc='lower right', fontsize='xx-large',markerscale=40)
# plt.xticks(fontsize=40)
# plt.yticks(fontsize=40)
# plt.show()



#### Faire varier le parametre x
t=np.arange(0,20001,1)
D=0.000016
epsilon=(v*t)/0.6
x1=0.6
x2=10*x1
x3=x1/10
eta_1=D/(v*x1)
y1=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_1*epsilon)))+(np.exp(1/eta_1)*special.erfc((1+epsilon)/(2*np.sqrt(eta_1*epsilon)))))
plt.plot(t, y1, 'r-', label='x= 60 cm')
eta_2=D/(v*x2)
y2=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_2*epsilon)))+(np.exp(1/eta_2)*special.erfc((1+epsilon)/(2*np.sqrt(eta_2*epsilon)))))
plt.plot(t, y2, 'b-', label='x=600 cm')
eta_3=D/(v*x3)
y3=0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta_3*epsilon)))+(np.exp(1/eta_3)*special.erfc((1+epsilon)/(2*np.sqrt(eta_3*epsilon)))))
plt.plot(t, y3, 'g-', label='x=6 cm')
plt.xlabel('Time (s)', fontsize=40)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=40)
plt.legend(loc='lower right', fontsize='xx-large',markerscale=40)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.show()
