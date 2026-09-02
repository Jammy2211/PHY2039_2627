# Handout 9

In handout 9 we look at a generalisation of some of analysis in week 7, especially now that we're tooled up with some linear algebra, we tidy up some loose ends and look at a couple of longer case studies.


## ODE Methods Module

In the lecture in week 7, I added the Euler and 4th-order Runge-Kutte methods into a module. Here's the module that I created:

```python
import numpy as np

def euler(f,y0,t):


    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])

    return y


def rk4(f,y0,t):

    y = np.zeros(len(t))
    y[0] = y0
    
    for n in range(0, len(t)-1): 
    
        h = t[n+1]-t[n]
        k1 = f(y[n],t[n]) 
        k2 = f(y[n] + h * 0.5 * k1,t[n] + 0.5 * h) 
        k3 = f(y[n] + h * 0.5 * k2,t[n] + 0.5 * h) 
        k4 = f(y[n] + h * k3,t[n] + h) 
      
        # Update next value of y 
        y[n+1] = y[n] + (1.0 / 6.0)*h*(k1 + 2 * k2 + 2 * k3 + k4) 
      
    return y
```

We can save that as a file, say, *ode_methods.py* and then in another file you can run some code, for example:

```python
import ode_methods as ode
import numpy as np

t = np.arange(0,6,1)
y0 = 5
y_euler = ode.euler(lambda y,t: -y/2,y0,t)
```

Note that the functions above are set up for first order ODES. Without making them more complex (have a go if you like), we will need to use the code outside of the functions, as done in the next section, for systems/2D problems.

### Exercise 9.1 {: .exercise}

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110518/midpoint-method/embed/?token=0063edbb-2f04-4db8-b6a6-4888cd91b8a4" data-id="exercise-9-1" data-cta="Show Exercise"></numbas-embed>



## Stablility in 2D

In handout 7 we considered the stability of the Euler Method. We found that we required $|1-ah|\lt 1$.

For a system of $n$ differential equations with constant coefficients, this can be generalised by considering

$$\mathbf{y}' = -\Lambda \mathbf{y}$$


where  $\Lambda$ is an $n$ x $n$ matrix of the coefficients, which will have $n$ eigenvalues $\lambda_i$

It can be shown that in this case, the Euler method is stable if $h < 2/\lambda_{max}$
where $\lambda_{max}$ is the largest eigenvalue of $\Lambda$.

Let's look at an example. Consider

\begin{align}
\frac{\mathrm{d}y_1}{\mathrm{d}t}&=y_2, \\
\frac{\mathrm{d}y_2}{\mathrm{d}t}&=-101y_1-99y_2 \\
\end{align}

Then this is 

\begin{align}
\frac{\mathrm{d}}{\mathrm{d}t}\begin{pmatrix} y_1 \\ y2 \end{pmatrix} = - \begin{pmatrix} 0 & -1 \\ 101 & 99 \end{pmatrix}\begin{pmatrix} y_1 \\ y2 \end{pmatrix}
\end{align}

i.e.

\begin{align}
\Lambda = \begin{pmatrix} 0 & -1 \\ 101 & 99 \end{pmatrix}
\end{align}

Having looked at the `scipy.linalg` functionality last week, we can find the eigenvalues of this matrix easily:

```python
import numpy as np
import scipy.linalg as sla

# Lambda matrix
L = np.array([[0,-1],[101,99]])

# Get eigenvalues and eigenvectors
eigenvalues,eigenvectors = sla.eig(L)

print("Max lambda: {}".format(max(eigenvalues)))
print("Critical h: {}".format(2/max(eigenvalues).real))
```
```output
Max lambda: (97.96906229751097+0j)
Critical h: 0.020414607970079678
```

This suggests that we require $h \le 0.0204$ for the Euler method to be stable. Let's try coding this up with $h = 0.02$ and $h = 0.021$ for comparison.

![](/static/images/week9/h0.02.png){style="float: left; width: 500px;"}

![](/static/images/week9/h0.021.png){style="float: left; width: 520px;"}

<br style="clear: both;">


The formula $h < 2/\lambda_{max}$ is for the Euler Method, but the critical $h$ gives a decent estimate when applied to other methods including Runge-Kutte.

### Exercise 9.2 {: .exercise}

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110525/stability-2d-system/embed/?token=44c8d7e8-595c-4783-90fe-6b21ad8d587b" data-id="exercise-9-2" data-cta="Show Exercise"></numbas-embed>



