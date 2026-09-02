"""
Histogram animation
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Number of frames
number_of_frames = 10

# Update histogram
def update_hist(num):
    plt.cla()
    n = 100+(num+1)**5
    plt.title(f'n = {n}')
    x = 10*np.random.rand(n,1)
    plt.hist(x,bins=20)
    plt.xlim([0,10])
    plt.xlabel('x')
    plt.xlabel('count')
    
# Initialise
fig = plt.figure(figsize=(20,10))
hist = plt.hist(x = 10*np.random.rand(1,1))
plt.rcParams.update({'font.size': 30})

# Save animation
ani = animation.FuncAnimation(fig, update_hist, number_of_frames )
ani.save('/Users/Chris/Desktop/animation.gif', writer='imagemagick', fps=1)