[Click here to open this handout in a new browser tab](#){target="_blank"}

# Handout 9 - Differential equations II

## Recap: odeint

Last week we numerically solved (systems of) first-order ODEs using the SciPy function `odeint`. For example

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# function on the rhs of dy/dt
def rhs(y,t):
    dydt = - y/2
    return dydt

# initial condition
y0 = 5

# t array
t = np.linspace(0,5,100)

# solve ODE
y = odeint(rhs,y0,t)

# plot results
plt.plot(t,y)
plt.xlabel('t')
plt.ylabel('y(t)')
```

This week we'll investigate the mathematics behind `odeint` and other numerical methods for ODEs.

## The Euler method

Recall our running example from Week 8, the following first-order ODE with an initial condition

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$

First we'll apply the *Euler method* to numerically solve this and other ODEs.

The Euler method proceeds by using what we know about the solution $y$ at $t=0$:

1) $y(0)=5$ 

2) $\frac{dy}{dt}=-\frac{5}{2}$

![The Euler Method](/static/images/week6/explanation3.png){width=80%}

We can use this information to estimate $y(0+nh)$, for $h$ the *step size* and $n=1,2,3,\ldots$:

![The Euler Method](/static/images/week6/explanation5.png){width=80%}

Notice that the gradient of $y$ is given by the differential equation (as $y$ is a solution)

$$ \frac{dy}{dt}=-\frac{y}{2} $$

Suppose that $y_n$ is an estimated value of the solution $y$. The next estimated value is the intersection of the line of gradient $\frac{dy}{dt}(t_n)$ and the vertical line at $t_{n+1} = t_n + h$. Therefore

$$y_{n+1} = y_{n} + \left(-\frac{y_n}{2}\right)h $$

This process is outlined in the following sequence of diagrams (note that we have set $h=1$ for illustrative purposes):

![Euler Method animation](/static/images/week6/euler.gif){width=80%}

### Implementing the Euler method

Suppose that we have stored the values $t_n = nh$, and $y_n$ in the arrays `t` and `y`, respectively. We could implement the equation involving $y_{n+1}$ and $y_n$ above in Python as

```python
y[n+1] = y[n] + (-y[n]/2)*h
```

Let's complete this implementation, over the $t$ range $[0,1,2,3,4,5]$ (so that we have set $h=1$). We create this array in Python as

```python
t = np.arange(0,6)
```

Next initialise an array of the correct length to store the values $y_n$

```python
y = np.zeros(len(t))
```

We are given the initial condition $y(0) = 5$, and override the first value of `y` to reflect this

```python
y[0] = 5
```

We can then fill in the remaining elements of `y` using the equation

$$y_{n+1} = y_{n} + \left(-\frac{y_n}{2}\right) $$

(recall that we have set $h=1$), using a `for` loop to iterate the following code

```python
y[n+1] = y[n] + (-y[n]/2)
```

In general, to apply Euler's method to the first-order ODE with initial condition

$$ \frac{dy}{dt} = f(y,t),\quad y(0) = c$$

we use the equation

$$ y_{n+1} = y_{n} + h f(y_n,t_n) $$

where the step size $h$ is the distance between two consecutive $t$ values. This can be implemented in Python as follows

```python
import numpy as np
import matplotlib.pyplot as plt

# Set up t array to estimate over
# Changing t value separation will change h
t = np.linspace(0,5,10)
y = np.zeros(len(t))
h = t[1]-t[0]

# Right-hand side of ODE
def f(y,t):
    return # Add mathematical expression for right-hand side here

# Initial condition
y[0] = c

# Iterative step
for n in range(len(t)-1):
    y[n+1] = y[n] + h * (f(y[n],t[n]))

# Plot numerical solution
plt.plot(t,y,'-o')
```

For our running example

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$

the code becomes

```python
import numpy as np
import matplotlib.pyplot as plt

# Set up t array to estimate over
# Changing t value separation will change h
t = np.linspace(0,5,10)
y = np.zeros(len(t))
h = t[1]-t[0]

# Initial condition
y[0] = 5

def f(y,t):
    return -y/2

# Iterative step
for n in range(len(t)-1):
    y[n+1] = y[n] + h * (f(y[n],t[n]))

# Plot numerical solution
plt.plot(t,y,'-o')
```

### Accuracy of the Euler method

In the case of our running example

$$ \frac{dy}{dt}=-\frac{y}{2}, \quad y(0)=5 $$

we can find an exact solution by hand, as the equation is *separable* i.e. it can be rearranged to separate the variables $y$ and $t$.

Specifically, rearranging the ODE we obtain

$$ \frac{dy}{y} = -\frac{dt}{2} $$

Integrating both sides yields

$$ \log(y) = -\frac{t}{2} + C $$

for $C$ a constant of integration. Exponentiating to recover $y$ we obtain

$$ y = e^{-t/2 + C} = Ae^{-t/2} $$

where $A = e^C$.

Applying the initial condition $y(0) = 5$ we evaluate $A$ as

$$ Ae^0 = 5 = A $$

Thus the exact solution to the ODE is

$$ y(t) = 5e^{-t/2} $$

We can add a plot of this exact solution to the plot of the numerical solution obtained above via

```python
t1 = np.linspace(0,5,100)
plt.plot(t1,5*np.exp(-t1/2))
plt.legend(['Euler Method','Exact solution'])
```

Repeating this process at different values of the step size $h$ we obtain:

![The Euler Method Animation](/static/images/week6/euler_animation.gif){width=80%}

Specifically, changing the `t` arrays in the above code to include more points will reduce the step size. It is clear that reducing the step size increases the accuracy of the numerical solution; we'll return to this below.

<div class="exercise" markdown=true>

### Exercise 9.1


<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81775/euler-method-adapt-existing/embed/?token=5dc5cf01-1b69-403a-bef7-b2f798c6fae1" data-id="exercise-7-1" data-cta="Show Exercise"></numbas-embed>

</div>


### An Euler method function

To make our lives easier we can write the algorithm described above as a (Python) function. Its arguments should be

* $f(y,t)$, the right-hand side of the ODE
* $y0$, an initial condition i.e. $y(0) = y_0$
* `t`, an array of $t$ values at which to approximate a solution

and it should return an array `y` containing the approximate vales of the solution. One way to write such a function is as follows

```python
def euler(f,y0,t):
	"""
	Returns the numerical solution y(t) for an initial value problem
	dy/dt = f(y,t), y(0) = y0
	over an array t
	"""

    y = np.zeros(len(t))   
    y[0] = y0            

    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f(y[n],t[n])*(t[n+1]-t[n])
        
    return y
```

Notice that the step size `h` has been replaced with `(t[n+1]-t[n])`. If `t` is an array of linearly spaced points this is equivalent to the syntax

```python
y[n+1] = y[n] + h * (f(y[n],t[n]))
```

If the points of `t` are not linearly spaced the function `euler` can still apply the Euler method e.g. `t = [0,2,3.5,4,6]`.

As an example, we can repeat the analysis in the previous section using the syntax

```python
t = np.linspace(0,10,20)
y0 = 5

def rhs(y,t):
    return -y/2

y = euler(rhs,y0,t)
plt.plot(t,y)
```

or using a lambda function:

```python
t = np.arange(0,5)
y0 = 5
y = euler(lambda y,t: -y/2, y0, t)
plt.plot(t,y)
```

### Dependence on $t$

Notice that the function `euler` can also be used to apply the Euler method to ODEs in which the right-hand side $f(y,t)$ explicitly depends on $t$. For example, consider the ODE with initial condition

$$ \frac{dy}{dt}=yt,\quad y(0)=1 $$

We can solve this as follows (notice that we only need to change the `rhs` function and initial condition)

```python
t = np.linspace(0,10,20)
y0 = 1

def rhs(y,t):
    return t*y

y = euler(rhs,y0,t)
# or y = euler(lambda t,y: t*y, y0, t)
```

<div class="exercise" markdown=true>


### Exercise 9.2

In this Exercise the right-hand side $f(y,t)$ is complicated enough that the Euler method does not produce a very good approximation of the solution, even at small step sizes.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/82104/euler-method-adapt-existing-function/embed/?token=ec57777a-1cf7-4f44-a411-7f5612a157bf" data-id="exercise-7-2" data-cta="Show Exercise"></numbas-embed>

</div>

### Rewriting to specify $h$

In the implementation above the step size $h$ is inferred from the `t` array i.e. $h$ is given by `(t[n+1]-t[n])`.

Suppose we wish to apply the method at specific values of $h$. Rather than having to reverse engineer the desired $h$ value by picking the correct array, we can amend our code to take $h$ as an argument:

```python
import numpy as np
import matplotlib.pyplot as plt

tmax = 5
h = 0.25
t = np.arange(0,tmax+h,h)
y0 = 1

def rhs(y,t):
    return t*y

y = euler(rhs,y0,t)
plt.plot(t,y)
```

## Truncation errors

Recall that the Euler method does not produce an exact solution to a differential equation, only an approximation of such a solution. The difference between the approximate solution and the exact solution is known as the **truncation error**. We'll now investigate this error in more detail, first by splitting it into two sources: local truncation error (LTE), associated with errors in a single step, and global truncation error (GTE), associated with the method as a whole.

### Local truncation error

The *local truncation error* (LTE) is the error associated with a single iterative step e.g. the error introduced when calculating $y_1 = y(t_1)$ from $y_0 = y(t_0)$.

Suppose that $y(t)$ is an exact solution to the first-order ODE (i.e. not an approximate solution as produced by the Euler method)

$$ \frac{dy}{dt} = f(y,t) $$

Consider the Taylor series of $y$ about $t_1 = t_0 +h$

$$ y_1 = y(t_1) = y(t_{0}+h)=y(t_{0})+hy'(t_{0})+{\frac {1}{2}}h^{2}y''(t_{0})+\mathcal{O}(h^{3}) $$

where $y'(t)= \frac{dy}{dt} = f(y,t)$ as $y$ is a solution to the ODE. It follows that $y_1$ is given by the following formula

$$ y_1 = y_0 +hf(t_0,y_0)+\mathcal{O}(h^{2}) $$

where $\mathcal{O}(h^{2})$ denotes terms of order $h^2$.

The algorithm for the Euler method yields the following 

$$ y_1 \approx y_0 +hf(t_0,y_0)$$

It follows that the LTE introduced at each step of the Euler method is $\mathcal{O}(h^{2})$.

For example, in the case of our running example $y' = -\frac{y}{2}, \quad y(0)=5$ we have

```python
def rhs(y,t):
    return -(1/2)*y

h = 1
y0 = 5
t0 = 0
t1 = t0+h

# Euler solution using
y1_euler = y0 + h*rhs(y0,t0)
y1_exact = 5*np.exp(-(1/2)*t1)
```

(recall that we found the exact solution to be $y(t)=5 e^{-(1/2)*t})$ above). The LTE is given by `y1_euler - y1_exact`, which is $-0.533\ldots$ in this case. 

Let's vary the step size $h$ and observe how the LTE is affected. We only want to consider how the magnitude of the LTE changes (not its sign), so we take the absolute value `abs(y1_euler - y1_exact)`:

```python
import numpy as np
import matplotlib.pyplot as plt

def rhs(y,t):
    return -(1/2)*y

h_values = [0.01,0.05,0.1,0.15,0.20,0.25,0.3,0.35,0.4]
errors = []
y0 = 5
t0 = 0

for h in h_values:
    t1 = t0+h
    y1_euler = y0 + h*rhs(y0,t0)
    y1_exact = 5*np.exp(-(1/2)*t1)
    errors.append(abs(y1_exact - y1_euler))
    
    
plt.plot(h_values,errors,'-o')
```

![Plot of the local truncation error against stepsize h](/static/images/week3/lte.png){width=80%}

There are two interesting observations to make:

* The plot approximates the graph of $x^2$, with a single minimum i.e. there is an optimum $h$ value at which the LTE is a minimum.
* After this optimum $h$ value the LTE increases; it turns out that it will continue to increase, so that $h$ values above the optimum value tend not to produce meaningful results.

### Global truncation error

The *global truncation error* (GTE) is the difference between the value of the exact solution $y(t)$ and approximation of $y(t)$ produced by the Euler method at some time $t$. At the time value $t$ the number of iterative steps that have taken place is $(t-t_0)/h$ i.e. it is proportional to $\frac{1}{h}$. Recall that the LTE (introduced at each step) is proportional to $h^2$. It follows that we can expect the GTE to be proportional to $h$. In other words, the Euler method is considered to be an $\mathcal{O}(h)$ method. (In practice, the GTE depends nontrivially on the LTE, which in turn vary in the range $[t_0,t]$.) By comparison, the classical *Runge-Kutta method* as covered below is an $\mathcal{O}(h^4)$ method.

## Stability

The term *stability* is used in many different contexts throughout mathematics. As a general theme, something is *stable* if it evolves in a predictable way, while something is *unstable* if its evolution is hard (or even impossible) to predict.

In the specific context of numerically solving differential equations *stability* refers to how the accuracy of the numerical solution depends on the input data. The Euler method depends on the step size $h$. As we shall see, there is a critical point $h_{\ast}$ such that values $h<h_{\ast}$ the numerical solution obtained is *stable*, and behaves predictably, while for values $h>h_{\ast}$ the resulting solution is *unstable*, and ceases to be a good approximation of the exact solution.

Consider the first-order ODE with initial condition

$$\frac{\mathrm{d}y}{\mathrm{d}t} = -2y, \quad y(0) = 1$$

By separation of variables as above we obtain the exact solution $y(t) = e^{-2t}$. Note that $y(t) = e^{-2t} \to 0$ as $t \to \infty$.

We can apply the Euler method with step sizes $h = 0.25, 0.5, 1, 1.25$ using the following code:

```python
import numpy as np
import matplotlib.pyplot as plt

def rhs(y,t):
    return -2*y

y0 = 1
tmax = 5
h_values = [0.25,0.5,1,1.25]

leg = []

for h in h_values: 
    
    t = np.arange(0,tmax+h,h)
    y = euler(rhs,y0,t)
    
    plt.plot(t,y,'-o')
    leg.append('h = {}'.format(h))

plt.legend(leg)
plt.xlabel('t')
plt.ylabel('y(t)')
```

![Plot of the Euler Solution with h = 0.1, 0.5, 1.0, 1.25](/static/images/week3/unstable.png){width=80%}

Notice that the numerical solution obtained for $h=1.25$ is clearly not a good approximation to the exact solution. In particular, it does not appear to be tending to $0$ as $t$ tends to $\infty$:

![Plot of the Euler Solution with h = 1.25](/static/images/week3/blownup.png){width=80%}

By extending the range further we can show that at $t = 200$ this numerical solution is $1.5 \times 10^{28}$, whereas the exact solution is $e^{-400} \approx 1.95 \times 10^{-174}$.

What is causing the Euler method to fail so badly at $h=1.25$? We know that the Euler method produces the $(n+1)$-th estimate from the $n$-th using the formula

$$y_{n+1} = y_n - 2hy_n = (1-2h)y_n$$

Further, as $y_n = (1-2h)y_{n-1}$ we have

$$ y_{n+1} = y_n - 2hy_n = (1-2h)y_n = (1-2h)^2y_{n-1} $$

Repeating the above step many times, we reach the equation

$$ y_{n+1} =  (1-2h)^{n+1} y_0 $$

It follows that $y_n \to 0$ as $t\to\infty$ if only if $|1-2h| < 1$, or equivalently $h < 1$. It follows that $h_{\ast} = 1$ is the critical value of the step size, beneath which the numerical solutions are stable (and above which they are unstable).

We can verify this by plotting the numerical solutions near $h_{\ast}$:

![Plot of the Euler Solution with h = 0.95, 1.0, 1.05](/static/images/week3/critical.png){width=80%}

<div class="exercise" markdown=true>


### Exercise 9.3 

Recall that such stability concerns did not occur when we altered the step size when solving the previous example

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2}, y(0) = 5$$

This Exercise investigates this further.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/83998/stability-of-euler-method-for-dy-dx-y-2/embed/?token=c0cccc44-fe65-4c76-b671-9d644e98d792" data-id="exercise-7-3" data-cta="Show Exercise"></numbas-embed>

</div>

## The Euler method applied to a system of ODEs

Recall the SIR model from Week 8:

\begin{align}
\frac{dS}{dt}&=-\beta IS, \\
\frac{dI}{dt}&=\beta IS -\gamma I \\
\frac{dR}{dt}&= \gamma I
\end{align}

where $S$, $I$, and $R$ depend on $t$, and $\beta$ and $\gamma$ are constants. For the purposes of this example we'll use the initial conditions $S(0)=99$, $I(0)=1$, $R(0)=0$, and constant values $\beta = 0.002$, $\gamma = 0.5$.

We can extend the Euler method to such systems of ODEs by applying the iterative step to each function $S$, $I$, and $R$ simultaneously:

```python
import numpy as np
import matplotlib.pyplot as plt

# Initialise arrays
t = np.linspace(0,20,50)
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))

