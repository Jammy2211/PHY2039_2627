[Click here to open this handout in a new browser tab](#){target="_blank"}

# Handout 7 - Numerical differentiation and integration

Numerical methods to compute derivatives and integrals are ubiquitous in mathematical modelling. Recall that the mathematical definition of differentiation and integration relies on the concept of a limit e.g. $f'(x) = \lim_{h \rightarrow 0} \left( \frac{f(x+h) - f(x)}{h} \right)$. In many applied settings it is not feasible (or possible) to compute such limits precisely, and so we must approximate them. This is done by simply taking a finite number of values for $h$, rather than the full limit $h \rightarrow 0$.

It is instructive to understand the basic methods, in order to judge how reliable their results are. In practice this often boils down to choosing a value of $h$ that is small enough to yield a good estimate, but not too small as to cause excessive computation.

## 7.1) The `roll` function

The NumPy function `roll` will be very useful for us in this Handout. Here is an example:

```python
import numpy as np
data = np.array([1, 2, 3, 4, 5, 6])
print(data)
print(np.roll(data, 1))
print(np.roll(data, -2))
```
```output
[1, 2, 3, 4, 5, 6]
[6, 1, 2, 3, 4, 5]
[3, 4, 5, 6, 1, 2]
```

For the 1D array `data` the `roll` function cyclically permutes the elements of `data` to the right (technically this is acheived by increasing the index of each value by the number specified). The name *roll* is chosen to remind the user that this permutation 'wraps around' i.e. notice that in `np.roll(data, 1)` the element `6` has been brought to from the back of the arry to the front.

We can also use `roll` for 2D arrays, but the results are less intuitive. If we provide an array and a single number $n$ to shift by, the array is effectively treated as a 1D array so that the last $n$ entries are moved from the last row(s) and moved to the first row(s), like so:

```python
import numpy as np
data = np.array([[1, 2, 3], 
				 [4, 5, 6],
				 [7, 8, 9]])
print(np.roll(data, 2))
```
```output
[[8 9 1]
 [2 3 4]
 [5 6 7]]
```

In this case NumPy flattens the array, shifts the numbers, then reshapes the array after. If we want to shift rows or columns we need to specify the `axis` parameter. Axis 0 refers to rows, axis 1 refers to columns. For example:

```python
import numpy as np
data = np.array([[1, 2, 3], 
				 [4, 5, 6],
				 [7, 8, 9]])
print(np.roll(data, 1, axis=0))
```
```output
[[7 8 9]
 [1 2 3]
 [4 5 6]]
```

and similarly:

```python
import numpy as np
data = np.array([[1, 2, 3], 
				 [4, 5, 6],
				 [7, 8, 9]])
print(np.roll(data, 1, axis=1))
```
```output
[[3 1 2]
 [6 4 5]
 [9 7 8]]
```

Finally, to shift by row and column we specify a tuple consisting of the shift and axis parameters. For example, to shift each row up one row and each column one to the right:

```python
import numpy as np
data = np.array([[1, 2, 3], 
				 [4, 5, 6],
				 [7, 8, 9]])
# Shift by -1 and 1 on axis 0 (rows) and 1 (columns) respectively.
print(np.roll(data, (-1, 1), axis=(0, 1)))
```
```output
[[6 4 5]
 [9 7 8]
 [3 1 2]]
```


<div class="exercise" markdown=true>

### Exercise 7.1

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/79673/using-numpy-roll/embed/?token=5b18fd32-d891-4e60-885d-241818ce9396" data-id="exercise-5-1" data-cta="Show Exercise"></numbas-embed>

</div>

## 7.2) Numerical differentiation

We'll consider two different in-built functions to perform numerical differentiation:
* using NumPy's `gradient` function, used if we do not have the exact form of a function, but rather some values at specific points. That is, an array containing $f(x_i) = y_i$ at given independent variable values $x_i$.
* SciPy's `derivative`, used when we have the exact form of a function.

Before using these functions we'll discuss the algorithms that underly them.

### How does numerical differentiation work?

Recall that the derivative of a function is defined

$$ \frac{\mathrm{d}f}{\mathrm{d}x} = f'(x) = \lim_{h\to 0}\left[ \frac{f(x+h)-f(x)}{h} \right] $$

This suggests that a good approximation of the derivative will be

$$ f'(x) \approx \frac{f(x+h)-f(x)}{h}  \quad \text{(*)} $$

if a small enough $h$ is chosen.

![The forward difference method](/static/images/wk7/finite_forwarddiff.png){width=80%}

Two types of error will be present in the estimated derivative, **truncation error** and **roundoff error**.

#### Truncation error

*Truncation error* occurs because a single value of $h$ is chosen (we cannot numerically consider the limit $h\to 0$, as this requires infinitely many values of $h$). Consider the Taylor-series expansion of $f(x)$ about the point $x + h$

$$ f(x + h) = f(x) + \frac{hf'(x)}{1!} + \frac{h^2f''(x)}{2!} + \cdots $$

that can be rearranged to yield

$$ f'(x) = \frac{f(x+h)-f(x)}{h} - \frac{hf''(x)}{2!} + \cdots $$

This is very similar to Equation (\*) above, but now we can see what is being masked by the $\approx$ symbol. The extra terms are the error that is introduced in the approximation of $f'(x)$ by *truncating* the Taylor series (hence truncation error). Since $h$ must be small ($h<<1$) for the numerical methods we'll cover to make sense, the largest of the missing terms will the term involving the second derivative. Therefore the error in $f'(x)$ will be *of the order of $h$*, written as $\mathcal{O}(h)$.


<div class="interlude" markdown=true>

#### Big O & Little O 

The symbol $\mathcal{O}$ is known as Big O (pronounced 'oh'). The formal definition is similar to that of a limit, but is outside the scope of this module. Additionally, there is a complimentary notion of error known as Little 0.

In computer science Big O and Little O are used to define upper and lower bounds on *computational complexity*. 

[This link contains further information](https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/content/analysis/notations.html){target="_blank"}.

</div>

#### Roundoff error

*Roundoff error* occurs due to the finite accuracy with which real numbers can be handled by a computer. The difference $f(x + h)-f(x)$ may have a very long decimal exapansion; generally there is a limit on the precision to which such expansions can be presented (recall machine epsilon from Weeks 4 and 5). If the roundoff error is very much smaller than the truncation error (this is very often the case) then it can be ignored.

###  Finite difference methods

The derivative of a function can be approximated by considering the difference between $f(x)$ and $(x+h)$, for small but finite values of $h$. Such techniques are refered to using the umbrella term *finite difference methods*.

These methods are ubiquitous throughout applied mathematics and physics, and will be useful to you if you take modules on PDEs or modelling later in your degree.

#### The forward difference method

The most basic finite difference method is known as the *forward difference method*. As discussed above

$$ f'(x) = \frac{f(x+h)-f(x)}{h} + \mathcal{O}(h) $$

That we can can approximate $f'(x)$ using the quantity $\frac{f(x+h)-f(x)}{h}$.

Notice that this method can be applied in the case in which we know the exact form of the function $f$, or if we only have a collection of values $f(x_i)$.

The error in this approximation is of the order of $h$. We are required to choose $h << 1$ so that $h^2 << h$. Therefore an approximation with error of the order $h^2$ will be a better model of the derivative. We can produce such an approximation by using more points, as follows.

#### Central Difference method

An obvious fault in the forward difference method is that it only uses one additional datapoint i.e. the point $f(x+h)$, to the right of $f(x)$. We can improve this by using an additional data point, to the left of $f(x)$. This is the premise of the *central difference method*:

$$ f'(x) = \frac{f(x+h)-f(x-h)}{2h} + \mathcal{O}(h^2) $$

This equation can be derived by taking the Taylor series for $f(x-h)$ and $f(x+h)$:

\begin{align}
f(x+h)  =& f(x)+hf'(x)+\frac{h^2f''(x)}{2} +\frac{h^3f'''(x)}{6} + \cdots \\
f(x-h)  =& f(x)-hf'(x)+\frac{h^2f''(x)}{2} -\frac{h^3f'''(x)}{6} + \cdots \\
\end{align}

