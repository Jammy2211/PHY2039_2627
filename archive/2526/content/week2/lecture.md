![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 2 - Curve Fitting

---

## 

* Assessment 1
    * released Friday 3rd October, due Friday 17th October (both at 16:00)
    * worth **5%** of the module grade
    * based on Weeks 1 and 2
    * Numbas test with supplementary plot upload

---

## Today

* Working with scripts
* Recap of `polyfit`
* Reading in data
* Further curve fitting
    * Higher degree polynomials
    * Fitting other functions

---

## Scripts

From here on we'll be writing longer and more complicated code. I recommend that you use *scripts* from this point on.

* Scripts are text files containing code. They can be saved for ease of editing and reuse. 

* They have the extension **.py**.

* It is good practice to *comment* your scripts.

---

### Components of a script

```python

# An inline comment

"""
A docstring is a comment
that runs over multiple lines
"""

x = 2 #Comments can also be placed at the end of a line
```

---

### Commenting

View:  <button onclick="showCode()">Comments and code</button> <button onclick="hideCode()">Comments only</button> 

<div id="content1" style="font-size: 0.8em; margin-top:-10px;" markdown=true>

```python
""" 
Script to calculate pi using Madhava's approximation
"""
import numpy as np

# Set up an array of k values
k = np.arange(21)

# pk array containing series contributions for each k
pk = 1/((2*k+1)*(-3)**k)

# Find the pi approximation, using the sum of pk
pi_approx = np.sqrt(12)*sum(pk)
```

</div>
<div id="content2" style="display: none; font-size: 0.8em; margin-top:-10px;"  markdown=true>

```python
""" 
Script to calculate pi using Madhava's approximation
"""

# Set up an array of k values


# pk array containing series contributions for each k


# Find the pi approximation, using the sum of pk

```

</div>


<script>
    function hideCode() {
        document.getElementById('content1').style.display = 'none';
        document.getElementById('content2').style.display = 'block';
    }
    function showCode() {
        document.getElementById('content1').style.display = 'block';
        document.getElementById('content2').style.display = 'none';
    }    
    
</script>

---

### Suggestions for scripts

* Organise your code in folders e.g. Top-level folder *Stage 2 Python*, then subfolders for each week.
* Consider using your Newcastle University Onedrive to ensure your scripts are backed up.
* Comment your code: even quick shorthand comments are better nothing.

---

### Printing Variables

You can print ndarrays to diagnose bugs:

```python
import numpy as np

arr = np.linspace(-5.0, 5.0, 101)

print(arr)
```

---

This prints the following:

```python
[-5.  -4.9 -4.8 -4.7 -4.6 -4.5 -4.4 -4.3 -4.2 -4.1 -4.  -3.9 -3.8 -3.7
 -3.6 -3.5 -3.4 -3.3 -3.2 -3.1 -3.  -2.9 -2.8 -2.7 -2.6 -2.5 -2.4 -2.3
 -2.2 -2.1 -2.  -1.9 -1.8 -1.7 -1.6 -1.5 -1.4 -1.3 -1.2 -1.1 -1.  -0.9
 -0.8 -0.7 -0.6 -0.5 -0.4 -0.3 -0.2 -0.1  0.   0.1  0.2  0.3  0.4  0.5
  0.6  0.7  0.8  0.9  1.   1.1  1.2  1.3  1.4  1.5  1.6  1.7  1.8  1.9
  2.   2.1  2.2  2.3  2.4  2.5  2.6  2.7  2.8  2.9  3.   3.1  3.2  3.3
  3.4  3.5  3.6  3.7  3.8  3.9  4.   4.1  4.2  4.3  4.4  4.5  4.6  4.7
  4.8  4.9  5. ]
```

---

## Week 1 recap

Last week we covered some background and concluded by fitting a straight line to a dataset via `polyfit`.

![Linear fit to our data](/static/images/week2/curve-fit.png){width=65%}

---

```python
import numpy as np
import matplotlib.pyplot as plt

# Original data
x = [1,2,3,4]
y = [5.5,7.0,9.5,9.9]

# Make a plot
plt.plot(x,y,'x')
plt.xlabel('x')
plt.ylabel('y')

# Polyfit 
p = np.polyfit(x, y, 1)
x1 = np.linspace(0,5,100)
f = p[0]*x1+p[1]

# Add to plot
plt.plot(x1,f,'-')
```

---

## `polyval`

When fitting a straight line it's not too tedious to define use the syntax

```python
f = p[0]*x1+p[1]
```
But when fitting higher degree polynomials this can quickly become tiresome.

We can use the function `polyval` to replace the above code with

```python
f = np.polyval(p,x1)
```

---

## Higher degree polynomials

![Quadratic fit](/static/images/week2/fit_quadratic.png){width=85%}

---

![Cubic fit](/static/images/week2/fit_cubic.png){width=85%}

Notice that the cubic goes through every point, so that $S = 0$.

---

![Cubic fit](/static/images/week2/new_point.png){width=85%}

Adding a new data point causes $S \neq 0$.

---

The fact that the cubic yields $S = 0$ does not necessarily mean that this cubic is the *most appropriate model* of the data.

> Given a dataset containing $n$ points there exists a polynomial, of degree at most $n$, with $S=0$.

---

![Overfitting and underfitting](/static/images/week2/fitting.png){width="100%"}

---

## Reading in data

Speaking of modelling data: in order to work with larger datasets we need to load external files into Python.

We can do this using the function `loadtxt`.

Let's look at an example:

[scores.csv](/static/data/scores.csv){target="_blank"}


----

## Fitting other functions

Fitting a function to a dataset is an example of *data modelling*: we are attempting to produce a mathematical model of an observed real-world phenomena.

We would be severely limited in which datasets we could model if were only able to fit polynomials.

For example, many real world phenomena obey power laws of the form

$$ y = ax^b $$

E.g. decay of a radioactive isotope obeys $N = N_0 e^{-\lambda t}$.

----

### Option 1: Apply a transform

Transform $y = ax^b$ into a linear equation by introducing new variables $X$ and $Y$


$$y = ax^b$$

. . .

$$\log(y) = \log(ax^b)$$

. . .

$$\log(y) = \log(a) + b\log(x)$$

. . .

Setting $Y = \log(y)$, $X = \log(x)$, and $c = \log(a)$ we obtain 

. . .

$$Y = bX + c$$

----

If we suspect that a dataset obeys a power law we can use the above method to model it, as follows.

1. Transform the data by taking $\log$ of independent and dependent variables.
2. Use `polyfit` to find the line of best fit for the transformed data.
3. Exponentiate to recover power law modelling the original data.

---

```python
# Data with plot
x = [1,2,3,4]
y = [5,81,402,1250]
plt.plot(x,y,'x')

# Fit line to transformed data
X = np.log(x)
Y = np.log(y)
p = np.polyfit(X,Y,1)

# Exponentiate to obtain a and b
b,c = p     # Equivalent to b = p[0], c = p[1]
a = np.exp(c)

# Model of original data
x1 = np.linspace(0,5,100)
f = a*x1**b
plt.plot(x1,f)
```

---

## Option 2: SciPy

Transforming the data is useful in some circumstances, but in general we need to be able to fit more complicated functions.

For example, supply and demand of a commodity is often modelled using trigonometric functions e.g.

$$ y ( x ) = a \sin ( b x ) + c$$

for $a, b, c$ constants.

---

We can fit more these more complicated functions using the module **SciPy**, and a it provides function called `curve_fit`:

```python
# imports, x, y data etc

import scipy.optimize as opt

def model(x, a, b, c): 
    return a * np.sin(b*x) + c

popt, pcov = opt.curve_fit(model, x, y)
```

---

### Defining Python functions

```runnable  lang="python"
def my_function(x, y): 
    return x**2 + y**2

print(my_function(2,3))
```

---

## Fitting data with uncertainties

![Sample data](/static/images/week2/errorbar_sampledata_fit.png){width=80%}

In this week's Handout we'll consider how the above methods change when modelling datasets containing uncertainties.

---

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}

The material sketched in this lecture is covered in greater detail in Handout 2.