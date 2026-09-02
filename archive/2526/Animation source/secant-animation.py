#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:22:53 2023

@author: chris
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


plt.rcParams['font.size'] = 20

def secant(f,x0,x1,eps):

    n = 0
    
    while abs(x1 - x0) > eps:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0, x1 = x1, x2
        n += 1
    return x1, n

r,n = secant(lambda x : x**2 - 2, 0.5, 2.5, 1e-6)

def makePlot(x0,x1,x2,state, n):
    
    global plot_id

    fig, ax = plt.subplots(figsize = (10,6),dpi=300)

    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    # Hide the top and right spines.
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Create axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    
    ax.text(3.0, -0.4, '$x$', size=13)
    ax.text(-0.1,3.75, '$y$', size=13)

    # Hide axes tick labels
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    # Hide axes tick marks
    ax.set_xticks([])
    ax.set_yticks([])

    # Base: draw function
    ax.plot(x,f(x),color = 'darkslateblue', linewidth=2)


    if state == 0.5:
        rect = patches.Rectangle((0.2,5.0), 1.6, 2, linewidth=1, edgecolor='#CCCCCC', facecolor='#EEEEEE')
        ax.add_patch(rect)
        ax.text(0.4,5.5,"Use the slider or arrows\nto explore the animation.", fontsize=16)

    # Draw xd and xu
    if state > 0.5:
        ax.scatter(x0, 0, s = 60, marker='o', color = 'forestgreen', zorder=10)
        ax.scatter(x1, 0, s = 60, marker='o', color = 'forestgreen', zorder=10)
        if f(x0) > 0:
            ax.text(x0-0.06, -0.6, f'$x_{n-2}$')
        else:
            ax.text(x0-0.06, 0.5, f'$x_{n-2}$')                              
        if f(x1) > 0:
            ax.text(x1-0.06, -0.6, f'$x_{n-1}$')
        else:
            ax.text(x1-0.06, 0.5, f'$x_{n-1}$')                              

      
    # Draw xd and xu and others
    if state > 0.5:


        # Vertical lines from points to the curve
        ax.plot([x0,x0],[0,f(x0)],'--', color='grey')
        ax.plot([x1,x1],[0,f(x1)],'--', color='grey')
        
       
    # Draw xd and xu and others
    if state > 1:

        # Secant
        ax.axline([x0,f(x0)],[x1,f(x1)], color='firebrick')

    # Draw xd and xu and others
    if state > 2:

        ax.scatter(x2, 0, s = 60, marker='o', color = 'forestgreen', zorder=10)

        if f(x2) > 0:
            ax.text(x2-0.06, -0.6, f'$x_{n}$')
        else:
            ax.text(x2-0.06, 0.5, f'$x_{n}$')                              



    plot_id += 1
    plt.savefig(f'secant_animation{plot_id}.png',bbox_inches='tight')


x = np.linspace(-0.15,3,100)
def f(x): 
    return x**2 - 2


x0 = 0.5
x1 = 2.5
x2 = 0

global plot_id 
plot_id = 0

makePlot(x0,x1,x2,0.5,2)
makePlot(x0,x1,x2,0,2)
makePlot(x0,x1,x2,1,2)
makePlot(x0,x1,x2,2,2)
x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
makePlot(x0,x1,x2,3,2)
x0, x1 = x1, x2
makePlot(x0,x1,x2,1,3)
makePlot(x0,x1,x2,2,3)
x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
makePlot(x0,x1,x2,3,3)
x0, x1 = x1, x2
makePlot(x0,x1,x2,1,4)
makePlot(x0,x1,x2,2,4)
x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
makePlot(x0,x1,x2,3,4)
x0, x1 = x1, x2
makePlot(x0,x1,x2,1,5)