# Handout 6

Welcome to handout 6! This week we're looking at solutions to differential equations.

## Introduction

Ordinary Differential Equations (ODEs) are very common in mathematical modelling and only a small sub-set can be solved exactly. So numerical methods for solving ODEs are an extremely valuable tool.

To solve a general first-order ODE, the initial value problem

$$\frac{\mathrm{d}y}{\mathrm{d}t}(t) = f(t,y), \quad y(t_0) = y_0 $$

we need to find $y(t)$ for all $t$ in the domain of interest. 

If $f(t,y) = p(t)q(y)$, the ODE is separable and the exact solution can be found directly by integration, so you might expect to see some similarity between quadrature methods for integration (that we saw last week) and numerical methods to solve ODEs. This is the case: just like the quadrature methods, the numerical solutions for ODEs break down the continuous variables $t$ and $y$ into lots of closely separated discrete values, $t_0,t_1,\ldots t_n$ and $y_0,y_1,\ldots y_n$, where $y_i = y(t_i)$. 

The goal is to find all of the $y_i$ in the domain of $t$ that is of interest. These $y(t_i)$ are then an approximation to the function $y(t)$.

## Solving ODEs with a computer

As in previous sections, we will be looking at built-in functions and then the underlying algorithms, which I'll talk about only briefly here to set the scene.

Consider the differential equation

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2} , \quad y(0)=5 $$

This is an initial value problem, where we know $y(t=0)$ and would like to infer how $y(t)$ evolves. The idea behind numerical methods for solving an ODE is that we can use what we know about $y$ at $t = 0$. Specifically that is: 

1) $y(0)=5$; and

2) $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}t}(0)=-\frac{5}{2}$,

![](/static/images/week6/explanation3.png){width=80%}

to estimate $y$ at some later point

![](/static/images/week6/explanation5.png){width=80%}

Functions such as `odeint`, that we'll meet in a moment, use this idea, or a sophisticated version of it at least, to solve initial value problems. We'll take a look in more depth at how these functions work next week.


## SciPy `odeint`

### Solving first-order ODEs

In this section we will begin by solving first-order ordinary differential equations, the type that you may well be able to solve with pen and paper, but we will actually be solving them numerically using SciPy's ODE solver, `odeint`.

Again we'll use the initial value problem

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2} , \quad y(0)=5 $$

<!--<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=c36e3b7f-592f-43ac-9344-ac820156e7d1&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>-->

The whole thing goes like this:

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

The magic happens in this line:
```python
y = odeint(rhs,y0,t)
```

The fist argument to `odeint` is the function handle `rhs` which is defined above it in the code. Note that `rhs` takes two input arguments `rhs(y,t)` (and note in that order) as it could depend on either or both of `t` and `y`.

The second argument to `odeint` is our initial data, in this case the value of $y(0)$, which we have set in the variable `y0`.

The final argument is an array `t` (or whatever the independent variable is). 

