# Practical 3 Exercise Solutions


## Exercise 4.1

### Exercise {: .exercise}

Write your own module called "sequences" in a file *sequences.py* which contains some functions to return some common integer sequences. 

* Fibonacci seqquenece (given)

* the triangular numbers $x_n = n(n+1)/2$

* square numbers $x_n = n^2$

* cube numbers $x_n = n^3$

* Lucas numbers


### Solution

In sequences.py

```python
"""
Prints out the values in some famous 
(and not so famous) integer sequences
"""

def fibonacci(n):
    """
    print n values from the Fibonacci series
    """
    f = []   # initialise an output list

    if n > 0:
        f.append(0)
    if n > 1:
        f.append(1)
    if n > 2:
        for i in range(2,n):
            f.append(f[i-2] + f[i-1])

    print(f)
    return f
    
def lucas(n):
    """
    print n values from the Lucas numbers
    """
    f = []   # initialise an output list

    if n > 0:
        f.append(2)
    if n > 1:
        f.append(1)
    if n > 2:
        for i in range(2,n):
            f.append(f[i-2] + f[i-1])

    print(f)
    return f
    
def cubes(n):
    """
    Returns i**3 for i up to the value n
    """      
    c = []   # initialise an output list
    
    for i in range(n):
        c.append(i**3)
            
            
    print(c)
    return c

def squares(n):
    """
    Returns i**2 for i up to the value n
    """   
    s = []   # initialise an output list
    
    for i in range(n):
        s.append(i**2)
            
            
    print(s)
    return s

def triangular(n):
    """
    Returns n values from the triangular numbers
    """
    t = []   # initialise an output list
    
    for i in range(n):
        t.append(int(i*(i+1)/2))
            
            
    print(t)
    return t
```

Using this in another script:


```python
import sequences as sq
sq.fibonacci(10)
sq.lucas(10)
sq.cubes(10)
sq.squares(10)
sq.triangular(10)
```


## Exercise 4.2

There was nothing to do here really. Just save your file as *shapes.py* and run the code given.