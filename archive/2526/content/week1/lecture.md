![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 1 - Foundations

<p style="text-align: center; font-size: 1.2em">
    Dr James Nightingale
</p>

---

## This week

 * Refresher of Python basics
 * Refresher of Python plotting
 * Curve fitting, part 1

---


## The Spyder interface

![Spyder](/static/images/week1/spyder.png)


---

## Python basics

```runnable  lang="python"
print("Hello, World!")
print(2**3)
``` 

---

### Built-in functions


```runnable  lang="python"
print(abs(-3)) 
``` 

---

### Limitations

```runnable  lang="python"
cos(0)
``` 

---

## Python lists



```runnable  lang="python"
x = [3,6,9,12]
```

---

### Limitations of lists

```runnable  lang="python"
x = [3,6,9,12]
print(x/3)
```

---

## The NumPy package


```runnable  lang="python"
import numpy as np
print(np.cos(0))
```

---

### Element-wise arithmetic with NumPy

```runnable  lang="python"
import numpy as np
x = np.array([3,6,9,12])
print(x/3)
```


---

## Plotting

```python
import matplotlib.pyplot as plt
import numpy as np

# Some data
x = [1,2,3,4]
y = [5.5,7.0,9.5,9.9]

# Make a plot
plt.plot(x,y,'x')
plt.xlabel('x')
plt.ylabel('y')
```

---

### A basic plot

![A linear polynomial fitted to some data](/static/images/week1/curve-points.png){width=80%}



---

## Fitting polynomials

**Aim** given a set of discrete data points (e.g. experimental observations), fit a continuous function, such as a degree $n$ polynomial 

$$ f(x) = a_nx^n + a_{n−1}x^{n−1} + \cdots + ax^2 + a_1x + a_0 $$

to them. In other words, model the data with the function $f$.

**Why?** Doing so allows us to make predictions about the modelled system.


---

## What makes a good fit?


![A linear polynomial fitted to some data](/static/images/week1/multifit.png){width=80%}


---

## Practical session

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}


* You'll be working through Handout 1 (available on Canvas).
* Myself and a team of postgraduate demonstrators will be there to help.


