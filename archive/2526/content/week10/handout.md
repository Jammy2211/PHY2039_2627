[Click here to open this handout in a new browser tab](#){target="_blank"}

# Handout 10 - In-depth examples and generalizations

This week we'll look at some case studies using the methods covered in previous weeks, and examples of how the methods can be extended.

## 10.1) ODE methods module

Earlier in the module we created a custom root-finding module, making it easier to use the code we had written to apply root-finding methods. We can do this same with the numerical ODE methods covered in Week 10:

```python
"""
Functions to solve ODEs
"""

import numpy as np

def euler(f,y0,t):
    """
    Returns the solution y(t) for an initial 
    value problem dy/dt = f(y,t) for an array t 
    and initial value y0 using the Euler Method
    """

    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])

    return y


def rk4(f,y0,t):
    """
    Returns the solution y(t) for an initial 
    value problem dy/dt = f(y,t) for an array t 
    and initial value y0 using the Runge-Kutta Method
    """

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

Once this code is saved in the script *ode_methods.py* we can import it as follows:

```python
import ode_methods as ode
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,6,1)
y0 = 5
y_euler = ode.euler(lambda y,t: -y/2,y0,t)
y_rk4 = ode.rk4(lambda y,t: -y/2,y0,t)

plt.plot(t,y_euler,t,y_rk4)
plt.xlabel("t")
plt.ylabel("y(t)")
plt.legend(["Euler","RK4"])
```

Recall that both the Euler and Runge-Kutta methods implemented in the code above only apply to first-order ODEs (those containing only first derivatives). As described in the Handout 9 we can convert a second-order ODE to a system of first-order ODEs; having done so we can then apply the above methods.

<div class="exercise" markdown=true>

### Exercise 10.1

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110518/midpoint-method/embed/?token=0063edbb-2f04-4db8-b6a6-4888cd91b8a4" data-id="exercise-9-1" data-cta="Show Exercise"></numbas-embed>

</div>

## 10.2) Stablility in 2D

In Handout 9 we investigated the *stability* of the Euler method i.e. how the accuracy of the numerical solution depended on the value of the step size $h$. We saw that there are critical values of $h$, below which the numerical solution was accurate but above which it ceased to be mathematically meaningful. For example, given the ODE

$$\frac{\mathrm{d}y}{\mathrm{d}t} = -2y $$

we require $|1-2h|\lt 1$ for stability. For the general ODE

$$\frac{\mathrm{d}y}{\mathrm{d}t} = -\lambda y $$

for $\lambda$ a constant, we require $|1-\lambda h|\lt 1$ for stability.

We can generalize this to a system of ODEs. Let $y_1, y_2, \ldots, y_{n}$ be a collection of functions $y_i$ that depend on $t$. Consider the following vectors

$$ \mathbf{y} = \begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix} $$

and

$$ \mathbf{y}' = \frac{d}{dt}\begin{pmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{pmatrix} = \begin{pmatrix} y^{\prime}_1 \\ y^{\prime}_2 \\ \vdots \\ y^{\prime}_n \end{pmatrix} $$

We can then describe a system of ODEs using the matrix equation

$$\mathbf{y}' = -\Lambda \mathbf{y}$$

where $\Lambda$ is an $n \times n$ matrix of coefficients.

Although it is outside the scope of this module, it can be proved that the Euler method is stable if and only if $h < 2/\lambda_{max}$ where $\lambda_{max}$ is the largest eigenvalue of the matrix $\Lambda$.

Let's look at an example. Consider the system of ODEs

\begin{align}
\frac{d y_1}{dt}&=y_2 \\
\frac{d y_2}{d t}&=-101y_1-99y_2 \\
\end{align}

This can be expressed as the following matrix equation

\begin{align}
\frac{d}{dt}\begin{pmatrix} y_1 \\ y2 \end{pmatrix} = - \begin{pmatrix} 0 & -1 \\ 101 & 99 \end{pmatrix}\begin{pmatrix} y_1 \\ y_2 \end{pmatrix}
\end{align}

so that

\begin{align}
\Lambda = \begin{pmatrix} 0 & -1 \\ 101 & 99 \end{pmatrix}
\end{align}

As we covered in Week 3 we can used Python to easily find the eigenvalues of a matrix:

```python
import numpy as np
import scipy.linalg as sla

