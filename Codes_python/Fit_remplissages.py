#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 00:33:10 2024

@author: ruben
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math

file_paths=['/home/ruben/M2-Stage-Liphy/test_colonne_sans_mousse_remplissage_8_co2.csv',
           '/home/ruben/M2-Stage-Liphy/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv' ,
            '/home/ruben/M2-Stage-Liphy/remplissage_600ml_eau_pur_mi_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/remplissage_mousse_70CMC_600ml_plus_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/remplissage_300ml_5gL_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/remplissage_600ml_cinqgramesparlittre_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/remplissage_aspiro_300ml_3point5_8_co2.csv',
            '/home/ruben/M2-Stage-Liphy/remplissage_CO2_600ml_aspiro_035gparL.csv'
            ]

Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A

for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/10000
    y=(db['Media value concentration']/10000)*100/(db['Media value concentration'].max()/100)
    def func(t, D):
        epsilon=(v*t)/0.6
        eta=D/(v*0.6)
        return 0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon)))))

    popt, pcov=curve_fit(func, x, y )
    popt
    if 'sans' in file_path:
        label='Remplissage sans mousse'
    if 'pure' in file_path:
        label='300 ml eau sans surfactant'
    if 'mi' in file_path:
        label='600 ml eau sans surfactant'
    if '160424' in file_path:
        label='300 ml SDS 1.7 g/L'
    if 'plus' in file_path:
        label='600 ml SDS 1.7 g/L'
    if '5gL' in file_path:
        label='300 ml SDS 5 g/L'
    if 'cinqgramesparlittre' in file_path:
        label='600 ml SDS 5 g/L'
    if '3point5' in file_path:
        label='300 ml ASPIRO 3.5 g/L'
    if '035gparL' in file_path:
        label='600 ml ASPIRO 3.5 g/L'
    plt.scatter(x, y, label=f'{label} ', marker='o', s=1)
    #plt.plot(x, func(x, *popt), label='fit: D=%5.8f' %tuple(popt))

plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=20)
plt.legend(loc='lower right', fontsize='x-large',markerscale=10)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()

# mask= y <= 0.6
# x_filtered=x[mask]
# y_filtered=y[mask]




### Plotting

