"""
Basic sine plot with axis labels
"""
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})


# 3d axes
ax = fig.gca(projection='3d')

# Create a meshgrid
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x, y)

Z = np.cos(np.sqrt(X**2 + Y**2))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.seismic)

# Add a colorbar
fig.colorbar(surf, shrink=0.5)

# Axis labels - note applied to the axes in a 3D plot
ax.set_xlabel('x',labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('f(x,y)', labelpad=20)


# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_surf.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

