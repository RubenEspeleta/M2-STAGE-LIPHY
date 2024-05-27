#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:18:05 2024

@author: stage
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
file_path='/home/stage/M2-Stage-Liphy/test_colonne_mai_remplissage_8_co2.csv'


Q=80/(60*(1000**2)) 

db=pd.read_csv(file_path)
x=db.index/2
y=db['Media value concentration']/100
y_ppm=y*10000
y_gL=(y_ppm*0.001*1000*(6.022*(10**23)))/44        ### Concentration in particules par m3



integral=np.trapz(y_gL, x=x)

rectangle=x.max()*y_gL.max()
area=rectangle-integral

particules=Q*integral

volume=(particules*24.79/(6.022*(10**23)))
print('The time max for 450 ml is ', x.max())
print('The volume of the column is: ', volume)
plt.scatter(x, y_ppm, label='Remplissage', marker='o', s=1)
plt.show()
