#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 16:47:30 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

### Experience 70% CMC du SDS ###

file_path='/home/stage/M2-Stage-Liphy/Points_1_partie_image.csv'
file_path_2='/home/stage/M2-Stage-Liphy/Points_2_partie_image.csv'
file_path_3='/home/stage/M2-Stage-Liphy/Points_countour_image_450ml.csv'
db=pd.read_csv(file_path)
db2=pd.read_csv(file_path_2)
db3=pd.read_csv(file_path_3)
h0=np.max(db['y'])
y=db['y']/48.3
x=db['x']*50
y2=(db2['y']+h0)/48.3
x2=db2['x']*50
x3=db3['x']*50
y3=db3['y']/50

plt.figure()
plt.scatter(x,y, s=1, color='blue')
plt.scatter(x2,y2,s=1, color='blue')
plt.xlabel('Temps (s)', fontsize=20)
plt.ylabel('Hauteur mousse (cm)', fontsize=20)
plt.title('Hauteur de mousse en fonction du temps 70% de la CMC du SDS', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax=plt.gca()
ax.annotate('Injection du CO2', xy=(1200,15.5), xytext=(1200, 10), arrowprops=dict(facecolor='black', arrowstyle='simple', connectionstyle='arc3, rad=-0.2'))
ax.annotate('Injection air', xy=(19000,14), xytext=(19000, 10), arrowprops=dict(facecolor='black', arrowstyle='simple', connectionstyle='arc3, rad=-0.2'))
plt.show()

plt.figure()
plt.scatter(x3,y3, s=1)
plt.xlabel('Temps (s)', fontsize=20)
plt.ylabel('Hauteur mousse (cm)', fontsize=20)
plt.title('Hauteur de mousse en fonction du temps 450 ml 70% de la CMC du SDS', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
ax=plt.gca()
ax.annotate('Injection du CO2', xy=(7400,10), xytext=(10000, 5), arrowprops=dict(facecolor='black', arrowstyle='simple', connectionstyle='arc3, rad=-0.2'))
ax.annotate('Injection air', xy=(21482,6), xytext=(25000, 2), arrowprops=dict(facecolor='black', arrowstyle='simple', connectionstyle='arc3, rad=-0.2'))
plt.show()

### Experience 70% CMC du SDS avec 450 ml de solution




