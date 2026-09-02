#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sraight line fit  to data points
"""

import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Data points
x = [1,2,3,4]
y = [5.5,7.0,9.5,9.9]

# Fit a*x+b
p = np.polyfit(x, y, 1)

# Add the best fit
x1 = np.linspace(0,5,100)
y1 = p[0]*x1+p[1]

# Plot
plt.plot(x,y,'x', markersize=24)
plt.plot(x1,y1)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["Data points","$f(x)=ax+b$"],loc=4)

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="linear_fit.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS2805-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)




