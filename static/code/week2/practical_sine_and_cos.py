"""
Sine and cosine plot
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Set up x and y
x = np.linspace(0,10,100)

# Make a plot
plt.plot(x,np.sin(x),'b')
plt.plot(x,np.cos(x),'r--')

# Labels
plt.xlabel('x') 
plt.ylabel('sin(x)')

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_sine_and_cos.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

