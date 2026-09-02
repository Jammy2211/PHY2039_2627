#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Polhynomial fits to data points
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


# Plot data points
plt.plot(x,y,'x', markersize=24)


x1 = np.linspace(0,5,100)

# Add best fit linear, quadratic, cubic
for i in range(1,4):
    p = np.polyfit(x, y, i)
    y1 = np.polyval(p,x1)
    plt.plot(x1,y1)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')
plt.legend(["Data points","$f(x)=ax+b$","$f(x)=ax^2+bx+c$","$f(x)=ax^3+bx^2+cx+d$"],loc=4)

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="multifit.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS2805-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)




