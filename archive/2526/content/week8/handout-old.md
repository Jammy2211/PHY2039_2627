

## Introduction

Welcome to the handout for the fifth week of MAS2805 material. These week's theme is **numerical differentiation and integration**.

Numerical methods to compute derivatives and integrals are frequently necessary in mathematical modelling. The basic algorithm used to differentiate or integrate a function is similar to the definition of these operations in terms
of infinitesimals, but rather than take the limit as the infinitesimal tends to zero, on a computer we stop at a finite value: the approach is called finite difference calculus.

It is useful to understand how the basic methods work in order to judge how reliable their results are; this often boils down to choosing an increment that is small enough, but not too small as to cause unnecessary computation.

Note that some Python packages can carry out symbolic calculus involving elementary functions. That is, they "know" that the derivative of $\sin(x)$ is $\cos(x)$ and that $\int \cos(x) \mathrm{d}x = \sin(x) + C$. In this chapter we are only concerned with numerical approximations to the operations of calculus and will not be using the symbolic functionality of Python. 

## Python functions for numerical differentiation and integration

### Using Numpy `gradient` to differentiate 


NumPy provides a useful function that calculates the first derivative of a vector. `gradient` calculates the difference between all of the consecutive pairs of numbers in a vector (i.e. the difference between consecutive $y$ values) and weights this difference by their separation (i.e. the difference between the corresponding $x$ values) in order to find an approximate value of the gradient $\mathrm{d}y/\mathrm{d}x$ at each point.

`gradient` is fairly straightforward to use.

```python
import numpy as np
y = [0, 1, 4, 9, 16]
dydx = np.gradient(y)
```

By default, `gradient` assumes that the dependent variables (called `y` here) are separated by an increment of $1$ in the independent variable. Throughout this handout we call this separation $h$. If necessary, for example if our $y$ values above correspond to $x = [0, 2, 4, 6, 8]$, we can specify the increment $h = 2$ directly:

```python
dydx = np.gradient(y,2)
```

To calculate the second derivative, we can just apply gradient again to `dydx`.

The algorithm that `gradient` uses is pretty much the simplest form of *finite differencing*. Further into today's session we'll look in more depth at how this method for approximating derivatives works.


### Exercise 5.1 {: .exercise}

This exercise explores some of the subtleties of using `gradient`

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise1" aria-expanded="false" aria-controls="exercise1">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise1">
<iframe class="numbas" data-src="../../static/numbas/week5/question-93681-using-numpy-gradient/index.html" src="about:blank" id="exercise1"></iframe>
</div>


### Integrating using SciPy's `quad`


We are going to look at two built-in functions that make it easy to numerically integrate a function, whether you know the analytic form of the function, or just have a collection of data points that define it. 

When the function is known, we can use SciPy's `quad`. This uses a very sophisticated quadratur method, similar to ones that you might be familiar with: Simpson's rule or the trapezoidal rule.

This example numerically evaluates the integral of the sinc-function

$$ \int_{0}^{2\pi}\frac{\sin x}{x} \mathrm{d}x $$

First define the function 

```python
import numpy as np
from scipy import integrate

def myfunc(x) 
	return np.sin(x)/x   
```

Note that `from scipy import integrate`  imports only the integrate subpackage from scipy and allows commands like `integrate.quad`. If you're more comfortable with it you can use `import scipy.integrate as int` and then `int.quad`. It amounts to the same thing, but I am following the convention of online documentation here.

Now call `quad`, telling it what the function is

```python
myint = integrate.quad(myfunc, 0, 2*np.pi)
```

`quad` returns the value of the integral and an estimate of the absolute error associated with this numerical approximation:

```python
print(myint)
```
```output
(1.4181515761326284, 2.5246396982818194e-14)
```


### Exercise 5.2 {: .exercise}