# Lambda matrix
L = np.array([[0,-1],[101,99]])

# Compute eigenvalues and eigenvectors
eigenvalues,eigenvectors = sla.eig(L)

print("Max eigenvalue: {}".format(max(eigenvalues)))
print("Critical h: {}".format(2/max(eigenvalues).real))
```
```output
Max eigenvalue: (97.96906229751097+0j)
Critical h: 0.020414607970079678
```

This suggests that the Euler method is stable for $h$ values less than $0.0204$. Let's now verify this for $h = 0.02$ and $h = 0.021$, and initial conditions $y_1 ( 0 ) = 2$, $y_2 ( 0 ) = -2$:

```python
import numpy as np
import matplotlib.pyplot as plt

for h in [0.02,0.021]: 
    t = np.arange(0,5+h,h)
    y1 = np.zeros(len(t))
    y2 = np.zeros(len(t))

    # Initial conditions
    y1[0] = 2
    y2[0] = -2
   
    # Solve with Euler Method
    for n in range(len(t)-1):
        y1[n+1] = y1[n] + (t[n+1]-t[n]) * (y2[n])
        y2[n+1] = y2[n] + (t[n+1]-t[n]) * (-101*y1[n]-99*y2[n])

    # Make a plot
    plt.figure()
    plt.plot(t,y1,t,y2)
    plt.title("h = {}".format(h))
    plt.xlabel("$t$")
    plt.legend(["$y_1(t)$","$y_2(t)$"])
```

![Euler Method with h = 0.02](/static/images/week9/h0.02.png){style="float: left; width: 500px;"}

![Euler Method with h = 0.021](/static/images/week9/h0.021.png){style="float: left; width: 520px;"}

<br style="clear: both;">

The system of ODEs can be solved exactly using methods outside the scope of this module. The resulting exact solutions for $y_1$ and $y_2$ both tend to $0$ as $t$ tends to infinity, so that our stability analysis is shown to be valid.

The formula $h < 2/\lambda_{max}$ holds for the Euler Method, but this critical $h$ can applied to other methods including Runge-Kutta.

<div class="exercise" markdown=true>

### Exercise 10.2

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110525/stability-2d-system/embed/?token=44c8d7e8-595c-4783-90fe-6b21ad8d587b" data-id="exercise-9-2" data-cta="Show Exercise"></numbas-embed>

</div>

## 10.3) Dynamical systems Example 1: Lotka-Volterra

In mathematics the term *dynamical system* typically refers to a collection of quantities that evolve in time. These quantities may have a physical meaning, but often we simply study them in the abstract. Mathematical modelling often involves evaluating how such systems evolve, including if they reach equilibrium states. Examples of dynamical systems from previous weeks include the SIR model and logistic equation.

We saw the Lotka-Volterra equations briefly in an exercise in Week 9:

\begin{align}
\frac{dx}{dt} &=\alpha x-\beta xy \\
\frac{dy}{dt} &=\delta xy-\gamma y
\end{align}

where $x$ denotes the population of a prey species, $y$ that of a predator species, and $\alpha$, $\beta$, $\delta$, $\gamma$ are constants.

We can solve this system using the `odeint` function. We use a very fine grid of $t$ points as the solutions involve a great deal of oscillation. Typical values of $\alpha$, $\beta$, $\gamma$ and $\delta$ (labelled `a`, `b`, `c`, `d` in the code) have been chosen, in addition to the initial conditions $x(0)=y(0)=1$:

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(u, t, a, b, c, d):
    x, y = u              # reads in u and assigns to x and y
    dxdt = a*x-b*x*y   # rhs of dx/dt
    dydt = d*x*y-c*y   # rhs of dy/dt 
    return [dxdt, dydt]   # note the order of the list elements

# Constants
a = 2/3
b = 4/3
c = 1
d = 1

# Initial conditions
u0 = [1,1]

# Time values
t = np.linspace(0,50,1000)

# Solve the ODE
u = odeint(model,u0,t,args=(a,b,c,d))

plt.plot(t,u)
plt.legend(['Prey, x(t)','Predator, y(t)'])
plt.xlabel('t')
plt.title('Predator-Prey Model')
```

