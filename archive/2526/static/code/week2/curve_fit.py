#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 13:52:57 2020

@author: chris
"""
import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# The data
x = np.arange(0,2,0.1)
y = np.array([1,2,4,5,6,6,5,5,4,3,2,0,-1,-1,-3,-2,-4,-3,-1,0])

# Plot the data
plt.plot(x,y,'x', markersize=20)

# function to define the fit parameters
def func(x, a, b, c): 
    return a * np.sin(b*x) + c

# Print the best fit parameters
param, param_cov = opt.curve_fit(func, x, y) 
print(param)

# Construct a function to fit
x1 = np.linspace(0,2,100)
y1 = func(x1,param[0],param[1],param[2])

plt.plot(x1,y1,'-')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(['Data','Best fit f(x)=$a\sin(bx)+c$'],loc=3)

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="curve_fit.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS2805-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)


