# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt
#### AIR ###
D=5.38
S=(np.pi*D**2)/4
scaling_volume_air=50/98
Q_air=np.tan(71.152*np.pi/180)*60*scaling_volume_air   ## Formule Cecile
Q_air_ruben=S*np.tan(71.152*np.pi/180)*60*2.6/98     ### Formule Ruben
print('Debit air measuré formule Cecile: ', Q_air)
print('Debit air measuré formule Ruben: ', Q_air_ruben)
## CO2 ###
scaling_volume_co2=50/94
Q_co2=np.tan(64.607*np.pi/180)*60*scaling_volume_co2  ## Formule Cecile
Q_co2_ruben=S*np.tan(64.607*np.pi/180)*60*2.6/94      ## Formule Ruben
print('Debit CO2 measuré formule Cecile: ', Q_co2)
print('Debit CO2 measuré formule Ruben: ', Q_co2_ruben)




#### Debitmètres inversés

## AIR
scaling_volume_air_inverse=50/96
Q_air_inverse=np.tan(75.981*np.pi/180)*60*scaling_volume_air_inverse   ## Formule Cecile
Q_air_ruben_inverse=S*np.tan(75.981*np.pi/180)*60*2.6/96  ## Formule Ruben
print('Debit air measuré debitmètre CO2 formule Cecile: ', Q_air_inverse)
print('Debit air measuré debitmètre CO2 formule Ruben: ', Q_air_ruben_inverse)

## CO2
scaling_volume_co2_inverse=50/98
Q_co2_inverse=np.tan(55.837*np.pi/180)*60*scaling_volume_co2_inverse   ## Formule Cecile
Q_co2_ruben_inverse=S*np.tan(55.837*np.pi/180)*60*2.6/98  ## Formule Ruben
print('Debit co2 measuré debitmètre air formule Cecile: ', Q_co2_inverse)
print('Debit co2 measuré debitmètre air formule Ruben: ', Q_co2_ruben_inverse)



theta_co2_8=68.259
longeur50ml_8_co2=117
scaling_volume_co2_80=50/longeur50ml_8_co2
Q_co2_8=np.tan(theta_co2_8*np.pi/180)*60*scaling_volume_co2_80

plt.figure()
plt.scatter(59.13, Q_co2_inverse, label='Débit mesuré avec débitmètre air', marker='^', color='blue')
plt.scatter(80, Q_co2, label='Débit mesuré dernière test', marker='D', color='blue')
plt.scatter(80, Q_co2_8, label='Débit mesuré test ancien', marker='X', color='blue')

Q_attendu=np.array([59.13, 80])
y=Q_attendu
plt.plot(Q_attendu, y, label='Idendité')
plt.xticks(Q_attendu, Q_attendu)
plt.ylabel('Q measuré (ml/min)', fontsize=20)
plt.xlabel('Q attendu (ml/min)', fontsize=20)
plt.legend()
plt.title('Débit CO mesuré (ml/min)', fontsize=20)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.show()

plt.figure()
longeur50ml_8=108 
theta_air_8=73.449
scaling_volume_air_80=50/longeur50ml_8
Q_air_8=np.tan(theta_air_8*np.pi/180)*60*scaling_volume_air_80
plt.scatter(80, Q_air, label='Débit mesuré dernière test', marker='D', color='red')
plt.scatter(106, Q_air_inverse, label='Débit mesuré avec débitmètre CO2', marker='^', color='red')
plt.scatter(80, Q_air_8, label='Débit mesuré test ancien', marker='X', color='red')
Q_attendu=np.array([80, 106])
y=Q_attendu
plt.plot(Q_attendu, y, label='Idendité')
plt.xticks(Q_attendu, Q_attendu)
plt.ylabel('Q measuré (ml/min)', fontsize=20)
plt.xlabel('Q attendu (ml/min)', fontsize=20)
plt.legend()
plt.title('Débit air mesuré (ml/min)', fontsize=20)
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)
plt.show()