## Dynamical Systems Example 1: Lotka-Volterra


We met the Lotka-Volterra equations briefly in an exercise in week 7:

\begin{align}
\frac{\mathrm{d}x}{\mathrm{d}t} &=\alpha x-\beta xy, \\[0.7em]
\frac{\mathrm{d}y}{\mathrm{d}t} &=\delta xy-\gamma y
\end{align}

For this one we're going to use the `odeint` function. 

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(u, t, a, b, c, d):
    x, y = u              # reads in u and assigns to x and y
    dxdt = a*x-b*x*y   # rhs of dx/dt
    dydt = d*x*y-c*y   # rhs of dy/dt 
    return [dxdt, dydt]   # important: this way around!

# Parameters
a = 2/3
b = 4/3
c = 1
d = 1

# Initial conditions
u0 = [1,1]

# Time points
t = np.linspace(0,50,1000)

# Solve ODE
u = odeint(model,u0,t,args=(a,b,c,d))

plt.plot(t,u)
plt.legend(['Prey, x(t)','Predator, y(t)'])
plt.xlabel('t')
plt.title('Predator-Prey Model')
```

The equations are used to represent predator-prey relationships. The prey population is $x(t)$ and the predator population $y(t)$.

![](/static/images/week9/predator-prey.png){style="width: 80%; max-width: 600px;"}

The dynamics are very neatly viewed with a "phase-space" plot, plotting $y(x)$ versus $x(t)$

```python
# Phase plot
plt.plot(u[:,0],u[:,1])
# Start value
plt.plot(u0[0],u0[1],'o',markersize=10)
plt.xlabel("Prey population")
plt.ylabel("Predator population")
```

This is actually a good case for using the axis option `set_aspect` to set the aspect ratio to 1:1.

```python
axes=plt.gca()
axes.set_aspect(1)
```

![](/static/images/week9/predatorpreyphase.png){style="width: 80%; max-width: 700px;"}



I've added a point for the start value, after which, moving forward in time, the solution follows a circular route back to the same point. We can see that at around $t=10$, the two solutions have returned back to $x=y=1$.

### Exercise 9.3 {: .exercise}


<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110538/lotka-volterra-initial-conditions/embed/?token=251504c8-4936-4a08-a830-58efec303509" data-id="exercise-9-3" data-cta="Show Exercise"></numbas-embed>


### Equilibrium solutions

The system reaches an equilibrium position if $\displaystyle \frac{\mathrm{d}x}{\mathrm{d}t} = \frac{\mathrm{d}y}{\mathrm{d}t} = 0$.

That is:

\begin{align}
\alpha x-\beta xy = x(\alpha -\beta y)&= 0 \\[0.7em]
\delta xy-\gamma y  = y(\delta x-\gamma) &= 0
\end{align}

There are two solutions:

One is trivial: $x = y = 0$ (we don't start with any predator or prey, so never will)

The other is $y = \alpha/\beta$ and $x = \delta/\gamma$


![](/static/images/week9/predatorpreyequilibrium.png){style="width: 80%; max-width: 700px;"}



We could take this further and analyse the stability of these equilibrium points, but I'd be stepping on the toes of the stage 3 module on *instabilities*, which covers this sort of thing in depth. Instead we're going to turn one final corner for the home straight.



## Dynamical Systems Example 2: The Logistic Map

Many dynamical systems exhibit chaotic behaviour, including the pendulum equation in assessment 2 and something similar to the logistic equation that we met in week 6, which we're going to see here.


### The logistic Map

In week 6 we met the logistic equation, used for population modelling:

$$ \frac{\mathrm{d}x}{\mathrm{d}t} = rx(1-x) $$

It is the continuous form of the *logistic map*, which we're going to explore here.

$$ x_{n+1} = rx_n(1-x_n) $$

We're going to aim to create this incredibly famous plot, 
which represents the values of $x_n$ that the solution settles at as $r$ is increased, initially finding one value, then oscillating between 2, then 4, 8 and so on until it reaches a chaotic state:

![](/static/images/week9/logisticmap.png){style="width: 80%; max-width: 600px;"}


### Solutions for $x_n$

Let's start by making a plot of $x_n$ for, say $n \le 100$ and $r = 1.5$, starting off with an equation that can take $x$ and return $rx(1-x)$

```python
def x_iter(x,r):
    """
    Takes in x and r and returns 
    r*x*(1-x)
    """
    return r*x*(1-x)

