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
t = np.linspace(0,40,200)
x = 2*np.exp(-t/10)*np.cos(t)
x0 = 2*np.cos(t)

# Top plot
plt.subplot(211)            
plt.plot(t,x)
plt.ylabel('with damping')
plt.xlim([0,40])

# Bottom plot
plt.subplot(212)            
plt.plot(t,x0,'--')
plt.ylabel('no damping')
plt.xlabel('t')
plt.xlim([0,40])

# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_exercise_subplots.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.4), transparent=True)

