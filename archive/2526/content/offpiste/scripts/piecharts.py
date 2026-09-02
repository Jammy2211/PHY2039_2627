#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 11:11:18 2022

@author: chris
"""

import matplotlib.pyplot as plt
import numpy as np

# Set title, weighting and default colours
weightings = [70,20,10] 
titles = ["Exam","Assessment 2","Assessment 1"]
colours = ["lightgrey","darkgrey","silver"]

#%% Basic pie chart
plt.figure(figsize=(12, 8))
plt.rcParams['font.size'] = 20

weightings = [70,20,10] 
titles = ["Exam","Assessment 2","Assessment 1"]

plt.pie(weightings, labels = titles, startangle = 90)

fname = '../images/piecharts/piechart.png'
plt.savefig(fname, bbox_inches='tight', transparent=True)
    

#%% Pie charts

# Loop over assessments to create individual plots
for n in range(len(weightings)):

    # Make a plot for this assessment
    plt.figure(figsize=(12, 8))
    plt.rcParams['font.size'] = 20
    
    # Explode the segment for this assessment only
    standout = np.zeros(len(weightings))
    standout[n] = 0.2
    
    # Create the pie chart and objects wedges and labels which can be manipulated
    wedges, labels = plt.pie(weightings, labels = titles, 
                explode = standout, startangle = 90,
                colors = colours, shadow = True)
    
    # Customise for this assessment
    wedges[n].set_color("firebrick")
    labels[n].set_color("firebrick")
    labels[n].set_text(labels[n].get_text()+"\n{:>10}%".format(weightings[n]))

    fname = '../images/piecharts/pie_{}.png'.format(titles[n].replace(" ", "").lower())
    plt.savefig(fname, bbox_inches='tight', transparent=True)
    
    

#%% Donut charts

# Loop over assessments to create individual plots
for n in range(len(weightings)):

    # Make a plot for this assessment
    ax = plt.figure(figsize=(12, 8)).subplots()
    plt.rcParams['font.size'] = 20

    # Explode the segment for this assessment only
    standout = np.zeros(len(weightings))
    standout[n] = 0.05

    wedges, labels = plt.pie(weightings, startangle = 90, explode = standout,
                            colors = colours, wedgeprops=dict(width=0.5))
    
    # Customise for this assessment
    wedges[n].set_color("firebrick")
    
    # Add the text in the centre
    ax.text(0.5, 0.5, "{}\n{}%".format(titles[n],weightings[n]), transform = ax.transAxes, va = 'center', ha = 'center')
    
    fname = '../images/piecharts/donut_{}.png'.format(titles[n].replace(" ", "").lower())
    plt.savefig(fname, bbox_inches='tight', transparent=True)
    
#%% Pyramid pie chart

plt.figure(figsize=(17, 8)).subplots()
plt.rcParams['font.size'] = 20

weightings = [77,17,6] 
titles = ["Sky","Sunny side of pyramid","Shady side of pyramid"]
colours = ["royalblue","gold","goldenrod"]

plt.pie(weightings, colors = colours, startangle = 315)  

plt.legend(titles,loc=3,bbox_to_anchor=(0.9,0.5))

fname = '../images/piecharts/pyramid.png'
plt.savefig(fname, bbox_inches='tight', transparent=True)
  