---
toc: false
css:
  - custom.css
---

# MAS1801 Python Practical 2

Welcome to the handout for the second week of Python material.

#### To Hand in this week: {.handin}

Upload your solutions to:

* Exercise 2.8

to NESS by midnight this **Sunday 18th Neverember**. [Click here to view instructions on how to upload to NESS](../introduction_and_handouts/uploading_to_ness.html){target="_blank"}. 

## Week 1 Recap

### Writing scripts

From here on I will drop the '>>>' prompt from my handout, as I expect you to type code into the Editor window and run it.


## The *matplotlib* module


Last week we imported and used the *numpy* module and we'll be doing so again today. We'll also be getting access to plotting tools through the *matplotlib* module.

In fact *matplotlib* is pretty extensive, it's a module containing many submodules, and we are only interested at the moment in one part of, called *pyplot*, which we can reference with `matplotlib.pyplot`. So let's load in that, and as last week create a shortcut to it. In a script:

``` {.code .python}
import matplotlib.pyplot as plt
```

Getting started with *matplotlib* is now pretty straightforward.

```{.code .python}
plt.plot([1,4,9,16]);
plt.show()
```

The first `plt` command creates a plot object. The second will display it in the Console.

With only a single argument, `plot()` will plot the list against its index. 


## 2D plotting

We can give `plot()` two lists to make a 'y versus x' plot.

```{.code .python}
plt.plot([1,2,3,4],[1,4,9,16]);
plt.show()
```



and can get the same thing by defining some variables

```{.code .python}
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y);
plt.show()
```



Let's bring in *numpy* to make a nice sine curve

```{.code .python}
import numpy as np
```

```{.code .python}
x = np.arange(0,10)
plt.plot(x,np.sin(x))
plt.show()
```

And note that your script might now look something like

```{.code .python}
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
plt.plot(x,np.sin(x))
plt.show()
```



OK, so it's not very smooth! We can use the `arange()` function to give us a nice smooth range of x values. Earlier we used this to create integer sequences, and if you recall it had a third argument for the step size.  `arange()` can also accept float arguments, for example:


```{.code .python}
np.arange(0.0,10.0,0.1)
```

Or even better, the function `linspace` accepts a start, end and number of values

```{.code .python}
np.linspace(0,10,100)     # 100 values between 0 and 10
```


Let's use this with our plotting command:

```{.code .python}
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.show()
```


Much better! Now lets add some axis labels

```{.code .python}
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x))
plt.xlabel('x') 
plt.ylabel('sin(x)')
plt.show()
```


By default we get a plot with a line through the points. The third argument to pyplot accepts a number of options to change this, for example `bo` will give blue circle markers

```{.code .python}
plt.plot(x,np.sin(x),'bo')
plt.show()
```

You can view more options with

```{.code .python}
help(np.plot)
```

Or in the [*matplotlib* online documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot).


### Exercise 2.1 {.exercise}

Investigate the help for pyplot, including how to change the line width and marker size.

For a bit of fun, try to recreate this (frankly pretty ugly) plot of $f(x)=x^3$. Note the range $-5\le x \le 5$.


### Adding multiple lines

We can add multiple lines to a single plot by adding further arguments to the `plot()` function

```{.code .python}
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x),'b',x,np.cos(x),'r--')
plt.show()
```

You might like to add a legend: *pyplot*'s legend accepts a list of strings:

```{.code .python}
plt.legend(['sin(x)','cos(x)'],loc=1))
```

The `loc` option sets the location - see `help(plt.legend)` - and perhaps a title

```{.code .python}
plt.title('My awesome plot')
```

We can set explicit limits for the x axis using `xlim` (and similar `ylim` if desired)

```{.code .python}
plt.xlim(0,10) 
```


Put together your whole script might now look like

```{.code .python}
# import required modules
import matplotlib.pyplot as plt
import numpy as np

# Grid of values from 0 to 10.
x = np.linspace(0,10,100)

# Plot sin(x) and cos(x)
plt.plot(x,np.sin(x),'b',x,np.cos(x),'r--')

# Make the plot pretty
plt.legend(['sin(x)','cos(x)'],loc=1)
plt.xlabel('x')
plt.xlim(0,10) 
plt.title('My awesome plot')

# Show the plot
plt.show()
```

