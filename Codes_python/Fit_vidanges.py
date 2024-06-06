#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 01:37:31 2024

@author: ruben
"""

import numpy as np
from scipy import special
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd
import math

file_paths=['/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_vidange_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/test_colonne_no_foam_vidange_8_co2.csv',
            
           '/home/stage/M2-Stage-Liphy/Test_eau_pure/test_colonne_3D_eau_alone_vidange_8_co2.csv' ,
           '/home/stage/M2-Stage-Liphy/vidange_300_ml_eau_no_surfactant_8_co2.csv',
           
           '/home/stage/M2-Stage-Liphy/vidange_600ml_eau_pur_mi_8_co2.csv',
           
           '/home/stage/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv',
           '/home/stage/M2-Stage-Liphy/vidange_mousse_SDS_70_CMC_300ml_8_co2.csv',
           
           
           '/home/stage/M2-Stage-Liphy/vidange_mousse_70CMC_600ml_plus_8_co2.csv',
           
           '/home/stage/M2-Stage-Liphy/vidange_300ml_5gL_8_co2.csv',
           '/home/stage/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_vidange_8_co2.csv',
           
           '/home/stage/M2-Stage-Liphy/vidange_600ml_cinqgramesparlittre_8_co2.csv',
           
           '/home/stage/M2-Stage-Liphy/vidange_aspiro_300ml_3point5_8_co2.csv',
           '/home/stage/M2-Stage-Liphy/vidange_CO2_600ml_aspiro_035gparL.csv'
            ]

Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A

for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/10000
    y=(db['Media value concentration']/10000)*100/(db['Media value concentration'].max()/100)

    
    
   ## Sans mousse 
    if 'sans' in file_path:
        label='CO2 filling without foaming'
        plt.scatter(x, y, label=f'{label} ', color='k', marker='o', s=1)
    if 'foam' in file_path:
        plt.scatter(x[::100], y[::100], color='k', marker='o', s=1)
   
    ### Avec de l'eau sans surfactant
    
    if 'surfactant' in file_path:
        label='300 ml water without surfactant'
        plt.scatter(x, y, label=f'{label} ', c='xkcd:carolina blue', marker='o', s=1)
    if 'alone' in file_path:
        plt.scatter(x[::100], y[::100], c='xkcd:carolina blue', marker='o', s=1)
    
    ## 600 ml eau sans surfactant
        
    if 'mi' in file_path:
        label='600 ml water without surfactant'
        plt.scatter(x, y, label=f'{label} ', color='b', marker='o', s=1)
        
    ### 300 ml 70% CMC SDS
    if 'SDS' in file_path:
        label='300 ml 1.7 g/L SDS'
        plt.scatter(x, y, label=f'{label} ', color='orchid', marker='o', s=1)
    if '160424' in file_path:
        plt.scatter(x[::100], y[::100], c='orchid', marker='o', s=1)
          
    if 'plus' in file_path:
        label='600 ml 1.7 g/L SDS'
        plt.scatter(x, y, label=f'{label} ',  c='mediumorchid', marker='o', s=1)
        
    if '5gL' in file_path:
        label='300 m 5 g/L SDS'
        plt.scatter(x, y, label=f'{label} ', color='pink', marker='o', s=1)
    if 'coloree' in file_path:
        plt.scatter(x[::100], y[::100], c='pink', marker='o', s=1)
    if 'cinqgramesparlittre' in file_path:
        label='600 ml 5 g/L SDS'
        plt.scatter(x, y, label=f'{label} ',  c='xkcd:red violet', marker='o', s=1)
    
    
    if '3point5' in file_path:
        label='300 ml ASPIRO 3.5 g/L'
        plt.scatter(x, y, label=f'{label} ', color='red', marker='o', s=1)
    if '035gparL' in file_path:
        label='600 ml ASPIRO 3.5 g/L'
        plt.scatter(x, y, label=f'{label} ', c='xkcd:dark red', marker='o', s=1)
    

plt.xlabel('Time (s)', fontsize=20)
plt.ylabel('Concentration $CO_2$ (%)', fontsize=20)
plt.legend(loc='lower right', fontsize='x-large',markerscale=10)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.show()