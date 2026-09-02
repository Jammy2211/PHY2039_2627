# Practical 1 Exercise Solutions

## Exercise 1.1

### Exercise {: .exercise}

* Set up the following vector $x$ as list of numbers (without inputting values individually):

$$x = (-3,0,3,6,9,12,15,18)$$

* Run the following command:
 ```python
 list(range(2, -3))
 ```
 It looks like the intended output was
 ```
 [2 1 0 -1 -2]
 ```
 What is the result instead? Can you figure out how to 'fix' it.


### Solution

We get back an empty list when running the command:

```python
list(range(2, -3))
```
```{.output}
[]
```

And that's because the default step size for the range function is 1. So this is the same as
```python
list(range(2, -3, 1))
```
```{.output}
[]
```

We're asking the function to return the values from 2 to (and excluding) -3 in steps of +1, where really the step from 3 to 2 to 1 to 0 and so on is -1. Therefore we need

```python
list(range(2, -3, -1))
```
```{.output}
[2, 1, 0, -1, -2]
```

## Exercise 1.2


### Exercise {: .exercise}

Consider the following:
```python
fizzy = ["Cola", "Lemonade", "Sparkling Water"] 
still = ["Orange Juice", "Still Water"]
```

* Find a way to combine the two lists into one list named `drinks`, by first copying `fizzy` to a variable `drinks` using the `copy()` method, and then extending it using `extend()`.

* Sort your new `drinks` list alphabetically using `sort()`.

* Note that Python is very intuitive and `drinks=fizzy+still` will also do the job.

### Solution

We can create a new list as a copy of `fizzy` with

```python
drinks = fizzy.copy()
```

and then add in the `still` list with 

```python
drinks.extend(still)
```

To sort the list and view
```python
drinks.sort()
print(drinks)
```


## Exercise 1.3


### Exercise {: .exercise}

The hyperbolic sine function $\sinh(x)$ can be defined in terms of exponentials as:

$$ \sinh(x)=\frac{e^x-e^{-x}}{2}. $$

* Use the function `exp` to calculate $\sinh(\pi)$ using the expression on the right of the above equation. 
* Verify that you get the same answer with the command `np.sinh(np.pi)`. 

Note that there is both a function `np.exp` as well as a mathematical constant `np.e`. Either could be used here.

### Solution

We need numpy for this

```python
import numpy as np
```

Two ways to do the right hand side:

```python
(np.exp(np.pi)-np.exp(-np.pi))/2
```
```{.output}
11.548739357257746
```

or

```python
(pow(np.e,np.pi)-pow(np.e,-np.pi))/2
```
```{.output}
11.548739357257746
```

We can compare with the right side using `np.sinh`


```python
np.sinh(np.pi)
```
```{.output}
11.548739357257746
```

## Exercise 1.4

### Exercise {: .exercise}

Find the sum of the first 100 triangular numbers, i.e.

$$ \sum_{n=1}^{100}\frac{n(n+1)}{2} $$


### Solution

The idea here is to create a vector of integers

```python
import numpy as np
n = np.arange(1,101)
```

then we can use vector arithmetic

```python
t = n*(n+1)/2
```

and finally use the `sum()` function

```python
sum(t)
```

## Exercise 1.5

Feedback will be given when your exercise submission is marked.



