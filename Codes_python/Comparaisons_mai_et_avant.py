#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 13:20:44 2024

@author: stage
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_paths=[#'/home/stage/M2-Stage-Liphy/test_colonne_mai_remplissage_8_co2.csv',     ## SANS MOUSSE
            #'/home/stage/M2-Stage-Liphy/test_colonne_mai_vidange_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_remplissage_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_vidange_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/remplissage_300_ml_eau_no_surfactant_8_co2.csv', ### 300 ml eau sans surfactant
            #'/home/stage/M2-Stage-Liphy/vidange_300_ml_eau_no_surfactant_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/Test_eau_pure/test_colonne_3D_eau_pure_vidange_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/remplissage_mousse_SDS_70_CMC_300ml_8_co2.csv',   ### 70% CMC
            '/home/stage/M2-Stage-Liphy/vidange_mousse_SDS_70_CMC_300ml_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv'
            
            
    ]
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x = db.index / 2
    y =  db['Media value concentration']/10000
    percentage = int(file_path.split('_')[-2])
    if 'mai' in file_path:
        if 'vidange' in file_path:
            #y=(db['Media value concentration']/100)/(db['Media value concentration'].max()/100)
            label='Vidange sans mousse 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='k', marker='x', s=1)
        else:
            #y=(db['Media value concentration']/100)/(db['Media value concentration'].max()/100)
            label='Remplissage sans mousse 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='k', marker='v', s=1)
    if 'sans' in file_path:
        if 'vidange' in file_path:
            label='Vidange sans mousse'
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='*', s=10)
        else:
            label='Remplissage sans mousse'
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='o', s=10)
    
    if 'surfactant' in file_path:
        if 'vidange' in file_path:
            label='Vidange 300 ml eau sans surfactant 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='b', marker='x', s=1)
        else:
            label='Remplissage 300 ml eau sans surfactant 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='b', marker='v', s=1)
    if 'pure' in file_path:
        if 'vidange' in file_path:
            label='Vidange 300 ml eau sans surfactant'
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='*', s=10)
        else:
            label='Remplissage 300 ml eau sans surfactant'
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='o', s=10)
    if '160424' in file_path:
        if 'vidange' in file_path:
            label='Vidange 1.7 g/L (70% CMC)'
            #y=(db['Media value concentration']/100)/(db['Media value concentration'].max()/100)
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='*', s=10)
        else:
            label='Remplissage 1.7 g/L (70% CMC)'
            #y=(db['Media value concentration']/100)/(db['Media value concentration'].max()/100)
            plt.scatter(x[::300], y[::300], label=f'{label} {percentage*10} ml/min CO2', color='m', marker='o', s=10)
    if 'SDS' in file_path:
        if 'vidange' in file_path:
            label='Vidange 1.7 g/L (70% CMC) 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='r', marker='x', s=1)
        else:
            label='Remplissage 1.7 g/L (70% CMC) 2eme experience'
            plt.scatter(x, y, label=f'{label} {percentage*10} ml/min CO2', color='r', marker='v', s=1)
    
    

plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=20)
plt.legend(loc='lower right', fontsize='x-large',markerscale=5)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()