### Exercise 2.2 {.exercise}


** black friday exercise **

### Sub-plots

It is often desirable to have multiple axes inside a single figure window. The `subplot()` function takes three arguments, the first specifies the number of rows, the second the number of columns, and the third the current plot number, starting with 1. So it goes like this:

```{.code .python}
x = np.linspace(0,10,100)

# First plot
plt.subplot(121)            # one row, two columns, first plot
plt.plot(x,np.sin(x),'--')

# Second plot
plt.subplot(122)            # one row, two columns, second plot 
plt.plot(x,np.cos(x),'--')
```


### Exercise 2.3 {.exercise}

The equation

$$x(t) = 2e^{\left(-\frac{t}{10}\right)}\cos(t)$$

represents the dispalcement $x(t)$ of an oscillator dying away due to the damping effect of e.g. air resistance. 

Place two plots on a single figure:
 
* the function $x(t)$; and
* the oscillation of the pendulum with no friction, given by $x_{0}(t) = 2\cos(t)$.

to recreate the below plot


### Interlude 2.1: It must be love {.interlude}

```{.code .python}
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2,2,100)
y=(np.sqrt(np.cos(x))*np.cos(200*x)+np.sqrt(np.abs(x))-0.7)*(4-x*x)**0.01;
plt.plot(x,y)
```

## Histograms and random numbers

### Random numbers from the uniform distribution

The *numpy* function `random.rand()` returns an array of random floats from the uniform distrbution on [0,1], in the dimensions specified by its argument. There are two other functions (`random.random()` and `random.random_sample()`) which do very similar jobs, so you might see those if you are browsing through documentation / the internet. We'l use `random.rand()` though, as it is very convenient. Here are some examples

```{.code .python}
np.random.rand()      # one value
```

```{.code .python}
np.random.rand(2)      # two values in a row vector
```

```{.code .python}
np.random.rand(1,2)    # the same as the above
```

```{.code .python}
np.random.rand(2,1)    # two values in a column vector
```

```{.code .python}
np.random.rand(2,2)    # 2 x 2 array
```

That's all very well, but what if we would like, say, 20 numbers in the range 0 to 10. We can multiply up:

```{.code .python}
10*np.random.rand(20,1)    
```

Marvellous. Let's visualise this with a histogram. *matplotlib.pyplot* has a function `hist()` just for this. Note that in this and the last command I've stored the values as a column, rather than row. `hist()` likes it this way!

```{.code .python}
x = 10*np.random.rand(20,1)  
plt.hist(x)  
```

Note you (probably) won't get the same plot.


There are a number of options to `hist()`, including the number of bins to use:

```{.code .python}
x = 10*np.random.rand(20,1)  
plt.hist(x,bins=5)  
```
So how do we know this is random? Let's ramp up to 100 values:

```{.code .python}
x = 10*np.random.rand(100,1)  
plt.hist(x)  
```

Keep going and you should see your histogram level out. Here's a little animation that I made...


### Exercise 2.4 {.exercise}

* Adjust your code so that you find 100 random numbers as before, but in the range $-5$ to $5$. Plot a histogram of the values.
* Rewrite your script so that two variables, say `a` and `b` are defined to be the limits of the range, and `n` the number of values: 
```{.code .python}
a = -5
b = 5
n = 100
```
write a command for `x` in terms of `a`, `b` and `n`.


### Random integers

The function `random.randint()` returns random integers from the discrete uniform distribution in a specified interval. 

```{.code .python}
np.random.randint(10)    # random integer between 0 and 9
```

```{.code .python}
np.random.randint(0,10)    # as above
```

```{.code .python}
np.random.randint(5,10)    # random integer between 5 and 9
```

```{.code .python}
np.random.randint(5,10, size = 10)    # 10 random integers between 5 and 9
```

```{.code .python}
np.random.randint(5,10, size = (5,5))    # 5 x 5 array of random integers
```



### Random numbers from the normal distribution

Many physical phenomena have a "normal distribution" (a bell-shaped distribution of values). To name but a few: human heights, examination grades, the size of snowflakes and measurement errors.

The function `random.normal(m,s)` returns a random number (float) from the normal distribution with mean `m` and standard deviation `s`. It has a further size option, as for `random.randint()`. 