![Predator Prey solution](/static/images/week9/predator-prey.png){style="width: 80%; max-width: 600px;"}

Notice the period nature of the solutions e.g. the populations alternate between maxima and minima.

A convenient way to describe this periodicity is by plotting $y(x)$ versus $x(t)$ in 2D space; such a plot is known as a *phase portrait*. A point on the curve described this way corresponds to a possible state of the biological system i.e. a pair of possible values for the prey and predator populations. As the populations are periodic the phase portrait is circular:

```python
# Phase plot
plt.plot(u[:,0],u[:,1])
# Start value
plt.plot(u0[0],u0[1],'o',markersize=10)
plt.xlabel("Prey population")
plt.ylabel("Predator population")
```

It's convenient here to use the option `set_aspect` to ensure the axes are displayed in a $1:1$ ratio:

```python
axes=plt.gca()
axes.set_aspect(1)
```

![A phase plot for the Predator-Prey Model](/static/images/week9/predatorpreyphase.png){style="width: 80%; max-width: 700px;"}

The marked point is the value at $t=0$.

It's instructive to repeat the above code with an array of $t$ values containing fewer points e.g. `t = np.linspace(0,50,50)`. Ensure you revert to `t = np.linspace(0,50,1000)` when completing the next exercise.

<div class="exercise" markdown=true>


### Exercise 10.3 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110538/lotka-volterra-initial-conditions/embed/?token=251504c8-4936-4a08-a830-58efec303509" data-id="exercise-9-3" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="interlude" markdown=true>


### Predator-Prey parameters 

The constants  $\alpha$, $\beta$, $\gamma$ and $\delta$ have a physical meaning:

* The term $+\alpha x$ represents an exponential reproductive growth that can be assumed to occur with no predators present
* The term $-\beta xy$ represents the predation. The model assumes this will be proportionate to $xy$ i.e. the more that predators meet prey, the more predation occurs.
* The term $+\delta xy$ represents growth of the predator population, also assumed to be proportional to $xy$.
* The term $-\gamma y$ represents the natural death of predators.

It is instructive to change these constants, and observe how the phase portrait changes.

</div>

### Equilibrium solutions

The system reaches an equilibrium position if $\frac{dx}{dt} = \frac{dy}{dt} = 0$.

In the case of Lokta-Volterra this occurs when

\begin{align}
\alpha x-\beta xy = x(\alpha -\beta y)&= 0 \\
\delta xy-\gamma y  = y(\delta x-\gamma) &= 0
\end{align}

There are two solutions to the above system of equations.

One is trivial: $x = y = 0$, corresponding to (the very boring case of) no prey or predators.

The other is $y = \alpha/\beta$ and $x = \gamma/\delta$.

We can verify this using the code:

```python
u0 = [c/d,a/b]

# Solve ODE
u = odeint(model,u0,t,args=(a,b,c,d))

plt.plot(t, u)
```

![Equilibrium plots for the Predator-Prey Model](/static/images/week9/predatorpreyequilibrium.png){style="width: 80%; max-width: 700px;"}


Notice that moving away from the equilibrium values, even by a small amount, yields nontrivial solutions:

