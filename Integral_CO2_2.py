#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 13:28:04 2024

@author: ruben
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Remplissage:
#file_path_eau='/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv'
#file_path_sans_mousse='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv'
file_path_eau='/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_vidange_8_co2.csv'
file_path_sans_mousse='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_8_co2.csv'

Q=80/60 
db_eau=pd.read_csv(file_path_eau)
db_sans_mousse=pd.read_csv(file_path_sans_mousse)
x1=db_sans_mousse.index*Q/2 
y1=(db_sans_mousse['Media value concentration']/100)*100/(db_sans_mousse['Media value concentration'].max()/100)
integral=np.trapz(y1,x=x1)
print('Integral au dessous de la courbe de remplissage sans mousse est: ', integral)
#plt.fill_between(x1, y1, color='red', alpha=0.3)


x_target=x1.max()
x2=db_eau.index*Q/2
y2=(db_eau['Media value concentration']/100)*100/(db_eau['Media value concentration'].max()/100)
x2_new=x2[x2<x_target]
y2_new=y2[:len(x2_new)]


integral_2=np.trapz(y2_new, x=x2_new)
print('Integral au dessous de la courbe de remplissage liquide sans surfactant est: ', integral_2)
#plt.fill_between(x2_new, y2_new, color='blue', alpha=0.3)
integral_diff=integral-integral_2
print('The difference of the integrals are: ', integral_diff)
plt.fill_between(x2_new, y2_new, y1[:len(x2_new)], where=(y1[:len(x2_new)] >=y2_new), color='blue', alpha=0.3)
plt.fill_between(x2_new, y2_new, y1[:len(x2_new)], where=(y1[:len(x2_new)] < y2_new), color='blue', alpha=0.3)
plt.scatter(x1, y1, label='Test 80 ml/min CO2 remplissage sans mousse', marker='o', s=1)
plt.scatter(x2, y2, label='Test 80 ml/min CO2 remplissage liquide sans surfactant', marker='o', s=1)
plt.xlabel('V=Qt')
plt.ylabel('Concentration CO$_2$ %')
plt.legend(fontsize='x-large',markerscale=10)
plt.show()

# file_paths=[#'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_remplissage_8_co2.csv', ## 70% CMC 300 ml SDS
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_160424_70cmc_vidange_8_co2.csv',
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_remplissage_8_co2.csv', ## Test 450 ml liquide 70% CMC SDS
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_450ml_SDS_70percentage_CMC/test_colonne_mousse_3D_450ml_liquide_vidange_8_co2.csv',
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_remplissage_23gL_8_co2.csv', ## Test 2.3 g/L SDS
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_vidange_23gL_8_co2.csv',
#            '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv', ### No mousse
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_8_co2.csv',
#            '/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_remplissage_8_co2.csv'] ### Test sans surfactant (eau pure)
#            #'/home/ruben/M2-THESE-RUBEN-LIPHY/Test_eau_pure/test_colonne_3D_eau_pure_vidange_8_co2.csv']
# Q=80/60
# for file_path in file_paths:
#     if 'remplissage' in file_path:
#         db=pd.read_csv(file_path)
#         x=(db.index*Q/2)
#         y=db['Media value concentration']/100
#         if 'sans' in file_path:
#             label='Remplissage sans mousse'
#             integral=np.trapz(y,x=x)
#             print(integral)
#             x_target=x.max()
#             plt.fill_between(x, y, color='red', alpha=0.3)
#         if 'pure' in file_path:
#             label='Remplissage eau pure'
#             y=(db['Media value concentration']/100)*100/(db['Media value concentration'].max()/100)
#             filtered_x=x[x<=x_target]
#             filtered_y=y[y:len(filtered_x)]
#             integral=np.trapz(filtered_y, filtered_x)
#             plt.fill_between(filtered_x, filtered_y, color='blue', alpha=0.3)
            
            
#     percentage = int(file_path.split('_')[-2])
#     plt.scatter(x, y, label=f'Test {label} {percentage * 10} ml/min CO2', marker='o', s=1)
#     plt.legend()
#     plt.xlabel('V = Qt')
#     plt.ylabel('Concentration CO$_2$ %')
#     plt.show()