```{.code .python}
np.random.normal(0,1)   
```

```{.code .python}
np.random.normal(0,1, size = 10) 
```

```{.code .python}
np.random.normal(0,1, size = (5,5)) 
```

Let's generate a histogram

```{.code .python}
x = np.random.normal(0,1, size = 100) 
plt.hist(x)
```

In the case of mean $\mu = 0$, standard deviation $\sigma = 1$, the theoretical probability density $\phi$ of the normal distribution is given by

$$ \phi(x)=\frac{e^{-{\frac{1}{2}x^2}}}{\sqrt{2\pi}} $$

We'll compare this function to the distribution of some randomly generated numbers in the next exercise.



### Exercise 2.5 {.exercise}

You can 'normalise' a histogram using the density option to `hist()` (otherwise the height is the count, and depends on the sample size):
```{.code .python}
x = np.random.normal(0,1, size = 100) 
plt.hist(x, density=True)
``` 
* Have a go at fitting the function $\phi$ above onto the histogram (using a command `plot()` from earlier will overlay the histogram). You should get something a bit like this:


* Bump up the number of $x$ values and watch your histogram approach $\phi(x)$. You might like to change the number of bins too. Below I have a sample size of 100,000 and 100 bins.



## 3D plots

To create 3D axes with *matplotlib* we use a new module

```{.code .python}
from mpl_toolkits.mplot3d import Axes3D 
```

and set the current axes to have a 3D projection

```{.code .python}
fig = plt.figure()
ax = fig.gca(projection='3d')
```


### Surface plots

A surface is defined mathematically by a function of two independent variables, $f(x,y)$, such that
for each value of $(x, y)$ we compute the "height" of the function, $z= f(x,y)$.

In order to draw a surface, we are going to need a grid of points that covers the region of $x$ and $y$ that we are interested in. In Python this is known as a *meshgrid* and the procedure is as follows:

First set the range of $x$ and $y$ that is of interest. Im going for $[-4,4]$ and I'm choosing a grid of 25x25 points.

```{.code .python}
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
```

The function `meshgrid` transforms two 1D arrays into a grid of values (a 2D array) covering the domain.

```{.code .python}
X, Y = np.meshgrid(x, y)
```

Note the syntax: the output is assigned to two different objects, `X` and `Y`. Compare the dimensions of `x` and `X`

```{.code .python}
print(x.shape)
print(X.shape)
```

Now we are ready to define the height in terms of our new objects `X` and `Y`. I'm going to plot

$$ z = f(x,y) = \cos(\sqrt(x^2+y^2)) $$

```{.code .python}
Z = np.cos(np.sqrt(X**2 + Y**2))
```

Note that `Z` is written in terms of `X` and `Y`. I'm keeping to a convention to keep 2d objects captalised. Due to the element-wise arithmetic, `Z` will have the same dimensions as `X` or `Y`

```{.code .python}
print(Z.shape)
```

Now we are ready to add the surface to our axes, which can be done with

