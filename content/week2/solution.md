# Hand-in 2 solution 

```python
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# Define f for a range of x values
x = np.linspace(-1,10,100)
f = (x**2+x+1)/(x+1)

# make a plot
plt.plot(x,f,'-',x,x,'--')
plt.xlabel('x',labelpad=20)
plt.ylabel('f(x)', labelpad=20)


print("The distance between the curves at x = 10 is {}".format(f[99]-10))


# new figure
fig = plt.figure()

# 3d axes
ax = fig.gca(projection='3d')

# Create a meshgrid
x = np.linspace(-2, 2, 25)
y = np.linspace(-2, 2, 25)
X, Y = np.meshgrid(x, y)

Z = np.exp(-X**2-Y**2)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.seismic)

# Add a colorbar
fig.colorbar(surf, shrink=0.5)

# Axis labels - note applied to the axes in a 3D plot
ax.set_xlabel('x',labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('f(x,y)', labelpad=20)
```