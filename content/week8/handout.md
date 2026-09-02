[Click here to open this handout in a new browser tab](#){target="_blank"}

# Handout 8 - Differential equations

This week is concerned with using Python to solve (systems of) differential equations.

## Introduction

Ordinary differential equations (ODEs) appear across a wide range of applied mathematics. However, it is in general very difficult (if not impossible) to solve them analytically. It follows that using numerical methods to approximate solutions are extremely valuable in real-world applications.

Consider the general form of a first-order ODE, with initial condition

$$\frac{dy}{dt}(t) = f(t,y), \quad y(t_0) = y_0 $$

A *solution* to this ODE is a function $y(t)$ that satisfies the equation and initial condition (i.e. plugging in $y(t)$ to the above equation causes the left-hand side to equal the right-hand side).

**An important note on terminology:** as above, a *solution* to an ODE is a function $y(t)$ with the desired properties. The numerical methods we'll consider do not find such a solution, in general. Rather, they find some form of approximate solution; typically this is a set of discrete datapoints, rather than an exact function. However, it is common to refer to such an approximation as a *numerical solution*. In other words, when *solving an ODE numerically* we are really *finding an approximation of a precise mathematical solution*.

## Numerically solving ODEs with a computer

Consider the ODE with initial condition

$$ \frac{dy}{dt} = -\frac{y}{2} , \quad y(0)=5 $$

This is also known as an *initial value problem*, as we are given the initial value of solutions $y(0) =5$. Many numerical methods of solving ODEs proceed by using the condition 

$$ \frac{dy}{dt} = -\frac{y}{2} $$

to grow a numerical solution out from $t=0$. That is, at $t=0$ we have 

1) $y(0)=5$ and

2) $\displaystyle \frac{dy}{dt}(0)=-\frac{5}{2}$,

![the euler method](/static/images/week6/explanation3.png){width=80%}

so that we know the starting point of the solution $y$ and its gradient at that point. We can use this to esimate $y(t_1)$ for $t_1 > 0$:

![the euler method](/static/images/week6/explanation5.png){width=80%}

This method is implemented in Python via the function `odeint`. This week we'll focus on using such implementations out-of-the-box. We'll investigate the mathematical background in more detail in Week 9.

## SciPy `odeint`

### First-order ODEs

To begin we'll use the SciPy function `odeint` to solve first-order ODEs. We'll continue to use the initial value problem given above as an example

$$ \frac{dy}{dt} = -\frac{y}{2} , \quad y(0)=5 $$

The syntax for implementing `odeint` is as follows:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Right-hand side of above equation
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

The function `odeint` is called on the line
```python
y = odeint(rhs,y0,t)
```
with arguments
* The function handle `rhs`, defined in the code above. Note that `rhs` takes two input arguments `rhs(y,t)` (in that precise order).
* The initial condition `y0`, that we set to `5` in the code above.
* An array `t` of $t$ values at which to approximate the solution $y$.

The output of `odeint` is an array `y` of the same length as `t`. We can therefore plot it as follows:

```python
plt.plot(t,y)
```

![plot of the odeint solution](/static/images/week6/odeint1.png){width=80%}

Using methods from modules such as MAS1612-PHY1040 or MAS2802-PHY2031 the exact solution to the ODE above can be show to be

$$ y(t)=5e^{-t/2} $$

Add this precise solution to the plot via
```python
t1 = np.linspace(0,5,100)
plt.plot(t1, 5*np.exp(-t1/2),'--')
```

The outcome should demonstrate that `odeint` has successfully approximated the exact solution.

#### Accuracy 

In Week 9 we'll look in more detail at the accuracy of numerical methods to solve differential equations. To get a sense of what the term *accuracy* means in this context, consider altering the code above in the following manner.

Alter the `t` array from `t = np.linspace(0,5,100)` to

```python
t = np.linspace(0,5,5)
```