```python
eps = 0.01
u0 = [c/d+eps,a/b+eps]

# Solve ODE
u = odeint(model,u0,t,args=(a,b,c,d))

plt.plot(t, u)
```

![Oscillations in the Predator Prey Model](/static/images/week9/predatorpreyoscillate.png){style="width: 80%; max-width: 600px;"}


## 10.4) Dynamical systems Example 2: The Logistic Map

Many dynamical systems exhibit *chaotic* behaviour: they are hard to predict over any length of time, and very complicated structures appear in phase portraits produced from them.

### The logistic map

We have previously considered the logistic equation

$$ \frac{\mathrm{d}x}{\mathrm{d}t} = rx(1-x) $$

There is a discrete form of this equation, known as the *logistic map*:

$$ x_{n+1} = rx_n(1-x_n) $$

for $r$ a constant. That is, for a given starting value $x_0$ we can produce an infinite family of terms $x_n$ using the above inductive formula.

Although the logistic map is very simply, it turns out that it exhibits extremely complicated behaviour as the constant $r$ is varied.

To conclude this module we shall recreate the so-called *period doubling cascade*, depicted in the following plot:

![The Logistic Map](/static/images/week9/logisticmap.png){style="width: 80%; max-width: 600px;"}


### Plotting $x_n$

Set $r = 1.5$. We'll first write a function that can take $x_n$ and return $x_{n+1} = r x_n (1-x_n)$, for a given choice of $x_n$:

```python
def x_iter(x,r):
    """
    Applies logistic map to x and r
    """
    return r*x*(1-x)

r = 1.5
x = 0.2
print(x_iter(x,r))     
```
```output
0.24000000000000005
```

Using this function we produce an array of the values $x_i$ for $n \le 100$:


```python
import numpy as np
import matplotlib.pyplot as plt

def x_iter(x,r):
    """
    Applies logistic map to x and r
    """
    return r*x*(1-x)

r = 1.5
x = np.zeros(100)
x[0] = 0.2
for n in range(len(x)-1):
	x[n+1] = x_iter(x[n],r)

plt.plot(x)
print("final value: x = {}".format(x[-1]))
```
```output
final value: x = 0.3333333333333333
```


![Logistic Map solution with r = 1.5](/static/images/week9/r1.5.png){style="width: 70%; max-width: 450px;"}


Now let's consider how the above plot changes we we increase $r$. Initially, there does not appear to be much dependence on $r$. Here we have set $r=2.5$:

```python
# ...
r = 2.5
# ...
plt.plot(x)
print("final value: x = {}".format(x[-1]))
```
```output
final value: x = 0.6000000000000001
```

![Logistic Map solution with r = 2.5](/static/images/week9/r2.5.png){style="width: 70%; max-width: 450px;"}

<div class="exercise" markdown=true>


### Exercise 10.4

Repeat the above code with $r$ equal to $2.8, 3.25, 3.5, 3.75, 4$. You should obtain some of the plots contained in the following animation:

![Logistic Map Animation](/static/images/week9/logistic_animation.gif){style="width: 80%; max-width: 600px;"}

