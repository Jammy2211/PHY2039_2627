"""
f(x)=x*exp(-ax) for different values of a
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure (increase figure size)
#fig = plt.figure(figsize=(20,10))

# Bigger font
plt.rcParams.update({'font.size': 30})

import numpy as np
import matplotlib.pyplot as plt

for n in range(1,4):
    #x = np.linspace(-3,3,1000)
    x_vals = list(range(-3,3))
    #y = np.sqrt(x**3+n)
    y = []
    for x in x_vals:
        y.append((x**3+n)**0.5)
    plt.plot(x_vals,y)

# Make pretty...