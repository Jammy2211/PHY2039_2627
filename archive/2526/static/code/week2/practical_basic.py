"""
A basic plot
"""
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Make a plot
#plt.plot([1,4,9,16])
plt.plot([1,2,3,4],[1,4,9,16])


# Tighter margins
plt.tight_layout()

# Set your own filename/directory here
fname="practical_basic2.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)

