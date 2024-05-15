#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 15:16:10 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#file_path = '/home/ruben/M2-THESE-RUBEN-LIPHY/humidite_temperature_100_et_50_co2_vidange_et_remplissage.csv'
#file_path='/media/ruben/RUBEN/16-04-24 test mousse 3D 70percentage CMC sds sans colorant/humidite_temperature_dedans_colonne.csv'
file_path='/media/ruben/RUBEN/23-04-24 test mousse 3D 70cmc 450ml solution/humidite_temperature_dedans.csv'
db = pd.read_csv(file_path)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (min)')
ax1.set_ylabel('Humidity (%)', color=color)
ax1.plot(db.index, db['%HR'], color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('Temperature (°C)', color=color)  
ax2.plot(db.index, db['TIME'], color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Temperature et humidite pendant le remplissage et vidange au débit 80 ml/min 450 ml liquide 70% CMC', fontsize=15)
plt.xticks(fontsize=20)
plt.show()