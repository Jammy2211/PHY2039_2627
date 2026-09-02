"""
Surface plot of (u,v)=(cos(x),sin(x))
"""
import matplotlib.pyplot as plt
import numpy as np

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Tighter margins
plt.tight_layout()

# Set up a meshgrid
x = np.arange(-np.pi,np.pi, 0.5)
y = np.arange(-np.pi,np.pi, 0.5)
X, Y = np.meshgrid(x, y)

# Components of our vector field
U = Y*np.cos(X)
V = Y*np.sin(X)

# Quiver plot
plt.quiver(X,Y,U,V)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')

# show the plot
plt.show()

# Set your own filename/directory here
fname="exercise_vector.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.4), transparent=True)
