#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:59:18 2024

@author: ruben
"""

import pandas as pd
import matplotlib.pyplot as plt
file_path='/home/ruben/M2-THESE-RUBEN-LIPHY/11-03-24-deuxieme-aiguille-hydrophobe-bullage/Results-bulles.csv'
file_path2='/home/ruben/M2-THESE-RUBEN-LIPHY/Results_tailles_des_bulles_1-7mm-aiguille.csv'
#file_path2='/home/ruben/M2-THESE-RUBEN-LIPHY/Results_tailles_des_bulles_1-35mm-aiguille-1fps.csv'
db=pd.read_csv(file_path)
db2=pd.read_csv(file_path2)

selected_indices=[5, 7, 11, 13, 18, 20, 25, 28, 32, 33, 34, 42, 47, 50, 53, 56, 59, 63, 65, 70, 71, 74, 76, 79, 83, 85, 89, 90, 96, 97, 99, 103, 108, 109]
filtered_db=db.loc[db.index.isin(selected_indices)]
selected_areas=filtered_db['Area']

selected_indices2=[4, 7, 8, 9, 10, 12, 15, 16, 17, 19, 23, 24, 25, 28, 29, 34, 36, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53, 59, 60, 63, 64, 65, 68, 70, 71, 76, 77, 79, 82, 83, 89, 92, 93, 94, 95, 96, 97, 100, 104, 105, 108, 109, 110, 112, 116, 117, 118, 127, 128, 131, 132, 137, 138, 142, 143, 147, 151, 153, 162, 163, 167, 168, 169, 170, 171, 174, 179, 182, 183, 186, 187, 191, 192, 197, 200, 203, 204, 207, 214, 216, 217, 219, 220, 221, 223, 224, 225]
filtered_db2=db2.loc[db2.index.isin(selected_indices2)]
selected_areas2=filtered_db2['Area']

plt.figure()
plt.scatter(selected_indices, selected_areas, label='Area bulles aiguille hydrophobe')
plt.axhline(selected_areas.mean(), color='red', linestyle='dashed', label='mean area bulles aiguille hypdrophobe 2')
plt.legend()
plt.show()

plt.figure()
plt.scatter(selected_indices2, selected_areas2, label='Area bulles aiguille 1,7 mm')
plt.axhline(selected_areas2.mean(), color='blue', linestyle='dashed', label='mean area bulles 1.7 mm')
plt.legend()
plt.show()
