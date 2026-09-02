"""
Sine and cosine plot
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Set up x 
x = 10*np.random.rand(100,1)  
plt.hist(x, bins=20) 

# labels
plt.xlabel('x')
plt.ylabel('Count')

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_hist2.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

