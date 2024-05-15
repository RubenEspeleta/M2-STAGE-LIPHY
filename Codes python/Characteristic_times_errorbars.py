#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 09:39:51 2024

@author: ruben
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
debit=np.array([15, 50, 100])
data_remplissage={'Test': [1,2,3,4,5],
                  'Tau': [48.4, 38.88, 92.6, 40.33, 450.45],
                  'debit': [100, 100, 50, 100, 15]}
df=pd.DataFrame(data_remplissage)

data_vidange={'Test': [1,2,3,4,5],
                  'Tau': [383.141, 383.141, 769.23, 398.4, 2631.578],
                  'debit': [100, 100, 50, 100, 15]}

df2=pd.DataFrame(data_vidange)

# for i in debit:
#     subset_df=df[df['debit']==i]
    
#     plt.scatter(subset_df['Test'], subset_df['Tau'], label=f'debit {i}')

# plt.xlabel('Test')
# plt.ylabel('Tau')
# plt.title('Tau values for different debit values')
# plt.legend()
# plt.show()

plt.figure()
for test in df['Test'].unique():
    subset_df = df[df['Test'] == test]
    #plt.scatter(subset_df['debit'], subset_df['Tau'], marker='o', label=f'Test {test}')
    plt.errorbar(subset_df['debit'], subset_df['Tau'], yerr=subset_df['Tau']*0.1, fmt='o', capsize=5, label=f'Test {test}')


plt.xlabel('Debit (% $CO_2$)')
plt.ylabel(r'$\tau$ (s)')
plt.title(r'$\tau$ values for different tests at various debit levels', fontsize=20)
plt.legend()
plt.xticks(debit)
# Display the plot
plt.show()

plt.figure()
for test in df2['Test'].unique():
    subset_df2=df2[df2['Test'] == test]
    plt.errorbar(subset_df2['debit'], subset_df2['Tau'], yerr=subset_df2['Tau']*0.1, fmt='o', capsize=5, label=f'Test {test}')

# Adding labels and legend
plt.xlabel('Debit ($CO_2$)')
plt.ylabel(r'$\tau$ (s)')
plt.title(r'$\tau$ values for different tests at various debit levels', fontsize=20)
plt.legend()
plt.xticks(debit)
# Display the plot
plt.show()