The output of `odeint` is an array `y` which is of the same length as `t` (slightly different dimensions which I'll talk about in a sec...). So can be plotted:

![](/static/images/week6/odeint1.png){width=80%}


You should have a plot, but we should check it... The analytic solution to this initial value problem is (check for yourself)

$$ y(t)=y(0)e^{-t/2} $$

Let's plot that over the top:
```python
t1 = np.linspace(0,5,100)
plt.plot(t1, 5*np.exp(-t1/2),'--')
```
You should find that this overlays your `odeint` solution.

#### Step size {: .interlude}

We'll look more closely next week at the accuracy of methods to solve differential equations. As a preview, try out the code above, varying the `t` array.

Start with 

```python
t = np.linspace(0,5,5)
```

i.e. 5 points in `t` and therefore `y`, and then increase the number of values in the array (which is reducing the step size in the method). You'll see that the more values that you include in `t`, the more accurate `odeint` is, when compared to the known solution.

#### Structure of y

Try out

```python
print(y)
```
```output
[[5.        ]
 [4.87531833]
 [4.7537457 ]
 [4.63520466]
 [...]]
```

```python
y.shape
```
```output
(100, 1)
```

You will see that `y` is a 2D array with 1 column and 100 rows. Why would it do that? Well, this is a very deliberate design decision by `odeint`: as we will see, it will use the space in further columns to handle systems of differential equations.

### Exercise 6.1 {: .exercise}

Here's an exercise to adapt the above code for a different initial value problem.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81771/odeint-adapt-existing-code/embed/?token=6e34466e-1416-486a-b8c8-871bfe441306" data-id="exercise-6-1" data-cta="Show Exercise"></numbas-embed>


### Passing arguments from odeint

Additional arguments can be passed to the model function as follows, for example two parameters `a` and `b`:

```python
def rhs(y,t,a,b):
    dydt = - a/2 + b
    return dydt
```

Then the `odeint` call would change as follows:

```python
y = odeint(rhs,y0,t,args=(2,3))
```

to use `a` = 2 and `b` = 3.

#### The `args` parameter 

The `args` parameter is a bit of a strange beast. The `odeint` function uses this information when it does it's number crunching, sending the values in the `args` parameter after `y` and `t` in the call to the `model` function. It's even stranger because of the type of variable

```python
x = (2,3)
type(x)
```
```output
tuple
```

A tuple is very similar to a list: the main difference is that the values are unchangeable in terms of value or order. One of their advantages is that the use and storage of tuples can be computationally more efficient than lists. So here's the strange bit: in order to differentiate a tuple with one value from a number in brackets like `(3)`, we include a trailing comma:

```python
x=(2)
type(x)
```
```output
int
```

```python
x=(2,)
type(x)
```
```output
tuple
```

We'll need to use this syntax if we're sending one parameter to our function.

### Exercise 6.2 {: .exercise}

Let's try this weird syntax out!

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/108571/odeint-single-variable/embed/?token=fa292f75-287d-45b7-ab7e-20b7c39e372d" data-id="exercise-6-2" data-cta="Show Exercise"></numbas-embed>







### Solving systems of ODEs 

Solving a system of ODEs in Python sounds tricky. We can easily see how we could call `odeint` several times in a row. But if the variables in our equations depend on eachother it just won't work like that mathematically. Fortunately `odeint` can handle this too!

Consider the following system of ODEs. I'm using a real-life model from the field of epidemiology:

\begin{align}
\frac{dS}{dt}&=-\beta IS + \gamma I, \\
\frac{dI}{dt}&=\beta IS -\gamma I
\end{align}

The number of individuals in a population susceptible to a virus is $S(t)$ and the number infected is $I(t)$, with two parameters: $\beta > 0$ is the rate of infection and $1/\gamma > 0$ is the time taken to recover. I've called these `b` and `c` in the code.

<!--<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=0df51acc-3244-4dd6-ba87-ac820156cfa0&autoplay=false&offerviewer=true&showtitle=true&showbrand=false&start=0&interactivity=all" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>-->

Things are a bit more complicated here. Firstly here's the function which was `rhs` and I've now called `model`:

```python
def model(y, t, b, c):
    S, I = y              # reads in y and assigns to S and I
    dSdt = -b*I*S + c*I   # rhs of dS/dt
    dIdt = b*I*S - c*I    # rhs of dI/dt 
    return [dSdt, dIdt]   # important: this way around!
```

Firstly note the arguments `(y, t, b, c)`: we're sending additional parameters `b` and `c` to our function.

Now going through line by line, note that `y` is going to be a list of two values. If you were to print it then you would see something like this at each iteration

```
[999.  1.]
```

and those two values can be placed into variables `S` and `I` like this:

```python
S, I = [999, 1]
```

to set `S` to 999 and `I` to 1. So the first line here just unpacks the `S` and `I` values which are being stored in `y`.

Note this is equivalent to ans just a neater way of doing 

```python
S = y[0]
I = y[1]
```

The variables `dSdt` and `dIdt` contain the right hand side of the two differential equations. We then pack those back up into a list in the return statement (which is just what `odeint` needs).

Now instruct `odeint` to call this function. We could choose to start with 999 susceptible individuals and 1 infected and look at say $0 \le t \le 20$.

```python
# Parameters
b = 0.002
c = 0.5

# Initial conditions
y0 = [999,1]

# Time points
t = np.linspace(0,20,100)

# Solve ODE
y = odeint(model,y0,t,args=(b,c))
```

Note that, just like we store S and I in a two element list, we start `odeint` off with a list for `y0`. 

The additional argument `args` sends the extra parameters `b` and `c` through to the `model` function.

The whole thing looks like this:


```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t, b, c):
    S, I = y              # reads in y and assigns to S and I
    dSdt = -b*I*S + c*I   # rhs of dS/dt
    dIdt = b*I*S - c*I    # rhs of dI/dt 
    return [dSdt, dIdt]   # important: this way around!

# Parameters
b = 0.002
c = 0.5

# Initial conditions
y0 = [999,1]

# Time points
t = np.linspace(0,20,100)

# Solve ODE
y = odeint(model,[999,1],t, args=(b,c))

plt.plot(t,y[:,0])   # y[:,0] contains S(t)
plt.plot(t,y[:,1])   # y[:,1] contains I(t)
plt.legend(['S(t)','I(t)'])
plt.xlabel('t')
plt.title('SI Model')
```

You should get the below plot:

![](/static/images/week6/simodel.png){width=90%}

Note that Matplotlib is quite clever, and the two lines which pick out columns for $S(t)$ and $I(t)$

```python
plt.plot(t,y[:,0])
plt.plot(t,y[:,1])
```

can also be written

```python
plt.plot(t,y)
```

### SIR models

There are many variations of the above for epidemiology, most famously the SIR model, which has an additional class of person denoted R for recovered (and assumed immune). It was proposed as a model to explain the rapid rise and fall in the number of infections observed in epidemics such as the plague (1600s) and cholera (1865) outbreaks in London and has been used to model the current Covid-19 pandemic. Here, instead of infected people moving back into the susceptible class, they move to recovered. The term $+\beta I$ moves to  $\frac{dR}{dt}$, such that $S(t)$ always declines and $R(t)$ always increases.


\begin{align}
\frac{dS}{dt}&=-\beta IS, \\
\frac{dI}{dt}&=\beta IS -\gamma I \\
\frac{dR}{dt}&= \gamma I
\end{align}

### Exercise 6.3 {: .exercise}

In this exercise we'll have a go at adapting the SI code to solve the SIR model.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/82126/sir-model/embed/?token=61696d1d-5ff6-4510-9acf-da31bc3774aa" data-id="exercise-6-3" data-cta="Show Exercise"></numbas-embed>



### More models of epidemiology

If you are interested, there are many variants of the SIR model, including modelling deaths, carriers and immunisation. Each one can be implemented in a similar way in Python. The [Wikipedia page on the subject](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology){target="_blank"} is a good starting point. 


## Higher-order ODEs

By now I hope you'll agree that Python, and `odeint`, are pretty cool! So you'll be initially devastated to learn that sadly it cannot handle second-order (or higher-order more generally) ODEs. But...fear not. We can turn a second-order ODE into two first-order ODEs in a fairly straightforward way. 

Here's an example:

$$ \frac{\mathrm{d}^2y}{\mathrm{d}t^2}+\frac{\mathrm{d}y}{\mathrm{d}t}-2y = 0 $$

with $y(0)=0$, $\displaystyle \frac{\mathrm{d}y}{\mathrm{d}t}(0)=1$

Let's introduce $u = \mathrm{d}y/\mathrm{d}t$. Then we have 2 first-order ODEs:

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = u $$

$$ \frac{\mathrm{d}u}{\mathrm{d}t} + u - 2y = 0 $$

or gathering terms on the right for the latter,

$$ \frac{\mathrm{d}y}{\mathrm{d}t} = u $$

$$ \frac{\mathrm{d}u}{\mathrm{d}t} = -u + 2y $$

with  $y(0)=0$, $u(0)=1$.

And this we can do. We just have done in the last section!

As before, let's knock up a function. Note I don't need the additional arguments any more and I've used `x` to store the values of $y$ and $u$.

```python
def model(x, t):
    y, u = x           		# reads in values in x and assigns to y and u
    dydt = u 				# rhs of dy/dt
    dudt = -u + 2*y  		# rhs of du/dt 
    return [dydt, dudt]
```

and a main script:
```python
x0 = [0,1]
t = np.linspace(0,5,100)
x = odeint(model,x0,t)

plt.plot(t,x[:,0])
plt.xlabel('t')
plt.ylabel('y(t)')
```

Here I'm plotting just column 1, which is $y(t)$ with `x[:,0]` (I could plot $u = \mathrm{d}y/\mathrm{d}t$ with `x[:,1]`).

![](/static/images/week6/higherorder.png){width=90%}

So solving higher order differential equations turns out to be no more complicated than systems of first order differential equations.

### Exercise 6.4 {: .exercise}

In this exercise I've coded up a similar example, but left it to you to figure out which differential equation I was solving.
<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81779/identify-a-second-order-ode/embed/?token=92b2c6ed-8374-4ba0-864b-900fd17692f0" data-id="exercise-6-4" data-cta="Show Exercise"></numbas-embed>


## Handout 6 Summary

In the next week's content we'll look at some of the algorithms that underly the `odeint` function and others like it.


