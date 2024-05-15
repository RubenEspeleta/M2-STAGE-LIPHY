#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:25:57 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt

####### METHODE NUMERO 1 ######################

Q1=80/60
Q2=150/60
Q3=500/60
Q4=1000/60
D=5.38
S=(np.pi*D**2)/4
h_experiments=np.array([0, 2.6, 2.6*2, 2.6*3 ])

### Air
t_experiment_air_8=np.array([45, 77, 108, 141])
t_experiment_air_8_sans_controleur=np.array([60, 95, 127, 159])
t_experiment_air_15=np.array([51, 69, 86, 104])
t_experiment_air_50=np.array([19, 24, 29, 34])
t_experiment_air_100=np.array([14, 17, 20, 22])

########### CO2

t_experiment_CO2_8=np.array([46, 92, 136, 180])
t_experiment_CO2_15=np.array([15, 31, 52, 74])
t_experiment_CO2_50=np.array([13, 20, 26, 32])
t_experiment_CO2_100=np.array([11, 14, 17, 20])


def plot_air_concentration(t_experiment, Q, title):
    t_air_teorique = np.arange(t_experiment[0], t_experiment[3], 1)
    h_air_teorique = Q * (t_air_teorique - t_experiment[0]) / S
    plt.plot(t_air_teorique, h_air_teorique, label='Theory h(t)=Qt/S')
    plt.scatter(t_experiment, h_experiments, label='Experimental data air')
    ## Linear fit
    m_air, b_air=np.polyfit(t_experiment, h_experiments, 1)
    linear_fit_air=m_air*t_experiment+b_air
    plt.plot(t_experiment, linear_fit_air, '--', color='blue', label=f'Linear Fit Air (Q=slope*S={m_air*S*60:.2f} ml/min)')
    
    plt.xlabel('time step (s)')
    plt.ylabel('h(t) air')
    plt.title(title)
    plt.legend()

def plot_CO2_concentration(t_experiment, Q, title):
    t_CO2_teorique = np.arange(t_experiment[0], t_experiment[3], 1)
    h_CO2_teorique = Q * (t_CO2_teorique - t_experiment[0]) / S
    plt.plot(t_CO2_teorique, h_CO2_teorique, label='Theory h(t)=Qt/S')
    plt.scatter(t_experiment, h_experiments, label='Experimental data CO2')
    
    ##Linear fit
    m_co2, b_co2=np.polyfit(t_experiment, h_experiments, 1)
    linear_fit_co2=m_co2*t_experiment+b_co2
    plt.plot(t_experiment, linear_fit_co2, '--', color='red', label=f'Linear Fit CO2 (Q=slope*S={m_co2*S*60:.2f} ml/min)')
    
    plt.xlabel('time step (s)')
    plt.ylabel('h(t) CO2')
    plt.title(title)
    plt.legend()

def linear_function(m, t, b):
    return  m*t + b

# Plotting air concentration
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plot_air_concentration(t_experiment_air_8, Q1, 'Debit air 80 ml/min')
plt.scatter(t_experiment_air_8_sans_controleur-15, h_experiments, label='Debit air 80 ml/min sans controleur de P')
plt.legend()
plt.subplot(2, 2, 2)
plot_air_concentration(t_experiment_air_15, Q2, 'Debit air 150 ml/min')
plt.subplot(2, 2, 3)
plot_air_concentration(t_experiment_air_50, Q3, 'Debit air 500 ml/min')
plt.subplot(2, 2, 4)
plot_air_concentration(t_experiment_air_100, Q4, 'Debit air 1000 ml/min')
plt.tight_layout()
plt.show()

# Plotting CO2 concentration
plt.figure(figsize=(10, 8))
plt.subplot(2, 2, 1)
plot_CO2_concentration(t_experiment_CO2_8, Q1, 'Debit CO2 80 ml/min')
plt.subplot(2, 2, 2)
plot_CO2_concentration(t_experiment_CO2_15, Q2, 'Debit CO2 150 ml/min')
plt.subplot(2, 2, 3)
plot_CO2_concentration(t_experiment_CO2_50, Q3, 'Debit CO2 500 ml/min')
plt.subplot(2, 2, 4)
plot_CO2_concentration(t_experiment_CO2_100, Q4, 'Debit CO2 1000 ml/min')
plt.tight_layout()
plt.show()