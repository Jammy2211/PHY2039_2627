[Click here to open this handout in a new browser tab](#){target="_blank"}

# PHY2039 Handout 2

Welcome to the handout for the second week of Python material. A reminder of some of the features of the handouts:

<div class="exercise" markdown=true>

**Exercise**

This is an exercise. They'll help you to check your progress and will give automatic feedback.

</div>

<div class="interlude" markdown=true>

**Interlude**

This is an interlude i.e. material outside the testable content of PHY2039 that you may find interesting.

</div>

This week we're continuing on the topic of curve fitting. Beforehand we'll revisit and expand on some concepts from Week 1.

## 2.1) More on arrays, plotting and scripts

### More on arrays

Last week we introduced the NumPy module, including a new object type - the NumPy array - that supports element-wise arithmetic:

```python
import numpy as np
x = np.array([5,3,2])
print(x**2)
```
```
[25  9  4]
```

You can think of an array as a list-like object that has been adapted for mathematical uses. We saw several different ways to create a NumPy array:

```python
x = np.array([5,3,2])   # Take a list as input, turn it into an array
y = np.arange(1,6)      # A sequence of values - same as np.arange(1,6,1)
z = np.linspace(0,1,5)  # Linearly spaced values
```

These commands give us three different ways to create the same array, e.g. `[0,2,4]`

```python
np.array([0,2,4])
np.arange(0,6,2)
np.linspace(0,4,3)
```

In practice (as in the following exercise) we'll use each of them in specific circumstances:

* `np.array` to convert an existing list to an array.
* `np.arange` to give a sequence of numbers.
* `np.linspace` to create an array of specified length between two values.

<div class="exercise" markdown=true>

#### Exercise 2.1 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/106150/numpy-array-functions/embed/?token=0a342d94-6a9f-48d7-804f-d1d539699fb4" data-id="exercise-2-1" data-cta="Show exercise >"></numbas-embed>

</div>


#### 2D arrays

Very similar syntax to that given above allows us to create *multidimensional* arrays: data arranged along two or more axes. For example, a 2 dimensional (2D) array is organised into rows and columns

```python
x = np.array([[2,5,7],[1,3,4],[0,6,8]])
print(x)
```
```output
array([[2, 5, 7],
       [1, 3, 4],
       [0, 6, 8]])
```

Elements of the array can be accessed with `x[row,column]`, where `row` and `column` are an index for the row/column number, starting at 0. E.g.

```python
# First row, second column (count from 0!)
x[0,1]
```
```output
5
```

The array can be sliced by row or column as follows using the wildcard `:` as follows

```python
# return the second row and all columns
x[1,:]
```
```output
array([1, 3, 4])
```


```python
# return the second column and all rows
x[:,1]
```
```output
array([5, 3, 6])
```

We'll see many more examples of 2D arrays in Week 3 when we cover linear algebra in Python.


#### The colon operator `:`

Consider a list

```python
x = [10,5,2,4,3,7]
```

We saw last week that we can access an *element* of the list (or a NumPy array) using an *index* in square brackets:

```python
x[0]
```
```output
10
```

There are some other really useful tricks to access elements in a list or array using the colon `:` operator. 

A colon by itself selects every element

```python
x[:]
```
```output
[10,5,2,4,3,7]
```

An index after the colon gives every element up to, but not including, that index

```python
x[:3]
```
```output
[10,5,2]
```

An index before the colon gives every element from that index to the end of the list

```python
x[3:]
```
```output
[4,3,7]
```

Using a number either side gives `start:stop` and, similar to the `range` and `np.arange` functions we've seen, the `stop` is not included:

```python
x[1:3]
```
```output
[5, 2]
```

Using a negative index returns elements from the end of the list:

```python
x[-1]
```
```output
7
```

```python
# Last two values
x[-2:]
```
```output
[3, 7]
```

```python
# Everything except last two values
x[:-2]
```
```output
[10, 5, 2, 4]
```

Finally, the colon operator can be used in a similar fashion to `range(start,stop,step)`

```python
x = [10,5,2,4,3,7,6,1,11,8,9]
x[1:10:2]
```
```output
[5, 4, 7, 1, 8]
```

All of these commands work with NumPy arrays as well as lists.

<div class="exercise" markdown=true>


#### Exercise 2.2 


<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/129648/colon-operator/embed/?token=df552819-06e8-45c9-89e0-02c1bfdf124a" data-id="exercise-2-2" data-cta="Show exercise >"></numbas-embed>

</div>


### More on scripts

It's strongly recommended to write your code in scripts (rather than direct in the Console). Scripts allow us to save our work and make editing code simple.

#### Creating a new script

Click the 'New file' button or go to File -> New file....

#### Saving a script

Save your script by clicking File -> Save As.... 

Spyder will default to saving this script with a generic name such as Untitled.py (and in an unhelpful location).

*OneDrive*](https://services.ncl.ac.uk/itservice/teaching-services/o365/onedrive/){target="_blank"}, the cloud storage system provided by the University, is the simplest way to store you files so that you have access to them everywhere.

On cluster computers (and other University-managed computers) you will be able to access your OneDrive via the File Explorer: simply open a File Explorer window and look in the *Quick access* area on the left. Alternatively, press the Windows key and type 'OneDrive', then press enter.

If you are using your personal device you can access [OneDrive via a brower](https://office365.ncl.ac.uk/){target="_blank"}; however, this is not appropriate for our needs in this course. 

We use OneDrive's ability to sync with your personal device; instructions for setting up syncing are [given here](https://support.microsoft.com/en-us/office/sync-with-onedrive-bb89981b-e382-4969-b8fd-d413a90b6db3?ui=en-us&rs=en-us&ad=us#ID0EAABAAA=Sync_files_and_folders){target="_blank"}. If you plan on frequently working with Python on your personal device it is highly recommended to set up OneDrive syncing.

It is of course possible to simply store your Python files locally on your personal computer; you are not required to use OneDrive. However, storing your files on OneDrive means they are backed up, and you can access them if you forget your laptop or your housemate spills a cup of tea over it.

#### Running a script

I recommend using the 'Run file' (a.k.a. play) button to run your code: this has the benefit of setting the *working directory* to the directory of your script, which will help when we load in files later in the handout.

You can also use the following line

```python
#%%
```

to split your script into "cells". These can be run individually with the "Run cell" button (left of the "Run file" button).


#### Script good practice

* Create a folder structure: a top-level folder called 'Stage 2 Python', with subfolders for each teaching week.

* Save your scripts with meaningful names in meaningful folders. E.g. `week_2_scipy.py` is much easier to find later than `script1.py`.

* Commenting your code is important: even quick shorthand notes are much better than nothign.

### More on plotting

Last week we covered some basic plotting. E.g.

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 25)
y = np.sin(x)

plt.plot(x, y, 'o')
```

![A basic plot](/static/images/week2/plot.png){width="50%"}


There are lots of other options for the marker style: `o` for circles, `v` for triangles... There are far too many to describe herel; [here's a reference](https://matplotlib.org/stable/api/markers_api.html){target="_blank"}.

#### Scatter plots

Scatter plots are briefly covered here, as created by Matplotlib's `plt.scatter` function, because it's likely you'll come across them when searching for help. The function `plt.scatter` is very similar to `plt.plot`, but gives more control over the output. In particular, `plt.scatter` allows much greater control over individual marker style; indeed, they can be customised on a point-by-point basis. Without specifying any further options, `plt.scatter` is called using the same syntax as `plt.plot`:

```python
# marker option instead of a third argument
plt.scatter(x, y, marker='o')
```

To see some of the features of `plt.scatter` we can create an array using random numbers:

```python
import numpy as np
import matplotlib.pyplot as plt

# Normal linearly spaced array
x = np.linspace(0, 10, 25)

# 25 random values between 0 and 1
y = np.random.rand(25)

# 25 random values between 0 and 1
# this is actually enough to get some random colours
colours = np.random.rand(25)

# 25 random integers between 1 and 200
sizes = np.random.randint(1,200,25)

plt.scatter(x, y, c=colours, s=sizes, marker='o')
plt.show()
```

![A scatter plot](/static/images/week2/scatter.png){width="50%"}

You can continue with `plt.plot` until a time that you need a scatter plot, but it's useful to be aware that `plt.scatter` exists.

#### Error bars

A plot with error bars uses a similar syntax again to `plt.plot`: this time the function is named `errorbar`, with a `yerr` option for the size of errors/uncertainty in $y$ (and corresponding `xerr` in $x$ if required). This time the option `fmt` sets the marker style:

```python
# x values
x = np.arange(1, 11)

# the np.randint function can be used to produce random y values
y = np.random.randint(1,5,10)

# The syntax np.ones(n) generates an array of length n filled with ones
err = np.ones(10)

plt.errorbar(x, y, yerr=err, fmt='o')
```

![A plot with error bars](/static/images/week2/errorbars.png){width="50%"}

We'll come back to this later in the Handout, when we look at curve fitting for data with uncertainties.


#### Preview: more advanced plotting

The tools above are sufficient for this week's material, but we'll continue to expand on these plotting techniques in Weeks 5 and 6.

It's worth pointing out here that nobody remembers all of the different ways to make plots, some of which are depicted in the [Matplotlib gallery](https://matplotlib.org/stable/gallery/index){target="_blank"}. Memorization isn't the appropriate skill here: general programming principles and a clear concept of what one wants to achieve are more than enough.

## 2.2) Curve fitting continued: `polyfit` and `polyval`

In Week 1 we looked at the `polyfit` function, that uses the least-squares method to find the best fitting polynomial of specified degree:

```python
p = np.polyfit(x, y, n)
```

The input arguments are

* `x`, a list or array of independent data points.
* `y`, a list or array  of dependent data points.
* `n`, the degree of the polynomial to fit. 

And the output (`p` here) is a list of coefficients for the specified polynomial.

```python
import numpy as np
import matplotlib.pyplot as plt

# Data points
x = [1,2,3,4]
y = [5.5,7.0,9.5,9.9]
plt.plot(x,y,'x')

# Fit a*x+b
p = np.polyfit(x, y, 1)

print(p)
```
```output
[1.57 4.05]
```

`polyfit` returns an array of two values. These are the optimum values of the parameters $a$ and $b$, as calculated by `polyfit`. We read the above output as 

$$ 1.57x + 4.05 $$

i.e. the coefficents appear in `p` in order of descending power.

Recall that array elements can be retrieved by using their index, so that the first element in `p` has index 0 and is

```python
p[0]
```

This returns the value 1.57.

We use these values to define the line of best fit:

```python
x1 = np.linspace(0,5,100)
f = p[0]*x1+p[1]

plt.plot(x1,f)
```

Notice that I've not typed in the values `1.57` and `4.05`: this is recommended as it reduces the potential for errors caused by rounding issues (or human input error)

<div class="exercise" markdown=true>


### Exercise 2.3 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/75839/fit-a-linear-function-with-polyfit/embed/?token=d8e3910c-5993-489e-b44d-2f5acd0f4bcc" data-id="exercise-2-3" data-cta="Show exercise >"></numbas-embed>

</div>

### Using `polyval`

Using `p[0]` and `p[1]` is superior to writing out (approximations of) the values of `p`. However, as we move to higher degree polynomials the syntax

```python
y1 = p[0]*x1+p[1]
```

can become tedious to write. For example, a cubic is written

```python
y1 = p[0]*x1**2+p[1]*x1+p[2]
```

The NumPy function `polyval` allows us to avoid this tedium. The syntax `np.polyval(p,x)` returns an array of values for a polynomial with coefficients given by `p` evaluated on the array `x`. For example, the code

```python
y1 = p[0]*x1+p[1]
```

is equivalent to

```python
y1 = np.polyval(p,x1)
```

Notice that we did not have to specify the degree of the polynomial when using `np.polyval` i.e. it detected the degree of the desired polynomial from the length of the array `p`.

This allows us to quickly change the degree of the polynomial we are fitting: we need only change `np.polyfit(x,y,1)` to `np.polyfit(x,y,2)`

```python
# Degree of polynomial changed here
p = np.polyfit(x,y,2)    
 # Polyval works with no change needed
y1 = np.polyval(p,x1)   
```

Our previous example can be edited as follows:

```python
import numpy as np
import matplotlib.pyplot as plt

# Data
x = [1,2,3,4];
y = [5.5,7.0,9.5,9.9];

# Fit data using polyfit
p = np.polyfit(x, y, 1)

# Set up array for curve using polyval
x1 = np.linspace(0,5,100)
y1 = np.polyval(p,x1)

# Plot
plt.plot(x,y,'o')
plt.plot(x1,y1,'-')

# Various other aesthetic changes
```

![A linear fit to the data](/static/images/week2/linear_fit.png){width=60%}


### Higher degree polynomials

Fit a quadratic and cubic to the data points by changing the degree in the `polyfit` command. They have been plotted on one figure below using a `for` loop (we'll be covering loops in Week 4), but you can do this one at a time by changing the line

```python
p = np.polyfit(x, y, 1)  
```

to e.g.

```python
p = np.polyfit(x, y, 2)  
```

This code fits the quadratic and cubic separately

```python
p = np.polyfit(x, y, 1)
y1 = np.polyval(p,x1)
plt.plot(x1,y1,'-')

p = np.polyfit(x, y, 2)
y1 = np.polyval(p,x1)
plt.plot(x1,y1,'-')

# etc
```

This code uses a `for` loop to fit a degree $n$ polynomial for $n = 1$, $n = 2$, $n = 3$

```python
for n in range(1,4):
    p = np.polyfit(x, y, n)
    y1 = np.polyval(p,x1)
    plt.plot(x1,y1,'-')
```

![linear, quadratic and cubic fits to the data](/static/images/week2/multifit.png){width=60%}

Note how well the cubic function fits.

### Degrees of freedom

It is important to appreciate that the most appropriate model of a dataset is not necessarily the function that produces the smallest $S$. It is always possible to find an $(n-1)$th degree polynomial that passes exactly through $n$ data points. In the figure above the cubic fit to the four data points is shown to pass exactly through each point.

The cubic fit has $S = 0$ (it is a perfect fit to the data) but there are a number of reasons why this may not be an appropriate model of the data. First, data often has noise or uncertainty: a model with $S=0$ is likely to be taking this noise into account to too great an extent. That is, any underlying law obeyed by the data may be obscured by the noise when fitting a high-degree polynomial. Second, we are attempting to model the dataset using a finite set of observations. Even if we have found a fit yielding $S = 0$, it is highly unlikely that this will remain true if we make another observation and add it to the dataset.

Fitting a cubic to the data given above is known as **overfitting**. Similarly, fitting a polynomial of too low a degree is known as **underfitting**. Here's an example where you might consider the middle fit to be most appropriate, the first underfitting and the last overfitting.

![Overfitting and underfitting](/static/images/week2/fitting.png){width="70%"}

Another way to think about this is to compare the number of data points, $n$, to the number of free variables in the function, $m$. The difference between the two, $n-m$, is referred to as the number of **degrees of freedom**. Determing the correct model of a dataset requires one to consider both the degrees of freedom, **and** the sum of square residuals $S$. That is, we usually need to find a balance between maximising the degrees of freedom and minimising $S$.

<div class="exercise" markdown=true>

### Exercise 2.4

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/77013/linear-fit-kelvin-s-thermometers/embed/?token=00d67d7e-4f1d-4022-b79d-51fa8ea80cfd" data-id="exercise-2-4" data-cta="Show exercise >"></numbas-embed>

</div>

## 2.3) Working with data files

We'd like to be able to apply our curve fitting techniques to real-world datasets. Such datasets almost always contain hundreds, thousands, or even millions of data points.

Such datasets are stored as external files, and then loaded into Python as described here.

Download the following files to your computer. **Place the files in the same folder as your script is saved**. Otherwise you will need to specify the full computer path to the file in the commands that follow

In each case, right click to save the file:

[data.txt](https://www.mas.ncl.ac.uk/~ncmg2/data/data.txt){target="_blank"}

[data.csv](https://www.mas.ncl.ac.uk/~ncmg2/data/data.csv){target="_blank"}


### Reading a `txt` file

A text file typically contains data in columns. Open *data.txt* with an app such as notepad and you will see the first few lines:

```
1	9.372192978
2	7.83317305
3	14.75977958
4	13.83689773
...
```

I.e. each line contains an integer and a decimal, separated by a tab character.

Reading a `txt` file can be done with the NumPy function `np.loadtxt` as follows

```python
np.loadtxt('data.txt')
```
```output
array([[  1.        ,   9.37219298],
       [  2.        ,   7.83317305],
       [  3.        ,  14.75977958],
...
```

Note that the data has been loaded as a 2D array.

### Setting the working directory
If the above code produces an error, it's likely to be caused by the data file not being where Spyder expects it to be. The *working directory* is the location in which Spyder looks for files to load; the current working directory is displayed in the top-right of the screen:

![The working directory display in Spyder](/static/images/week2/working_directory.png){width=70%}

The easiest way to avoid errors caused by Spyder being unable to find external files is to change this working directory to the folder corresponding to the current teaching week e.g. Stage 2 Python/Week 2. To change the working directory click on the folder icon to the right of the directory display and select the desired folder.

Once you get more comfortable with loading external files you could set this working directory to your Stage 2, and instruct Spyder to load a file from a specific subfolder, via the syntax `Week 2/test_data.txt`, for example.

#### Unpacking the data into variables

We typically wish to import data from the individual columns in the external file as variables, for example column 1 to a variable `x` and column 2 to a variable `y`.

There are a couple of ways to do this: the first is to assign all of the data to a variable, say `data`

```python
data = np.loadtxt('data.txt')
```

and then use the array techniques described above to extract the columns

```python
x = data[:,0]
y = data[:,1]
```

Alternatively, we can use the option `unpack` in the `loadtxt` command, which directly places the columns into variables:

```python
x,y = np.loadtxt('data.txt', unpack=True)
```

Note the syntax `x,y =`: this produces two arrays, one for each column.

### Reading a CSV file

CSV (Comma-separated values) files are a very common format for storing data. The CSV file linked has a header row. We don't want to include this in the arrays of data, so we can use the `skiprows` option. We also need to specify the `delimiter` used in the external file:


```python
data = np.loadtxt('data.csv', delimiter=',', skiprows=1)
```

Again the data can be placed directly into variables with the `unpack` option

```python
x,y = np.loadtxt('data.csv', delimiter=',', skiprows=1, unpack=True)
```

<div class="exercise" markdown=true>

### Exercise 2.5

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/147233/linear-fit-with-sample-data-file/embed/?token=d38843c5-d514-411d-b292-df1b72c5209c" data-id="exercise-2-5" data-cta="Show Exercise"></numbas-embed>


</div>


## 2.4) What if my function is not a polynomial?

### Example: power law $f(x)=ax^b$

Many elementary functions can be written in polynomial form using a transform.

For example, the function

$$ y = ax^b $$

where $a$ and $b$ are constants, can be transformed to the linear equation

$$ Y = bX + c $$ 

by applying the natural logarithm to both sides, where $X = \ln(x)$, $Y = \ln(y)$ and $c = \ln(a)$.

Suppose we have some data to which we would like to fit a power-law function $y=a x^b$:

```python
import numpy as np
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y = [2.1,2.9,3.5,3.8,4.2]
```

If this dataset does indeed obey a power law, then plotting on *log-log* axes then we can expect to see a straight line. Matplotlib has a plotting function called `loglog` which is exactly for this:

```python
# Plot on log-log axes
plt.loglog(x,y,'o')
plt.xlabel('x')
plt.ylabel('y')
```

![A loglog plot](/static/images/week2/loglog.png){width=60%}

Alternatively we can plot $Y$ versus $X$:

```python
X = np.log(x)      # don't forget Python is case sensitive
Y = np.log(y)		# so y and Y are different variables
plt.plot(X,Y,'o')
plt.xlabel('X = log(x)')
plt.ylabel('Y = log(y)')
```

![A loglog plot](/static/images/week2/loglog-2.png){width=60%}


We can use `polyfit` and `polyval` to fit a linear function, note `log(x)` and `log(y)` is being used inside the `polyfit` command to exaggerate the difference (this could be `X` and `Y`).

```python
p = np.polyfit(np.log(x),np.log(y),1)    # np.polyfit(X,Y,1) would work too
x1 = np.linspace(0,3,100)
y1 = np.polyval(p,x1)

# Plot
plt.plot(X,Y,'o')
plt.plot(x1,y1,'-')

plt.xlabel('X = log(x)')
plt.ylabel('Y = log(y)')
```

![A loglog fit](/static/images/week2/loglog_fit.png){width=60%}


After running the above code we can note the output of `polyfit` (take a look at the value of `p`). Doing so would show us that

\begin{align} 
b &= 0.314\text{,}  \\
c &= \ln(a) = 0.736 \implies a = 2.087\text{.}
\end{align}

to 3 decimal places (we can do this accurately in Python using the `np.exp` function). Therefore our power law fit is 

$$f(x) = 2.087x^{\left(0.314\right)}$$

We can verify that this looks sensible on a linear (lin-lin) plot of the original data:

```python
x1 = np.linspace(0,10,100)

plt.plot(x,y,'x')
plt.plot(x1,2.087*pow(x1,0.314),'-') 
# Or even better, use the p values to keep accuracy
 
plt.xlabel('x')
plt.ylabel('y')
```

*Note it would have been better to retain accuracy by using the values in `p` without rounding.*


![A lin-lin fit](/static/images/week2/linlin-fit.png){width=60%}


### Matplotlib functions for log plots

In carrying out the above analysis using a power law we found that it was useful to make a log-log plot. Here are some other Matplotlib plotting commands to produce log plots: 

Command     |  Type of plot  
------------|----------------
`plt.plot`      |   lin-lin       
`plt.semilogx`  |   lin-log (logarithmic $x$ axis)    
`plt.semilogy`  |   log-lin (logarithmic $y$ axis)
`plt.loglog`    |   log-log      


<div class="exercise" markdown=true>

### Exercise 2.6 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/77019/linearise-functions/embed/?token=44fa2f39-6a06-4738-aeb6-4c7880d2b85e" data-id="exercise-2-5" data-cta="Show exercise >"></numbas-embed>

</div>

<div class="exercise" markdown=true>

### Exercise 2.7: Worked Example 

Consider the following data:

```python
x = np.arange(1,11)
y = np.array([4.0, 7.0, 7.5, 8.0, 9.5, 9.0, 10.5, 10.0, 10.0, 11.5])
```

Apply an appropriate transform to the data to fit a function $f(x) = a e^{bx}$ to it, using `polyfit`. Compute $a$ and $b$ and illustrate the fit on a plot.

<details markdown=true>
<summary>Click here to reveal a solution.</summary>

The desired function is $f(x) = a e^{bx}$, so that we assuming that the relationship between $x$ and $y$ is modelled by $y = a e^{bx}$. Taking the natural logarithm we obtain

\begin{align}
y(x) &= a e^{bx} \\
\ln ( y ) &= \ln \left( a e^{bx} \right) \\
\ln ( y ) &= \ln \left( a \right) + b \ln \left( e^{x} \right) \\
\ln ( y ) &= \ln \left( a \right) + b x
\end{align}

Setting $Y = \ln (y)$ and $A = \ln (a)$ the above equation is linear i.e. $Y = bx + A$. Therefore applying a log transform to $y$ and leaving $x$ unchanged will allow us to use `polyfit` to find $b$ and $A$, as follows

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = np.array([4.0, 7.0, 7.5, 8.0, 9.5, 9.0, 10.5, 10.0, 10.0, 11.5])
Y = np.log(y)

p = np.polyfit(x,Y,1)
b = p[0]
A = p[1]
```

We can recover $a$ via $a = e^A$, and define the fitted curve as

```python
a = np.exp(p[1])
r = np.linspace(1,11,100)
f = a*np.exp(b*r)
```

By calling `print(a,b)` (or using the variable explorer) we determine that $a = 5.22\ldots$, $b=0.086\ldots$.

Plotting the original (untransformed) data and the fitted curve yields

![A plot of the data together with the fitted function](/static/images/week2/worked_example.png){width="100%"}

The complete code is
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,11)
y = np.array([4.0, 7.0, 7.5, 8.0, 9.5, 9.0, 10.5, 10.0, 10.0, 11.5])
Y = np.log(y)

p = np.polyfit(x,Y,1)
b = p[0]
a = np.exp(p[1])
print(a,b)
r = np.linspace(1,11,100)
f = a*np.exp(b*r)

plt.plot(x,y,'o')
plt.plot(r,f)
plt.show()
```
A final thought: we could compute the sum of squared residuals to determine the improved fit given by $f(x) = a e^{bx}$ (over $f(x) = mx + c$).

</details>
</div>


## 2.5) Fitting more functions with SciPy `curve_fit` 

📖 [SciPy documentation](https://docs.scipy.org/doc/scipy/){target="_blank"}

SciPy is a scientific computing package that we'll see in more detail as the module progresses. For this week we're interested in a function that is contained in the *optimize* submodule of SciPy, imported as follows:

```python
import scipy.optimize as opt
```

The function we're interested in is called `curve_fit`, with syntax

```python
popt, pcov = opt.curve_fit(model, x, y) 
```

where the arguments are

 * `x`, data for the independent variable.
 * `y`, data for the dependent variable.
 * `model`, the function to fit to the data. The first argument should be `x` and any further fitting parameters should then follow.

The output is two arrays (we have used `popt` and `pcov` but you can label them as you like)

* `popt`, the optimum parameters presented in an array. These will correspond to the fitting parameters specified in the function.
* `pcov`, an array containing the covariance matrix for the fitting parameters. 

Here's an example. First consider the dataset

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# The data
x = np.arange(0,2,0.1)
y = np.array([1,3.5,4,6,7,7,5,5,4,3,2,-0.5,-1,-3,-3,-3.5,-4,-3,-2,0])

# Plot the data
plt.plot(x,y,'o')
```
We intend to model this data via the function $f(x) = a\sin(bx)+c$, with three parameters $a$, $b$ and $c$. This is set up using a user-defined function called `model` (if you'd like an introduction to or refresher on Python functions consult the transition materials):

```python
# function to define the fit parameters
def model(x, a, b, c): 
    return a * np.sin(b*x) + c
```

Note that this can be called with the syntax `model(1,2,3,4)`, for example: this would return the value $f(1)$ if the parameters take the values $a=2$, $b=3$ and $c=4$.

We now invoke the `curve_fit` function, providing `model` and the data to be fitted:

```python
# Print the best fit parameters
popt, pcov = opt.curve_fit(model, x, y) 
```

Note again that `curve_fit` is returning two objects, which we've labelled as `popt` and `pcov`. The array `popt` contains the optimum values of the parameters $a$, $b$ and $c$

```python
print(popt)
```
```output
[5.08488863 3.12757722 1.37112038]
```

These are read in the same order specified in the definition of `model`: so `popt[0]` is $a$, and so on.

The second variable `pcov` contains the covariance matrix, which indicates the uncertainties and correlations between the parameters in `model` 

```python
print(pcov)
```
```output
[[0.03147395 0.00080958 0.0002184 ]
 [0.00080958 0.00105036 0.00031385]
 [0.0002184  0.00031385 0.0155849 ]]
```

The diagonals represent the variance i.e.

$a = 5.08488863 \pm \sqrt{0.03147395}$ (square root of the value in `pcov[0,0]`)

$b = 3.12757722 \pm \sqrt{0.00105036}$ (square root of the value in `pcov[1,1]`)

$c = 1.37112038 \pm \sqrt{0.0155849}$ (square root of the value in `pcov[2,2]`)

In a nutshell, these values describe how the parameters would change if a slight change was made to the input dataset.

We won't concern ourselves in this module with the off-diagonal entries (they describe how strongly each parameter is correlated to the others).

Since we now know the best fit parameters we can plot the model as follows:

```python
# Construct a function to fit
x1 = np.linspace(0,2,100)
y1 = model(x1,popt[0],popt[1],popt[2])
```

And plotted with

```python
plt.plot(x,y,'o')
plt.plot(x1,y1,'-')
```

![Fit using curve_fit](/static/images/week2/curve_fit.png){width=70%}


<div class="exercise" markdown=true>

### Exercise 2.8

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/77021/scipy-curve-fit/embed/?token=ca3f0c8e-2985-4a7b-8ab2-1714ae23e63a" data-id="exercise-2-8" data-cta="Show exercise >"></numbas-embed>

</div>

## 2.6) Curve fitting with uncertainties

Suppose that we have a dataset that includes uncertainties (e.g. measurement error). The data may be presented as follows

```
x        y        uncertainty
1.0      5.23     0.1
1.2.     5.34     0.2
```

You can find a sample CSV file containing data with uncertainties [here](https://www.mas.ncl.ac.uk/~ncmg2/data/sample_data.csv){target="_blank"} (right click and download to the same location as your script).

Consulting the file we see that it is made up of 3 columns:

```
x,y,y_uncertainty
0,3.483130064,0.615826385
0.1,3.053400247,0.291228075
0.2,2.778235268,0.60100842
```

We can unpack this into three variables as follows:

```python
x,y,u = np.loadtxt("sample_data.csv", delimiter=",", skiprows=1, unpack=True)
```

This can be plotted using `errorbar` (as described earlier in the handout):

```python
plt.errorbar(x,y,yerr=u,fmt='o')
plt.xlabel('x')
plt.ylabel('y')
```

![Sample data](/static/images/week2/errorbar_sampledata.png){width=80%}

We can fit a line to this data, and incorporate the uncertainties into the fitting process, using `curve_fit`.

First create a function for the model

```python
def linear_fit(x,a,b):
	return a*x+b
```

We use the additional option `sigma` as follows:

```python
popt, pcov = opt.curve_fit(linear_fit, x, y, sigma=u)
```

This yields the script

```python
import numpy as np
import scipy.optimize as opt

x,y,u = np.loadtxt("sample_data.csv", delimiter=",", skiprows=1, unpack=True)

popt, pcov = opt.curve_fit(linear_fit, x, y, sigma=u)
```

The array `popt` contains the optimum values for $a$ and $b$

```python
popt
```
```output
array([-1.88124503,  3.54322507])
```

and `pcov` contains the variance on the diagonals (as above)

```python
pcov
```
```output
array([[ 0.01741491, -0.01082811],
       [-0.01082811,  0.01158384]])
```

The optimum parameters are therefore $a = -1.88124503 \pm\sqrt{0.01741491}$, $b = 3.54322507\pm\sqrt{0.01158384}$

This can be plotted using the following script

```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

x,y,u = np.loadtxt("sample_data.csv", delimiter=",", skiprows=1, unpack=True)

def linear_fit(x,a,b):
	return a*x+b

# Find the best fit line
popt, pcov = opt.curve_fit(linear_fit, x, y, sigma=u)

# Make a plot
plt.errorbar(x,y,yerr=u,fmt='o')
plt.plot(x,popt[0]*x+popt[1])
plt.xlabel('x')
plt.ylabel('y')
```

![Sample data](/static/images/week2/errorbar_sampledata_fit.png){width=80%}

### Weighted sum of squared differences

In Week 1 we quantified how well the fitted function modelled the data using the sum of the squared residuals

$$ S = \sum_{i} r_i^2 = \sum_i \left[f(x_i) - y_i\right]^2$$

This takes no account of the uncertainty in each data point $y_i$. A weighted version, that does incorporate uncertainty, denoted $S_w$, is calculated as

$$ S_w = \sum_{i} \left(\frac{f(x_i) - y_i}{\sigma_i}\right)^2$$

where $\sigma_i$ is the uncertainty associated with the $y_i$ data point. 

Note that $x_i$, $y_i$ and $\sigma_i$ are the values in one row of our data, so we can implement this using element-wise arithmetic. For example

```python
r_w = ((popt[0]*x+popt[1])-y)/u
S_w = sum(r_w**2)
```

Note that, in this weighted version, data points with larger uncertainty ($\sigma_i$) contribute less to the summation.

<div class="exercise" markdown=true>

### Exercise 2.9

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/147111/curve-fit-radioactive-decay-data-with-uncertainties/embed/?token=f7418529-a565-47c2-acbc-8c27d54b54eb" data-id="exercise-2-9" data-cta="Show exercise >"></numbas-embed>

</div>

### Next week

Next week we'll look at linear algebra in Python, including

* Vectors
* Matrices: multiplication, eigenvalues and vectors

