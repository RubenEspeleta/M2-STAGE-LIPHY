#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:05:22 2024

@author: ruben
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

# Define file paths
file_paths = [
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_vidange_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_vidange_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_horizontal_vidange_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test2_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test2_vidange_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test3_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test3_vidange_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_vidange_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_vidange_100_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_vidange_50_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_test4_vidange_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_3d_test2_15_co2.csv',            #### Avec la mousse
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_3d_test2_vidange_15_co2.csv',
    # '/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_3D_8_co2.csv',
      #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_remplissage_8_co2.csv',
      #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_040324_vidange_8_co2.csv',
     #'/home/ruben/M2-THESE-RUBEN-LIPHY/test_colonne_sans_mousse_remplissage_8_co2.csv',
     '/home/stage/M2-Stage-Liphy/test_colonne_sans_mousse_vidange_8_co2.csv',
     #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_remplissage_23gL_8_co2.csv',
     #'/home/ruben/M2-THESE-RUBEN-LIPHY/Tests_colonne_mousse_3D/test_colonne_mousse_3D_coloree_100424_vidange_23gL_8_co2.csv'
]

# Define CO2 vidange function
def func(x, a, b):
    return a * np.exp(-b * x)

# Define CO2 remplissage function
def func2(x, a, b, c, phi):
    return a*(1-np.exp(-b*x+phi))+c #a / (1 + ((a - c) / c) * np.exp(-b * x + phi))


epsilon=0.1
# Create plot
plt.figure(figsize=(10, 6))

