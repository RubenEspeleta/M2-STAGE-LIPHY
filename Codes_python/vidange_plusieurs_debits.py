#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 13:54:42 2024

@author: stage
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math
file_paths=['/home/stage/M2-Stage-Liphy/vidange_sin_nada_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_test3_vidange_100_co2.csv',
            #'/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_test4_vidange_15_co2.csv',
            '/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_vidange_15_co2.csv'
            #'/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_test4_vidange_50_co2.csv'
            ]
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/10000
    y=(db['Media value concentration']/10000)*100/(db['Media value concentration'].max()/100)
    
    if '100' in file_path:
        label='1000 ml/min'
        Q=1000/(60*1000**2)
        A=0.125*0.09        ## Area de la section transversale de la colonne en m2
        v=Q/A
        def func(t, D):
            epsilon=(v*t)/0.6
            eta=D/(v*0.6)
            return 1-(0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon))))))
        popt, pcov=curve_fit(func, x, y )
        popt
        plt.scatter(x, y, label=f'{label} ', color='r', marker='o', s=1)
    
    if 'nada' in file_path:
        label='80 ml/min'
        Q=80/(60*1000**2)
        A=0.125*0.09        ## Area de la section transversale de la colonne en m2
        v=Q/A
        def func(t, D):
            epsilon=(v*t)/0.6
            eta=D/(v*0.6)
            return 1-(0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon))))))
        popt, pcov=curve_fit(func, x, y )
        popt
        plt.scatter(x, y, label=f'{label} ', color='k', marker='o', s=1)
   
    ### Avec de l'eau sans surfactant
    
    if '50' in file_path:
        label='50 ml/min'
        Q=500/(60*1000**2)
        A=0.125*0.09        ## Area de la section transversale de la colonne en m2
        v=Q/A
        def func(t, D):
            epsilon=(v*t)/0.6
            eta=D/(v*0.6)
            return 1-(0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon))))))
        popt, pcov=curve_fit(func, x, y )
        popt
        plt.scatter(x, y, label=f'{label} ', c='xkcd:carolina blue', marker='o', s=1)
    
    
    
    ## 600 ml eau sans surfactant
        
    if '15' in file_path:
        label='150 ml/min'
        Q=150/(60*1000**2)
        A=0.125*0.09        ## Area de la section transversale de la colonne en m2
        v=Q/A
        def func(t, D):
            epsilon=(v*t)/0.6
            eta=D/(v*0.6)
            return 1-(0.5*(special.erfc((1-epsilon)/(2*np.sqrt(eta*epsilon)))+(np.exp(1/eta)*special.erfc((1+epsilon)/(2*np.sqrt(eta*epsilon))))))
        popt, pcov=curve_fit(func, x, y )
        popt
        plt.scatter(x, y, label=f'{label} ', color='b', marker='o', s=1)
        
    #plt.plot(x, func(x, *popt), label='fit: D=%5.8f' %tuple(popt))
    
plt.xlabel('Time (s)', fontsize=40)
plt.ylabel(r'Concentration $CO_2$ ($\frac{n_{CO_2}}{n_{total}}$)', fontsize=40)
plt.legend(loc='lower right', fontsize='xx-large',markerscale=20, title_fontsize='xx-large')
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.show()