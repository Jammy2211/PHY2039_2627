[Click here to open this handout in a new browser tab](#){target="_blank"}

# PHY2039 Handout 6

This week covers more advanced plotting techniques, including visualizing more complicated data and gaining greater control over the display of plots. 

In addition to adding these new techniques, the plotting material covered in previous weeks is also provided, so that this handout can act as a reference page for plotting with Python.


## 6.1) 2D plots 

### Functions used in previous weeks

In the following sections we are assumming that NumPy and Matplotlib have been imported via

```python
import numpy as np
import matpotlib.pyplot as plt 
```

#### Line or marker plot of dataset with one independent and dependent variable

📖 Matplotlib documentation on [plt.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html){target="_blank"}.

```python
x = np.linspace(0,5,100)
plt.plot(x,x**2)
plt.plot(x,x**2,'--')
plt.plot('o')
```

#### Scatter plot

📖 Matplotlib documentation on [plt.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html){target="_blank"}.


```python
x = np.arange(10)
y = x + np.random.rand(10)
# s is size of the markers
plt.scatter(x,y,s=10,color='firebrick',marker='o')
```

#### Logarithmic axes

📖 Matplotlib documentation on [plt.semilogx](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogx.html){target="_blank"}, [plt.semilogy](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.semilogy.html){target="_blank"}, [plt.loglog](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.loglog.html){target="_blank"}.

```python
plt.semilogx(x,y)   # Log x axis
plt.semilogy(x,y)   # Log y axis
plt.loglog(x,y)     # Log x and y axes
```

#### 2D raster plot 

📖 Matplotlib documentation on [plt.imshow](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html){target="_blank"}

We used this function to create Newton fractals in Week 5:

```python
x = np.arange(25).reshape([5,5])
plt.imshow(x)
```


#### Other common 2D plotting functions

For completeness we include some other common plotting functions that may be useful in your further degree studies:

```python
labels = ['A','B','C']
values = [2, 6, 4]

# Bar plot
plt.bar(categories, values)

# Pie chart
plt.pie(values, labels=categories)

# Histogram
x = np.random.normal(0, 1, 10)
plt.hist(x)

# Box and whisker plot
labels = ['A', 'B', 'C']
data = []
for n in range(3):
    data.append(np.random.normal(0, 1, 10))

plt.boxplot(data)
plt.xticks([1, 2, 3], labels)

```

### 2D parametric curves

If you are taking a Vector Calculus module such as MAS2801 or PHY2026 it's likely that you have encountered curves (and surfaces) defined *parametrically*:

$$ f ( x(t), y(t) ) $$

for $x(t)$ and $y(t)$ continuous functions of a parameter $t \in [a,b]$. We can use `plt.plot` to make a plot such curves.

For example, consider the parametric curve

$$ \left(x(t),y(t)\right) = \left(\sin(2t),\sin(3t)\right), \quad 0 \leq t \leq 2\pi $$

This is known as a *Lissajous curve* (such curves are covered in more detail in the Off-piste section of the module Canvas page). To plot this curve we first create an array of $t$ values, before using element-wise arithmetic to produce the $x$ and $y$ values:


```python
t = np.linspace(0, 2*np.pi, 200)
x = np.sin(2*t)
y = np.sin(3*t)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

![Parametric Curve](/static/images/wk6/lissajous.png){width=60%}

By default Matplotlib will produce a plot with distinct `x` and `y` axis scales. This is useful in many cases, but in this specific context we might wish to override this behaviour using the option

```python
plt.axis('equal')
``` 

Here's the above plot with this option:

![Parametric Curve](/static/images/wk6/lissajous2.png){width=60%}

The affect of `plt.axis('equal')` is most obvious with a circle:

```python
t = np.linspace(0, 2*np.pi, 200)
x = np.sin(t)
y = np.cos(t)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')  # Try the same plot without this line
```
![A circle](/static/images/wk6/circle.png){width=60%}


<div class="exercise" markdown=true>

#### Exercise 6.1

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/148779/2d-parametric-curve-rhodonea/embed/?token=4c2a720f-2170-446b-b025-1eef1e399c12
" data-id="exercise-6-1" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="exercise" markdown=true>


#### Exercise 6.2

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/148781/parametric-curve-arrows/embed/?token=4fb7cd35-d507-4e81-8c14-039aac294b24" data-id="exercise-6-1" data-cta="Show Exercise"></numbas-embed>

</div>



## 6.2) Plots that require meshgrid

Almost all of the plots we have produced so far use the same model as the parametric plots above:

1. Set up arrays for independent and dependent variables `x`, `y`.
2. Plot `y` against `x` via `plt.plot()` or similar.

In order to visualize more complicated data we need to use a slightly more complicated method. Specifically, we require an intermediate object known as a `meshgrid`.

### Vector plots (a.k.a. quiver plots)

[📖 Matplotlib documentation on `plt.quiver`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.quiver.html){target="_blank"}

Consider a function $f(x,y) = (u,v)$, that takes a vector $(x,y)$ and outputs another vector $(u,v)$. Such functions are often known as *vector fields*, as they can be thought of as placing the vector $(u,v)$ at the point $(x,y)$ in the $(x,y)$-plane.

For example, the function $f(x,y) = (1,1)$ places the vector $(1,1)$ at every point in the $(x,y)$-plane:

![A vector plot of the function f(x,y) = (1,1).](/static/images/week6/quiver1.png){width="60%"}

The function $f(x,y) = (-y,x)$ places the vector $(-y,x)$ at every point in the $(x,y)$-plane:

![A vector plot of the function f(x,y) = (-y,x).](/static/images/week6/quiver2.png){width="60%"}

Notice that in the second plot the magnitude of the vectors changes, as it depends on the value of $x$ and $y$, whereas the magnitude of the vectors in the first plot is constant. Also, we have only plotted a selection of the vectors produced by $f$: if we tried to plot every vector the image would be impossible to interpret.

How where these plots created? We'll illustrate the method using the following function

$$f(x,y) = (\sin(x),\cos(x)+\sin(y))$$

Denote $u = \sin(x)$ and $v = \cos(x)+\sin(y)$. We'll produce a plot of the vectors $f(x,y) = (u,v)$ for linearly spaced $x$ and $y$ points in the interval $[-4,4]$.

Our first instinct may be to use a pair of arrays like

```python
x = np.arange(-4,4)
y = np.arange(-4,4)
```

But upon plotting it is clear that this does produce enough points:

```python
plt.plot(x,y,'o')
```

![A grid of x and y values set up without meshgrid.](/static/images/wk6/lecture_nomeshgrid.png){width="60%"}

This is has occured because `plt.plot()` only considers the points `[x[i], y[i]]`. In order to produce a plot of the vector field $f(x,y) = (\sin(x),\cos(x)+\sin(y))$ we also require the points `[x[i], y[j]]` for $i \neq j$.

We can do this using the function `np.meshgrid()`, that yields the result

![A grid of x and y values, set up with NumPy's meshgrid function shows an x and y value at every permutation of x and y coordinates.](/static/images/wk6/lecture_meshgrid.png){width="60%"}

The specific procedure is as follows.

First we set arrays of the desired $x$ and $y$ points. The `start,stop,step` functionality of `np.arange` is often useful here, as we can use the `step` term to ensure that the plotted vectors will not be too close together 

```python
x = np.arange(-4, 4.5, 0.5)
y = np.arange(-4, 4.5, 0.5)
```

The function `np.meshgrid()` transforms two 1D arrays into a 2D array i.e. the desired grid of points

```python
X,Y = np.meshgrid(x, y)
```

It is very important to note that `np.meshgrid` creates two variables, `X` and `Y`, that we can use separately. The simplest way to think about them is as separate variables linked together in Python's memory. For example, we can see that `x` and `X` have different properties by consulting their shapes

```python
print(x.shape)
print(X.shape)
```

```output
(10,)
(10, 10)
```

We can now implement the function $f(x,y) = (u,v)$ in Python using the variables `X` and `Y`. As $f(x,y) = (\sin(x),\cos(x)+\sin(y))$, we set

```python
U = np.sin(Y)
V = np.cos(X)+np.sin(Y)
```

The function `plt.quiver()` creates the desired vector plot via the following syntax

```python
plt.quiver(X,Y,U,V)
```

Here is the complete code (with labels):

```python
"""
A vector plot
"""
import matplotlib.pyplot as plt
import numpy as np

# Set up meshgrid
x = np.arange(-4,4.5, 0.5)
y = np.arange(-4,4.5, 0.5)
X, Y = np.meshgrid(x, y)

# Components of the function f(x,y) = (u,v)
U = np.sin(Y)
V = np.cos(X)+np.sin(Y)

# Vector plot
plt.quiver(X,Y,U,V)

# Labels etc
plt.xlabel('x')
plt.ylabel('y')
```
 
![A vector plot](/static/images/wk6/practical_vector.png){width=70%}


<div class="exercise" markdown=true>

#### Exercise 6.3

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/131948/vector-plot-practice/embed/?token=6d553481-052e-488f-9048-80f8928e0983" data-id="exercise-6-1" data-cta="Show Exercise"></numbas-embed>
</div>


### Contour plots

Consider a multivariable function $f (x,y) = z$, that takes a vector $(x,y)$ and returns a number $z$. Such functions are often known as *scalar fields* (in contrast to the vector fields considered above). Later in the handout we will see how such functions can be visualized in 3D, treating $z$ as the height above the $(x,y)$-plane. However, before we see such 3D visualizations we'll consider an alternative way to visualize functions $f (x,y) = z$ that does not require a 3D plot.

Specifically, we can use a *contour plot* to present the value of $z$, using lines of constant $z$ value (as is done with contour lines on an Ordnance Survey map). To do so we combine a `meshgrid` with the functions `plt.contour` and `plt.contourf`.

We'll illustrate this by plotting the the function $\displaystyle f(x,y)=\sqrt{x^2+y^2}$ for $x$ and $y$ in the range $[-5,5]$:

```python
import matplotlib.pyplot as plt
import numpy as np

# Set up arrays for the domain
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

# Create meshgrid
X,Y = np.meshgrid(x,y)

# Define Z in terms of X and Y
Z = np.sqrt(X**2 + Y**2)
        
# Plot
plt.contour(X,Y,Z)
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.show()
```

![A contour plot.](/static/images/wk6/contour_notfilled.png){width="60%"}


By replacing `plt.contour` with `plt.contourf` we obtain a filled contour plot:

```python
plt.contourf(X,Y,Z)
plt.colorbar()
```

![A filled contour plot.](/static/images/wk6/contour.png){width="60%"}


##  6.3) 3D plots 

By default Matplotlib expects to produce a 2D plot i.e. with a pair of axes. To create 3D plots we must use the option `projection='3d'`, as follows

```python
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
```

Notice that we have create a figure object with `fig = plt.figure()`, and then converted this figure to a 3D plot using `ax = plt.axes(projection='3d')`. This second command produces a set of 3-dimensional axes, that we can add plots to. At present the axes are empty:

![Empty 3D axes](/static/images/wk6/empty3d.png){width=60%}


### 3D parametric plots

Once the 3D axes have been set up, adding plots to them is very similar to adding 2D plots, albeit with modified syntax. Perhaps the simplest example is provided by a 3D parametric function, such as those you may have encountered in a Vector Calculus module

$$ f (t ) = (x,y,z), \quad t \in [a,b] $$

That is, such a function takes an input $t$ (the parameter), and returns a point in 3D space. Here is an example, plotting the function $f(t) = (\sin(t), \cos(t), t)$ for $t \in [0,30]$:

```python
import matplotlib.pyplot as plt
import numpy as np

# new figure
fig = plt.figure(figsize=(5,4), dpi=300)

ax = plt.axes(projection='3d')

t = np.linspace(0, 30, 300)
x = np.sin(t)
y = np.cos(t)
z = t

ax.plot(x, y, z)

# Set axes label
ax.set_xlabel('x',labelpad=20) 
ax.set_ylabel('y',labelpad=20) 
ax.set_zlabel('z',labelpad=20) 
```

![Parametric 3D](/static/images/wk6/parametric3d.png){width=60%}

Some important points:

* Notice that we have controlled the size and resolution (i.e. level of detail) of the produced plot using the command `fig = plt.figure(figsize=(5,4), dpi=300)`. Try varying these size parameters and observing the result.
* Notice the new syntax for specifiying the axes labels when plotting in 3D: `ax.set_xlabel('x',labelpad=20)`, and so on. The option `labelpad=20` controls how close to the axes the label is, and is discussed in more detail below.

We can also create 3D scatter plots using the following syntax:

```plt.plot
x = [1,6,3,7,5]
y = [3,6,1,9,4]
z = [1,10,12,3,5]

ax.scatter(x, y, z, c='firebrick', s = 100)
```

![Parametric 3D](/static/images/wk6/scatter3d.png){width=60%}



### 3D vector plots

Previously in the handout we considered plotting functions $f(x,y) = (u,v)$, that take a vector as input and return another vector. We referred to such functions as *vector fields*, as they can be thought of as placing a vector at every point in the $(x,y)$-plane.

This concept can be generalised to 3-dimensions. That is, we also refer to a function $f(x,y,z) = (u,v,w)$ as a vector field, as it takes a point in 3-dimensional space $(x,y,z)$ and associates a vector $(u,v,w)$.

We can visualize 3D vector fields in much the same was as we did 2D vector fields, by using additional arguments for `np.meshgrid` and `plt.quiver`. Here we illustrate this for the function $f(x,y,z) = (-x,-y,-z)$:

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(7,5),dpi=500)
ax = plt.axes(projection='3d')

# Set up meshgrid
x = np.arange(-4,4.5, 2)
y = np.arange(-4,4.5, 2)
z = np.arange(-4,4.5, 2)
X, Y, Z = np.meshgrid(x, y, z)

# Components of the function f(x,y,z)
U = -X
V = -Y
W = -Z

# Vector plot
ax.quiver(X,Y,Z,U,V,W,normalize=True)

# Add labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
```

![Parametric 3D](/static/images/week6/quiver3.png){width=60%}

Notice that we have used the option `normalize=True` when calling `plt.quiver`. This normalizes all plotted vectors to be of length $1$ i.e. it only displays the *direction* of the vector, and not their magnitude. Try running the code above without this option to see why it's very useful.

### Surface plots

Previously in the handout we considered producing a contour plot of functions of the form $f(x,y) = z$ a.k.a. scalar fields: functions that take in a vector $(x,y)$ and return a number $z$. Contour plots produced in this way have their advantages, but we also wish to be able to visualize such functions in 3D.

To do so we'll interpret the output $z$ as the height above the $(x,y)$-plane. That is, for every point $(x,y)$ the function returns a value $f(x,y)$, and we'll plot the point $(x,y,f(x,y))$ on 3D axes. By varying $x$ and $y$ the points $(x,y,f(x,y))$ describe a surface, sitting above the $(x,y)$-plane.

As we did in the case of contour plots we'll use a `meshgrid`, as follows. We'll illustrate the method using the function $f(x,y) = \sqrt{x^2+y^2} = z$, for $x$ and $y$ in the range $[-4,4]$.

First create arrays for the desired $x$ and $y$ values

```python
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
```

and use them to create a `meshgrid`

```python
X,Y = np.meshgrid(x, y)
```

We use the variables $X$ and $Y$ to implement the function $f(x,y) = \sqrt{x^2+y^2}$ in Python

```python
Z = np.sqrt(X**2 + Y**2)
```

(Note that `Z` is a function of `X` and `Y`, so that it is a 2D array.)


We can produce a 3D plot of $f(x,y) = \sqrt{x^2+y^2}$ using the command `plot_surface()`:

```python
surf = ax.plot_surface(X, Y, Z, cmap='seismic')
```
The option `cmap` sets the colormap of the resulting surface. There are many other options, as described on [this page](https://matplotlib.org/tutorials/colors/colormaps.html){target="_blank"}

A bar displaying the colour legend can be added via

```python
plt.colorbar(surf)
```

The complete code is as follows


```python
"""
A surface plot
"""
import matplotlib.pyplot as plt
import numpy as np

# 3d axes
ax = plt.axes(projection='3d')

# Set up meshgrid
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x, y)
 
# Define function to plot 
Z = np.sqrt(X**2 + Y**2)

# Create surface plot
surf = ax.plot_surface(X, Y, Z, cmap='seismic')

# Add a colorbar
plt.colorbar(surf, shrink=0.5)

# Add labels
ax.set_xlabel('x',labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('f(x,y)', labelpad=10)
plt.show()
```

![A surface plot](/static/images/wk6/surf.png){width=70%}



#### Surface plot figure adjustments

It is often desirable to tweak the output plot, in particular to ensure that axis labels and titles are not pushed out of frame by the axes themselves. The following commands come in useful when doing so:


```python
ax.set_xlabel('x',labelpad=20)   # labelpad adds some padding to the label e.g. creates distance between it and other objects
```

The size of the resulting plot can be altered with the following commands

```python
# Change the size of the axes
ax.dist = 10    
# Change the size of the figure
fig.dist = 10
```

Try adding these commands to your plots and changing the parameters. It is also often useful to alter the step size in the `x` and `y` arrays, so create a higher fidelity plot of the surface e.g. change `x = np.linspace(-4, 4, 25)` to `x = np.linspace(-4, 4, 100)`. This is particularly noticable at larger plot sizes.


<div class="exercise" markdown=true>

#### Exercise 6.4  

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/131601/surface-plots/embed/?token=cdcc8f80-4b24-44a2-9515-95fc4e383292" data-id="exercise-6-2" data-cta="Show Exercise"></numbas-embed>
</div>

#### Rotating 3D images 

In the Spyder console (not in your script via the Editor window) type the command `%matplotlib qt`

![Matplotlib qt](/static/images/wk6/matplotlibqt.png){width=300px}

Running your script again will open a new window in which you'll be able to rotate the 3D plot created above:

![Matplotlib qt](/static/images/wk6/surfaceqt.gif){width=80%}

This can be turned off (and normal plotting behaviour recovered) via the command `%matplotlib inline` (again in the console):

![Matplotlib qt](/static/images/wk6/matplotlibinline.png){width=300px}

<div class="interlude" markdown=true>

##### Interlude: Magic commands

The commands above starting with `%` are known as 'magic commands', and are designed to make common tasks (such as rotating a figure) as easy as possible. Here are a couple more examples, that are to be run in the console as in the above example.

The command `whos` produces a list of variables and their structure (similar to what is visible in the variable explorer)

```
%whos
```

The command `reset` resets all variables, and is often a quicker alternative to restarting the Python kernel

```
%reset
```

</div>


## 6.4) Figure customization

📖 Matplotlib documentation on [plt.figure](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html){target="_blank"}

The `figure` environment can be extensively customized. We now discuss some of the available options.

Figures are created via the command

```python
plt.figure()
```

The simplest way to think of a `figure` is as a bundle of plot objects: every time Python is instructed to create a plot object it will add it to the current figure, and display it.

It can be useful to assign a `figure` object to a variable via the syntax

```python
fig = plt.figure()
```

As we'll see below, doing so allows us to greater control of the display of the figure.

### Figure size

The following options are used to change the figure size and resolution

* `figsize` specifies the size in inches as `figsize=(width,height)`
* `dpi` specifies the resolution of the image (in dots per inch)

The commands `ax.dist` and `fig.dist` described above do not apply to all plot types, but the commands `figsize` and `dpi` can be applied to any plot. They are implemented as follows

```python
# Change the figure size
plt.figure(figsize=(6,4),dpi=300)
```

### Font size

For technical reasons changing the figure size (usually) not change the font size accordingly. We can manually control the font size as follows

```python
# Change the font size
plt.rcParams['font.size'] = 20
```
The font size for individual text elements can be controlled as follows

```python
plt.xlabel('A huge label', fontsize=40)
```
(The units are points, as used in Word and other word processors.)


### LaTeX

📖 Matplotlib documentation on [LaTeX in plots](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html){target="_blank"}

LaTeX is a typesetting language for mathematics, and is universal across academia: almost every document you have encountered in your modules so far will include LaTeX to some degree.

**LaTeX is not required for this module**. However, if you wish to make the mathematics used in your plots more aesthetically pleasing you can use LaTeX via the dollar symbol e.g.

```python
# Use latex in a label
plt.ylabel('$\phi$')
```

Depending on the context you may need to escape the backslash characters used in LaTeX e.g. Python may report an error if you attempt to use the caption `'$\sin(x)$'`. To escape the slahes we simply add an extra slash, so that the command becomes `'$\\sin(x)$'`.

[This reference is a good place to get started](https://en.wikibooks.org/wiki/LaTeX/Mathematics){target="_blank"}.

### Further adjustments


#### Limits

For 2D plots we can use `plt.xlim` and `plt.ylim` to control the axis ranges

```python
plt.xlim([0,1])
plt.ylim([-1,2])
```

The syntax is for 3D plots is as follows

```python
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,1.5)
ax.set_zlim(0,3.5
```

#### Legends

Legends can be added via

```python
plt.plot(x,2*x)
plt.plot(x,3*x)
plt.legend(['2x','3x'])
```

or 

```python
plt.plot(x,2*x,label='2x')
plt.plot(x,3*x,label='3x')
plt.legend()
```

#### Grid

Grid lines can be added to 2D plots via

```python
# Optional grid
plt.grid()
```


### Annotations

Text can be added at a desired point via

```python
plt.text(0.5,-0.5,'Some text')
```

We can use `plt.annotate` to further decorate plots, for example:

```python
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,4),dpi=300)

x = np.linspace(0,np.pi,100)
y = np.cos(x)
plt.plot(x,y)

# Text
plt.text(0.5,-0.5,'Some text')

# An arrow
plt.annotate('Text with an arrow', xy=(np.pi/2,0), xytext=(2,0.7),
             arrowprops=dict(facecolor='firebrick'))

plt.xlabel('x')
plt.ylabel('y')
```

![A plot with an annotation](/static/images/wk6/annotation.png){width=70%}

### Horizontal and vertical lines

Horizontal and vertical lines can be added to 2D plots via the commands`plt.axhline` and `plt.axvline`, for example

```python
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(6,4),dpi=300)

x = np.linspace(-15, 15, 200)
y = np.sin(x)/x

plt.plot(x, y, label='f(x) = sin(x) / x')

# Horizontal and vertical lines
plt.axvline(0, color='firebrick', linestyle='--')
plt.axhline(0, color='forestgreen', linestyle='--')

plt.xlabel('x')
plt.ylabel('y')
```

![axhline and axvline](/static/images/wk6/axlines.png){width=70%}

### Force axes go through (0,0)

By default Matplotlib will not draw axes passing through the origin. We can force this behaviour using the command `ax = plt.gca()`, as follows

```python
import numpy as np
import matplotlib.pyplot as plt

# Random plot
x = np.linspace(-1,1,100)
plt.plot(x, x**3)

# Get axes object
ax = plt.gca()

# Set axis positions to zero
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')

# Hide right and top
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
```
![Plot through the origin](/static/images/wk6/origin.png){width=70%}

Note that if this method is used we need to manaully add the axis labels using annotations.

### Saving figures

The easiest way to save your figures is to right click on the plot in Spyder and save to your computer (or use the save button in the top of the plot window).

Sometimes it's useful to include a command to save a plot inside your script e.g. if you're creating many plots.

To do so we first use the command `plt.figure` to attach the `figure` object to a variable

```python
fig = plt.figure()  
```

We can then save the figure using the syntax

```python
fig.savefig("filename.png")
```

Note that the string `"filename.png"` can be a full path to a location on your computer. As written above the figure will be saved to the same location as the script.

The function but `savefig` can produce several formats in addition to `.png`. For more more details use consult the help

```python
help(plt.savefig)
```

## 6.5) Subplots

It is often desirable to have multiple axes collected into a single figure. We can achieve this using the `subplot()` function, that creates a grid structure on which to place multiple plots. The function `subplot()` takes three arguments: the first specifies the number of rows of the grid, the second the number of columns, and the third the current plot number, starting with 1. Here is an example of plotting two axes side by side:

```python
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,4),dpi=300)

x = np.linspace(0,10,100)

# one row, two columns, first plot
plt.subplot(1,2,1)            
plt.plot(x,np.sin(x),'--')
plt.xlabel('x')

# one row, two columns, second plot 
plt.subplot(1,2,2)            
plt.plot(x,np.cos(x),'--')
plt.xlabel('x')

fig.suptitle("Figure title")
```

![Subplot figure](/static/images/wk6/subplots.png){width=70%}


<div class="exercise" markdown=true>

#### Exercise 6.5

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/76919/oscillations-subplot/embed/?token=ebcaa9e9-1258-4f76-90b1-b383b908d106" data-id="exercise-6-5" data-cta="Show Exercise"></numbas-embed>
</div>

## 6.6) Plotting data from files

In Week 2 we considered reading in external data files:

```python
# Read in a text file
data = np.loadtxt('data.txt')

# Read in a CSV with comma delimiter and a header row
data = np.loadtxt('data.csv', delimiter=',', skiprows=1)

# As above but unpack two columns into two variables x,y
x,y = np.loadtxt('data.csv', delimiter=',', skiprows=1, unpack=True)
```

### Reading and plotting multidimensional data 

It is very common in academia and industry to work with datasets that contain many variables. In Week 2 we only worked with datasets containing two variables, `x` and `y`, but we can use similar techniques to handle multidimensional data.

#### Example: temperature contour plot

Supose that we have recoreded the value of the temperature across a metal sheet. Specifically, we have a temperature value $t$ for each point $(x,y)$ stored in a CSV file:

```python
x,y,t
0,0,0.7
0.5,0,0.6
1,0,0.5
0,0.5,0.8
0.5,0.5,0.7
1,0.5,0.6
0,1,0.9
0.5,1,0.8
1,1,0.7
```

You can [download the file here](/static/data/temp_data_small.csv). We load it into Python as follows

```python
x,y,t = np.loadtxt('data.csv',delimiter=',',skiprows=1, unpack=True)
```

However, we can't immediately plot this data as the arrays `x`,`y`, and `T` are all 1D. To produce plots we can either use a `meshgrid`, or use specialised built-in functions.

##### Triangulation functions

Perhaps the simplest method is to the function `tricontour`, that is specifically designed to plot data in this form

```python
# Contour plot
plt.tricontour(x, y, t, cmap='viridis')

# Filled contour plot
plt.tricontourf(x, y, t, cmap='viridis')
```
 

##### `meshgrid`

We can also use a `meshgrid` to produce a plot of this dataset.

First, notice that the $x$ and $y$ values are $[0,0.5,1]$. We can create these manually via

```python
[X,Y] = np.meshgrid([0,0.5,1],[0,0.5,1]) 
```

However, in general we would like to extract the correct values from the dataset itself. In this case we notice that the first three $x$ values are $[0,0.5,1]$, so we can take

```python
n = 3
x_vals = x[:3]
```

By further inspection we determine that we can obtain $[0,0.5,1]$ by running through `y` with a step size of $3$

```python
y_vals = y[::3]
```

Note that this is `y[start:stop:3]` where `start` and `stop` are left empty, as we wish to run through the whole list array `y`.

We can now construct the desired `meshgrid` as

```python
n = 3
x_vals = x[0:3]
y_vals = y[::3]
X,Y = np.meshgrid(x_vals,y_vals)
```

The temperature values are

```python
print(t)
```
```output
array([0.7, 0.6, 0.5, 0.8, 0.7, 0.6, 0.9, 0.8, 0.7])
```

We can use `reshape` to convert this into an array of the correct size

```python
T = t.reshape([3,3])
```
and use `plt.contour` or `plt.contourf` to produce the plot. The complete code is

```python
import numpy as np
import matplotlib.pyplot as plt

# Load data
x,y,t = np.loadtxt('data.csv',delimiter=',',skiprows=1, unpack=True)

# n by n grid of points
n = 3

# Set up meshgrid
x_vals = x[0:3]
y_vals = y[::3]
X,Y = np.meshgrid(x_vals,y_vals)

# Place temperature values on grid
T = t.reshape([3,3])

# Plot
plt.contourf(X,Y,T)
plt.colorbar()
plt.show()
```


<div class="interlude" markdown=true>

### Reading data with pandas

**Pandas** is a Python module that is used extensively in data science. It is not part of this module, but we include a brief discussion here as it may be useful for you in other modules.

The central tool of provided by Pandas is a *dataframe*. Here's an example: consider the short CSV

```
year,city,population
2023,Newcastle,823000
2023,Sheffield,746000
2022,Newcastle,818000
2022,Sheffield,741000
2021,Newcastle,814000
2021,Sheffield,735000
2020,Newcastle,809000
2020,Sheffield,730000
```
You can [download the file here](/static/data/pandas_cities.csv).

Import the pandas module via

```python
import pandas as pd 
```

A CSV file can be loaded into a dataframe `df` via 

```python
df = pd.read_csv('pandas_cities.csv')
```

We can view the dataframe via

```python
print(pd)
head(pd)  # View the top of the dataframe
tail(pd)  # View the bottom of the dataframe
```

Individual columns of the dataframe are extracted via

```python
# population data series
df["population"]

# as a numpy array
df["population"].to_numpy()

```

Dataframes can be quiered like lists and arrays

```python
ncl = df[df["city"]=="Newcastle"]
ncl["population"]
```

We could plot the data in the CSV using Pandas as follows

```python
import matplotlib.pyplot as plt
import pandas as pd

# Read the dataframe
df = pd.read_csv('pandas_cities.csv')

# Create subsets for ncl and sheff
ncl = df[df["city"]=="Newcastle"]
sheff = df[df["city"]=="Sheffield"]

# Plot
plt.plot(ncl["year"],ncl["population"],'-o',label="Newcastle")
plt.plot(sheff["year"],sheff["population"],'--o',label="Sheffield")

# Make pretty
plt.legend()
plt.xlabel('Year')
plt.ylabel('Population')
```

![A pandas image](/static/images/wk6/pandas_image.png){width=60%}

</div>


## Next week

In Week 7 we'll consider methods for estimating derivatives and integrals using Python.

