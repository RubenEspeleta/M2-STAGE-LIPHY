#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:12:14 2024

@author: stage
"""

import numpy as np
import matplotlib.pyplot as plt

def solve_advection_diffusion(v, D, f, L, T, nx, nt):
    """
    Solve the advection-diffusion equation numerically.
    
    Parameters:
        v (float): Velocity constant.
        D (float): Diffusion constant.
        f (callable): Function f(t) representing the boundary condition at x=0.
        L (float): Length of the spatial domain.
        T (float): Total time to simulate.
        nx (int): Number of spatial grid points.
        nt (int): Number of time steps.
        
    Returns:
        x (numpy array): Spatial grid points.
        t (numpy array): Time steps.
        c (numpy array): Solution matrix c(x, t).
    """
    dx = L / (nx - 1)
    dt = T / nt
    x = np.linspace(0, L, nx)
    t = np.linspace(0, T, nt)
    
    c = np.zeros((nx, nt))
    
    for j in range(1, nt):
        c[0, j] = f(t[j])
    
    for j in range(0, nt - 1):
        for i in range(1, nx - 1):
            c[i, j + 1] = c[i, j] + dt * (
                -v * (c[i + 1, j] - c[i - 1, j]) / (2 * dx)
                + D * (c[i + 1, j] - 2 * c[i, j] + c[i - 1, j]) / (dx ** 2)
            )
        c[-1, j + 1] = 0  # Boundary condition at x = infinity (approximated by the end of the domain)
    
    return x, t, c

# Example usage
Q=80/(60*1000**2)    ## Debit imposé en m3/s
A=0.125*0.09        ## Area de la section transversale de la colonne en m2
v=Q/A
D = 0.01
L = 10.0
T = 2.0
nx = 101
nt = 200

# Define the boundary condition function f(t)
def f(t):
    return t ** 6  # Polynomial of degree 6

x, t, c = solve_advection_diffusion(v, D, f, L, T, nx, nt)

# Plotting the results
plt.figure(figsize=(8, 6))
for i in range(0, nt, nt // 10):
    plt.plot(x, c[:, i], label=f't={t[i]:.2f}')
plt.xlabel('x')
plt.ylabel('c(x, t)')
plt.legend()
plt.title('Solution to the Advection-Diffusion Equation')
plt.show()