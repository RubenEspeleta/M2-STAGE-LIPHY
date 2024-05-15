# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
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