You'll notice that the resulting numerical solution is not as accurate as it was previously. Increase the number of points in the `t` array (i.e. by increasing the final argument in `np.linspace`), and observe as the accuracy of the numerical solution increases.

In Week 9 we'll discuss why this is the case, and consider other ways numerical accuracy can be improved.

#### Structure of the output array `y`

Replace the original command for the `t` array (i.e. ``t = np.linspace(0,5,100)`). We can view the array `y` via the syntax

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

The ellipsis `[...]` indicates that Python has suppressed most of `y` i.e. it is too long to show all of it. We can determine the precise size of `y` via the syntax

```python
y.shape
```
```output
(100, 1)
```

This indicates that `y` is a 2D array with 100 rows and 1 column. This is contrast with `t`, which is a 1D array 100 elements (you can confirm this with the command `t.shape`).

Why does `y` have this particular shape? It turns out that this is a deliberate design decision by the developers of SciPy: as we will see below, `y` being a 2D arrays allows for a direct extension to *systems* of differential equations.

<div class="exercise" markdown=true>

### Exercise 8.1 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81771/odeint-adapt-existing-code/embed/?token=6e34466e-1416-486a-b8c8-871bfe441306" data-id="exercise-6-1" data-cta="Show Exercise"></numbas-embed>

</div>

### Passing parameters to `odeint`

Consider the ODE

$$ \frac{dy}{dt} = - \frac{ay}{2} + b, \quad y(0)=5  $$

for $a$ and $b$ constants. Notice that setting $a=1$, $b=0$ recovers the ODE of the previous section.

We can modify the code above to incorporate these constants. First, we alter the `rhs` function as follows

```python
def rhs(y,t,a,b):
    dydt = - (y*a)/2 + b
    return dydt
```

The solution to the ODE will depend heavily on the values of the $a$ and $b$, so that `odeint` cannot find a numerical solution unless these constants are fixed. Let's fix $a=1$, $b=0$, so that we are considering the original ODE again. The `odeint` function call must be altered as follows

```python
y = odeint(rhs,y0,t,args=(1,0))
```

The additional argument `args=(1,0)` implements the desired values for $a$, $b$ (notice the order in `args=(1,0)` is inherited from the definition of `rhs`).

Why would we want to do this? We may be studying this particular ODE in a larger context, in which altering the values of $a$, $b$ allows for important analysis. This new code allows us to easily change the values of $a$ and $b$ e.g. using a `for` loop.

#### Nuances of `args` 

The argument `args` in `odeint` takes as input a *tuple*, a Python data type we have not covered in detail:

```python
x = (2,3)
type(x)
```
```output
tuple
```

A tuple is similar to a list, but differs in that the elements of a tuple cannot be changed. That is, we cannot overwrite individual elements of a tuple as we can a list. For this and other reasons computations are more efficient if using tuples (rather than lists).

A nuance of the `args` argument in `odeint` is that if we are solving an ODE involving a single constant, $a$ for example, we must use the syntax `args(1,)`. Notice the trailing comma: this is to indicate to Python that `(1,)` is a tuple containing a single element (rather than a variable in brackets).

We can verify this as follows:

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

This is important for the following exercise.

<div class="exercise" markdown=true>

### Exercise 8.2 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/108571/odeint-single-variable/embed/?token=fa292f75-287d-45b7-ab7e-20b7c39e372d" data-id="exercise-6-2" data-cta="Show Exercise"></numbas-embed>

</div>

### Other applications

There is a strong case to be made that differential equations are the most widely applied mathematical object of all: [this list](https://en.wikipedia.org/wiki/List_of_named_differential_equations){target="_blank"} gives hundreds of examples from across the scientific landscape, and there are many (many) more. 

An prototypical example is the differential equation governing radioactive decay

\[ \frac{dN}{dt} = -\lambda N \] 

where $N(t)$ is the quantity of a radioactive substance and $\lambda$ is the exponential decay constant, measuring how fast the substance decays.

This version of the differential equation can be solved analytically in a straightforward manner, but we will discuss generalizations of it that necessitate numerical solutions.

<div class="exercise" markdown=true>

### Exercise 8.3 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/132951/radioactive-decay/embed/?token=7341a6b4-269a-4c9c-8545-935970ef14d0" data-id="exercise-8-3new" data-cta="Show Exercise"></numbas-embed>

</div>

### Systems of ODEs 

A *system* of ODEs is a collection of ODEs involving a single independent variable (that we'll continue to denote by $t$), and multiple functions $y_1(t), y_2(t), \ldots , y_n(t)$. A solution to the system of ODEs is a solution for all the functions $y_1(t), y_2(t), \ldots , y_n(t)$ such that every ODE in the system is satisfied. For example, consider the system made up of two ODEs and two functions $y_1 (t) = S(t)$, $y_2(t) = I(t)$:

\begin{align}
\frac{dS}{dt}&=-\beta IS + \gamma I, \\
\frac{dI}{dt}&=\beta IS -\gamma I
\end{align}

where $\beta$ and $\gamma$ are constants. This system of ODEs arises in epidemiology: $S(t)$ is the number of individuals in a population that are susceptible to a virus, $I(t)$ is the number of individual infected, $\beta > 0 $ is the rate of infection (i.e. the probability that an individual becomes infected if they come into contact with an infected individual), and $\gamma >0 $ is the time taken to recover from infection.

To solve this system we must determine the form of $S(t)$ and $I(t)$ such that the equations above are satisfied. Notice that $S(t)$ and $I(t)$ appear in both equations. This means we cannot simply solve the first equation separately, and then solve the second: the equations are linked together and must be solved simultaneously.

We can also use `odeint` to obtain numerical solutions to systems of ODEs such as this. For convenience we'll denote $\beta$ and $\gamma$ by `b` and `c` respectively in the code below.

We must alter the function we previously called `rhs` to incorporate both of the ODEs. We'll also rename it to `model`, as follows

```python
def model(y, t, b, c):
    S, I = y              # Once we have fixed this order of S and I we must abide by it in the remaining code
    dSdt = -b*I*S + c*I   
    dIdt = b*I*S - c*I     
    return [dSdt, dIdt]   # Notice S and I appear in the same order as above
```

Note the arguments `(y, t, b, c)`: we are including the parameters $\beta$ and $\gamma$. The syntax `S, I = y` is simply a shorthand way of setting the variables `S` and `I` to the elements of a list `y` i.e. it is equivalent to the lines

```
S = y[0]
I = y[1]
```

The variables `dSdt` and `dIdt` give the right hand sides of the ODEs forming the system. Notice that the function `model` returns a list `[dSdt, dIdt]`: this is required for `odeint` and returning objects other than lists will lead to errors.

We now apply `odeint` to `model`. Let's consider the initial conditions

$$ S(0) = 999, \quad I(0) = 1 $$

parameter values $\beta = 0.002$, $\gamma = 0.5$, and look over $100$ points for $t$ in the range $[0,20]$:

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

Notice that we must also provide `odeint` with the initial conditions in a list `y0`, and recall that `args` incorporate the parameters `b` and `c` into the process.

The full code is:

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def model(y, t, b, c):
    S, I = y              
    dSdt = -b*I*S + c*I   
    dIdt = b*I*S - c*I    
    return [dSdt, dIdt]   

# Parameters
b = 0.002
c = 0.5

# Initial conditions
y0 = [999,1]

# Time points
t = np.linspace(0,20,100)

# Solve ODE
y = odeint(model,y0,t, args=(b,c))

plt.plot(t,y[:,0],label='S(t)')   # y[:,0] contains numerical solution for S(t)
plt.plot(t,y[:,1],label='I(t)')   # y[:,1] contains numerical solution I(t)
plt.legend()
plt.xlabel('t')
plt.title('SI Model')
```

This should yield the following plot:

![The SI Model](/static/images/week6/simodel.png){width=90%}

The array `y` now has the following shape

```
y.shape
```
```output
(100,2)
```

That is, it is a 2D array with 100 rows and 2 columns: the numerical solution for $S(t)$ is contained in the first column, and that for $I(t)$ in the second column.

Finally, note that Matplotlib can often guess the correct form of a plot given the input data. Specifically, instead of plotting $S(t)$ and $I(t)$ individually via

```python
plt.plot(t,y[:,0])
plt.plot(t,y[:,1])
```

we could use the single line

```python
plt.plot(t,y)
```

### SIR models

There are many variations of the above model, most famously the *SIR model*. In this model there is an additional type of individual, known as *recovered*, who have been infected previously and are now immune to the virus. The number of recovered individuals at time $t$ is denoted $R(t)$. The SIR model has been successfully applied to the Bubonic Plague, the cholera outbreaks in 1800s London, and COVID 19.

The precise form of the model is given by the system of ODEs

\begin{align}
\frac{dS}{dt}&=-\beta IS, \\
\frac{dI}{dt}&=\beta IS -\gamma I \\
\frac{dR}{dt}&= \gamma I
\end{align}

<div class="exercise" markdown=true>

### Exercise 8.4

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/82126/sir-model/embed/?token=61696d1d-5ff6-4510-9acf-da31bc3774aa" data-id="exercise-6-3" data-cta="Show Exercise"></numbas-embed>

</div>

### Radioactive decay revisited

We can use `odeint` to solve systems of ODEs related to radioactive decay, as in the following exercise.

<div class="exercise" markdown=true>


### Exercise 8.5

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/132952/radioactive-decay-parent-daughter/embed/?token=ad49c094-a7c2-4e02-abcd-02b6dcfdd9c8" data-id="exercise-8-5" data-cta="Show Exercise"></numbas-embed>

</div>

## Higher-order ODEs

While `odeint` is able to handle systems of first-order ODEs, it cannot be applied to higher-order ODEs: those involving second derivatives and higher e.g.

$$ \frac{d^2 y}{dt^2} + 4 \frac{d y}{dt} - 2 y = 2t^2 - 3t + 6 $$

This is an example of a *second-order ODE* i.e. an ODE involving the derivative and second derivative. Happily, there is an algorithm that converts a second-order ODE into a system of first-order ODEs. We'll carry out this algorithm on the second-order ODE

$$ \frac{d^2y}{dt^2}+\frac{dy}{dt}-2y = 0 $$

with initial conditions $y(0)=0$, $\displaystyle \frac{dy}{dt}(0)=1$.

Setting $u = dy/dt$ we obtain the system of ODEs in $u$ and $y$

$$ \frac{dy}{dt} = u $$

$$ \frac{du}{dt} + u - 2y = 0 $$

Rewriting the second equation to fit the format described above we obtain

$$ \frac{dy}{dt} = u $$

$$ \frac{du}{dt} = -u + 2y $$

with initial conditions $y(0)=0$, $u(0)=1$.

As we saw in the previous section, we can use `odeint` to solve this system of first-order ODEs.

We'll use the function `model` as above, with the following alterations: we no longer need additional parameters (`b` and `c` above), and we have used `x` rather than `y` to denote the function input (as $y$ appears in the system of ODEs)

```python
def model(x, t):
    y, u = x           		
    dydt = u 				
    dudt = -u + 2*y  		 
    return [dydt, dudt]
```

We alter the rest of the code as follows
```python
x0 = [0,1]
t = np.linspace(0,5,100)
x = odeint(model,x0,t)

plt.plot(t,x[:,0])
plt.xlabel('t')
plt.ylabel('y(t)')
```

You should obtain the following plot

![A higher order solution](/static/images/week6/higherorder.png){width=90%}

Notice that we are only plotting $y(t)$ (via `plt.plot(t,x[:,0])`): this is because the system of ODEs was derived from the single second-order ODE involving $y$ only, so that $y$ is the only mathematically meaningful variable in this case.

<div class="exercise" markdown=true>

### Exercise 8.6 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81779/identify-a-second-order-ode/embed/?token=92b2c6ed-8374-4ba0-864b-900fd17692f0" data-id="exercise-6-4" data-cta="Show Exercise"></numbas-embed>

</div>

## Visualising solutions via vector plots

We'll conclude this Handout by returning to first-order ODEs, and considering how we can use the vector plots (a.k.a. quiver plots) introduced in Week 6 to visualise solutions found by `odeint`.

Recall the first-order ODE studied above

$$ \frac{dy}{dt} = -\frac{y}{2} $$

Suppose that $y(t)$ is a solution to this ODE. Notice that even if we don't know the precise form of $y$, we know it's tangent at every $t$: as $y$ is a solution to the ODE the tangent must be given by the above equation. This allows us to plot the tangent lines to solutions of the ODE, without having to solve the ODE itself.

Recall that a vector plot places a vector at each point of a meshgrid. In this case, at each $y$ and $t$ value we'll plot the vector given by the tangent line to a solution to the ODE passing through that point. 

For the ODE given above we would obtain the following plot

![Directional field plot for dy/dt = -y/2](/static/images/week3/directional1.png){width=90%}

As the right-hand side of the ODE does not depend on $t$ the tangents are constant as we move through $t$. On the other hand, notice that as we move away from $0$ on the $y$-axis the tangents grow in magnitude.

The Matplotlib plotting function `quiver` is used to produce plots such as this. Before invoking `quiver` we must set up a meshgrid, a 2D grid of points at which the vectors will be plotted. Recall the following code from Week 6

```python
import numpy as np
import matplotlib.pyplot as plt 

t = np.arange(0, 5, 0.25)
y = np.arange(-6, 6, 0.5)
T, Y = np.meshgrid(t, y)
```

We must now create the vector components; let's denote the vector to be plotted at point $(t,y)$ by $(u,v)$. As we observed above, the tangents to solutions to the ODE do not depend on $t$, so that we are free to choose $u = 1$ at every point. By considering the ODE itself we can determine that $v = -\frac{y}{2}$. We can implement this in Python as

```python
u = np.ones(T.shape)   # T.shape returns the dimensions of T
v = -Y/2

plt.quiver(T, Y, u, v, angles='xy')
```

The option `angles='xy'` is required as we wish to plot the vector at the point $(t,y)$ relative to the point $(t,y)$ itself (rather than having a fixed origin at the point $(0,0)$).

To remind yourself what the function `np.ones` does try the following commands

```python
np.ones(5)
np.ones([2,5])
```

As we solved the ODE earlier in the handout we can add two solution curves to the plot:

```python
# The arrow style has been changed using the command
# plt.quiver(T,Y,u,v, angles='xy',color='gray',width=0.002)

t = np.linspace(0,5,100)
y = odeint(rhs,5,t)
plt.plot(t,y,label='y(0)=5')

y = odeint(rhs,-5,t)
plt.plot(t,y,label='y(0)=-5')

plt.legend()
```

![Directional field plot for dy/dt = -y/2 with solutions y(0)=5 and y(0)=-5](/static/images/week3/directional2.png){width=90%}

<div class="exercise" markdown=true>

### Exercise 8.7 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/83999/quiver-plot/embed/?token=c7e66cc1-3b21-4a0c-81f8-1d8222c5525a" data-id="exercise-7-7" data-cta="Show Exercise"></numbas-embed>


</div>


## Next week

Next week we'll consider the algorithms behind `odeint` in more depth, and introduce alternative Python functions for solving ODEs.


