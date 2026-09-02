"""
Surface plot of (u,v)=(sin(x),cos(x)+sin(y))
"""
import matplotlib.pyplot as plt
import numpy as np

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Tighter margins
plt.tight_layout()

# Set up grid points
x = np.arange(0,11)
y = np.arange(0,11)

plt.plot(x,y,'go', markersize=12)
plt.xlabel('x')
plt.ylabel('y')

# Set your own filename/directory here
fname="lecture_nomeshgrid.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)
