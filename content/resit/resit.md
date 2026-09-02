
# MAS1801 Project (August)

Place your code and results for the below tasks into a single (PDF preferred) document and upload to Canvas. 

The following will be taken into account when marking your work:

* Have you have submitted a single PDF document containing your work?
* Does your code gives the correct answers?
* Is your code clearly commented and does it use a sensible approach?
* Is your report well presented, including clear plots?

## 1) Damped oscillations   

The function

\[ x(t) = Ae^{-\gamma t}\cos\left(\omega t + \phi\right)\text{,} \]

describes the amplitude $x(t)$ of damped oscillations, for example, of a pendulum or spring. $A$ is the initial amplitude, $\lambda$ is the decay constant of oscillations, and $\omega$ and $\phi$ represent the angular frequency and phase angle.

### a) 

Create a Python function called `oscx` that takes five arguments as input: the four parameters in the function (you can rename these e.g. to `a`, `b`, `c`, `d` if you like) and a (*numpy*) array `t`. The function should return an array of $x$ values. 

*[5 marks]*

### b) 

Create some plots using your function to illustrate how the parameters affect the behaviour. One such plot is illustrated below, which includes the envelope of oscillations $\pm Ae^{-\gamma t}$. 

![](/static/images/resit.png){width=80%}

[Hint: the greek letters are unnecessary, but can be displayed using e.g. `'\omega = 0'` in the title command.]


*[5 marks]*



## 2) Quadratic Class

### a) 


Create a Python class called *Quadratic* that represents the quadratic equation

\[ ax^2+bx+c = 0\text{.} \]

The class should have an `__init__` function, such that an equation can be defined with, for example,

```python
q = Quadratic(1,4,-2)
```

which would represent $x^2+4x-2=0$.


Create a method for each of the following

* `discriminant` returns the discriminant $b^2-4ac$ of the equation.
* `classify` - returns a string "real", "repeated" or "complex", depending on the classification of the equation's roots.
* `realroots` - returns the real roots of the equation (if any)
* `display` - prints out the quadratic formula, e.g. prints out `x^2 + 5x + 2 = 0`.
* `plot` - takes two arguments, a minimum and maximum x value, and plots the equation in that range. Called with, for example, `q.plot(-5,5)`

Include some example commands in your report and a plot created using your class.

*[6 marks]*



### b)

Write a function called `quadratic_from_roots` that takes two real roots as input and identifies and returns the corresponding quadratic using the class defined in part a).

You should be able to call it with, for example with:

```python
q = quadratic_from_roots(-3,1)
q.display()
```
```output
x^2 + 2x - 3 = 0
```

and check your answer with:

```python
q.realroots()
```
```output
[-3.0, 1.0]
```






*[4 marks]*