Here's an exercise using `quad`. Keep hold of your code, as you'll use this for exercise 5.4 in a few minutes.

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise2" aria-expanded="false" aria-controls="exercise2">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise2">
<iframe class="numbas" data-src="../../static/numbas/week5/question-93682-scipy-quad/index.html" src="about:blank" id="exercise2"></iframe>
</div>



### Integrating using NumPy's `trapz`


To integrate a function that is defined by a set of data points, i.e. when you don’t know what the function is in terms of elementary functions, use the NumPy function `trapz`. This uses [trapezoid quadrature](https://en.wikipedia.org/wiki/Trapezoidal_rule){target="_blank"} and can cope with non-uniform separation of the points:

```python
import numpy as np
x=[1, 2.5, 7, 10, 25]
y=[0.3, 0.6, 2.2, 8.3, 100]
T = np.trapz(y,x)  # Note y,x 
```

### Exercise 5.3 {: .exercise}

Here's an example where care is needed with `trapz`.

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise3" aria-expanded="false" aria-controls="exercise3">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise3">
<iframe class="numbas" data-src="../../static/numbas/week5/question-93685-numpy-trapz/index.html" src="about:blank" id="exercise3"></iframe>
</div>




### Exercise 5.4 {: .exercise}

Here's a comparison of `trapz` and `quad`.

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise4" aria-expanded="false" aria-controls="exercise4">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise4">
<iframe class="numbas" data-src="../../static/numbas/week5/question-93686-trapz-vs-integral/index.html" src="about:blank" id="exercise4"></iframe>
</div>



## How does numerical differentiation work?

The definition of the derivative of a function is

$$ \frac{\mathrm{d}f}{\mathrm{d}x} = f'(x) = \lim_{h\to 0}\left[ \frac{f(x+h)-f(x)}{h} \right] $$

This suggests that a good approximation to the derivative will be

$$ f'(x) \approx \frac{f(x+h)-f(x)}{h}  \quad \text{(*)} $$

if a small enough $h$ is chosen.

![](/static/images/week3/finite_forwarddiff.png){width=80%}

The choice of $h$ is critical though, and here’s why: two types of error will be present in the estimated gradient, **truncation error** and **roundoff error**. It's useful to know a little bit about them:

### Truncation error

Truncation error occurs because $h$ is finite (since we cannot numerically "take the limit" $h\to 0$). Let’s look at the Taylor-series expansion of $f(x)$ about the point $x + h$; this converges on the correct value
of $f(x + h)$ as more terms in the series are added

The Taylor expansion of $f(x + h)$ is 

$$ f(x + h) = f(x) + \frac{hf'(x)}{1!} + \frac{h^2f''(x)}{2!} + \cdots $$

which can be rearranged to give

$$ f'(x) = \frac{f(x+h)-f(x)}{h} - \frac{h^2f''(x)}{2!} + \cdots $$

very similar to equation (\*) above, but now we can see what the $\approx$ symbol represents. The extra terms are the error that is introduced in the approximation of $f'(x)$ by *truncating* the Taylor series (hence *truncation error*). Since $h$ has to be small ($h<<1$) for the method to make sense, the biggest of the missing terms will
be the first, involving the second derivative, and so the error in $f'(x)$ will be *of the order of $h$*, written as $\mathcal{O}(h)$

### Interlude: "Oh!" {: .interlude}

As you probably expect, everything in mathematics has to have a formal definition, and one exists for $\mathcal{O}$, which is known as "big-oh". This is formulated in a similar way to the definition of a limit, but need not concern us here, not least because there is yet another definition of "order of" called “little-oh”.

If you are interested in this stuff then [this is quite a good read](https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/content/analysis/notations.html){target="_blank"}, but as they quite rightly say in that link, for the purposes of what we are doing, just use the information to rank the different methods for accuracy, and know that a finite difference method with $\mathcal{O}(h^2)$ truncation error is preferred to one with $\mathcal{O}(h)$.

### Roundoff error

Roundoff error occurs because of the finite accuracy with which real numbers can be computed. The difference $f(x + h)-f(x)$ may not have an exact representation; generally there is a limit on the precision (epsilon of the numbers). If the roundoff error is a lot smaller than the truncation error, which is very often the case, then it is not worth worrying about (and we'll take that approach here!).

##  Finite difference methods

The method for approximating derivatives by computing the difference between function values at two nearby points is called finite differencing.

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=5da463c1-83f0-41ec-be12-ac7a016bf205&autoplay=false&offerviewer=false&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

### Forward Difference Method

The simplest method for finite differencing is described above, and is known as the *forward difference method*:

$$ f'(x) = \frac{f(x+h)-f(x)}{h} + \mathcal{O}(h) $$

This method is very easy to apply to any data that can be represented on a regular grid. We will only consider
one-dimensional data (i.e. $x$ and $f(x)$ are both $(1, n)$ arrays), but the principle can be readily extended to calculate derivatives of multi-dimensional data such as $f(x, y, z)$.

We can get a better approximation than the forward difference method though...

### central difference method

An obvious fault in the forward difference method is that it only uses the data on one side of $f(x)$. Surely a better idea is to use information from both sides of the point at which we want the derivative. The way to do this is to use more data points in the approximation.

Suppose we use the points $f(x-h)$, $f(x)$ and $f(x+h)$ to estimate $f'(x)$, and that there is an approximation

$$ \frac{\mathrm{d}f}{\mathrm{d}x} \approx Af(x-h)+Bf(x)+Cf(x+h) $$

where $A,B,C$ are coefficients to be determined. The coefficients can be obtained by taking the Taylor-series expansion for $f(x-h)$ and $f(x+h)$. Keeping terms up to $h^2$, this reads


\begin{align}
\frac{\mathrm{d}f}{\mathrm{d}x} &=& A\left[ f(x)-hf'(x)+\frac{h^2f''(x)}{2} \right] + \\
& & Bf(x) + \\
& & C\left[ f(x)+hf'(x)+\frac{h^2f''(x)}{2} \right]
\end{align}

Equating coefficients of $f(x)$, $f'(x)$, $f''(x)$ on the left and right side gives three equations


\begin{align}
0 &=& A+B+C \\
1 &=& -Ah+Ch \\
0 &=& \frac{Ah^2}{2}+\frac{Ch^2}{2}
\end{align}


which can be solved to find $A = -1/(2h)$, $B = 0$ and $C = 1/(2h)$. Then the so-called central (or centered) difference approximation for $f'(x)$ is

$$ f'(x) = \frac{f(x+h)-f(x-h)}{2h} + \mathcal{O}(h^2) $$

(Note this is accurate to $\mathcal{O}(h^2)$).

The important point here is that we have improved the accuracy of the finite difference scheme by taking into account the behaviour of f(x) at more points near to x, which meant using more terms in the Taylor expansion.

### Second derivative using the central difference method

The same principles give finite difference approximations for higher derivatives. For example, an $\mathcal{O}(h^2)$ accurate second derivative is given by

$$ f''(x) = \frac{f(x+h)-2f(x)+f(x-h)}{h^2} + \mathcal{O}(h^2)  $$

This is also a central difference method, as an equal number of points have been used either side of $f(x)$.

### Gaining more accuracy

Accuracy of $\mathcal{O}(h^3)$ could be obtained by using $f(x-2h)$, $f(x-h)$, $f(x)$, $f(x+
h)$ and $f(x+2h)$: the five unknown coefficients can be found by keeping terms
in the Taylor series up to $f''''(x)$. 

The trade-off for increased accuracy is that $f(x)$ has to be evaluated at more points, which slows down the computation. In one dimension this hardly matters, but for higher dimensional data this can be a significant overhead.

### One-sided methods
The above methods work fine if there are the required number of points available, and this is always the case for periodic functions.

But what if we want to know the derivative at the boundaries of a range, when $f(x-h)$ or $f(x+h)$ is not available.

Well, the forward-difference method that we looked at first is a one-sided difference scheme (it doesn't use $f(x-h)$),
and a similar approach to that taken above gives the following useful formulae, accurate to O(h^2) for approximating first and second derivatives at a boundary:

#### Right-sided schemes

The second-order (uses the point $f(x)$ plus two more) right-sided method is as follows, with error $\mathcal{O}(h^2)$:

$$ f'(x) = \frac{-3f(x)+4f(x+h)-f(x+2h)}{2h} + \mathcal{O}(h^2)   $$

$$ f''(x) = \frac{2f(x)-5f(x+h)+4f(x+2h)-f(x+3h)}{h^2} + \mathcal{O}(h^2)  $$

The first derivative is illustrated below

![](/static/images/week3/finite_onesided_forward.png){width=70%}


#### Left-sided schemes

Similarly, the second-order left-sided method is as follows:

$$ f'(x) = \frac{3f(x)-4f(x-h)+f(x-2h)}{2h} + \mathcal{O}(h^2)   $$

$$ f''(x) = \frac{2f(x)-5f(x-h)+4f(x-2h)-f(x-3h)}{h^2} + \mathcal{O}(h^2)  $$

The first derivative is illustrated below

![](/static/images/week3/finite_onesided_backward.png){width=70%}


### Using `roll` for finite differencing

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=1f5ec0c2-692f-45bb-a726-ac7a016bca1e&autoplay=false&offerviewer=false&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

The NumPy function `roll` is very useful for computing finite differences, especially for periodic data. If the data is not periodic then some tidying up is required at the boundaries using one-sided differences. `roll` circularly shifts all of the values in a list/array to the right

```python
import numpy as np
a=np.arange(1,11)
np.roll(a,[0,-2])
np.roll(a, [0,2])
```

```
1 2 3 4 5 6 7 8 9 10

3 4 5 6 7 8 9 10 1 2

9 10 1 2 3 4 5 6 7 8

```


where `[0,2]` means don’t shift the rows, but shift the columns 2 steps to the right. As you can see, the vector is treated circularly, so that $10$ and $1$ are treated as being next to each other.

Python will interpret the following so that `roll(a, -2)` is read the same as `roll(a,[0,-2])` above. I'll use the former throughout, but it's good to recognise that the function is not strictly speaking just for $1$x$n$ arrays.


```python
import numpy as np
a=np.arange(1,11)
np.roll(a, -2)
np.roll(a, 2)
```

### Exercise 5.5 {: .exercise}

Here's some `roll` practice:

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise5" aria-expanded="false" aria-controls="exercise5">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise5">
<iframe class="numbas" data-src="../../static/numbas/week5/question-93693-using-numpy-roll/index.html" src="about:blank" id="exercise5"></iframe>
</div>




### Worked example

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=79a6cbaf-5226-469a-8c32-ac7a016b98a6&autoplay=false&offerviewer=false&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

*(At the end of the video above, when I got way sidetracked(!), I needed `\\frac{df}{dx}` (extra backslash to 'escape' the original backslash) to get "df/dx" to appear as a fraction. It turns out this was a bit small for a fraction in the legend anyway. The point still stands that [LaTeX](https://www.latex-project.org/){target="_blank"} is well worth checking out if you have spare time / are finding this module OK).*

I'm going to go through the example from the video above, $f(x)=\exp(2x)$ in small steps. A compact algorithm to implement the central difference method using circular shifts is as follows

Evaluate f(x) for all values of x

``` python
n = 50      
x = np.linspace(0,1,n)
f = np.exp(2*x)
```
Define the separation, $h$, which is the distance between any two `x` values

``` python
h = x[1]-x[0]
```

Shift `f` one step left, so that the index of all the $f(x+h)$ points will correspond to the $f(x)$ points:

``` python
np.roll(f,-1)
```

* Shift `f` one step right, so that the index of all the $f(x-h)$ points will correspond to the $f(x)$ points:

``` python
np.roll(f,1)
```

* Subtract the second from the first and divide by $2h$


``` python
dfdx = (np.roll(f,-1)-np.roll(f,1))/(2*h)
```

This lets us compute $\mathrm{d}f/\mathrm{d}x$ on one line and `roll` helps us to avoid using a for loop, which would be more time-consuming.

If $f(x)$ is not periodic (i.e. if `f[0]` is not the value of $f(x)$ that follows
`f[n]`), then `dfdx` will need to be overwritten with its correct values at `dfdx[0])` and `dfdx[n-1]`
for example using the second-order one-sided difference schemes:

``` python
dfdx[0] = (-3*f[0]+4*f[1]-f[2])/(2*h)   	# right-sided
dfdx[n-1] = (3*f[n-1]-4*f[n-2]+f[n-3])/(2*h)    # left-sided
```

We could then plot to check the results, noting that we know $\frac{\mathrm{d}}{\mathrm{d}x}\left(\exp(2x)\right)=2\exp(2x)$.

![](/static/images/week3/exp2x.png){width=80%}


### Exercise 5.6  {: .exercise}

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise6" aria-expanded="false" aria-controls="exercise6">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise6">
<iframe class="numbas" data-src="../../static/numbas/week5/question-95521-finite-difference-periodic/index.html" src="about:blank" id="exercise6"></iframe>
</div>


## How does numerical integration work?
Since integration, even of elementary functions, is harder than finding derivatives, methods for the numerical calculation of integrals date back to the early days of calculus. Numerical evaluation of a definite integral is historically called quadrature and this terminology is useful, as it distinguishes the calculation of integrals from the numerical solution of ODEs, which is often also called integration.

Quadrature methods can be split into two groups: those that integrate a given function (like `quad`) and those that integrate a set of discrete datapoints that correspond to $f(x)$ (like `trapz`).

### Quadrature
The basic idea of quadrature harks back to the way in which integration is often first introduced in school mathematics. Represent $f(x)$ with a set of shapes whose area is known: the definite integral is then approximated as
the sum of all of these small areas.

There is a balance between making the intervals in $x$ small enough to get accuracy but few enough to compute in a reasonable time. The size of the sub-areas will depend on how rapidly the function varies: a slowly changing $f(x)$ can be approximated by larger "blocks" than a rapidly varying function.

Here are some of the ways to define these areas:

### The midpoint rule 

The midpoint rule approximates the integral by a set of rectangles of base
$h = b-a$. So the area of each is given by

$$ M = h\left(f\left(\frac{a+b}{2}\right)\right), $$

which is a rectangle whose height is $f(x)$ at the midpoint of $a$ and $b$. 

### The trapezoid rule 

The trapezoid rule uses a set of trapeziums to approximate the area, with each having an area of

$$ T = h\frac{f(a)+f(b)}{2}. $$

### Simpson's rule

It can be shown that for short intervals $h$, $M$ is generally twice as accurate as $T$ and that the signs of the errors are opposite: one always underestimates and the other overestimates. So a better estimate for the area can be obtained by combining both $M$ and $T$ as


$$ S = \frac{2}{3}M+\frac{1}{3}T, $$

which turns out to be the same as fitting a quadratic to the points $f(a)$, $f((a + b)/2)$ and $f(b)$. This is known as Simpson’s rule.

### Exercise 5.7  {: .exercise}

<button class="btn btn-primary toggle" type="button" data-toggle="collapse" data-target="#exercise7" aria-expanded="false" aria-controls="exercise7">
<span id="txt">Show</span> exercise >
</button> 
<div class="collapse" id="exercise7">
<iframe class="numbas" data-src="../../static/numbas/week5/question-95434-trapezoid-rule/index.html" src="about:blank" id="exercise7"></iframe>
</div>


## Handout Summary

That's all for this week. Next week we move on to a not entirely dissimilar topic: numerical solutions to ordinary differential equations.