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
x = np.linspace(-5,5,20)
y = x**3

# Make a plot
plt.plot(x,y,'--o',color="green",markersize=20)


# Labels
plt.xlabel('x') 
plt.ylabel('f(x)')

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_exercise_2d.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.4), transparent=True)