# Plot data and fit curve
for file_path in file_paths:
    db = pd.read_csv(file_path)
    xdata = db.index / 2
    ydata=db['Media value concentration']/100
    significant_indices_1=np.where(np.abs(ydata-ydata[0])>epsilon)[0]
    significant_indices_2=np.where(np.abs(ydata-ydata[len(ydata)-1])>epsilon)[0]
    significant_indices=np.intersect1d(significant_indices_1, significant_indices_2)
    
    if 'vidange' in file_path:
        popt, pcov = curve_fit(func, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
        label = 'vidange'
        fit_func = func
        if 'sans' in file_path:
            label='vidange sans mousse'
        if '23gL' in file_path:
            label='vidange 2.3 g/L SDS'
    else:
        popt, pcov = curve_fit(func2, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
        label = 'remplissage'
        fit_func = func2
        if 'sans' in file_path:
            label='remplissage sans mousse'
        if '23gL' in file_path:
            label='remplissage 2.3 g/L'
    # Extract CO2 percentage from file name
    percentage = int(file_path.split('_')[-2])
    plt.scatter(xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices], label=f'Test {label} {percentage*10} ml/min CO2', marker='o', s=1)
    plt.plot(xdata[significant_indices]-np.min(xdata[significant_indices]), fit_func(xdata[significant_indices]-np.min(xdata[significant_indices]), *popt), label=f'fit {label} {percentage*10} ml/min CO2: a={popt[0]:.5f}, b={popt[1]:.5f}')

plt.xlabel('Pas de temps (s)')
plt.ylabel('Concentration $CO_2$ %')
plt.legend()
plt.title('Concentration $CO_2$ en function du temps pour differents débits')
plt.show()

#####################################
# Create plot of non dimensional values for vidange du CO2
# plt.figure(figsize=(10,6))
# for file_path in file_paths:
#     db=pd.read_csv(file_path)
#     percentage=int(file_path.split('_')[-2])
#     xdata=db.index/2
#     ydata=db['Media value concentration']/100
#     significant_indices_1=np.where(np.abs(ydata-ydata[0])>epsilon)[0]
#     significant_indices_2=np.where(np.abs(ydata-ydata[len(ydata)-1])>epsilon)[0]
#     significant_indices=np.intersect1d(significant_indices_1, significant_indices_2)
#     if 'vidange' in file_path:
#         popt, pconv = curve_fit(func, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
#         label= 'vidange'
#         fit_func=func
#         if 'sans' in file_path:
#             label='vidange sans mousse'
#         plt.plot((xdata[significant_indices]-np.min(xdata[significant_indices]))*popt[1], ydata[significant_indices]/100, label=f'Test {label} {percentage*10} ml/min CO2')
#     else:
#         popt, pcov = curve_fit(func2, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
#         label='Remplissage'
#         fit_func=func2
#         if 'sans' in file_path:
#             label='remplissage sans mousse'
#         plt.plot((xdata[significant_indices]-np.min(xdata[significant_indices]))*popt[1], ydata[significant_indices]/100, label=f'Test{label} {percentage*10} ml/min CO2')
# plt.xlabel(r't/$\tau$', fontsize=20)
# plt.ylabel('$Concentration CO2/Concentration initiale$', fontsize=15)
# plt.legend()
# plt.title('Concentration $CO_2$ comme function du temps adimensionnel', fontsize=20)
# plt.xticks(fontsize=12)
# plt.yticks(fontsize=15)
# plt.show()




# ######################################################################################################################
# ######################################################################################################################
# ## Create a plot to compare the Q obtained from the curves with Q experimentales debitmetres
# plt.figure(figsize=(10,6))
# D=5.38
# S=(np.pi*D**2)/4
# VT=np.array([1,1,1])*12.5*9*70
# VT2=np.array([1,1,1])*12.5*9*70
# ### AIR
# longeur50ml_15=112  ## Longeur de 50 ml de volume d'eau en pixels pour 150ml/min
# longeur50ml_50=110 ## Longeur de 50ml de volume d'eau en pixels pour 500 ml/min
# longeur50ml_100=111 ## Longeur de 50 ml de volume d'eau en pixels pour 1000 ml/min
# theta_air_15=81.034
# theta_air_50=87.241
# theta_air_100=88.751
# #### CO2
# longeur50ml_15_CO2=112
# longeur50ml_50_CO2=111
# longeur50ml_100_CO2=110
# theta_co2_15=80.879
# theta_co2_50=86.722
# theta_co2_100=88.475

# Q_air_15=(S*np.tan(theta_air_15*np.pi/180)*2.6*60)/longeur50ml_15
# Q_air_50=(S*np.tan(theta_air_50*np.pi/180)*2.6*60)/longeur50ml_50
# Q_air_100=(S*np.tan(theta_air_100*np.pi/180)*2.6*60)/longeur50ml_100



# Q_co2_15=(S*np.tan(theta_co2_15*np.pi/180)*2.6*60)/longeur50ml_15_CO2
# Q_co2_50=(S*np.tan(theta_co2_50*np.pi/180)*2.6*60)/longeur50ml_50_CO2
# Q_co2_100=(S*np.tan(theta_co2_100*np.pi/180)*2.6*60)/longeur50ml_100_CO2


# Q_experimentales_air=np.array([Q_air_100, Q_air_50, Q_air_15])
# Q_experimentales_air=np.round(Q_experimentales_air, 2)
# Q_experimentales_co2=np.array([Q_co2_100, Q_co2_50, Q_co2_15])
# Q_experimentales_co2=np.round(Q_experimentales_co2, 2)
# i=-1
# j=-1
# my_array=np.zeros(3)
# my_array2=np.zeros(3)
# for file_path in file_paths:
#     db=pd.read_csv(file_path)
#     xdata=db.index/2
#     ydata=db['Media value concentration']/100
#     significant_indices_1=np.where(np.abs(ydata-ydata[0])>epsilon)[0]
#     significant_indices_2=np.where(np.abs(ydata-ydata[len(ydata)-1])>epsilon)[0]
#     significant_indices=np.intersect1d(significant_indices_1, significant_indices_2)
#     if 'vidange' in file_path:
#         i=i+1
#         popt, pconv = curve_fit(func, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
#         label= 'vidange'
#         fit_func=func
#         my_array[i]=VT[i]*popt[1]*60
#         plt.scatter(VT[i]*popt[1]*60, Q_experimentales_air[i], label='vidange (debit air)')
#     else:
#         j=j+1
#         popt, pconv = curve_fit(func2, xdata[significant_indices]-np.min(xdata[significant_indices]), ydata[significant_indices])
#         label= 'remplissage'
#         fit_func=func2
#         my_array2[j]=VT2[j]*popt[1]*60
#         plt.scatter(VT2[j]*popt[1]*60, Q_experimentales_co2[j], label='remplissage (debit co2)')   

# slope_air, intercept_air=np.polyfit(my_array, Q_experimentales_air, 1)
# linear_fit_air=slope_air*my_array+intercept_air
# slope_co2, intercept_co2=np.polyfit(my_array2, Q_experimentales_co2, 1)
# linear_fit_co2=slope_co2*my_array2+intercept_co2
# plt.plot(my_array2,linear_fit_co2, label=f'Linear Fit co2 (slope={slope_co2:.2f})')
# plt.plot(my_array,linear_fit_air, label=f'Linear Fit air (slope={slope_air:.2f})')
# plt.xticks(np.round(my_array, 2),np.round(my_array, 2) )
# plt.yticks(Q_experimentales_air, Q_experimentales_air)
# plt.xlabel(r'Q experimental $V_T$/ $\tau$ (ml/min)')
# plt.ylabel('Q mesuré debitmetres (ml/min)')
# plt.legend()
# plt.show()

# ##### Comparaison des volumes######
# ### Remplissage:
# plt.figure()
# Taus_remplissage=([398, 787, 2439])
# Q=([1000, 500, 150])
# V_remplissage=np.round(Q_experimentales_co2*Taus_remplissage/60, 2)
# y=np.array([1,1,1])*7875
# plt.plot(Q, y)
# plt.scatter(Q, V_remplissage, label='Volumen remplissage')