```{.code .python}
surf = ax.plot_surface(X, Y, Z, cmap=cm.seismic)
```
The extra option `cmap` sets the colormap of the surface. Pick your own pretty colour scheme on [this page for a full list of colormaps](https://matplotlib.org/tutorials/colors/colormaps.html)

A bar displaying the colour legend can be added with

```{.code .python}
fig.colorbar(surf)
```

The whole thing looks like this:


```{.code .python}
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

# new figure
fig = plt.figure()
    
# 3d axes
ax = fig.gca(projection='3d')

# Create a meshgrid
x = np.linspace(-4, 4, 25)
y = np.linspace(-4, 4, 25)
X, Y = np.meshgrid(x, y)
 
Z = np.cos(np.sqrt(X**2 + Y**2))

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.seismic)

# Add a colorbar
fig.colorbar(surf, shrink=0.5)

# Axis labels - note applied to the axes in a 3D plot
ax.set_xlabel('x',labelpad=20)
ax.set_ylabel('y', labelpad=20)
ax.set_zlabel('f(x,y)', labelpad=20)

plt.show()
```

#### Aside: Figure adjustments

Sometimes you might find that you need to make adjustments to avoid axis labels/labels/the colorbar from ovelapping or leaving the page. Here are a couple of fixes you can play around with to get your plot looking great:

```{.code .python}
ax.set_xlabel('x',labelpad=20)   # labelpad adds some padding to the label
```

```{.code .python}
fig.set_size_inches(12, 6)       # Changes the size of the figure window.
```

```{.code .python}
fig.set_size_inches(12, 6)       # Changes the size of the figure window.
```

```{.code .python}
ax.dist = 10  	# Changes the size of the axes ("distance away from it")
# or
fig.dist = 10  	# Changes the size of the figure

```			

### Exercise 2.6 {.exercise}

Have a go at changing some of these parameters. 

In addition have a go at changing the step size in the definitions of `x` and `y`. This will change the density of the grid and in turn how the surface looks. You should find that too few grid points (larger step size) will give you a surface that is not smooth. You'll notice that if you reduce the step size you'll no longer see an effect beyond a certain point - that's because *matplotlib* quite sensibly downsamples the points to give you a sensible looking surface. This can be changed with the `rcount` option if you really, really want.



## Vector plots

A vector field is a collection of vectors (arrows) with a given magnitude and direction, each attached to a point in some space. For example, a vector defined at every point on an (x,y) grid. Vector fields are an important tool for visualisation in for example fluid dynamics (the flow of a fluid), gravitation and many other areas.

I'm going to plot the field

$$\vec{v}=(u,v)=(\sin(x),\cos(x)+\sin(y))$$


Becuse a vector is defined at each point on (x,y), we once again need a meshgrid. I'll use `arange()` this time.

```{.code .python}
x = np.arange(-4, 4.5, 0.5)
y = np.arange(-4, 4.5, 0.5)
X, Y = np.meshgrid(x, y)
```
Then we can define components of a vector in terms of X and Y

```{.code .python}
U = sin(Y)
V = cos(X)+sin(Y)
```

The `quiver()` function creates a vector plot

```{.code .python}
plt.quiver(X,Y,U,V)
```

Here's the whole thing, tidied up with axis labels etc

```{.code .python}
import matplotlib.pyplot as plt
import numpy as np

# Set up a meshgrid
x = np.arange(-4,4.5, 0.5)
y = np.arange(-4,4.5, 0.5)
X, Y = np.meshgrid(x, y)

# Components of our vector field
U = np.sin(Y)
V = np.cos(X)+np.sin(Y)

# Quiver plot
plt.quiver(X,Y,U,V)

# Make pretty
plt.xlabel('x')
plt.ylabel('y')
```


### Exercise 2.7 {.exercise}

Create a quiver plot of the vector field

$$\vec{v}=(u,v)=(y\cos(x),y\sin(x))$$

## More plotting

There's an awful lot that *matplotlib* can do beyond what we've discussed today. The [Matplotlib gallery page](https://matplotlib.org/gallery/index.html) has lots of inspiration and example code if you want to check out other possibilies. 


### Interlude 2.2: xkcd plots {.interlude}

The webcomic [Xkcd](https://en.wikipedia.org/wiki/Xkcd) was clearly popular with someone on the *matplotlib* team, as they added the method `xkcd()` to 'cartoonise' your plots (including the quiver and surface examples above)!


```{.code .python}
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()
x = np.linspace(0,10,100)   
plt.plot(x,np.sin(x),x,np.cos(x))
plt.legend(['sin(x)','cos(x)'])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Ensure that we go back to default settings
matplotlib.rcdefaults() 
```


Don't even think about handing work in using this style! :-)


### Exercise 2.8 {.handin}

Write a script file to produce the following two plots (there is no need to submit the images themselves, we'll generate them from your code, though you should make them pretty!).

**(a)** Make a plot of 

$$ f(x) = \frac{x^2+x+1}{x+1}, \quad  -1\le x \le 10 $$

(Don't worry about the singularity at $x=-1$, Python will still make the plot). On the same figure, add the asymptote for the function $y = x$, using a dashed line. 

Find the distance between $f(x)$ and the asymptote at $x = 10$ and print its value in your code.

**(b)** Plot the following function as a surface:

$$ f(x,y)=\exp\left(-x^2-y^2\right), \quad -2\le x \le 2,\quad -2\le y \le 2$$


