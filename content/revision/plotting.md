[Click here to open this handout in a new browser tab](#){target="_blank"}

# Plotting

## More on scripts

Before we start, let's talk a little bit more about scripts

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=3c7bb277-debd-480d-ad9c-ada000d4f66a&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


## The Matplotlib module

📖 [Matplotlib.org documentation](https://matplotlib.org/contents.html){target="_blank"}

Last week we imported and used the *NumPy* module and we'll be doing so again today. We'll also be getting access to plotting tools through the *Matplotlib* module.

In fact Matplotlib is pretty extensive: it's a package containing many modules, and we are only interested at the moment in one part, called *pyplot*, which we can reference with `matplotlib.pyplot`. So let's load in that, and as last week create a shortcut to it. In a script:

``` python
import matplotlib.pyplot as plt
```

Getting started with Matplotlib is now pretty straightforward.

```python
plt.plot([1,4,9,16])
```

Note that in older versions of Spyder this will display in the Console; in the latest version of Spyder plots appear in the "plots" tab (next to "help", "variable explorer", etc). If you are using something other than Spyder then you may need the command

```python
plt.show()
```

to display the plot.


With only a single argument, `plt.plot()` will plot a list/array (`[1,4,9,16]` here) against its index (0,1,2,3 here). 

![A plot made up of the points (0,1),(1,4),(2,9) and (3,16)](/static/images/week2/practical_basic.png){width=80%}

Let's see how we can use pyplot to make some beautiful plots:

## 2D plotting with pyplot

📖 [Matplotlib.org Pyplot documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot){target="_blank}

We can give pyplot's  `plot` function two lists, or arrays, to make a 'y versus x' plot. For example,

```python
plt.plot([1,2,3,4],[1,4,9,16])
```

and can get the same thing by defining some variables

```python
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y)
```

Let's start a script off in the left. You won't necessarily want to save every part of this handout, but we'll do a lot of adding or modifying our code, and writing in a script will help:


```python
"""
Script to plot sin(x)
"""
import matplotlib.pyplot as plt

# Make a plot
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y)
```

Click the ▷ *run* button, or *F5* and your plot will appear in the Console.

![A plot made up of the points (1,1),(2,4),(3,9) and (4,16)](/static/images/week2/practical_basic2.png){width=80%}


Now let's make a nice sine curve. Because we need NumPy to compute the sine, and to do so for every element of an array, let's import it as we did last week (actually technically we need *any* module that has a sine function, but we're sticking with NumPy for this purpose).

```python
import numpy as np
```

And as we did at the end of last week, we'll create a numeric array

```python
x = np.arange(0,10)
```

We'll use this to set up an array of `y` values:

```python
y = np.sin(x)
```

And then make a plot of y versus x:

```python
plt.plot(x,y)
```

Put together, your script might now look something like

```python
"""
Script to plot sin(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,10)
y = np.sin(x)
plt.plot(x,y)
```

![A plot of sin(x) versus x which is jagged because of very few x data points.](/static/images/week2/practical_sine0a.png){width=90%}


OK, so it's not very smooth! We can modify the `np.arange()` function to give us a nice smooth range of x values. Earlier we used this to create integer sequences, and if you recall it had a third argument for the step size.  `np.arange()` can also accept float arguments, for example:


```python
x = np.arange(0,10,0.1)
```

Or even better, the function `np.linspace(a,b,n)` defines a list of $n$ linearly-spaced numbers in the interval $[a,b]$, for example

```python
# 100 values between 0 and 10
x = np.linspace(0,10,100)    
```


Let's use this with our plotting command:

```python
"""
Script to plot sin(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
```

![A plot of sin(x) versus x using 100 x values, showing a smooth curve.](/static/images/week2/practical_sine0b.png){width=90%}


Much better! Now let's add some axis labels

```python
"""
Script to plot sin(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x') 
plt.ylabel('sin(x)')
```

![A plot of sin(x) versus x with axis labels](/static/images/week2/practical_sine1.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_sine1.py){target="_blank"}*

By default we get a plot with a line through the points. The third argument to `plt.plot()` accepts a number of options to change this, for example `bo` will give blue circle markers

```python
plt.plot(x,np.sin(x),'bo')
```

![A plot of sin(x) versus x with axis labels and a curve made up of blue circle markers.](/static/images/week2/practical_sine1a.png){width="90%"}

You can view more options by running the following in the console.

```python
help(plt.plot)
```

Or in the [Pyplot online documentation](https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot){target="_blank}.




### Adding multiple lines

We can add multiple lines to a single plot by adding further arguments to the `plot()` function

```python
plt.plot(x,np.sin(x),'b',x,np.cos(x),'r--')
```

Or by using two plot commands. Your script might look like

```python
"""
Script to plot sin(x) and cos(x)
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)
plt.plot(x,np.sin(x),'b')
plt.plot(x,np.cos(x),'r--')
```

![A plot of sin(x) and cos(x) versus x](/static/images/week2/practical_sine_and_cos.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_sine_and_cos.py){target="_blank"}*

You might like to add a legend: `plt.legend()` accepts a list of strings:

```python
plt.legend(['sin(x)','cos(x)'],loc=1)
```

The `loc` option sets the location - see `help(plt.legend)`. Perhaps a title too:

```python
plt.title('Trig. functions')
```

We can set explicit limits for the x axis using `plt.xlim()` (and similar `plt.ylim()` if desired)

```python
plt.xlim(0,10) 
```


Put together your whole script might now look like

```python
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
plt.xlim([0,10]) 
plt.title('Trig. functions')
```


![A plot of sin(x) and cos(x) versus x with a legend, axis labels and a title](/static/images/week2/practical_sine_and_cos_pretty.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_sine_and_cos_pretty.py){target="_blank"}*



## Sub-plots and figures

It is often desirable to have multiple axes inside a single figure window. The `subplot()` function takes three arguments, the first specifies the number of rows, the second the number of columns, and the third the current plot number, starting with 1. So it goes like this:

```python
"""
Subplot example
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,100)

# one row, two columns, first plot
plt.subplot(121)            
plt.plot(x,np.sin(x),'--')

# one row, two columns, second plot 
plt.subplot(122)            
plt.plot(x,np.cos(x),'--')
```

Note that in the below plots I have added a title and axis label. These commands go after each of the `plot` commands. Take a look at the link to the source code below if you are interested.

![Side by side plots of sin(x) and cos(x) created using the subplot commands](/static/images/week2/practical_subplots.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_subplots.py){target="_blank"}*


### Managing figures

The command `plt.figure()` function starts a new figure

```python
"""
Script to create two figures
"""
import numpy as np
import matplotlib.pyplot as plt

# Set up an array
x = np.linspace(0,10,100)

# First figure
plt.figure()
plt.plot(x,np.sin(x))

# Second figure
plt.figure()
plt.plot(x,np.cos(x))
```

Note that in the latest Spyder, you will find the first figure in the plot history (thumbnails to the right of the main plot).

The help for the command `help(plt.figure)` gives other options, for example setting an ID for the figure, or changing its size.

The command `plt.figure()` also returns a figure 'class' which can be assigned to a variable, for example

```python
fig = plt.figure()  
```

Alternatively, if you already have a figure window then the current figure window can be retrieved with

```python
# "get current figure"
fig = plt.gcf()     
```


This then allows the figure properties to be changed dynamically with commands such as

```python
# Changes the size of the figure window.
fig.set_size_inches(12, 6)       
```

Similarly, the current axes can be retrieved with

```python
# "get current axes"
ax = plt.gca()     
```

rather than starting a new figure, you can also clear the current figure with `plt.clf()` or the current axes with `plt.cla()`. For example, this code will only display the cosine curve:

```python
x = np.linspace(0,10,100)
plt.plot(x,np.sin(x),'b')
plt.cla()
plt.plot(x,np.cos(x),'r--')
```

### Saving your plots

If we use the above to assign a figure to an object in Python

```python
fig = plt.figure()  
```

Then once we have made our beautiful plot, we can export our figure with the command

```python
fig.savefig("filename.png")
```

Note that the string could be a full path to a location on your computer, e.g. `"H:/Python/PHY2039/filename.png"`.

This has a number of options. You'll see by opening up any of the source code links under my plots that I set the background to be slightly transparent (so they aren't entirely white in the dark mode of these notes). I use the format "png" as it works well for websites, but `savefig` can save in several other formats.

For more info try the help

```python
help(plt.savefig)
```

Here's a full example, saving a plot to your H: (change this to wherever you like)

```python
"""
save a plot :-)
"""
import numpy as np
import matplotlib.pyplot as plt

# New figure
fig = plt.figure()

# Make a plot
x = np.linspace(-np.pi,np.pi,100)
plt.plot(x,np.sinh(x))

# Make it pretty...

# Save the plot
fig.savefig('myplot.png')
```

## More plotting options

There's an awful lot that Matplotlib can do beyond what we won't have time to discuss today. The [Matplotlib gallery page](https://matplotlib.org/gallery/index.html){target="_blank"} has lots of inspiration and example code if you want to check out other possibilities. 


## Histograms and random numbers

📖 [NumPy random documentation](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html){target="_blank"}


Random numbers are provided by the NumPy module, or in fact a submodule of NumPy called `random`. 

Before we continue, let's talk a little bit about modules and submodules.

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=cdf8893c-814f-42fb-8656-ada000d4f6c9&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


We could import this alone with e.g.

```python
import numpy.random as rnd
```

and then use `rnd.whatever` to access the functions, but I'm assuming we're going to be using other bits of NumPy too, so sticking with

```python
import numpy as np
```

and referring to all of the random distribution functions using `np.random.whatever`.

There are few to look at:


### Random numbers from the uniform distribution

The NumPy function `np.random.rand()` returns an array of random floats from the uniform distribution on [0,1], in the dimensions specified by its argument. There are two other functions (`np.random.random()` and `np.random.random_sample()`) which do very similar jobs, so you might see those if you are browsing through documentation / the internet. We'll use `np.random.rand()` though, as it is very convenient. Here are some examples, probably best to just run these 'one-liners' in the Console at the moment, to get a feel for what they do:

```python
# one value
np.random.rand()     
```

```python
# two values in a row vector
np.random.rand(2)      
```

```python
# the same as the above
np.random.rand(1,2)    
```

```python
# two values in a column vector
np.random.rand(2,1)    
```

```python
# 2 x 2 array
np.random.rand(2,2)    
```

That's all very well, but what if we would like, say, 20 numbers in the range 0 to 10. We can multiply up:

```python
10*np.random.rand(20,1)    
```

Marvellous. Let's visualise this with a histogram. The Matplotlib pyplot submodule has a function `plt.hist()` just for this. Note that in this and the last command I've stored the values as a column, rather than row. `plt.hist()` likes it this way!

```python
import numpy as np
import matplotlib.pyplot as plt

x = 10*np.random.rand(20,1)  
plt.hist(x)  
```

Note you (almost certainly!) won't get the same plot. Axis labels etc are all added as before.

![A histogram of 10 random numbers between 0 and 10](/static/images/week2/practical_hist.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_hist.py){target="_blank"}*


There are a number of options to `plt.hist()`, including the number of bins to use:

```python
x = 10*np.random.rand(20,1)  
plt.hist(x,bins=20)  
```
So how do we know this is random? Let's ramp up to 100 values:

```python
x = 10*np.random.rand(100,1)  
plt.hist(x,bins=20)  
```

![A histogram of 10 random numbers between 0 and 10, with 20 bins](/static/images/week2/practical_hist2.png){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_hist2.py){target="_blank"}*


Keep going and you should see your histogram level out. Here's a little animation that I made...


![An animation of a histogram with increasing sample size.](/static/images/week2/practical_animation_loop.gif){width="90%"}

*[Download the full source code for this plot](/static/code/week2/practical_animation.py){target="_blank"}*




### Random integers

The function `np.random.randint()` returns random integers from the discrete uniform distribution in a specified interval. 

```python
# random integer between 0 and 9
np.random.randint(10)    
```

```python
# as above
np.random.randint(0,10)    
```

```python
# random integer between 5 and 9
np.random.randint(5,10)   
```

```python
# 10 random integers between 5 and 9
np.random.randint(5,10, size = 10)    
```

```python
# 5 x 5 array of random integers
np.random.randint(5,10, size = (5,5))    
```



### Random numbers from the normal distribution

Many physical phenomena have a "normal distribution" (a bell-shaped distribution of values). To name but a few: human heights, examination grades, the size of snowflakes and measurement errors.

The function `np.random.normal(m,s)` returns a random number (float) from the normal distribution with mean `m` and standard deviation `s`. It has a further size option, as for `random.randint()`. 


```python
np.random.normal(0,1)   
```

```python
np.random.normal(0,1, size = 10) 
```

```python
np.random.normal(0,1, size = (5,5)) 
```

Let's generate a histogram

```python
x = np.random.normal(0,1, size = 100) 
plt.hist(x)
```

![A normal distribution plot](/static/images/week2/normal1.png){width=80%}

You can 'normalise' a histogram using the density option to `plt.hist()` (otherwise the height is the count, and depends on the sample size):
```python
x = np.random.normal(0,1, size = 100) 
plt.hist(x, density=True)
``` 






#### Aside: Figure adjustments

Sometimes you might find that you need to make adjustments to avoid axis labels/labels/the colorbar from overlapping or leaving the page. Here are a couple of fixes you can play around with to get your plot looking great:

```python
ax.set_xlabel('x',labelpad=20)   # labelpad adds some padding to the label
```

```python
fig = plt.figure()  
fig.set_size_inches(12, 6)       # Changes the size of the figure window.
```

```python
# Changes the size of the axes ("distance away from it")
ax.dist = 10  	
# or change the size of the figure
fig.dist = 10  	

```			

Have a go at changing some of these parameters. 

In addition have a go at changing the step size in the definitions of `x` and `y`. This will change the density of the grid and in turn how the surface looks. You should find that too few grid points (larger step size) will give you a surface that is not smooth. You'll notice that if you reduce the step size you'll no longer see an effect beyond a certain point - that's because Matplotlib quite sensibly down-samples the points to give you a sensible looking surface. This can be changed with the `rcount` option if you really, really want.