Subtracting the second equation from the first yields

\begin{align}
f(x+h)-f(x-h) &= (0)f(x) + 2hf'(x) + (0)f''(x) + 2\frac{h^3f'''(x)}{6} + \cdots \\
&=  2hf'(x)+ \frac{2h^3f'''(x)}{6} + \cdots
\end{align}

Dividing by $2h$ and rearranging we obtain

\begin{align}
f'(x) = \frac{f(x+h)-f(x-h)}{2h} - \frac{h^2f'''(x)}{6}
\end{align}

Therefore the error in the approximation, $- \frac{h^2f'''(x)}{6}$, is of the order $\mathcal{O}(h^2)$. We have improved on the accurary of the forward difference method, reducing the error from $\mathcal{O}(h)$ to $\mathcal{O}(h^2)$.


#### Approximating second derivatives via the central difference method

Finite difference methods can be adapted in a straightforward way to approximate higher derivatives. For example, an $\mathcal{O}(h^2)$ accurate approximationg of the second derivative is given by

$$ f''(x) = \frac{f(x+h)-2f(x)+f(x-h)}{h^2} + \mathcal{O}(h^2)  $$

This is also a central difference method, as an equal number of points have been used either side of $f(x)$.

#### Increasing the accuracy further

An approximation with error of the order $\mathcal{O}(h^3)$ can be obtained by using two points on either side of $x$. That is, using the values $f(x-2h)$, $f(x-h)$, $f(x)$, $f(x+h)$ and $f(x+2h)$. Specficaly, one can consider the Taylor series up to $f''''(x)$. 

The trade-off for increased accuracy is that $f(x)$ must be evaluated at more points, slowing down the computation. For single-variable functions this hardly matters, but for higher dimensional data this can create a significant computational overhead.

### One-sided methods

The central difference method work well if there are the required number of points available i.e. if there is a point to the left and to the right of $f(x)$.

However, we encounter a problem if $x$ is the initial or final value in the range, so that $f(x-h)$ or $f(x+h)$ is not available.

We can modify the central difference method to accommodate for these situations, as follows. Both produce second-order approximations i.e. with error of the order $\mathcal{O}(h^2)$.

#### Right-sided method

The second-order right-sided method is as follows, with error $\mathcal{O}(h^2)$:

$$ f'(x) = \frac{-3f(x)+4f(x+h)-f(x+2h)}{2h} + \mathcal{O}(h^2)   $$

$$ f''(x) = \frac{2f(x)-5f(x+h)+4f(x+2h)-f(x+3h)}{h^2} + \mathcal{O}(h^2)  $$

The first derivative is illustrated below

![One sided forward difference](/static/images/wk7/finite_onesided_forward.png){width=70%}


#### Left-sided schemes

Similarly, the second-order left-sided method is as follows:

$$ f'(x) = \frac{3f(x)-4f(x-h)+f(x-2h)}{2h} + \mathcal{O}(h^2)   $$

$$ f''(x) = \frac{2f(x)-5f(x-h)+4f(x-2h)-f(x-3h)}{h^2} + \mathcal{O}(h^2)  $$

The first derivative is illustrated below

![One sided backward difference](/static/images/wk7/finite_onesided_backward.png){width=70%}


### Implementation in Python

The NumPy function `roll` is very useful for implementing finite difference methods in Python. As a simple example we shall approximate the derivative of $f(x)=\exp(2x)$. A compact algorithm to implement the central difference method using `roll` is as follows:

Evaluate $f(x)$ for all values of $x$:

``` python
n = 50      
x = np.linspace(0,1,n)
f = np.exp(2*x)
```

Set the $h$ parameter:

``` python
h = x[1]-x[0]
```

Shift `f` one step to the left, so that the index of all the $f(x+h)$ points will correspond to the $f(x)$ points:

``` python
np.roll(f,-1)
```

Shift another copy of `f` one step to the right, so that the index of all the $f(x-h)$ points will correspond to the $f(x)$ points:

``` python
np.roll(f,1)
```

Subtract the second array from the first and divide by $2h$:


``` python
dfdx = (np.roll(f,-1)-np.roll(f,1))/(2*h)
```

This allows us to compute the approximation in one line of code; using `roll` allows us to avoid a `for` loop.

The array `dfdx` contains the correct value of the approximation obtained by the finite difference method, except at the boundary i.e. the first and last elements. This is due to the fact that `roll` wraps around and moves elements from the front to the back of the array. 

We need to overwrite these elemenst with their correct values at `dfdx[0])` and `dfdx[n-1]`, using the second-order one-sided difference schemes:

``` python
dfdx[0] = (-3*f[0]+4*f[1]-f[2])/(2*h)   	# right-sided
dfdx[n-1] = (3*f[n-1]-4*f[n-2]+f[n-3])/(2*h)    # left-sided
```

We could then plot to check the results, noting that we know $\frac{\mathrm{d}}{\mathrm{d}x}\left(\exp(2x)\right)=2\exp(2x)$.

![A plot of the derivative of exp(2x)](/static/images/wk7/exp2x.png){width=80%}

<div class="exercise" markdown=true>

#### Exercise 7.2 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81284/finite-difference-periodic/embed/?token=c33d0808-b837-4cc8-82b3-ded2eb1b2d95" data-id="exercise-5-2" data-cta="Show Exercise"></numbas-embed>

</div>


### NumPy's `gradient` function

In the example above we considered the function $f(x) = \exp(2x)$. However, the methods we've discussed can be applied even if we don't know the exact form of $f$. That is, all we need to approximate the derivative of $f$ is a set of values $f(x_i)$, for $x_i$ values of the independent variable.

NumPy provides a useful in-built function that can approximate the derivative of $f$ given an array of such values $y_i = f(x_i)$. The function `gradient` calculates the difference between all of the consecutive pairs of numbers in an array (i.e. the difference between consecutive $y_i$ values) and weights this difference by their separation (the $h$ value) in order to compute an approximate value of the gradient $\mathrm{d}y/\mathrm{d}x$ at each point.

For example:

```python
import numpy as np
y = [0, 1, 4, 9, 16]
dydx = np.gradient(y)
```

The output array `dydx` contains the approximated gradient of $f$ at each value $x_i$, so that in the example above $dydx$ has five elements.

By default `gradient` assumes that the dependent variables (denoted `y` here) correspond to values of a function $f$ at independent variable values with separation $h=1$ i.e. $y_0 = f(x_0)$, $y_1 = f(x_0+1)$, $y_2 = f(x_0+2)$, and so on. We can specify a different value of the separation via the syntax

```python
dydx = np.gradient(y,2)
```

This is necssary if the $y$ values above correspond to $x = [0, 2, 4, 6, 8]$, for example.

We can also directly input the values of the independent variable, via the syntax:

```python
dydx = np.gradient(y,[0, 1, 2, 3, 4])
```

To approximate the second derivative of $f$ we can simply apply `gradient` again to the array `dydx`.

The algorithm that `gradient` uses is a form of the central difference method discussed above ([as noted in the NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html)).

<div class="exercise" markdown=true>

#### Exercise 7.3 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/79662/using-numpy-gradient/embed/?token=aafc95f3-7b10-4123-9b5a-c9def1051dff" data-id="exercise-5-3" data-cta="Show Exercise"></numbas-embed>

</div>

#### Approximating gradients of multivariable functions

The `gradient` function can be used to approximate the derivatives of multivariable functions, using higher-dimensional arrays. We'll illustrate the method using 2D arrays, but it can be extended to arrays of arbitary size.

Consider the following $10 \times 10$ array:

```python
import numpy as np
array2d = np.array([[   1,   4,   9],
                    [   4,   9,  16],
                    [   9,  16,  25]])
```

The $(i,j)$-th element of this array is given by $(i + j + 1)^2$ (recall that array indexing starts at $0$ so that $(0,0)$ corresponds to the top-left corner).

Applying the `gradient` function to this array will produce two arrays: one containing the result of approximating the derivative across the rows, and another containing the result of approximating across the columns:

```python
print(np.gradient(array2d))
```
```output
[array([[3., 5., 7.],
       [4., 6., 8.],
       [5., 7., 9.]]), 
array([[3., 4., 5.],
       [5., 6., 7.],
       [7., 8., 9.]])]
```

We can restrict to either rows or columns by specifying the axis parameter. Axis $0$ refers to the rows and axis $1$ refers to the columns. For example, to approximate the derivative across the rows:

```python
print(np.gradient(array2d, axis=0))
```
```output
[[3. 5. 7.]
 [4. 6. 8.]
 [5. 7. 9.]]
```

#### NumPy `gradient` edge order

Recall our first example

```python
import numpy as np
y = [0, 1, 4, 9, 16]
print(np.gradient(y))
```
```output
[1. 2. 4. 6. 7.]
```

Notice that the array `y` contains values that correspond to the function $y = x^2$, for $x=0,1,2,3,4$. Therefore we would expect the result of `gradient` to be the array `[0. 2. 4. 6. 8.]`, not the array `[1. 2. 4. 6. 7.]` as outputted above.

This is expanded on in Exercise 7.3, occurs as `gradient` uses a first-order method by default at the boundaries of the range i.e. it does not implement the second-order left- or right-sided methods discussed above. We can address this using the `edge_order` parameter:

```python
print(np.gradient(y,edge_order=2))
```
```output
[0. 2. 4. 6. 8.]
```

This option causes `gradient` to use a higher-order method at the boundary, resulting in the expected output.

For full details on this and other aspects of `np.gradient` [see the NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.gradient.html){: target="_blank"}.


### Scipy's `derivative` function

The `gradient` function is applied to datapoints, so that it can be used even if we don't know the exact form of the function. On the other hand, suppose that we do know the exact form of a function $f$, but that it is very hard (or impossible) to differentiate. In such a setting we may be interested in the value of the derivative at single point (or small collection of points), rather than working hard to compute the entire derivative. The `scipy.misc.derivative` function allows us to do this quicker, and often more accurately, than `gradient`.

The syntax is as follows:

```python
import scipy.misc as sm
sm.derivative(func, x0, dx=1.0, n=1, args=(), order=3)
```

The arguments are

* `func`: the function to differentiate
* `x0`: the point to approximate the derivative at
* `dx`: Equivalent to $h$ in `gradient`, the spacing between points to use when getting the derivative, defaults to $1$
* `n`: the number of times to differentiate (i.e. the order of differentiation, such that $d^n y/dx^n$ is obtained), defaults to $1$
* `args`: additional parameters to send to the function
* `order`: the number of points to use when determining the derivative, this must be odd and defaults to $3$

It may be tempting to set $dx$ to be very small and $order$ to be very large, in the hope of achieving the best estimate. However, in most cases this will cause the function to take a (very) long time to run. We must find a balance between accuracy and runtime: setting `dx` to be on the order of `1e-6` generally produces a good approximation in a reasonable time.

Here is an example, with $y = sin(x)$ at $x=0$:

```python
import numpy as np
import scipy.misc as sm

def f(x):
	return np.sin(x)

print(sm.derivative(f, 0, dx=1e-6))

# Or sm.derivative(lambda x: np,sin(x), 0, dx=1e-6)
```
```output
0.9999999999998334
```

Of course, analytically the correct answer is $1$. However, this approximate value is totally appropriate in many settings.

## 7.3) Numerical Integration

We'll now consider methods to approximate integrals of functions using Python.

### How does numerical integration work?

Methods for the numerical approximation of definite integrals are often achieved via a technique known as *quadrature*.

Such techniques can be split into two types: those that approximate the integral of a given function, and those that approximate the integral of an unknown function given a set of discrete datapoints.

### Quadrature

The basic idea is as follows: approximate the area beneath the graph of $f(x)$ with a set of shapes whose area is known. The integral is then approximated as the sum of these small areas.

As in the case of numerical differentation, there is a balance between the accuracy of approximation and the runtime of the method.


### The midpoint rule 

The midpoint rule approximates the integral using a set of rectangles of base $h = b-a$. Given a function $f(x)$ the area of each rectangle approximates the integral of $f$ from $a$ to $b$:

$$ \int _{a}^{b}f(x) \approx  h f\left(\frac{a+b}{2}\right) $$

The rectangle in question has height $f(x_0)$ where $x_0$ is the midpoint of the interval $[a,b]$. This is illustrated as follows:

![Midpoint Rule](/static/images/wk7/midpoint.png){width="70%"}


### The trapezoid rule

The trapezoid rule is similar to the midpoint rule, but approximates the area via trapezoids rather than rectangles. Specifically, the area of the trapezoid above the interval $[a,b]$ is

\[ (b-a)\frac{f(a)+f(b)}{2} \approx \int _{a}^{b}f(x) \]


The full integral is then approximated as the sum of the areas of the trapezoids.

This is is illustrated as follows:

![Trapezoid Rule](/static/images/week5/trapezoid_zoom.png){width="70%"}

<div class="exercise" markdown=true>

#### Exercise 7.4

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/132584/trapezoid-integrate-no-python/embed/?token=dca89160-4e84-4a05-b505-99c9c65fa115" data-id="exercise-5-4" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="exercise" markdown=true>


#### Exercise 7.5 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/81218/trapezoid-rule/embed/?token=9bf89226-fe18-4a1e-ae02-0062b381d42e" data-id="exercise-7-5" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="exercise" markdown=true>


#### Exercise 7.6

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/149725/integration-diagrams-with-fill-between/embed/?token=5c0bcacf-dd7c-4286-906c-8ed6a1aa2dcc" data-id="exercise-7-6" data-cta="Show Exercise"></numbas-embed>

</div>


### Simpson's 1/3 rule

It can be shown that the signs of the errors given by the trapezoid and midpoint rules are opposite: one always underestimates and the other overestimates. It follows that a better estimate for the area can be obtained by combining both the midpoint and trapezoid rules. It turns out that contributions of $2/3$ and $1/3$ respectively work very well. This is known as Simpson's 1/3 rule, with equation

$$ \int_a^b f(x)\mathrm{d}x \approx \frac{b-a}{6}\left[f(a)+4f\left({\frac {a+b}{2}}\right)+f(b)\right] $$

Note that $(b-a)/2$ is the step-size in Simpson's rule. (Behind the scences this is equivalent to fitting a quadratic to the points $f(a)$, $f((a + b)/2)$ and $f(b)$). 

<div class="exercise" markdown=true>


#### Exercise 7.7 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/132592/simpsons-rule-integrate-no-python/embed/?token=4c16ada0-26fb-4c2f-8138-4945a339afde" data-id="exercise-5-7" data-cta="Show Exercise"></numbas-embed>

</div>


#### The composite Simpson's rule

When Simpson's rule is applied across several sub-intervals it is commonly referred to as the *composite Simpson's Rule*.

Given $n$ sub-intervals in $[a,b]$ with step-size $h$, the composite Simpson's rule provides the estimate

$$\int _{a}^{b}f(x)\, \mathrm{d}x \approx \frac {h}{3}\left[f(x_{0})+4\sum _{j=1,\text{ odd}}^{n-1}f(x_j)+2\sum _{j=2,\text{ even}}^{n-2}f(x_j)+f(x_n)\right]$$

where $x_0 = a$, $x_n = b$ and $x_j = x_0 + jh$. Note that $n$ must be even.


<div class="exercise" markdown=true>

#### Exercise 7.8

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/149729/integration-functions/embed/?token=be6206ab-b978-4ba8-b43e-d53f6315250f" data-id="exercise-7-8" data-cta="Show Exercise"></numbas-embed>


</div>

### Approximating integrals using SciPy's `quad`

There are a number of in-built functions that implement the methods described above. When the exact form of the function is known SciPy's `quad` can be used. This uses a very sophisticated quadrature method, similar to the above methods.

As an example we'll approximate the following integral

$$ \int_{0}^{2\pi}\frac{\sin x}{x} \mathrm{d}x $$

First define the integrand function

```python
import numpy as np
from scipy import integrate

def myfunc(x):
	return np.sin(x)/x   
```

Note that `from scipy import integrate`  imports only the integrate subpackage from scipy and allows commands like `integrate.quad`. If you prefer you can use the syntax `import scipy.integrate as int`, and call the function via `int.quad`.

We can now apply `quad`, as follows:

```python
myint = integrate.quad(myfunc, 0, 2*np.pi)
```

The output of `quad` is the value of the integral and an estimate of the absolute error associated with this numerical approximation:

```python
print(myint)
```
```output
(1.4181515761326284, 2.5246396982818194e-14)
```

<div class="exercise" markdown=true>


#### Exercise 7.9 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/79663/scipy-quad/embed/?token=0d6cb554-cd04-4287-ab1f-4ab56def04b6" data-id="exercise-5-9" data-cta="Show Exercise"></numbas-embed>

</div>

### Integrating using SciPy's `trapezoid`

Note: in earlier versions of SciPy the `trapezoid` functio is known as `trapz`. [See the SciPy release notes](https://docs.scipy.org/doc/scipy/reference/release.1.6.0.html#scipy-integrate-improvements).

Suppose instead that we wish to approximate the integral of an unknown function, given a set of datapoints representing values of the function. That is, given a set of values $f(x_i)$ for independent variable values $x_i$.

One way to do this is to use the in-built function `trapezoid`, that uses [trapezoid quadrature](https://en.wikipedia.org/wiki/Trapezoidal_rule){target="_blank"} and can handle non-uniform separation of datapoints. For example:

```python
from scipy import integrate

x=[1, 2.5, 7, 10, 25]
y=[0.3, 0.6, 2.2, 8.3, 100]
T = integrate.trapezoid(y,x)  # Note the order y,x 
```

<div class="exercise" markdown=true>


#### Exercise 7.10

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/79666/scipy-trapezoid/embed/?token=eea90bc1-d48c-4e86-899b-bbfca0b75e91" data-id="exercise-5-10" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="exercise" markdown=true>


#### Exercise 7.11

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/79667/trapezoid-vs-quad/embed/?token=13be2597-b271-458e-a1a0-1570b8aafa01" data-id="exercise-5-11" data-cta="Show Exercise"></numbas-embed>

</div>

### Multivariable integration

SciPy also allows for us to approximate the integrals of multivariable functions.

#### Two-dimensional integration via `dblquad`

Double integrals are common in applied mathematics and physics e.g. when investigating a process occuring over a surface. The function `dblquad` is a multivariable version of `quad`, with the following syntax:

```python
from scipy import integrate
result, abserr = integrate.dblquad(func, a, b, gfun, hfun)
```

where:

* `func` is a function with two arguments, `y` and `x` **in that order**, returning a number.
* `a` and `b` are the limits of integration for the `x` variable, and are real numbers.
* `gfun` and `hfun` are the limits of integration for the `y` variable and are
    * real numbers; or more generally
	* a function that takes a parameter `x` and returns the limit in `y` for that given `x`

For example, we can approximate the integral

$$ \int_{x=0}^2 \int_{y=0}^1 x^2 + y^2 \mathrm{d}y\mathrm{d}x $$

with the following code:

```python
from scipy import integrate

def to_integrate(y, x):
	return x**2 + y**2

result, abserr = integrate.dblquad(to_integrate, 0, 2, 0, 1)
print(result)
```
```output
3.3333333333333335
```

### Three-dimensional integration via `tplquad`

We can do the same with triple integrals via the function `tplquad`, via the syntax:

```python
from scipy import integrate
integrate.tplquad(func, a, b, gfun, hfun, sfun, rfun)
```

* `func` is a function with three arguments, `z`, `y` and `x` **in that order**, returning a number.
* `a` and `b` are the limits of integration for the `x` variable, and are real numbers.
* `gfun` and `hfun` are the limits of integration for the `y` variable and are either:
    * real numbers; or more generally
	* a function that takes a parameter `x` and returns the limit in `y` for that given `x`
* `sfun` and `rfun` are the limits of integration for the `z` variable and are either:
    * real numbers; or more generally
	* a function that takes two parameters `x` and `y` **in that order** and returns the limit in `z` for that given `x` and `y`


<div class="exercise" markdown=true>

### Exercise 7.12 


<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/108110/double-integral-with-scipy-dblquad/embed/?token=139f9434-3b5d-4ca5-bd36-d17c0f2997a9" data-id="exercise-5-12" data-cta="Show Exercise"></numbas-embed>

</div>

<div class="interlude" markdown=true>


### Double integral bounded by a cylinder 

Consider integrating a surface with height $f(x,y)=x^2+y^2$, bounded by a cylinder with radius 1, centred at $(x,y)=(1,1)$. 

As you travel between $x=0$ and $x=2$ the upper and lower limits of integration for $y$ change. To integrate over this domain we need to determine what these limits are for a given value of $x$. To do so we use the equation of a circle with radius $1$ centred at $(1,1)$

$$ (x-1)^2 + (y-1)^2 = 1 \implies y = 1 \pm\sqrt{1 - (x-1)^2} $$

Thus the integral becomes (for our circle of radius 1):

$$ \int_{x=0}^2 \int_{y=1-\sqrt{1 - (x-1)^2}}^{1+\sqrt{1 - (x-1)^2}} x^2 + y^2 \;\mathrm{d}y\;\mathrm{d}x $$


We can implement this in Python as:

```python
from scipy import integrate

def to_integrate(y, x):
	return x**2 + y**2

def upper_limit(x):
    return 1 + (1 - (x-1)**2)**0.5

def lower_limit(x):
    return 1 - (1 - (x-1)**2)**0.5

result, abserr = integrate.dblquad(to_integrate, 0, 2, lower_limit, upper_limit)
print(result)
```
```output
7.853981633974366
```

Or alternatively as on one line:

```python
from scipy import integrate
result, abserr = integrate.dblquad(lambda y, x: x**2 + y**2, 0, 2, 
									lambda x: 1 - (1 - (x-1)**2)**0.5, 
										lambda x: 1 + (1 - (x-1)**2)**0.5)
print(result)
```
```output
7.853981633974366
```


#### Visualising this integral 

Using the surface plots covered in Week 6 we can visualise the above integral


```python
import numpy as np
import matplotlib.pyplot as plt

# 3d axes
ax = plt.axes(projection='3d')

# Make a plot
x = np.linspace(0,2, 100)
y =  np.linspace(0,2, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2

# Little trick to throw out values beyond (x-1)^2+(y-1)^2=1
Z[(X-1)**2+(Y-1)**2>1] = None

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap='seismic')

# Add a colorbar
fig.colorbar(surf, shrink=0.5)
ax.set_xlabel('x',labelpad=10)
ax.set_ylabel('y', labelpad=10)
ax.set_zlabel('f(x,y)', labelpad=10)
```

![Surface in a circular path](/static/images/wk7/surfacecircle.png){width="60%"}

</div>


## Next week

Next week:

 * Solving ODEs numerically
 * Visualizing these solutions
