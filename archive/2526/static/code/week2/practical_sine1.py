"""
Basic sine plot with axis labels
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Set up x and y
x = np.linspace(0,10,100)
y = np.sin(x)

# Make a plot
plt.plot(x,y)

# Labels
plt.xlabel('x') 
plt.ylabel('sin(x)')


# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_sine1.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

