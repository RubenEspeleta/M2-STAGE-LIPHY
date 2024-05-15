#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 14:14:08 2024

@author: stage
"""
import numpy as np
import matplotlib.pyplot as plt
longeur50ml_8=108  ## Longeur de 50ml de volume d'eau en pixels pour 80 ml/min
longeur50ml_15=112  ## Longeur de 50 ml de volume d'eau en pixels pour 150ml/min
longeur50ml_50=110 ## Longeur de 50ml de volume d'eau en pixels pour 500 ml/min
longeur50ml_100=111 ## Longeur de 50 ml de volume d'eau en pixels pour 1000 ml/min
theta_air_8=73.449
theta_air_15=81.034
theta_air_50=87.241
theta_air_100=88.751
#### CO2
longeur50ml_8_CO2=117
longeur50ml_15_CO2=112
longeur50ml_50_CO2=111
longeur50ml_100_CO2=110
theta_co2_8=68.259
theta_co2_15=80.879
theta_co2_50=86.722
theta_co2_100=88.475

Q_attendu=np.array([80, 150, 500, 1000])     ## Il manque 59.13 et 106

scaling_volume_air_80=50/longeur50ml_8
scaling_volume_air_150=50/longeur50ml_15
scaling_volume_air_500=50/longeur50ml_50
scaling_volume_air_1000=50/longeur50ml_100

scaling_volume_co2_80=50/longeur50ml_8_CO2
scaling_volume_co2_150=50/longeur50ml_15_CO2
scaling_volume_co2_500=50/longeur50ml_50_CO2
scaling_volume_co2_1000=50/longeur50ml_100_CO2

Q_air_8=np.tan(theta_air_8*np.pi/180)*60*scaling_volume_air_80
Q_air_15=np.tan(theta_air_15*np.pi/180)*60*scaling_volume_air_150
Q_air_50=np.tan(theta_air_50*np.pi/180)*60*scaling_volume_air_500
Q_air_100=np.tan(theta_air_100*np.pi/180)*60*scaling_volume_air_1000

Q_co2_8=np.tan(theta_co2_8*np.pi/180)*60*scaling_volume_co2_80
Q_co2_15=np.tan(theta_co2_15*np.pi/180)*60*scaling_volume_co2_150
Q_co2_50=np.tan(theta_co2_50*np.pi/180)*60*scaling_volume_co2_500
Q_co2_100=np.tan(theta_co2_100*np.pi/180)*60*scaling_volume_co2_1000

Q_experimentales_air=np.array([Q_air_8, Q_air_15, Q_air_50, Q_air_100])
Q_experimentales_air=np.round(Q_experimentales_air, 2)
Q_experimentales_co2=np.array([Q_co2_8, Q_co2_15, Q_co2_50, Q_co2_100])
Q_experimentales_co2=np.round(Q_experimentales_co2, 2)

slope_air, intercept_air=np.polyfit(Q_attendu, Q_experimentales_air, 1)
linear_fit_air=slope_air*Q_attendu+intercept_air
slope_co2, intercept_co2=np.polyfit(Q_attendu, Q_experimentales_co2, 1)
linear_fit_co2=slope_co2*Q_attendu+intercept_co2

## Set the identity function
y=Q_attendu

plt.figure()
ax1 = plt.gca()  # Get the current axes

# Scatter plot and linear fit
ax1.scatter(Q_attendu, Q_experimentales_air, label='air', color='blue')
ax1.plot(Q_attendu, linear_fit_air, color='blue', label=f'Linear Fit air (slope={slope_air:.2f})')
ax1.plot(Q_attendu, y, color='black', label='Identity (slope=1)')
# Set ticks for the primary y-axis
ax1.set_ylabel('Q experimentales air (ml/min)')
ax1.set_yticks(Q_experimentales_air)
ax1.set_yticklabels(Q_experimentales_air)
plt.legend()
plt.xlabel('Q attendu (ml/min)')
plt.grid(True)

# Create a second y-axis on the right side
ax2 = ax1.twinx()
ax2.set_ylabel('Q experimentales CO2 (ml/min)')  # Set label for the secondary y-axis
ax2.scatter(Q_attendu, Q_experimentales_co2, label='CO2', color='red')
ax2.plot(Q_attendu, linear_fit_co2, color='red', label=f'Linear Fit CO2 (slope={slope_co2:.2f})')
ax2.set_yticks(Q_experimentales_co2)
ax2.set_yticklabels(Q_experimentales_co2)
# Adjust the y-axis limits
y1_min, y1_max = ax1.get_ylim()
y2_min, y2_max = ax2.get_ylim()
y_min = min(y1_min, y2_min)
y_max = max(y1_max, y2_max)
ax1.set_ylim(y_min, y_max)
ax2.set_ylim(y_min, y_max)

plt.xticks(Q_attendu, Q_attendu)
plt.title('Valeurs experimentales debitmetres', fontsize=20)
plt.xlabel('Q attendu')
plt.legend()
plt.grid(True)
plt.show()