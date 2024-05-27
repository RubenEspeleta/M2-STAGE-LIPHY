#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 11:25:55 2024

@author: ruben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

### Fichier pour les tests
file_paths=[#'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_remplissage_23gL_8_co2.csv',    ##### Tests avec 2.3 g/L SDS avec colorant
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_vidange_23gL_8_co2.csv',
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_remplissage_8_co2.csv',   ### Tests avec 5 g/L SDS avec colorant (100%)
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_vidange_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv',  ### Tests avec 70% de la CMC sans colorant
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv',
            #'/home/stage/M2-Stage-Liphy/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_remplissage_8_co2.csv'] ## Tests avec 450ml de SDS 70% de la CMC sans colorant
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_vidange_8_co2.csv',
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv', ### Tests sans mousse pour comparer
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_8_co2.csv',
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv', ##  Test sans surfactant (eau pure)
            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_vidange_8_co2.csv',
            '/home/stage/M2-Stage-Liphy/test_colonne_mai_remplissage_8_co2.csv'
            ]
fig, ax = plt.subplots()
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/100
    if '23gL' in file_path:
        db=pd.read_csv(file_path)
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse coloree 2.3 g/L SDS'
        else:
            label='Remplissage mousse coloree 2.3 g/L SDS'
    if '70cmc' in file_path:
        db=pd.read_csv(file_path)
        x=db.index/2
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse sans colorant 300 ml 70% CMC SDS'
        else:
            label='Remplissage mousse sans colorant 300ml 70% CMC SDS'
            print('the time max for 70% CMC avec moins de liquide est ', x.max())
            integral=np.trapz(y,x=x)
            print('The integral of the curve of 70 % CMC avec moins de liquide est ', integral)
            plt.fill_between(x, y, color='red', alpha=0.3)
    if 'sans' in file_path:
        if 'vidange' in file_path:
            label='Vidange sans mousse'
        else:
            label='Remplissage sans mousse'
    
    if '040324' in file_path:
        if 'vidange' in file_path:
            label='Vidange mousse coloree 5 g/L SDS'
        else:
            label='Remplissage mousse coloree 5 g/L SDS'
    if 'pure' in file_path:
        db=pd.read_csv(file_path)
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange sans mousse 300 ml eau pure'
        else:
            label='Remplissage sans mousse 300 ml eau pure'
    if 'mai' in file_path:
         db=pd.read_csv(file_path)
         y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        
         if 'vidange' in file_path:
             label='Vidange mousse sans colorant 450ml de liquide SDS 70% CMC'
         else:
            label='Remplissage mousse sans colorant 450ml de liquide SDS 70% CMC'
            integral=np.trapz(y, x=x)
            print('The time max for 450 ml is ', x.max())
            print('the integral of the curve of 450ml de liquide est ', integral)
            plt.fill_between(x, y, color='skyblue', alpha=0.3)
    percentage = int(file_path.split('_')[-2])
    ax.scatter(x,y,label=f'Test {label} {percentage*10} ml/min CO2', marker='o', s=1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)  
axin1 = inset_axes(ax, width='20%', height='20%', loc='center')
axin1.set_xlim(2500, 4000)
axin1.set_ylim(25, 45)
ax.indicate_inset_zoom(axin1)
mark_inset(ax, axin1, loc1=2, loc2=4, fc="none", ec="0.5")
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/100
    if '23gL' in file_path:
        db=pd.read_csv(file_path)
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse coloree 2.3 g/L SDS'
        else:
            label='Remplissage mousse coloree 2.3 g/L SDS'
    if '70cmc' in file_path:
        db=pd.read_csv(file_path)
        x=db.index/2
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse sans colorant 70% CMC SDS'
        else:
            label='Remplissage mousse sans colorant 70% CMC SDS'
            print('the time max for 70% CMC avec moins de liquide est ', x.max())
            integral=np.trapz(y,x=x)
            print('The integral of the curve of 70 % CMC avec moins de liquide est ', integral)
            plt.fill_between(x, y, color='red', alpha=0.3)
    if 'sans' in file_path:
        if 'vidange' in file_path:
            label='Vidange sans mousse'
        else:
            label='Remplissage sans mousse'
    
    if '040324' in file_path:
        if 'vidange' in file_path:
            label='Vidange mousse coloree 5 g/L SDS'
        else:
            label='Remplissage mousse coloree 5 g/L SDS'
    if 'pure' in file_path:
        db=pd.read_csv(file_path)
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
            integral=np.trapz(y, x=x)
            print('The time max for 450 ml is ', x.max())
            print('the integral of the curve of 450ml de liquide est ', integral)
            plt.fill_between(x, y, color='skyblue', alpha=0.3)
    percentage = int(file_path.split('_')[-2])
    axin1.scatter(x, y, marker='o', s=1)

axin2 = inset_axes(ax, width='20%', height='20%', loc='center right')
axin2.set_xlim(12250, 14250)
axin2.set_ylim(92, 100)
ax.indicate_inset_zoom(axin2)
mark_inset(ax, axin2, loc1=2, loc2=4, fc="none", ec="0.5")
for file_path in file_paths:
    db=pd.read_csv(file_path)
    x=db.index/2
    y=db['Media value concentration']/100
    if '23gL' in file_path:
        db=pd.read_csv(file_path)
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse coloree 2.3 g/L SDS'
        else:
            label='Remplissage mousse coloree 2.3 g/L SDS'
    if '70cmc' in file_path:
        db=pd.read_csv(file_path)
        x=db.index/2
        y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
        if 'vidange' in file_path:
            label='Vidange mousse sans colorant 70% CMC SDS'
        else:
            label='Remplissage mousse sans colorant 70% CMC SDS'
            print('the time max for 70% CMC avec moins de liquide est ', x.max())
            integral=np.trapz(y,x=x)
            print('The integral of the curve of 70 % CMC avec moins de liquide est ', integral)
            plt.fill_between(x, y, color='red', alpha=0.3)
    if 'sans' in file_path:
        if 'vidange' in file_path:
            label='Vidange sans mousse'
        else:
            label='Remplissage sans mousse'
    
    if '040324' in file_path:
        if 'vidange' in file_path:
            label='Vidange mousse coloree 5 g/L SDS'
        else:
            label='Remplissage mousse coloree 5 g/L SDS'
    if 'pure' in file_path:
        db=pd.read_csv(file_path)
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
            integral=np.trapz(y, x=x)
            print('The time max for 450 ml is ', x.max())
            print('the integral of the curve of 450ml de liquide est ', integral)
            plt.fill_between(x, y, color='skyblue', alpha=0.3)
    percentage = int(file_path.split('_')[-2])
    axin2.scatter(x, y, marker='o', s=1)
ax.set_xlabel('Temps (s)', fontsize=20)
ax.set_ylabel('Concentration $CO_2$ %', fontsize=20)
ax.set_title('Comparaison de concentration de $CO_2$ pour 2 volumes de liquides differents', fontsize=20)
ax.legend(loc='lower right', fontsize='x-large',markerscale=10)

    # plt.xlabel('Temps (s)')
    # plt.ylabel('Concentration $CO_2$ %')
    # plt.legend(loc='upper right', fontsize='x-large')
    # plt.title('Concentration $CO_2$ en function du temps colonne avec mousse SDS')
    # plt.legend(loc='lower right', fontsize='x-large',markerscale=10)
    # plt.show()
    
    
