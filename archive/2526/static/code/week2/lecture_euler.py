""" 
Script to estimate e using (1+1/n)^n method
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

# Tighter margins
plt.tight_layout()

# Set up an array of n values
n = np.arange(1,101)

# en array containing e estimates for each n value
en = (1+1/n)**n

# Make a plot of en versus n
plt.plot(n,en)

# Add dashed line at np.e
plt.plot([0,100],[np.e,np.e],"--")

# Make plot pretty with axis labels etc...
plt.ylim([2,3])
plt.xlim([1,100])
plt.xlabel("n")
plt.title("$(1+1/n)^n$ approximation to Euler's number")
# Note in the latter, the bit in $...$ is a LaTeX expression - you'll learn about this later in your programme


# Set your own filename/directory here
fname="lecture_euler.png"
fdir="/Users/Chris/Code/makecourse/modules/MAS1801-python/static/images/week2/"

# Save the file
fig.savefig(fdir+fname, facecolor=(1,1,1,0.8), transparent=True)