# Initial conditions
S[0] = 999
I[0] = 1
R[0] = 0

# Parameters
b = 0.002
c = 0.5

for n in range(len(t)-1):
    S[n+1] = S[n] + (t[n+1]-t[n]) * (-b*I[n]*S[n])
    I[n+1] = I[n] + (t[n+1]-t[n]) * (b*I[n]*S[n] - c*I[n])
    R[n+1] = R[n] + (t[n+1]-t[n]) * (c*I[n])

# Make a plot
plt.plot(t,S)
plt.plot(t,I)
plt.plot(t,R)
plt.xlabel('t')
plt.title('SIR Model with the Euler Method')
plt.legend(['S(t)','I(t)','R(t)'])
```

This yields the plot:
<img src="/static/images/week7/sir.png" alt="SIR Model" style="width: 100%; max-width: 700px; margin: 20px 0;"/>

Compare this to the plot found using `odeint` in Exercise 8.4 (in Handout 8).

<p>Investigate the stability of this model by varying the step size. You should find that the method becomes unstable at a certain point.</p>

<div class="exercise" markdown=true>

### Exercise 9.4 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/83147/lotka-volterra-euler-method/embed/?token=127848d8-83fd-4f19-a6e5-ed411d26c120" data-id="exercise-7-5" data-cta="Show Exercise"></numbas-embed>

</div>

## Runge-Kutte Methods

The iterative step of the Euler method can be described as follows:

1. Plug the value of the $n$-th estimate $y_n$ into the ODE $y' = f(y,t)$ to find the gradient of the numerical solution at this point.
2. Trace the line with this gradient to the next time value, $t_{n+1} = t_n +h$, to calculate the next estimate $y_{n+1}$.

Notice that only one evaluation of the gradient is used in the Euler method. It is therefore natural to ask if we can devise more accurate numerical methods by evaluating the gradient at a greater number of points.

A family of algorithms that use this construction are known as *Runge-Kutta methods*. One of the most widely-used is the fourth-order Runge-Kutta method that makes four evaluations of $y'$: once at the initial point $t_n$, two evaluations at the midpoint $t_n + h/2$, and one evaluation at the endpoint $t_n + h$ during the iterative step. A schematic of this process is:

![Runge-Kutte Method](/static/images/week7/rk4.png){width=60%}

<small style="margin-bottom: 20px;">Image: Wikipedia</small>

The elements of the above schematic are:

* $k_{1}$ is the slope of the tangent line at initial point $t_0$
* ${\displaystyle k_{2}}$ is a slope at the midpoint $(t_0 + h/2)$
* ${\displaystyle k_{3}}$ is another slope at the midpoint
* ${\displaystyle k_{4}}$ is a slope at the endpoint $t_0 + h$

The different slopes at the midpoint are calculated using different initial slopes at $t_0$, and a weighted average is used to produce the next estimate $y_{n+1}$, as described below.

Overall, this method is more stable and accurate than the Euler method. This construction can be pushed further by making more evaluations of the gradient, but, as is common in mathematics, there is a trade off between speed and precision. The fourth-order Rung-Kutta method strikes a balance between accuracy of the approximation and time needed to compute.

### The method in detail

The classical Runge-Kutta method, sometimes simply known as the Runge-Kutta method or RK4 (for fourth order, numerically solves the first-order ODE with initial condition

\[ \frac{dy}{dt}=f(y,t) ,\quad y(0) = y_0\] 

using the iterative formula

\[ y_{n+1}=y_{n}+\frac{1}{6}h\left(k_1+2k_2+2k_3+k_4\right) \]

where 

\[
\begin{align}
k_1 &= f(y_n,t_n) \\[0.7em]
k_2 &= f\left(y_n+h\frac{k_1}{2},t_n+\frac{h}{2}\right) \\[0.7em]
k_3 &= f\left(y_n+h\frac{k_2}{2},t_n+\frac{h}{2}\right) \\[0.7em]
k_4 &= f\left(y_n+hk_3,t_n+h\right)
\end{align}
\]

It can be shown that RK4 is significantly more accurate than the Euler method, as can be seen when using it to numerically solve our running example:

![The Runge-Kutte Method](/static/images/week7/runge-kutta-1.png){width=80%}

Specifically, it can be shown that the GTE for RK4 is $\mathcal{O}(h^4)$ (recall the the Euler method was $\mathcal{O}(h)$). (Proving this is beyond the scope of this module.)

<div class="exercise" markdown=true>

### Exercise 9.5 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/82425/runge-kutta-method/embed/?token=e5c1d5bd-c2ea-46f2-9e94-579d35e787d7" data-id="exercise-7-6" data-cta="Show Exercise"></numbas-embed>

</div>


## Next week

Next week we'll conclude the testable content of the module by looking at some dynamical systems and their Pyton implementation
