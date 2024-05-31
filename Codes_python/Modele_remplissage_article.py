#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 16:05:46 2024

@author: stage
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math

# file_paths=['/home/stage/M2-Stage-Liphy/test_colonne_mai_remplissage_8_co2.csv',
#             '/home/stage/M2-Stage-Liphy/remplissage_300_ml_eau_no_surfactant_8_co2.csv',
#             '/home/stage/M2-Stage-Liphy/remplissage_600ml_eau_pur_mi_8_co2.csv',
#             '/home/stage/M2-Stage-Liphy/remplissage_mousse_SDS_70_CMC_300ml_8_co2.csv'
#             ]

Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A

file_path='/home/stage/M2-Stage-Liphy/remplissage_600ml_eau_pur_mi_8_co2.csv'
db=pd.read_csv(file_path)
x=db.index/2
y=db['Media value concentration']/10000
#y=(db['Media value concentration']/10000)*100/(db['Media value concentration'].max()/100)

Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A


mask= y <= 0.6
x_filtered=x[mask]
y_filtered=y[mask]

def func(t, D):
    epsilon=(v*t)/0.6
    eta=D/(v*0.6)
    return 0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon)))))

popt, pcov=curve_fit(func, x, y )
popt


### Plotting

plt.scatter(x, y, label='Remplissage 450 ml 70% cmc SDS avant', marker='o', s=1)
plt.plot(x, func(x, *popt), 'r-', label='fit: D=%5.8f' %tuple(popt))

plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=20)
plt.legend(loc='lower right', fontsize='x-large',markerscale=10)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()