r = 1.5
x = 0.2
print(x_iter(x,r))     
```
```output
0.24000000000000005
```

OK, good stuff. Now lets iterate to see how $x$ changes with $n$ by putting values into an array


```python
import numpy as np
import matplotlib.pyplot as plt

def x_iter(x,r):
    """
    Takes in x and r and returns 
    r*x*(1-x)
    """
    return r*x*(1-x)

r = 1.5
x = np.zeros(100)
x[0] = 0.2
for n in range(len(x)-1):
	x[n+1] = x_iter(x[n],r)

plt.plot(x)
print("final value: x = {}".format(x[99]))
```
```output
final value: x = 0.3333333333333333
```


![](/static/images/week9/r1.5.png){style="width: 70%; max-width: 450px;"}


### Exercise 9.4 {: .exercise}

Change the above code with $r$ equal to each of $2.8, 3.25, 3.5, 3.75, 4$. I've created an animation of the whole thing with values in between...

![](/static/images/week9/logistic_animation.gif){style="width: 80%; max-width: 600px;"}

(Just to reiterate, I don't expect you to create an animation!)

### Bifurcations

You'll notice that from around $r = 3$, the long term behaviour of $x_n$ is to oscillate between values. Here's the last 5 values in the $x$ array for $r=2.8$ (tends to a single value)

Here's $r = 3.1$ (oscillates between two values)

```python
# ...
r = 3.1
# ...
print(x[95:100])
```
```output
[0.55801413 0.76456652 0.55801413 0.76456652 0.55801413]
```

![](/static/images/week9/r3.1.png){style="width: 70%; max-width: 450px;"}


Once we get to around $r = 3.5$, we see new peaks appear (oscillates between 4 values):


![](/static/images/week9/r3.5.png){style="width: 70%; max-width: 450px;"}


At $r = 3.55$ we are oscillating between 8 values (at least rounding to a few decimal places):

![](/static/images/week9/r3.55.png){style="width: 70%; max-width: 450px;"}


The solution then oscillates between 16, 32 etc. This is known as period doubling and continues until around $r \approx 3.56995$ when we have the onset of chaos (through definitions we won't get into here), where a tiny variation results in a dramatically different solution.


### Capturing the oscillation values

Lets take the example of $r = 3.5$ (oscillating between 4 values). We want to capture the unique values in `x`, but we'd also like to ignore the initial transient, so we might let the code run further and store values like this:

```python
r = 3.5
x = 0.2
v = []
for n in range(200):
	x = x_iter(x,r)
	if n > 100 and round(x,6) not in v:
		v.append(round(x,6))
print(v)
```
```output
[0.874997, 0.38282, 0.826941, 0.500884]
```

Note we're no longer bothering to store the full `x` array, just the unique values, and we're storing them in list `v` to a fixed number of decimal places, to avoid duplicates cause by number precision issues.

To create the plot at the top of the section we now plot these values on the y axis for several $r$ values on the x axis, by putting the above code into a for loop for r and adding a marker to the plot for each solution. Here's the full code:

```python
import numpy as np
import matplotlib.pyplot as plt

def x_iter(x,r):
    """
    Takes in x and r and returns 
    r*x*(1-x)
    """
    return r*x*(1-x)

x = 0.2
v = []
for r in np.linspace(2.7,4,500):
    for n in range(200):
    	x = x_iter(x,r)
    	if n > 100 and round(x,6) not in v:
            v.append(round(x,6))
            plt.plot(r,x,'ko',markersize=0.5)
            
plt.xlabel('r')
plt.ylabel('x')
```

![](/static/images/week9/logisticmap.png){style="width: 80%; max-width: 600px;"}


There we go: one of the most famous mathematical plots there is, in barely 15 lines of Python code!

### Exercise 9.5 {: .exercise}

There is a tonne of things you could explore from here if you feel so inclined. For starters, check out those stable values around $r \approx 3.8$, in between the chaos, known as the "islands of stability"! Just google "logistic map" and you will find an astonishing amount of literature. 

If there's one thing that I'd recommend then it's looking into the "Feigenbaum constant", which represents the ratio of intervals at which period doubling occurs, which incredibly turns out to be a constant! 

## Summary

That's all for new content in this module: week 10 will run a little different, to give you an idea of the sort of work a researcher in applied mathematics or physics does using a programming language like Python. And then week 11 we'll be dedicating to revision.





