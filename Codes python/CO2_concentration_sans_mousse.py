#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 15:48:30 2024

@author: ruben
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

file_path='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2.csv'
file_path2='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage.csv'
file_path3='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2-2.csv'
file_path4='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage-2.csv'
file_path5='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_50_co2.csv'
file_path6='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage-50.csv'
file_path7='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2-3.csv'
file_path8='/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_co2-vidage-3.csv'
file_path9='/home/ruben/M2-THESE-RUBEN-LIPHY/test-colonne-3d-co2-15-sans-mousse.csv'
file_path10='/home/ruben/M2-THESE-RUBEN-LIPHY/test-colonne-3d-co2-15-sans-mousse-vidange.csv'

db=pd.read_csv(file_path)
db2=pd.read_csv(file_path2)
db3=pd.read_csv(file_path3)
db4=pd.read_csv(file_path4)
db5=pd.read_csv(file_path5)
db6=pd.read_csv(file_path6)
db7=pd.read_csv(file_path7)
db8=pd.read_csv(file_path8)
db9=pd.read_csv(file_path9)
db10=pd.read_csv(file_path10)

### CO2 VIDANGE FUNCTION """"
def func(x, a, b, c, phi):
    return a*np.exp(-b*x+phi)+c


#### CO2 REMPLISSAGE ####
def func2(x, a, b, c, phi):
    return a/(1+((a-c)/c)*np.exp(-b*x+phi))                             ######   a-a*np.exp(-b*x+phi)+c



### CO2 VIDANGE FIT 
xdata=db8.index/2   #### TEST 4 VIDANGE
popt, pcov=curve_fit(func, xdata, db8['Media value concentration']/100)#, bounds=(0, [75., 1., 0.5]))
popt


xdata2=db2.index/2  ### TEST 1 VIDANGE
popt2, pcov2=curve_fit(func, xdata2, db2['Media value concentration']/100)#, bounds=(0, [75., 1., 0.5]))
popt2

xdata3=db4.index/2   ### TEST 2 VIDANGE
popt3, pcov3=curve_fit(func, xdata3, db4['Media value concentration']/100)#, bounds=(0, [75., 1., 0.5]))
popt3

xdata4=db6.index/2   ### TEST 3 VIDANGE
popt4, pcov4=curve_fit(func, xdata4, db6['Media value concentration']/100)#, bounds=(0, [75., 1., 0.5]))
popt4

xdata10=db10.index/2   ### TEST 5 VIDANGE
popt10, pcov10=curve_fit(func, xdata10, db10['Media value concentration']/100)#, bounds=(0, [75., 1., 0.5]))
popt10

#### CO2 REMPLISSAGE FIT
xdata5=db7.index/2   #### TEST 4 REMPLISSAGE
popt5, pcov5=curve_fit(func2, xdata5, db7['Media value concentration']/100)
popt5

xdata6=db.index/2   ### TEST 1 REMPLISSAGE
popt6, pcov6=curve_fit(func2, xdata6, db['Media value concentration']/100)
popt6

xdata7=db3.index/2  ### TEST 2 REMPLISSAGE
popt7, pcov7=curve_fit(func2, xdata7, db3['Media value concentration']/100)
popt7

xdata8=db5.index/2  ### TEST 3 REMPLISSAGE 50% CO2
popt8, pcov8=curve_fit(func2, xdata8, db5['Media value concentration']/100)
popt8

xdata9=db9.index/2  ### TEST 5 REMPLISSAGE 15% CO2
popt9, pcov9=curve_fit(func2, xdata9, db9['Media value concentration']/100)
popt9

###PLOTTING

plt.figure()
plt.scatter(db.index/2, db['Media value concentration']/100, label='Test_1 concentration', marker='o', s=2)
plt.scatter(db2.index/2, db2['Media value concentration']/100, label = 'Test_1 emptying', marker='o', s=2)
plt.plot(xdata2, func(xdata2, *popt2), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt2))
plt.plot(xdata6, func2(xdata6, *popt6), 'b-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt6))
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.show()



plt.figure()
plt.scatter(db5.index/2, db5['Media value concentration']/100, label='Test_3 concentration', marker='o', s=2)
plt.scatter(db6.index/2, db6['Media value concentration']/100, label='Test_3 emptying', marker='o', s=2)
plt.plot(xdata4, func(xdata4, *popt4), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f  ' % tuple(popt4))
plt.plot(xdata8, func2(xdata8, *popt8), 'b-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f  ' % tuple(popt8))
plt.legend()
plt.show()


plt.figure()
plt.scatter(db3.index/2, db3['Media value concentration']/100, label='Test_2 concentration', marker='o', s=2)
plt.scatter(db4.index/2, db4['Media value concentration']/100, label='Test_2 emptying', marker='o', s=2)
plt.plot(xdata3, func(xdata3, *popt3), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f  ' % tuple(popt3))
plt.plot(xdata7, func2(xdata7, *popt7), 'b-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt7))
plt.xlabel('timestep')
plt.ylabel('Concentration of CO2')
plt.legend()
plt.show()


plt.figure()
plt.scatter(db7.index/2, db7['Media value concentration']/100, label='Test_4 concentration', marker='o', s=2)
plt.scatter(db8.index/2, db8['Media value concentration']/100, label='Test_4 emptying', marker='o', s=2)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt))
plt.plot(xdata5, func2(xdata5, *popt5), 'b-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt5))
plt.xlabel('Timestep')
plt.ylabel('Concentration CO2')
plt.legend()
plt.show()
    
plt.figure()
plt.scatter(db9.index/2, db9['Media value concentration']/100, label='Test_5 remplissage', marker='o', s=2)
plt.scatter(db10.index/2, db10['Media value concentration']/100, label='Test_5 vidange', marker='o', s=2)
plt.plot(xdata10, func(xdata10, *popt10), 'r-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt10))
plt.plot(xdata9, func2(xdata9, *popt9), 'b-', label='fit: a=%5.5f, b=%5.5f, c=%5.5f, phi=%5.5f ' % tuple(popt9))
plt.xlabel('Timestep')
plt.ylabel('Concentration CO2')
plt.legend()
plt.show()
