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

# data points
x = [0,81,162];
y = [0,55,0];

# Fit using polyfit and polyval
p = np.polyfit(x,y,2)
x1 = np.linspace(0,162,100);
y1 = np.polyval(p,x1);


# plot
plt.plot(x,y,'x', markersize=25)
plt.plot(x1,y1)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')

# Set axis aspect ratio
plt.axes().set_aspect('equal')

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="tynebridge.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS2805-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)




