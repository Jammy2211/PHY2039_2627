#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 11:41:39 2020

@author: chris
"""

import numpy as np
import matplotlib.pyplot as plt


def euler(f,y0,t):

    y = np.zeros(len(t))   # Create an 'empty' array for y
    y[0] = y0              # The initial value of y

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(t[n],y[n])*(t[n+1]-t[n])
        
    return y

plt.figure(figsize=(18,10))
plt.rcParams.update({'font.size': 30})

m = -1
t = np.linspace(0,5,100)
y0 = 5
y = euler(lambda t,y: -y/2, y0, t)

#plt.plot(t,y,'-o',markersize=int(1+100/(len(t))))
#plt.plot(np.linspace(0,5,100),5*np.exp(-np.linspace(0,5,100)/2))
#plt.legend(['Euler Method','Exact solution'])

if m == 1:
    plt.plot(t,5-t**3/100,'k--')
    plt.plot(t,1.4*t+1,'k--')
    plt.plot(t,t**2,'k--')
    plt.text(1.7,2,'?',fontsize=80)
    plt.text(0.6,2.4,'?',fontsize=80)
    plt.text(2.1,5.4,'?',fontsize=80)

colors = ['slateblue','seagreen','goldenrod','hotpink','steelblue','indianred']

for i in range(0,6):
    plt.plot(t[i],y[i],'o',markersize = 30, color=colors[i])
   # plt.plot([t[i]-0.3,t[i]+0.3],[y[i]+0.3*y[i]/2,y[i]-0.3*y[i]/2], color=colors[i],linewidth=3)
   # plt.plot([t[i]-0.3,t[i]+1.0],[y[i]+0.3*y[i]/2,y[i]-1*y[i]/2], color=colors[i],linestyle='dashed')
   # plt.vlines(t[i+1],0,6.5,colors=colors[i+1],linestyles='dashed',linewidth=0.8)
    
for i in range(0,5):
    plt.plot(t[i],y[i],'o',markersize = 30, color=colors[i])
    plt.plot([t[i]-0.3,t[i]+0.3],[y[i]+0.3*y[i]/2,y[i]-0.3*y[i]/2], color=colors[i],linewidth=3)
    plt.plot([t[i]-0.3,t[i]+1.0],[y[i]+0.3*y[i]/2,y[i]-1*y[i]/2], color=colors[i],linestyle='dashed')
    plt.vlines(t[i+1],0,6.5,colors=colors[i+1],linestyles='dashed',linewidth=0.8)
    
       

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.tick_params(axis='both', which='major', pad=24)
ax.spines['bottom'].set_position('zero')

plt.xlabel('t')
plt.ylabel('y(t)')
plt.ylim(-0.5,6.5)
plt.xlim(-0.5,5.3)
#plt.title('Euler Method dt/dt = -y/2'.format(round(t[1]-t[0],2)))
plt.savefig('/Users/chris/Code/makecourse/modules/PHY2039/static/images/week6/explanation{}.png'.format(m))

