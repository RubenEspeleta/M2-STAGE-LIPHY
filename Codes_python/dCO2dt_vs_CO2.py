#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 17:01:49 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import savgol_filter
file_paths=['/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv', ## 70% CMC 300 ml SDS
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv',
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_remplissage_8_co2.csv', ## Test 450 ml liquide 70% CMC SDS
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_vidange_8_co2.csv',
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_remplissage_23gL_8_co2.csv', ## Test 2.3 g/L SDS
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_vidange_23gL_8_co2.csv',
           '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv', ### No mousse
           '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_8_co2.csv',
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv', ### Test sans surfactant (eau pure)
           '/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_vidange_8_co2.csv']
           
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/100
    if '23gL' in file_path:
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse colorée 2.3 g/L SDS'
        else:
            label='Remplissage mousse colorée 2.3 g/L'
    if '70cmc' in file_path:
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse sans colorant 70% CMC SDS'
        else:
            label='Remplissage mousse sans colorant 70% CMC SDS'
    if 'sans' in file_path:
        if 'vidange' in file_path:
            label='Vidange colonne sans mousse'
        else:
            label='Remplissage colonne sans mousse'
    if '040324' in file_path:
        if 'vidange' in file_path:
            label='Vidange mousse colorée 5 g/L SDS'
        else:
            label='Remplissage mousse colorée 5 g/L SDS'
    if 'pure' in file_path:
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange sans mousse 300 ml eau pure'
        else:
            label='Remplissage sans mousse 300 ml eau pure'
    if '450' in file_path:
         db=pd.read_csv(file_path)
         y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
         if 'vidange' in file_path:
             label='Vidange mousse sans colorant 450ml de liquide SDS 70% CMC'
         else:
            label='Remplissage mousse sans colorant 450ml de liquide SDS 70% CMC'
    percentage = int(file_path.split('_')[-2])
    yhat=savgol_filter(y, 1000, 3)
    derivative=np.gradient(yhat, x)
    plt.plot(y, derivative, label= f'Test {label} {percentage * 10} ml/min CO2')
    #plt.plot(x, yhat, label= f'Test {label} {percentage * 10} ml/min CO2')
plt.xlabel('Concentration CO$_2$', fontsize=20)
plt.ylabel(r' $\frac{d}{dt}CO_2$', fontsize=20)
plt.legend(loc='lower left', fontsize='x-large',markerscale=10)
plt.title(r' $\frac{d}{dt}CO_2$ vs concentration $CO_2$', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()
