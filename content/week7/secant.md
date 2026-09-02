


## The Secant Method


### Method description

The secant method finds a root by approximating the slope of a function using a secant (a secant is a straight line that passes through two points on a curve. A chord is an interval of a secant: joining the two points on the curve but not extending beyond them). 

The method starts with two points and then replaces one of them with the intersection of the secant and the $x$-axis. 

* We start with two initial guesses $x_0$ and $x_1$. 

* Find where the secant between the two points intersects the $x$ axis.

* This will be $x_2$. 

* Find where the secant between $x_1$ and $x_2$ intersects the $x$ axis...

* Repeat until the values $x_n$ and $x_{n-1}$ converge.

![The secant method](/static/images/week2/secantschematic.png){width=80%}


*Above: Schematic representation of the secant method for finding the root of $f(x) = x^2-2$, the curve shown in black. The starting points are $x_0 = 3$ and $x_1 = 2$ shown as red circles, with a red line showing the extension of the secant through $(x_0, f(x_0))$ and $(x_1, f(x_1))$. The intercept of the secant and the $x$-axis gives the new estimate for the root, $x_2$, the blue circle at around $x = 1.7$. The secant through $(x_1, f(x_1))$ and $(x_2, f(x_2))$ is the blue line, which leads to the next estimate for the root, $x_3$, shown by the black circle to the left of $x = 1.5$.*


Here's an animation of the method:

![Animation of the  Secant Method Animation](/static/images/week2/secant_animation.gif){width=65%}

<small>Image: Wikipedia</small>


The iteration steps for the Secant Method are described by the recurrence relation

$$ x_{n}=x_{n-1}-f(x_{n-1}){\frac {x_{n-1}-x_{n-2}}{f(x_{n-1})-f(x_{n-2})}} $$

I'm not going to cover the derivation of this, but if you're interested it is [fairly straightforward](https://en.wikipedia.org/wiki/Secant_method){target="_blank"}. 

### Coding the Method

Just like the Bisection Method, we start by defining the function we're interested in:

```python
def f(x):
    return x**2-2
```

This time I need two starting values - I'm choosing $x_0 = 3$ and $x_1$ = 4.

```python
x0 = 3
x1 = 4
```

Then `x2` will be given by the recurrance relation:

```python
x2 = x1 - f(x1*(x1-x0)/(f(x1)-f(x0))
```

`x3` is given by

```python
x3 = x2 - f(x2*(x2-x1)/(f(x2)-f(x1))
```

and so on.


In this video I look at how this can be moved forward into a function:

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=0af88e7b-fdb4-43a6-85b5-ac6d016f6074&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


Here's the function we came up with:

```python
def secant(f,x0,x1,eps):

    n = 0
    
    while abs(x1 - x0) > eps:
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        x0 = x1
        x1 = x2
        n += 1
        
    return x1, n

r,n = secant(lambda x : x**2 - 2, 3, 4, 1e-6)

print("root found at {} after {} iterations".format(r,n))
```






### Exercise 4.2 {: .exercise}



