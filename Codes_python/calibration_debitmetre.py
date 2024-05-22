#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:19:23 2024

@author: ruben
"""

### CALIBRATION DEBITMETRES
import numpy as np
import matplotlib.pyplot as plt

Q1=80/60
Q2=150/60
Q3=500/60
Q4=1000/60
D=5.38
S=(np.pi*D**2)/4
h_experiments=[0, 2.6, 2.6*2, 2.6*3 ]

### Air
t_experiment_air_8=[45, 77, 108, 141]
t_experiment_air_8_sans_controleur=[60, 95, 127, 159]
t_experiment_air_15=[51, 69, 86, 104]
t_experiment_air_50=[19, 24, 29, 34]
t_experiment_air_100=[14, 17, 20, 22]

#### 80 ml/min
t_air_teorique8=np.arange(t_experiment_air_8[0], 163, 1)
h_air_teorique8=Q1*(t_air_teorique8-t_experiment_air_8[0])/S

plt.figure()
plt.plot(t_air_teorique8, h_air_teorique8, label='Theory h(t)=Qt/S')
plt.scatter(t_experiment_air_8, h_experiments, label='Experimental data air 80 ml/min')
plt.scatter(t_experiment_air_8_sans_controleur, h_experiments, label='Experimental data air 80 ml/min sans controleur de P')
plt.xlabel('time step (s)')
plt.ylabel('h(t) air')
plt.title('Debit air 80 ml/min')
plt.legend()
plt.show()


#### 150 ml/min
t_air_teorique15=np.arange(t_experiment_air_15[0], 110, 1)
h_air_teorique15=Q2*(t_air_teorique15-t_experiment_air_15[0])/S


plt.figure()
plt.plot(t_air_teorique15, h_air_teorique15, label='h(t)=Qt/S')
plt.scatter(t_experiment_air_15, h_experiments, label='experimental data air')
plt.xlabel('time step (s)')
plt.ylabel('h(t) air')
plt.title('Debit air 150 ml/min')
plt.legend()
plt.show()


#### 500 ml/min

t_air_teorique50=np.arange(t_experiment_air_50[0], 50, 1)
h_air_teorique50=Q3*(t_air_teorique50-t_experiment_air_50[0])/S

plt.figure()
plt.plot(t_air_teorique50, h_air_teorique50, label='h(t)=Qt/S')
plt.scatter(t_experiment_air_50, h_experiments, label='experimental data air')
plt.xlabel('time step (s)')
plt.ylabel('h(t) air')
plt.title('Debit air 500 ml/min')
plt.legend()
plt.show()

#### 1000 ml/min
t_air_teorique100=np.arange(t_experiment_air_100[0], 30, 1)
h_air_teorique100=Q4*(t_air_teorique100-t_experiment_air_100[0])/S

plt.figure()
plt.plot(t_air_teorique100, h_air_teorique100, label='h(t)=Qt/S')
plt.scatter(t_experiment_air_100, h_experiments, label='experimental data air')
plt.xlabel('time step (s)')
plt.ylabel('h(t) air')
plt.title('Debit air 1000 ml/min')
plt.legend()
plt.show()


########### CO2

t_experiment_CO2_8=[46, 92, 136, 180]
t_experiment_CO2_15=[15, 31, 52, 74]
t_experiment_CO2_50=[13, 20, 26, 32]
t_experiment_CO2_100=[11, 14, 17, 20]

### 80 ml/min
t_CO2_teorique8=np.arange(t_experiment_CO2_8[0], 200, 1)
h_CO2_teorique8=Q1*(t_CO2_teorique8-t_experiment_CO2_8[0])/S


plt.figure()
plt.plot(t_CO2_teorique8, h_CO2_teorique8, label='theory h(t)=Qt/S')
plt.scatter(t_experiment_CO2_8, h_experiments, label='experimental data CO2')
plt.xlabel('time step (s)')
plt.ylabel('h(t) CO2')
plt.title('Debit CO2 80 ml/min')
plt.legend()
plt.legend()
plt.show()

### 150 ml/min
t_CO2_teorique15=np.arange(t_experiment_CO2_15[0], 80, 1)
h_CO2_teorique15=Q2*(t_CO2_teorique15-t_experiment_CO2_15[0])/S


plt.figure()
plt.plot(t_CO2_teorique15, h_CO2_teorique15, label='theory h(t)=Qt/S')
plt.scatter(t_experiment_CO2_15, h_experiments, label='experimental data CO2')
plt.xlabel('time step (s)')
plt.ylabel('h(t) CO2')
plt.title('Debit CO2 150 ml/min')
plt.legend()
plt.legend()
plt.show()

### 500 ml/min
t_CO2_teorique50=np.arange(t_experiment_CO2_50[0], 40, 1)
h_CO2_teorique50=Q3*(t_CO2_teorique50-t_experiment_CO2_50[0])/S


plt.figure()
plt.plot(t_CO2_teorique50, h_CO2_teorique50, label='theory h(t)=Qt/S')
plt.scatter(t_experiment_CO2_50, h_experiments, label='experimental data CO2')
plt.xlabel('time step (s)')
plt.ylabel('h(t) CO2')
plt.title('Debit CO2 500 ml/min')
plt.legend()
plt.legend()
plt.show()


### 1000 ml/min
t_CO2_teorique100=np.arange(t_experiment_CO2_100[0], 25, 1)
h_CO2_teorique100=Q4*(t_CO2_teorique100-t_experiment_CO2_100[0])/S


plt.figure()
plt.plot(t_CO2_teorique100, h_CO2_teorique100, label='theory h(t)=Qt/S')
plt.scatter(t_experiment_CO2_100, h_experiments, label='experimental data CO2')
plt.xlabel('time step (s)')
plt.ylabel('h(t) CO2')
plt.title('Debit CO2 1000 ml/min')
plt.legend()
plt.legend()
plt.show()