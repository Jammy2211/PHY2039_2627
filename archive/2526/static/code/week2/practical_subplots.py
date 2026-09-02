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
x = np.linspace(0,10,100)

# one row, two columns, first plot
plt.subplot(121)            
plt.plot(x,np.sin(x),'--')
plt.xlabel('x')
plt.title('sin(x)')

# one row, two columns, second plot 
plt.subplot(122)            
plt.plot(x,np.cos(x),'--')
plt.xlabel('x')
plt.title('cos(x)')

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_subplots.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