You are not required to reproduce this animation, [but here is a description of how it can be made](https://ncl.instructure.com/courses/59162/modules/items/3399035).

</div>

### Bifurcations

You'll notice that above $r = 3$ the long term behaviour of $x_n$ is to oscillate. The last $5$ values in the $x$ array for $r=2.8$ are

```python
# ...
r = 2.8
# ...
print(x[-5:])
```
```output
[0.64285714 0.64285714 0.64285714 0.64285714 0.64285714]
```

![Logistic Map solution with r = 2.8](/static/images/week9/r2.8.png){style="width: 70%; max-width: 450px;"}

I.e. $x_n$ tends to a constant as $n$ tends to infinity.

On the other hand for $r = 3.1$ we have

```python
# ...
r = 3.1
# ...
print(x[-5:])
```
```output
[0.55801413 0.76456652 0.55801413 0.76456652 0.55801413]
```

![Logistic Map solution with r = 3.1](/static/images/week9/r3.1.png){style="width: 70%; max-width: 450px;"}

I.e. $x_n$ oscillates between two values.

Above approximately $r = 3.5$ the values $x_n$ oscillates between $4$ values:

```python
# ...
r = 3.5
# ...
print(x[-10:])
```
```output
[0.87499726 0.38281968 0.82694071 0.50088421 0.87499726 0.38281968
 0.82694071 0.50088421 0.87499726 0.38281968]

```

![Logistic Map solution with r = 3.5](/static/images/week9/r3.5.png){style="width: 70%; max-width: 450px;"}


Above approximately $r = 3.55$ the $x_n$ oscillates between $8$ values:

```python
# ...
r = 3.55
# ...
print(x[-10:])
```
```output
[0.88737072 0.35480092 0.81265616 0.54047375 0.88168466 0.37032472
 0.82780434 0.50603232 0.88737082 0.35480066]
```

![Logistic Map solution with r = 3.55](/static/images/week9/r3.55.png){style="width: 70%; max-width: 450px;"}

It turns out that increase $r$ the values $x_n$ oscillate between $16$ values, then $32$ values, then $64$ values, and so on.

This is known as a *period doubling cascade*, and continues until $r \approx 3.56995$. At this value of $r$ the behaviour of the logistic map becomes chaotic (a full description is outside the scope of this module). E.g. at $r = 4$ we have

![Logistic Map solution with r = 4.0](/static/images/week9/r4.0.png){style="width: 70%; max-width: 450px;"}


### Capturing the period double cascade

We'd like to capture the values that $x_n$ is oscillating between (in order to plot them) for each value of $r$. As an example set $r = 3.5$, at which point $x_n$ oscillates between $4$ values. Looking at the plot of $x_n$ above we can see that we must ignore some initial values of $x_n$. To do so we apply $100$ iterations of the logistic map before capturing the values $x_n$:

```python
r = 3.5
x = 0.2
# List to store values
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

Notice that we do not need to store the full list of values $x_n$: we simply want the values $x_n$ is oscillating between. These values are stored in a list `v`, and to a fixed number of decimal places to avoid number precision issues.

To create the plot at the top of the section we now plot these values on the vertical axis for several $r$ values on the horizontal axis. We do this by putting the above code in a loop and adding a marker to the plot for each solution. The full code is:

```python
import numpy as np
import matplotlib.pyplot as plt

def x_iter(x,r):
    """
    Applies logistic map to x and r
    """
    return r*x*(1-x)

x = 0.2
for r in np.linspace(2.7,4,250):
    # List to store unique values for this r
    v = []
    for n in range(200):
        x = x_iter(x,r)
        if n > 100 and round(x,6) not in v:
            v.append(round(x,6))
    # x value for each v value to make the plot
    rx = r*np.ones(len(v))          
    plt.plot(rx,v,'ko',markersize=0.5)

plt.xlabel('r')
plt.ylabel('x')
```

You may wish to change the $250$ values for `r` to $500$ or even $1000$ to produce a higher quality plot. If so, use the following options

```python
plt.figure(figsize=(16,8))
plt.rcParams.update({'font.size': 30})
```

![The Logistic Map](/static/images/week9/logisticmap.png){style="width: 80%; max-width: 600px;"}

The study of dynamical systems like the logistic map is an active area of research. For example, there are the stable ranges where the period stays the same as $r$ changes: can we predict where they will lie just from the form of the equation $x_{n+1} = r x_n (1 - x_n )$? It turns out that is is (sometimes) possible, and is described by a number known as the *Feigenbaum constant*.

## Next week

Week 11 is a revision week. Please don't hesitate to email me with any questions or topics (from the Assessments, Handouts, Test Yourself quizzes, or mock exams) that you'd like to go through.







