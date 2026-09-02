![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

<h1 style="text-align: center;">Lecture 8 - Differential equations I</h1>

----

* Assessment 2: deadline **Friday at 16:00**.
* Please email me with questions or to book an office hours appointment.

----

## Differential equations

A *differential equation* is an equation involving a function (or functions) and it's derivatives e.g.

$$ F(t) = m s '' (t) $$

\begin{align}
x^2 y '' (x) + x y ' ( x ) + (x^2 -a^2)y(x) &= 0 \\
p '' ( t ) - \frac{1}{p(t)} \left( p ' ( t ) \right)^2 + \frac{1}{t} p' ( t ) &= 0
\end{align}

----

There is a strong case to be made that differential equations are the most widely applied mathematical object of all; entire fields of science are dedicated to their study e.g.

* Fluid dynamics
* Classical mechanics
* ...

Analysing interacting quantities that evolve with respect to one another almost always leads to differential equations.

----

A *solution* to a differential equation is a choice of function or functions that satisfies the equation (i.e. plugging in this choice causes the left-hand side to be equal to the right-hand side). E.g. $y(x) = e^{2x}$ is a solution to $y'(x) = 2 y(x)$.

You may have covered techniques to solve differential equations in modules such as MAS1611-PHY1039, MAS1612-PHY1040, or MAS2802-PHY2031. This week we'll implement such methods in Python, with one important difference.

The numerical methods we'll consider do not find an exact solution, in general. Instead, they find some form of approximate solution. It's common to refer to such an approximation as a *numerical solution*. In other words, when *solving an ODE numerically* we are really *finding an approximation of a precise mathematical solution*.

----

## Numerical solution methods

We'll use the following differential equation as a running example

$$ \frac{dy}{dt}= y' ( t ) = -\frac{y}{2}, \quad y(0)=5 $$

This a first-order ordinary differential equation (ODE), with initial condition $y(0)=5$.

(Differential equations with initial conditions are also known as *initial value problems*.)


----

The central idea is that we already know $y(0)=5$ and $y'(0) = -\frac{5}{2}$

![The Euler Method](/static/images/week6/explanation3.png){width=80%}

----

We can use this information to estimate a solution $y$ at another $t$ value e.g. $y(1) = 5 -\left(\frac{5}{2}\right)$

![The Euler Method](/static/images/week6/explanation5.png){width=80%}

----

In Week 9 we'll investigate the mathematics behind this (and other) numerical methods to solve ODEs; this week we'll focus on applying the SciPy function `odeint`.

Let's preview the code required to numerically solve the initial value problem

\[ y' ( t ) = -\frac{y}{2}, \quad y(0)=5 \]

----

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def rhs(y,t):
    dydt = - y/2
    return dydt

y0 = 5						
t = np.linspace(0,5,5)		

y = odeint(rhs,y0,t)		

plt.plot(t,y)				
```

---

## Visualising solutions with vector plots

We can visualise solutions to $y' ( t ) = -\frac{y}{2}$ without having to solve the equation.

Notice that at $y = 0$ we have $y' = 0$,  $y = 2$ we have $y' = -1$, and so on:

![Directional field plot for dy/dt = -y/2](/static/images/week3/directional1.png){width=70%}

---

```python
import numpy as np
import matplotlib.pyplot as plt 

t = np.arange(0, 5, 0.25)
y = np.arange(-6, 6, 0.5)
T, Y = np.meshgrid(t, y)

u = np.ones(T.shape)  
v = -Y/2

plt.quiver(T, Y, u, v, angles='xy')
```


---

### Systems of differential equations

A *system of differential equations* is a collection of differential equations, involving one or more functions e.g.

\begin{align}
\frac{dS}{dt}&=-\beta IS + \gamma I \\
\frac{dI}{dt}&=\beta IS -\gamma I
\end{align}

A *solution* to such a system is a choice of these functions that satisfies every equation simultaneously. We can use `odeint` to find numerical solutions to systems of ODEs.

---

We must alter the input to `odeint` to accommodate for multiple functions and equations. Specifically, we must use the syntax

```python
def model(y, t, b, c):
    S, I = y            
    dSdt = -b*I*S + c*I 
    dIdt = b*I*S - c*I  
    return [dSdt, dIdt] 
```

---

### Higher-order differential equations

So far we have considered first-order ODEs e.g. those involving only the first derivative. What about equations involving higher derivatives? E.g.

$$ \frac{d^2 y}{dt^2} + 4 \frac{d y}{dt} - 2 y = 2t^2 - 3t + 6 $$

It turns out that `odeint` cannot be applied directly to higher-order ODEs. However, in some cases we can introduce a new variable in order to reduce a higher-order equation to first-order.

---

For example, set $u = dy/dt$. Then

\begin{align}
\frac{d^2 y}{dt^2} + 4 \frac{d y}{dt} - 2 y &= 2t^2 - 3t ~\text{becomes}\\
\frac{du}{dt} + 4 u - 2y &= 2t^2 - 3t
\end{align}

so that we have the system of first-order ODEs

\begin{align}
\frac{dy}{dt} &= u \\
\frac{du}{dt} &= 2 y - 4u + 2t^2 - 3t
\end{align}

---

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}

The material sketched in this lecture is covered in greater detail in Handout 8.

