#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 20:22:53 2023

@author: chris
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.size'] = 20

def makePlot(xd,xu,state):
    
    global plot_id

    fig, ax = plt.subplots(figsize = (10,6))

    # Move the left and bottom spines to x = 0 and y = 0, respectively.
    ax.spines["left"].set_position(("data", 0))
    ax.spines["bottom"].set_position(("data", 0))
    # Hide the top and right spines.
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    # Create axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    
    ax.text(2.5, -0.4, '$x$', size=13)
    ax.text(-0.1,3.75, '$y$', size=13)

    # Hide axes tick labels
    ax.xaxis.set_tick_params(labelbottom=False)
    ax.yaxis.set_tick_params(labelleft=False)
    # Hide axes tick marks
    ax.set_xticks([])
    ax.set_yticks([])

    # Base: draw function
    ax.plot(x,f(x),color = 'darkslateblue', linewidth=2)

    # Draw xd and xu
    if state > 0:
        ax.scatter(xd, 0, s = 60, marker='o', color = 'forestgreen', zorder=10)
        ax.scatter(xu, 0, s = 60, marker='o', color = 'firebrick', zorder=10)
        ax.text(xd-0.04, 0.3, '$x_d$')
        ax.text(xu-0.04, -0.6, '$x_u$')
      
    # Draw xd and xu and others
    if state > 1:


        ax.scatter(xd, 0, s = 60, marker='o', color = 'forestgreen', zorder=10)
        ax.scatter(xu, 0, s = 60, marker='o', color = 'firebrick', zorder=10)

        # Vertical lines from points to the curve
        ax.plot([xd,xd],[0,f(xd)],'--', color='grey')
        ax.plot([xu,xu],[0,f(xu)],'--', color='grey')

        # Horizontal lines from curve to y axis
        ax.plot([0,xd],[f(xd),f(xd)],'--', color='grey')
        ax.plot([0,xu],[f(xu),f(xu)],'--', color='grey')

        ax.text(xd-0.04, 0.3, '$x_d$')
        ax.text(xu-0.04, -0.6, '$x_u$')
        ax.text( -0.25,f(xd), '$f(x_d)$')
        ax.text( -0.25,f(xu), '$f(x_u)$')
        

    if state > 2:
        # show x mid
        xmid = (xu+xd)/2
        ax.scatter(xmid, 0, s = 60, marker='o', color = 'darkorange', zorder=10)
        if f(xmid) > 0:
            ax.text(xmid-0.06, -0.6, '$x_{mid}$')
        else:
            ax.text(xmid-0.06, 0.3, '$x_{mid}$')
        ax.plot([xmid,xmid],[0,f(xmid)],'--', color='grey')
        
    if state > 3:
        # show x mid
        xmid = (xu+xd)/2
        ax.scatter(xmid, 0, s = 60, marker='o', color = 'darkorange', zorder=10)
        if f(xmid) > 0:
            ax.text(xmid-0.06, -0.6, '$x_{mid}$')
        else:
            ax.text(xmid-0.06, 0.3, '$x_{mid}$')
        ax.plot([xmid,xmid],[0,f(xmid)],'--', color='grey')


    plot_id += 1
    plt.savefig(f'bisection_animation{plot_id}.png',bbox_inches='tight')


x = np.linspace(-0.15,2.4,100)
def f(x): 
    return x**2 - 2


xd = 0.5
xu = 2

global plot_id 
plot_id = 0

makePlot(xd,xu,0)
makePlot(xd,xu,1)
makePlot(xd,xu,2)
makePlot(xd,xu,3)
xd = (xu+xd)/2
makePlot(xd,xu,2)
makePlot(xd,xu,3)
xu = (xu+xd)/2
makePlot(xd,xu,2)
makePlot(xd,xu,3)
xu = (xu+xd)/2
makePlot(xd,xu,2)
makePlot(xd,xu,1)
xd = (xu+xd)/2
makePlot(xd,xu,1)
xd = (xu+xd)/2
makePlot(xd,xu,1)
xu = (xu+xd)/2
makePlot(xd,xu,1)
xd = (xu+xd)/2
makePlot(xd,xu,1)