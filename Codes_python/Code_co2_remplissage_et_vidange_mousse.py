#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:44:34 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
humidity='/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/temperature_humidite.csv'
file_paths=[
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_remplissage_8_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_vidange_8_co2.csv',
    '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv',
    '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_8_co2.csv'
    #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_3D_coloree_8_co2.csv'
    ]



for file_path in file_paths:
    db=pd.read_csv(file_path)
    #db2=pd.read_csv(humidity)
    x=db.index/2
    y=db['Media value concentration']/100
    if 'vidange' in file_path:
        label='Vidange'
        if 'sans' in file_path:
            label='Vidange sans mousse'
        if 'coloree' in file_path:
            label='Vidange coloree'
    else:
        label='Remplissage'
        if 'sans' in file_path:
            label='Remplissage sans mousse'
        if 'coloree' in file_path:
            label='Remplissage coloree'
    
    percentage = int(file_path.split('_')[-2])
    
    ax1 = plt.gca()
    ax1.scatter(x,y,label=f'Test {label} {percentage*10} ml/min CO2', marker='o', s=1)
    
    
    plt.xlabel('Temps (s)')
    plt.ylabel('Concentration $CO_2$ %')
    plt.legend(loc='lower right')
    plt.title('Concentration $CO_2$ en function du temps colonne avec mousse SDS')
    plt.show()
    

    
# ax2 = ax1.twinx()
# ax2.set_ylabel('Humidité %HR')
# ax2.plot(db2.index*60, db2['HR'], color='red', label='Humidité')
plt.legend()

 