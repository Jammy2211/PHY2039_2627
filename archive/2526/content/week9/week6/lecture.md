
---


## Sub-plots and figures

It is often desirable to have multiple axes inside a single figure window. The `subplot()` function takes three arguments, the first specifies the number of rows, the second the number of columns, and the third the current plot number, starting with 1. So it goes like this:

```python
"""
Subplot example
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

# one row, two columns, first plot
plt.subplot(121)            
plt.plot(x,np.sin(x),'--')

# one row, two columns, second plot 
plt.subplot(122)            
plt.plot(x,np.cos(x),'--')
```

Note that in the below plots I have added a title and axis label. These commands go after each of the `plot` commands. Take a look at the link to the source code below if you are interested.

![Side by side plots of sin(x) and cos(x) created using the subplot commands](/static/images/week2/practical_subplots.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_subplots.py){target="_blank"}*


### Exercise 2.5 {: .exercise}

Here's some more practice with subplots.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/76919/oscillations-subplot/embed/?token=ebcaa9e9-1258-4f76-90b1-b383b908d106" data-id="exercise-2-5" data-cta="Show Exercise"></numbas-embed>




## Advanced plotting

At the practical this week we will also look at how to create surface and vector plots. 

![A surface plot.](/static/images/week2/practical_surf.png){width="80%"}

*[Download the full source code for this plot](/static/code/week2/practical_surf.py){target="_blank", style="font-size: 0.7em;"}*

---

![A vector plot.](/static/images/week2/practical_vector.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_vector.py){target="_blank", style="font-size: 0.7em;"}*

. . .

Both of these rely on what is called a "meshgrid". 

---

### Creating a meshgrid

Let's say I want to draw a vector with components $(u,v)$ at uniformly spaced $x$ and $y$ coordinates in the interval $[0,10]$.

I might think that I can define values for variables `u` and `v` if I have `x` and `y` as follows

```python
x = np.arange(0,11)
y = np.arange(0,11)
```

But plotting `y` versus `x` shows why this doesn't work...

```python
plt.plot(x,y,'o')
```

---

![A grid of x and y values set up without meshgrid.](/static/images/week2/lecture_nomeshgrid.png){width="80%"}

*[Download the full source code for this plot](/static/code/week2/lecture_nomeshgrid.py){target="_blank", style="font-size: 0.7em;"}*

What we really want is an $x$ and $y$ grid covering that entire plot. That's what NumPy's `meshgrid()` function does for us.


---


![A grid of x and y values, set up with NumPy's meshgrid function shows an x and y value at every permutation of x and y coordinates.](/static/images/week2/lecture_meshgrid.png){width="80%"}

*[Download the full source code for this plot](/static/code/week2/lecture_meshgrid.py){target="_blank", style="font-size: 0.7em;"}*

```python
x = np.arange(0,11)
y = np.arange(0,11)
X,Y = np.meshgrid(x,y)
plt.plot(X,Y,'o')
```


---

We can then go on to define, say a height `Z` for a surface plot in terms of our (big) `X` and `Y`

```python
Z = np.sqrt(X^2+Y^2)
```

. . .

```python
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z, cmap='seismic')
```

. . . 

or a `U` and `V` for a vector plot 

```python
U = np.sin(Y)
V = np.cos(X)
plt.quiver(X,Y,U,V)
```


******************



## Topics

 * Announcements
 * Differential equations

---

## Where are we?


<table class="table" style="font-size: 0.75em;">
    <tbody>
        <tr >
        	<th></th>
            <th >Week #</th>
            <th >Week Begin</th>
            <th>Topic</th>
            <th>Assessment</th>
        </tr>
        <tr >
        	<td></td>
            <td>1</td>
            <td>27th Sept</td>
            <td>Background + Curve Fitting I</td>
            <td></td>
        </tr>
        <tr>
        	<td></td>
            <td>2</td>
            <td>4th Oct</td>
            <td>Curve Fitting II</td>
            <td></td>
        </tr>
        <tr >
        	<td></td>
            <td>3</td>
            <td>11th Oct</td>
            <td>Background + Root Finding I</td>
            <td></td>
        </tr>
        <tr>
        	<td></td>
            <td>4</td>
            <td>18th Oct</td>
            <td>Root Finding II</td>
            <td>Assessment 1 19th-26th Oct</td>
        </tr>
        <tr>
	        <td></td>
            <td>5</td>
            <td>25th Oct</td>
            <td>Numerical differentiation and integration</td>
            <td></td>
        </tr>
        <tr style="background-color: #edffab;" >
        	<td>→</td>
            <td>6</td>
            <td>1st Nov</td>
            <td>Differential Equations I</td>
            <td>Assessment 2 2nd - 22nd Nov</td>
        </tr>
        <tr >
            <td style="background-color: #ced4d9; text-align: center;" colspan="5"><em><strong>Enrichment week</strong></em></td>
        </tr>
        <tr >
        	<td></td>
            <td>7</td>
            <td>15th Nov</td>
            <td>Differential Equations II</td>
            <td></td>
        </tr>
        <tr >
        	<td></td>
        	<td></td>
            <td colspan="3">...</td>
        </tr>
    </tbody>
</table>

---

## Announcements

* Assessment 1 feedback coming soon...

. . .

* Assessment 2
    * Based primarily on weeks 5 and 6
    * Due 4pm Monday 22nd November
    * Report format
    * Saving plots

. . .

* Enrichment week
    * Office hours
    * LaTeX material


---

## Assessment 2: Format

![](/static/images/report_guidelines.jpg){width=80%}


---

## Assessment 2: Saving plots

A few words on best practice for saving plots for a report...

. . .

Here are some useful commands

```python
# Change the figure size
plt.figure(figsize=(20,10))

# Change the font size
plt.rcParams['font.size'] = 30

# Use latex in a label
plt.ylabel('$\phi$')

# Optional grid
plt.grid()
```

---

## Differential equations


Our challenge this week is going to be to tackle solving a differential equation like this one:

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2} $$

