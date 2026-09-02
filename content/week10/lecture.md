![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

<h1 style="text-align: center;">Lecture 10 - In-depth examples and generalizations</h1>

---

## Announcements

* Week 11 is a revision week; please email me with any topics or questions you'd like to go through.

* Release of Assessment 2 marks may be delayed.

---

### Recap: Stability of Euler method

We considered the *stability* of the numerical solution obtained via the Euler method applied to

$$\frac{dy}{dt} = -\lambda y$$

for $\lambda$ a constant.

The Euler method iterative step is (with step size $h$)

$$ y_{n+1} = y_n - \lambda hy_n = (1-\lambda h) \; y_n $$

---

Repeated application of the iterative step yields

\begin{align}
y_{n+1} &= (1-\lambda h) \; y_n  \\
&= (1-\lambda h)^2 \; y_{n-1} \\
&= (1-\lambda h)^{n+1} \; y_0
\end{align}

It follows that $y_n \to 0$ as $t\to\infty$ if and only if $|1-\lambda h|\lt 1$.

Rearrange to obtain 

$$h \lt \frac{2}{\lambda}$$

---

Recall that exact solution to 

$$\frac{dy}{dt} = -\lambda y$$

is $y = A e^{-\lambda t}$, for $A$ a constant that depends on the initial condition.

It is clear that the exact solution tends to $0$ as $t$ tends to infinity. Therefore the Euler method is *stable* if and only if $h \lt \frac{2}{\lambda}$.

---

### Stability in 2D

Consider the second-order ODE

$$\frac{d^2 y}{dt^2}+16\frac{dy}{dt}-10y = 0 $$

Set $u = \frac{dy}{dt}$ to obtain system of first-order ODEs

$$ \frac{dy}{dt} = u, \qquad \frac{du}{dt} = 10y - 16u $$

We can express this system as a matrix equation

$$ \frac{d}{dt} \begin{pmatrix} y \\ u \end{pmatrix} =  \begin{pmatrix} 0 & 1 \\ 10 & -16 \end{pmatrix} \begin{pmatrix} y \\ u \end{pmatrix} $$ 


---

We saw that the Euler method is stable for

$$\frac{\mathrm{d}y}{\mathrm{d}t} = -\lambda y$$

precisely when $h \lt \frac{2}{\lambda}$.

Notice that the matrix equation above can be written

$$\mathbf{y'} = -\Lambda \mathbf{y}$$

where $\mathbf{y'}$ and $\mathbf{y}$ are appropriate vectors.

---

We shall see in this week's Handout that the stability of the Euler method for this system is governed by the eigenvalues of $\Lambda$.

In particular, the method is stable if and only if 

$$h \lt \frac{2}{\lambda_{max}}$$

where $\lambda_{max}$ is the largest eigenvalue of $\Lambda$.

---

```python
import numpy as np
import scipy.linalg as sla

# Lambda matrix
L = np.array([[0,-1],[-10,16]])

# Get eigenvalues and eigenvectors
eigenvalues,eigenvectors = sla.eig(L)

print("Max eigenvalue: {}".format(max(eigenvalues)))
print("Critical h: {}".format(2/max(eigenvalues).real))

```

Critical $h \approx 0.12$

---

We can verify this using the following code:

```python
import numpy as np
import matplotlib.pyplot as plt

h = 0.1 
t = np.arange(0,10+h,h)
y = np.zeros(len(t))
u = np.zeros(len(t))

y[0] = 5
u[0] = 5
   
# Solve with Euler Method
for n in range(len(t)-1):
    y[n+1] = y[n] + (t[n+1]-t[n]) * (u[n])
    u[n+1] = u[n] + (t[n+1]-t[n]) * (10*y[n]-16*u[n])
```

---

## Two in-depth examples

This week's Handout contains two in-depth examples of these methods applied to *dynamical systems*.

---

In mathematics the term *dynamical system* typically refers to a collection of quantities that evolve in time. These quantities may have a physical meaning, but often we simply study them in the abstract.

We use differential equations to predict how these quantities will change over time.

---

## The Lotka-Volterra equations

A very common system of ODEs that is used to describe population dynamics of biological systems

$$
\begin{align}
\frac{dx}{dt} &=\alpha x-\beta xy \\
\frac{dy}{dt} &=\delta xy-\gamma y
\end{align}
$$

where $x$ denotes the population of a prey species, and $y$ that of a predator species, and $\alpha$, $\beta$, $\delta$, $\gamma$ are constants.

---

![The Predator Prey Model](/static/images/week9/predator-prey.png)

---

![Hare Lynx findings](/static/images/week9/harelynx.png)

---

![Predator Prey Phase Portrait](/static/images/week9/predatorpreyphase.png)

---

## The logistic Map

Recall the logistic equation from Week 9, also used in population modelling

$$ \frac{\mathrm{d}x}{\mathrm{d}t} = rx(1-x) $$

The equation above is the continuous counterpart to the discrete *logistic map*

$$ x_{n+1} = rx_n(1-x_n) $$

This very simple equation possesses remarkable properties.

---

Plotting $x_i$ at various values of $r$ yields

![Animation of the logistic map](/static/images/week9/logistic_animation.gif)


---

In this week's Handout we'll recreate the *period doubling bifurcation plot*:

![the logistic map](/static/images/week9/logisticmap.png)

---

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}

The material sketched in this lecture is covered in greater detail in Handout 10.



