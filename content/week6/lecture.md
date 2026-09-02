
![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 6 - Advanced plotting

---

## This week

* Using `meshgrid` for advanced plotting e.g. of multivariable functions $f(x,y)$.
* More control of plots e.g. size, layout, colours.

---

## Mid-semester survey

Most respondents seem to be enjoying the module so far.

Most common suggestion of something to improve: make the lecture more useful. I hope to be able to do this when we come back from the reading week: we'll be covering numerical integration and systems of differential equations, that benefit from more detailed exposition in lecture. 

---

## Assessment 2

* Based on Weeks 4 to 6.
* Open Friday 31th.
* Due *Friday* 21st November at 16:00.
* Includes submission of a report.

---

![Report guidelines](/static/images/report_guidelines.jpg){width=100%}

Recommend consulting [the Assessment 2 sample question](https://ncl.instructure.com/courses/59162/modules/items/3398915){target="_blank"}

---

## Advanced plotting

This week's handout covers:

1. Plotting more complicated objects e.g. higher-dimensional data, parametrically defined functions.
2. Gaining greater control over the display of plots e.g. size, layout, colours.

---

### 1. Vector-valued functions $f(x,y) = (u,v)$

![A vector plot](/static/images/wk6/practical_vector.png){width=70%}

Such plots will be useful for us in Week 8.

---

### 1. Parametric curves

![Parametric 3D](/static/images/wk6/parametric3d.png){width=70%}

Parametrically defined functions are commonplace in any Vector Calculus module.

---

### 1. Surface plots of functions $f(x,y) = z$

![A surface plot](/static/images/wk6/surface-lecture.png){width=70%}

Such plots will be useful for us in Week 7.

---

## 1. Contour plots of functions $f(x,y) = z$

![A surface plot.](/static/images/wk6/contour.png){width="70%"}

An alternative way to plot $f(x,y) = z$ that does not require 3D axes.

---

### Meshgrids

Many of the above plots require a `meshgrid`. Suppose we wish to plot $f(x,y) = \sqrt{x^2+y^2} = z$.

We might try

```python
x = np.arange(0,11)
y = np.arange(0,11)
z = np.sqrt(x**2+y**2)
```

---

But this only computes the points `np.sqrt(x[i]**2+y[i]**2)`

![A grid of x and y values set up without meshgrid.](/static/images/week2/lecture_nomeshgrid.png){width="80%"}

We can use `meshgrid` to compute the points `np.sqrt(x[i]**2+y[j]**2)` for $i \neq j$.

---


![A grid of x and y values, set up with NumPy's meshgrid function shows an x and y value at every permutation of x and y coordinates.](/static/images/week2/lecture_meshgrid.png){width="80%"}

```python
x = np.arange(0,11)
y = np.arange(0,11)
X,Y = np.meshgrid(x,y)
plt.plot(X,Y,'o')
```

---

Using `meshgrid` allows us to plot multivariable functions e.g.

<div style="background-color: #FFFFFF" markdown=true>
![A contour plot of y*cos(x)+x*sin(y)](/static/images/week6/surface1.png){width="49%"} ![A surface plot of y*cos(x)+x*sin(y)](/static/images/week6/surface2.png){width="49%"}
</div>

---

### 2. Figure size

This week's handout also includes a great deal of customisation options for plots e.g. size:

<div style="background-color: #FFFFFF" markdown=true>
![A contour plot of y*cos(x)+x*sin(y)](/static/images/week6/surface3.png){width="49%"} ![A surface plot of y*cos(x)+x*sin(y)](/static/images/week6/surface1.png){width="49%"}
</div>

---

### 2. Annotations

Adding annotations to 2D and 3D plots:

![A simple plot of a graph with text annotation](/static/images/wk6/annotation.png){width="70%"}

---

### 2. Subplots

Adding multiple plots under the same title:

![Two subplots side by side under one title](/static/images/wk6/subplots.png){width="70%"}

---

## Looking ahead

After the reading week we'll use Python to:

* Compute numerical estimates of derivatives and integrals.
* Solve and analyse systems of differential equations.

We'll use the plotting techniques discussed in this week's handout to visualize these situations.

---

### Estimating integrals

In Week 7 we'll estimate multivariable integrals, such as $\iint_{-1}^{1} (\sin(x+y) + 2)dx dy$:

![Two subplots side by side under one title](/static/images/week6/integral_estimate.png){width="70%"}

---

### Visualizing solutions to differential equations

In Week 8 we'll consider differential equations such as $\frac{\mathrm{d}y}{\mathrm{d}t} = -\frac{y}{2}$.

We can plot the value of $\frac{\mathrm{d}y}{\mathrm{d}t}$ at each point $(x,y)$ using a vector plot:

![Directional field plot for dy/dt = -y/2](/static/images/week3/directional1.png){width=90%}

---

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}

The material sketched in this lecture is covered in greater detail in Handout 6.
