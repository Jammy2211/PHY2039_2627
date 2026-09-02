# Practical 2 Exercise Solutions

## Exercise 2.1

### Exercise {: .exercise}

Investigate the help for pyplot, including how to change the line style (I'm using `--o` below), line width and marker size.

For a bit of fun, try to recreate this plot of $f(x)=x^3$ in the range $-5\le x \le 5$, or if you like make up your own and investigate some other options! 

![](/static/images/week2/practical_exercise_2d.png){width=80%}


### Solution

I did this one with

```python
"""
Basic sine plot with axis labels
"""
import numpy as np
import matplotlib.pyplot as plt

# Set up x and y
x = np.linspace(-5,5,20)
y = x**3

# Make a plot
plt.plot(x,y,'--o',color="green",markersize=20)

# Labels
plt.xlabel('x') 
plt.ylabel('f(x)')
```

## Exercise 2.2

### Exercise {: .exercise}

A Black Friday special... over the past decade there has been a steady increase in the proportion 
of sales which take place online, and in particular each November, thanks to *Black Friday*, *Traffic Jam 
Weekend*&#42; and *Cyber Monday*...

Set up three vectors, `n`, `d` and `y`, containing the data in the following table.

Year  | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2017 | 2018
------|------|------|------|------|------|------|------|------|------|------|------
*Nov* | 6.0  | 7.9  | 9.0  | 10.3 | 10.7 | 12.1 | 13.7 | 15.5 | 18.8 | 19.9 | 21.5
*Dec* | 5.8  | 6.9  | 8.5  | 9.4  | 10.9 | 11.8 | 12.8 | 14.1 | 17.1 | 17.9 | 19.8

Nov and Dec are the % of total UK retail sales which are made online in November and December
respectively. *([Data from the Office for National Statistics](https://www.ons.gov.uk/businessindustryandtrade/retailindustry/timeseries/j4mc/drsi){target="_blank"})*

* Make a plot of `n` and `d` versus `y` on the same axes. I quite like the `'--o'` marker/line type for this sort of thing
* Make it pretty... add axis labels and a legend to your plot.

*&#42; I just made this up*

### Solution

```python
"""
UK Retail sales
"""
import matplotlib.pyplot as plt
import numpy as np

y = list(range(2008,2019))
n = [6.0,7.9,9.0,10.3,10.7,12.1,13.7,15.5,18.8,19.9,21.5]
d = [5.8,6.9,8.5,9.4,10.9,11.8,12.8,14.1,17.1,17.9,19.8]

plt.plot(y,n,y,d)

# Make pretty
plt.xlabel('Year')
plt.ylabel('%')
plt.title('Percentage of UK retail sales made online')
plt.legend(['Nov','Dec'],loc=1)
```


![Plot of the retail sales online percentage by year](/static/images/week2/exercise_sales.png)



## Exercise 2.3

### Exercise {: .exercise}

The equation

$$x(t) = 2e^{\left(-\frac{t}{10}\right)}\cos(t)$$

represents the displacement $x(t)$ of an oscillator dying away due to the damping effect of e.g. air resistance. 

Place two plots on a single figure:
 
* the function $x(t)$; and
* the oscillation of the pendulum with no friction, given by $x_{0}(t) = 2\cos(t)$.

to recreate the below plot

![Two subplots: the top containing the solution x(t), a decaying cosine curve. The bottom shows the function x0(t) which does not decay.](/static/images/week2/practical_exercise_subplots.png){width="90%"}

### Solution

```python
"""
Subplot exercise
"""
import numpy as np
import matplotlib.pyplot as plt

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
```


## Exercise 2.4

### Exercise {: .exercise}

Modify (don't start again) the above code to create the below plot of the vector field

$$\vec{v}=(u,v)=(y\cos(x),y\sin(x))$$

in the range $-\pi\le x\le\pi$, $-\pi\le y\le\pi$.

### Solution

The key here was just to change the relevant lines in the example that was above:

```python
"""
Vector plot of (u,v)=(cos(x),sin(x))
"""
import matplotlib.pyplot as plt
import numpy as np

# Set up a meshgrid
x = np.arange(-np.pi,np.pi, 0.5)
y = np.arange(-np.pi,np.pi, 0.5)
X, Y = np.meshgrid(x, y)

# Components of our vector field
U = Y*np.cos(X)
V = Y*np.sin(X)

# Quiver plot
plt.quiver(X,Y,U,V)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')
```

![Vector plot of (u,v)=(ycos(x),ysin(x))](/static/images/week2/exercise_vector.png)


