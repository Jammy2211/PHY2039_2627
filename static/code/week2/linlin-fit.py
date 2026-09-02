#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fit a power law function to some data
"""

import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# data points
x = [1,3,5,7,9]
y = [2.1,2.9,3.5,3.8,4.2]

# Fit using polyfit and polyval
p = np.polyfit(np.log(x),np.log(y),1)    # np.polyfit(X,Y,1) would work too

# construct f(x)=ax^b
x1 = np.linspace(0,10,100)
b = p[0]
a = np.exp(p[1])
y1 = a*pow(x1,b)

# plot
plt.plot(x,y,'x', markersize=25)
plt.plot(x1,y1)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')

plt.legend(['Data points','f(x)=ax^b'],loc=4)

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="linlin-fit.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS2805-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)




