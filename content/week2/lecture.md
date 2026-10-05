![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 2 - Bug Fixing & Curve Fitting

---

## Today

* Bug fixing
* Working with scripts
* Recap of `polyfit`
* Reading in data
* Further curve fitting
    * Higher degree polynomials
    * Fitting other functions

---

## Finding bugs

A **bug** is a mistake in a program. Finding and fixing bugs is a normal part of writing Python.

1. **Predict** the intended result, then **run** the code.
2. **Read** the error, if there is one; **inspect** values with `print()`.
3. **Change one thing**, then **rerun** and check your prediction.

---

## Spot the bug: rectangle area

A rectangle has length 5 and width 3. This program should print its area: **15**.

**Before running:** predict what will happen. Can you spot the bug?

```runnable lang="python"
length = 5
width = 3
area = lenght * width
print(area)
```

---

## Diagnose: rectangle area

```runnable lang="python"
length = 5
width = 3
print(length, width)
area = lenght * width
print(area)
```

---

## What the error tells us

* Read the last line of the error: `NameError` means an undefined name. Compare spellings on the failing line and the assignments.
* Why put the diagnostic print **before** the failing line?
* Edit the correction live, remove the diagnostic print and rerun. Expected: **15**.

---

## Choosing with `if`

* An `if` checks a condition, such as `temperature < 18`: it is either `True` or `False`.
* Its indented lines run only when the condition is `True`.
* An `else` provides an alternative when its condition is `False`.
* A conditional **chooses** what to do; a loop **repeats** instructions.

---

## Spot the bug: thermostat

Print **one** message: `Heating` below 18°C, `Cooling` above 24°C, or `Comfortable` from 18°C to 24°C inclusive.

At 16°C, expect **Heating only**. Predict what happens, then run.

```runnable lang="python"
temperature = 16
if temperature < 18:
    print('Heating')
if temperature > 24:
    print('Cooling')
else:
    print('Comfortable')
```

---

## Diagnose: thermostat

Inspect both conditions, then follow the branches.

```runnable lang="python"
temperature = 16
print('Below 18:', temperature < 18)
print('Above 24:', temperature > 24)
if temperature < 18:
    print('Heating')
if temperature > 24:
    print('Cooling')
else:
    print('Comfortable')
```

---

## Which `if` owns the `else`?

* At 16°C, the first condition is `True`; the second is `False`. Which messages appear?
* The `else` belongs to the **second** `if`. The two `if` statements make separate decisions.
* Use `elif` ("else if") to link the second condition to the first. It is checked only if the first condition was false.
* Edit live and remove the diagnostic prints. Test 16, 21 and 26°C: expect `Heating`, `Comfortable` and `Cooling`, respectively.
* Also test the boundaries: 18 and 24°C should both print `Comfortable`, once.

---

## Repeating with `for`

* `for distance in [2, 3, 4]:` takes each distance in turn: 2, then 3, then 4 metres.
* The indented lines repeat for each distance; an unindented line after the loop runs when it finishes.
* `total = total + distance` adds the current distance to the running total.
* The running total must retain the distances already added.

---

## Spot the bug: total distance

Add three distances: 2, 3 and 4 metres. Print **9 once**, after the loop.

Predict the output, then run. Which lines repeat?

```runnable lang="python"
for distance in [2, 3, 4]:
    total = 0
    total = total + distance
print(total)
```

---

## Diagnose: total distance

Inspect the running total after each addition.

```runnable lang="python"
for distance in [2, 3, 4]:
    total = 0
    total = total + distance
    print('distance:', distance, 'total:', total)
print(total)
```

---

## What should run only once?

* The diagnostic totals are **2, 3, 4**. We expected **2, 5, 9**. Where is the earlier distance lost?
* Which statement resets the total? Should it run before every addition, or just once before the loop?
* Move the initialisation to run once before the loop. Check the indentation of the lines that should still repeat.
* Remove the diagnostic print and rerun the whole block. Expected: **9**, once.

---

## Debugging habits

* An error message is **evidence**: use it to locate the problem.
* Code that runs can still be wrong: compare with an expected result.
* Rerun the **whole block**, including its starting assignments, after a correction.

---

## Assessment 1

* Assessment 1
    * released Friday 9th October, due Friday 23rd October (both at 16:00)
    * worth **5%** of the module grade
    * based on Weeks 1 and 2
    * Numbas test with supplementary plot upload

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

## From x values to fitted y values

`p[0]` is the fitted gradient; `p[1]` is the intercept.

```python
x1 = np.linspace(0, 5, 100)
f = p[0] * x1 + p[1]
```

Each x value gives one fitted y value:

```python
f[0] = p[0] * x1[0] + p[1]
f[1] = p[0] * x1[1] + p[1]
```

`plt.plot(x1, f)` draws the fitted line.

---

## The same calculation with `polyval`

These are equivalent:

```python
f = p[0] * x1 + p[1]
f = np.polyval(p, x1)
```

**`polyfit` finds `p`; `polyval` evaluates it at `x1`.** No new fit.

For a quadratic, the same `polyval` call replaces:

```python
f = p[0] * x1**2 + p[1] * x1 + p[2]
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

### The transform written out

Transform $y = ax^b$ into a linear equation by introducing new variables $X$ and $Y$.
For $x > 0$ and $a > 0$ (so $y > 0$), use natural logarithms:

$$\ln(y) = \ln(ax^b) = \ln(a) + b\ln(x).$$

Define the transformed coordinates and intercept:

$$X = \ln(x), \qquad Y = \ln(y), \qquad c = \ln(a).$$

The transformed points $(X, Y)$ lie on a straight line:

$$Y = bX + c \qquad \text{(gradient } b,\; \text{intercept } c\text{).}$$

After fitting that line, transform back:

$$a = e^c, \qquad y = e^Y = e^{bX+c} = e^c x^b = ax^b.$$

The gradient gives $b$ directly; exponentiate only the intercept to recover $a$.

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
