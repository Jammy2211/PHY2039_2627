"""
Basic sine plot without axis labels
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Generate some random numbers from the normal distribution with mean 0 and s.d. 1
x = np.random.normal(0,1, size = 100) 

# A plain histogram 
#plt.hist(x)

# Or a histogram normalised to give prob. density
plt.hist(x, density=True)

# Set a x label
plt.xlabel("x")
plt.ylabel("Density")

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="lecture_hist.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

