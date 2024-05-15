#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:32:09 2024

@author: ruben
"""

import numpy as np
import matplotlib.pyplot as plt
# tension_surface_200ppm=np.array([36.083, 40.389, 32.5, 35.86])
# tension_surface_100ppm=np.array([44.269, 46.685, 47.633, 50.243, 52.6, 50.64])
# tension_surface_50ppm=np.array([41.634, 37.01, 48.669])
tension_surface_10ppm=np.array([69.73, 69.68, 69.57, 69.72, 69.42])
tension_surface_50ppm=np.array([40.6, 41.275, 46.36, 42.365, 43.81])
tension_surface_100ppm=np.array([43.27, 43.145, 42.374, 43.127, 41.26])
tension_surface_150ppm=np.array([31.51,  37.66, 36.38, 36.41, 36.69])
tension_surface_200ppm=([31.34, 34.46, 34.15, 34.14, 30.714])
tension_surface_300ppm=([34.14, 30.25, 30.76, 32.81, 31.175])
tension_surface_400ppm=([28.02, 28.6, 31.02, 28.82, 28.1 ])
tension_surface_500ppm=([27.04, 28.025, 28.37, 29.15, 28.09])
tension_surface_1000ppm=np.array([28.83, 28.02, 28.83, 26.92, 27.99])
median_values=np.array([np.mean(tension_surface_10ppm), np.mean(tension_surface_50ppm), np.mean(tension_surface_100ppm), np.mean(tension_surface_150ppm), np.mean(tension_surface_200ppm), np.mean(tension_surface_300ppm), np.mean(tension_surface_400ppm), np.mean(tension_surface_500ppm), np.mean(tension_surface_1000ppm)])
concentration=np.array([10, 50, 100, 150, 200, 300, 400, 500, 1000])
std_devs=np.array([np.std(tension_surface_10ppm, ddof=1), np.std(tension_surface_50ppm, ddof=1), np.std(tension_surface_100ppm, ddof=1), np.std(tension_surface_150ppm, ddof=1), np.std(tension_surface_200ppm, ddof=1), np.std(tension_surface_300ppm, ddof=1), np.std(tension_surface_400ppm, ddof=1), np.std(tension_surface_500ppm, ddof=1), np.std(tension_surface_1000ppm, ddof=1)])

# plt.errorbar(concentration, median_values, yerr=std_devs, fmt='x', markersize=10, capsize=5, capthick=2, ecolor='red', label='Error bars')
# plt.scatter(concentration, median_values, marker='x', s=100, color='black', label='Tension surface moyenne')
# plt.xlabel('Concentration log scale (ppm)', fontsize=12)
# plt.ylabel('Surface tension (mN/m)', fontsize=12)
# plt.title('Tension surface vs  log concentration Aspiro', fontsize=14)
# plt.legend(fontsize=12)
# plt.grid(True)
# plt.show()

plt.plot(concentration, median_values, marker='o', color='black', label='Moyenne tension surface')
plt.fill_between(concentration, median_values - std_devs, median_values + std_devs, color='lightgrey', label='Error')
plt.xlabel('Concentration log scale (ppm)', fontsize=20)
plt.ylabel('Tension surface (mN/m)', fontsize=20)
#plt.xscale('log')
plt.title('Surface Tension vs. log Concentration Aspiro', fontsize=20)
plt.grid(True)
plt.legend(fontsize=12)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show()