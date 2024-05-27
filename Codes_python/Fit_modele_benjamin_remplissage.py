#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:41:44 2024

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

# def func(t, D, t0):
#     z=0.6*v/D  ### Hauteur du capteur adimenssionel
#     t2=(t+t0)*v**2/D   ## temps adimenssionnel
#     return 0.5*(special.erfc((z-t2)/(2*np.sqrt(t2))) + (2*np.sqrt(t2/np.pi)*np.exp(-((z-t2)**2)/(4*t2))) - (1+t2+z)*np.exp(z)*special.erfc((t2+z)/(2*np.sqrt(t2)))  )

# for file_path in file_paths:
#     db=pd.read_csv(file_path)
#     y=db['Media value concentration']/10000
#     if 
file_path='/home/stage/M2-Stage-Liphy/remplissage_mousse_SDS_70_CMC_300ml_8_co2.csv'
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

def func(t, D, t0):
    z=0.6*v/D  ### Hauteur du capteur adimenssionel
    t2=(t+t0)*v**2/D   ## temps adimenssionnel
    return 0.5*(special.erfc((z-t2)/(2*np.sqrt(t2))) + (2*np.sqrt(t2/np.pi)*np.exp(-((z-t2)**2)/(4*t2))) - (1+t2+z)*np.exp(z)*special.erfc((t2+z)/(2*np.sqrt(t2)))  )

popt, pcov=curve_fit(func, x_filtered, y_filtered )
popt


### Plotting

plt.scatter(x, y, label='Remplissage 450 ml 70% cmc SDS avant', marker='o', s=1)
plt.plot(x, func(x, *popt), 'r-', label='fit: D=%5.8f, t0=%5.8f' %tuple(popt))

plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=20)
plt.legend(loc='lower right', fontsize='x-large',markerscale=10)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()



