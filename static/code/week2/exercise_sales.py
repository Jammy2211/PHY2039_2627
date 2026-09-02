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

y = list(range(2008,2019))
n = [6.0,7.9,9.0,10.3,10.7,12.1,13.7,15.5,18.8,19.9,21.5]
d = [5.8,6.9,8.5,9.4,10.9,11.8,12.8,14.1,17.1,17.9,19.8]

plt.plot(y,n,y,d)

# Make pretty
plt.xlabel('Year')
plt.ylabel('%')
plt.title('Percentage of UK retail sales made online')
plt.legend(['Nov','Dec'],loc=1)

# show the plot
plt.show()

# Set your own filename/directory here
fname="exercise_sales.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.4), transparent=True)
