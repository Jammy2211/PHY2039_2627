# Practical 3 Exercise Solutions


## Exercise 3.1

### Exercise {: .exercise}

One thing that we might like to do is to calculate something inside each iteration of the for loop and to store its value somewhere. Consider this example:

```python
x = []     
for n in range(1,6):
    x.append(n**3)
```

* What do you think the object `x` will look like at the end of the loop? Run the code and check.
* What does the list method `append` do?
* Can you think of another way (better and faster way in fact) to obtain `x` from the values used in `n` (see handout 1 hand in exercise)?


### Solution

The code fills the vector with values of $n^3$. The list method `append` adds a value for each `n` to the end of the list.

An alternative using a NumPy array would be

```python
import numpy as np
n = np.arange(1,7)
x = n**3
```


## Exercise 3.2

### Exercise {: .exercise}

Curves of the form

$$y^2 = x^3 + n$$

for integer $n$, are known as [Mordell Curves](http://mathworld.wolfram.com/MordellCurve.html){target="_blank"} and are of interest in exploring the relationship between square and cube numbers (particularly for integer $x$ and $y$). 

Use a for loop to make a plot of the curves with $n=1,2\ldots10$ for $-3\le x\le 3$. [*Hint: take the square root on the right and plot both the positive and negative solution at each iteration*].

You should get something like this:

![Mordell curves](/static/images/week3/mordellcurves.png){width=100%}


### Solution

```python

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3,3,100)

#plot the +-sqrt solution at each n
for n in range(1,11):
    plt.plot(x,np.sqrt(x**3+n))
    plt.plot(x,-np.sqrt(x**3+n))

# Note to get the curves to "meet", increase density of x vector.
```


## Exercise 3.3

### Exercise {: .exercise}
Write a function called `cube_and_add` that takes in $x$ and $y$ and returns $x^3+y^3$. Test your function with

```python
cube_and_add(3,5)
cube_and_add(np.arange(3),np.arange(3))
```


### Solution

```python
def cube_and_add(x,y):
    return x**3+y**3

print(cube_and_add(3,5))

import numpy as np
print(cube_and_add(np.arange(3),np.arange(3)))
```