----

A differential equation is one which relates a function (or functions) to its derivative(s). The derivative represents a rate of change.

* They are vitally important in so many fields, including fluid dynamics, economics, epidemiology, radioactivity, population dynamics...

* They can often be solved "by hand", but complicated ones can only be solved with the help of a computer.

* We are going to have a go at solving differential equations "numerically" using Python

----


## Solving differential equations with a computer


In the first instance we are going to solve

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$

sometimes called an "initial value problem".


----

The idea behind the method is that we know $y(0)=5$ and $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}t}(0)=-\frac{5}{2}$

![](/static/images/week6/explanation3.png){width=80%}

----

So this can be used to estimate $y$ at some later point

![](/static/images/week6/explanation5.png){width=80%}

$y(1) = 5 -\left(\frac{5}{2}h\right)$, where we've used a distance between $t$ values of $h = 1$

----

Next week we'll code up the algorithm for doing this, but this week we're going to focus on a SciPy function, `odeint` that does the hard work for us.

----

## Worked example

Let's see the set up for

\[ \frac{\mathrm{d}y}{\mathrm{d}t} = - \frac{y}{2} \]

---

## Worked example `odeint` solution

Solving with `odeint` goes something like this:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# function on the rhs of dy/dt
def rhs(y,t):
    dydt = - y/2
    return dydt

y0 = 5						# initial condition
t = np.linspace(0,5,5)		# t array

y = odeint(rhs,y0,t)		# solve ODE

plt.plot(t,y)				# plot results
```

---

### Systems of differential equations

\begin{align}
\frac{dS}{dt}&=-\beta IS + \gamma I, \\
\frac{dI}{dt}&=\beta IS -\gamma I
\end{align}

Let $S(0)=999, I(0)=1$, and parameters $\beta = 0.002, \gamma = 0.5$.

---

```python
def model(y, t, b, c):
    S, I = y            # reads in values in y 
    dSdt = -b*I*S + c*I # rhs of dS/dt
    dIdt = b*I*S - c*I  # rhs of dI/dt 
    return [dSdt, dIdt] 
```

. . .

```python
y0 = [999,1]    # initial y
```

. . .

```python
t = np.linspace(0,5,5)		# t array

y = odeint(model,y0,t, args=(0.002,0.5))
```

---

### Higher order differential equations
$$\frac{\mathrm{d}^2y}{\mathrm{d}t^2}-2y = 0$$

with $\displaystyle y(0)=2, \frac{\mathrm{d}y}{\mathrm{d}t}(0)=0$

. . .

Let $\displaystyle u=\frac{\mathrm{d}y}{\mathrm{d}t}$, then we have a system of two first order differential equations:

. . .

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = u,  $$

. . .

$$ \frac{\mathrm{d}u}{\mathrm{d}t} = 2y, $$

with $y(0)=2, u(0)=0$.

---

## Summary

Differential equations will be something that will be increasingly part of your future studies. We'll build on this week's work with a look at the underlying algorithms after enrichment week.

