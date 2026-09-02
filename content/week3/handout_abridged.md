
# Handout 8


## Defining Vectors and Matrices

During this course, we have made extensive use of defining 1D NumPy arrays already - so we already know how to define vectors! They are defined in the same way - a 1D array is treated as a vector by NumPy.

So, let's say we have the vector

$$ x = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} $$

then we can use the NumPy array data type that we are familiar with.

```python
import numpy as np
x = np.array([1, 2, 3])
```

A matrix is represented as a list of lists, with each of the inner list representjng a row. It can help to put each inner list on a new line to try to help visualise what the matrix looks like.

```python
matrix = np.array([[1, 2], 
                   [3, 4]])
print(matrix)
```


*(Note: you should avoid using the `np.mat` or `np.matrix` functions.** The matrix type is going to be removed from NumPy at some point in the future.()*

We're going to make use of `np.zeros` a fair bit, which we've seen before 

```python
np.zeros(3)
```

and also works in  2d 

```python
np.zeros([3, 4]) # 3 rows x 4 columns
```


There are similar functions to fill arrays with the value 1:

```python
np.ones([2, 3])
```

or indeed an arbitrary value:

```python
np.full([2,3], np.pi)
```



### Diagonal arrays

If you are defining a diagonal array, a combination of `np.zeros` and `np.fill_diagonal` may also be useful.


```python
matrix = np.zeros((3, 3))
np.fill_diagonal(matrix, 1)
print(matrix)
```
```output
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

Note that `fill_diagonal` does not make a copy of the array, rather alters it in place.

### Tri-diagonal matrices

A tri-diagonal matrix is a matrix that is all zeros except for the main diagonal and two diagonals either side of it. For example, a tri-diagonal matrix that has 1s along the main diagonal and 2s along the sub-diagonals is:

$$ 
\begin{pmatrix}
1 & 2 & 0 & 0 & 0 \\
2 & 1 & 2 & 0 & 0 \\
0 & 2 & 1 & 2 & 0 \\
0 & 0 & 2 & 1 & 2 \\
0 & 0 & 0 & 2 & 1
\end{pmatrix}
$$

To create this in Python we can use the SciPy function `scipy.sparse`.

```python
import scipy.sparse as sparse
sparse.diags([2,1,2], [-1, 0, 1], [5, 5]).toarray()
```

In the command `sparse.diags([2,1,2], [-1, 0, 1], [5, 5]).toarray()`,


* The first array are the values that are put down the diagonals, in the order the offsets are in: lower diagonal (one below), leading diagonal and upper diagonal (one above)
* The second array is the offsets: -1 represents the lower diagonal, 0  the leading diagonal, 1 the upper diagonal
* The third parameter is the size of the matrix in the form [number of rows, number of columns]


Notice the the use of `toarray()`, this is important to get a NumPy array out. Otherwise we end up with a _sparse matrix_ which is not inherently bad, but may confuse you as you're getting used to things.


### Exercise 8.1 {: .exercise}

Try manipulating vectors in this exercise.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110250/creating-vectors-and-matrices/embed/?token=98b1cf9b-e363-4f75-805d-df3909e8c9d7" data-id="exercise-8-1" data-cta="Show Exercise"></numbas-embed>



## Vector Operations

As we already know, NumPy's operations are **vectorised**, meaning that if you pass n NumPy array into most of the NumPy functions, or use stanadrd Python operators with them, Python and NumPy will choose the appropriate operation to do on the array and carry it out element-wise.

So far, we've seen that if we write:

```python
vec = np.array([1, 2, 3])
print(vec + 2)
```

the result is that 2 is added to every element and a new array is returned.


We can also do this with two arrays and do element wise addition:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(vec1 + vec2)
```

The size and shape of the two arrays must be the same for such an operation to work:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5])
print(vec1 + vec2)
```

Using any of the standard Python operators (such as `+`, `-`, `*` and `/`) on two arrays of the same size and shape will perform that operation element-wise. For example, multiplication of two vectors results in the following:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(vec1 * vec2)
```


However, in general, for vectors this is **not** how we would want to multiply two vectors together.

## Vector multiplication

Recall that there are two ways to multiply vectors together - the sclar product and the vector product. NumPy can do both.

### The scalar (dot) product

The scalar product should be familiar to you, for a three dimensional vector, it is:

$$ x = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \cdot \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = x_1 \times y_1 + x_2 \times y_2 + x_3 \times y_3 $$

In NumPy, we can use the `dot` function to perform a scalar product between the two vectors:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(np.dot(vec1, vec2))
```

## The vector (cross) product

The vector product should also be familiar to you:

$$ x = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \times \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = 
\begin{pmatrix} (x_2 \times y_3) - (x_3 \times y_2) \\ (x_3 \times y_1) - (x_1 \times y_3) \\ (x_1 \times y_2) - (x_2 \times y_1) \end{pmatrix} $$

In NumPy, we can use the `cross` function to perform a vector product between the two vectors:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(np.cross(vec1, vec2))
```

As with the `dot` function, `cross` also works with complex numbers. However, `cross` may only be used on two or three component vectors:

```python
vec1 = np.array([1, 2, 3, 4])
vec2 = np.array([4, 5, 6, 7])
print(np.cross(vec1, vec2))
```
```output
ValueError: incompatible dimensions for cross product
(dimension must be 2 or 3)
```

## Exercise 8.2 {: .exercise}

Try manipulating vectors in this exercise.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110252/numpy-scalar-and-vector-products/embed/?token=84c6d531-a3df-4ad5-ab8a-be7911f4c943" data-id="exercise-8-2" data-cta="Show Exercise"></numbas-embed>

## Matrix Operations

Addition and substraction between two Matrices of the same size and shape are done element-wise.

```python
mat1 = np.array([[1, 2, 3]])
mat2 = np.array([[4, 5, 6]])

print(mat1 + mat2)
```

However, multiplication between two matrices should not be element wise. So, performing a multiplication like this:

```python
mat1 = np.array([[1, 2, 3]])
mat2 = np.array([[4, 5, 6]])
print(mat1 * mat2)
```


gives an element-wise multiplication, which is incorrect. Instead, you should use the `@` operation

```python
mat1 = np.array([[1, 2, 3]])
mat2 = np.array([[4, 5, 6]])

# this could also be np.dot(mat1, mat2)
print(mat1 @ mat2)
```
```output
ValueError: matmul: Input operand 1 has a mismatch...
```

This error should not be surprising, considering the rules of matrix multiplication - the number of columns in the first matrix must match the number of rows in the second. Let's (manually) take the transpose of the second matrix and then multiply them together.


The transpose of a matrix can be found by using the `T` attribute on the array

```python
# This is a 1x3 matrix
mat1 = np.array([[1, 2, 3]])

# creates the transpose of the matrix
mat1_transpose = mat1.T

print(mat1_transpose)
```
```output
[[1]
 [2]
 [3]]
``` 
### Exercise 8.3 {: .exercise}

Try manipulating matrices in this exercise.


<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110251/numpy-matrix-operations/embed/?token=264a53a6-9df6-4fef-982c-7ef30bda75e5" data-id="exercise-8-3" data-cta="Show Exercise"></numbas-embed>



## Linear Algebra with SciPy

Now we know how to define and manipulate Matrices simply using NumPy, we can start to talk about performing linear algeba tasks. Both NumPy and SciPy have linear algebra modules, we'll generally be using SciPy's module as they are more precise and faster than NumPy's module. We can import this in the following way:

```python
# We'll be using the sla name for the SciPy import
import scipy.linalg as sla
```

That's it! We can now unlock the power of NumPy and SciPy on many linear algebra tasks. [You can read an exhaustive list of all the things that SciPy linalg can do here](https://docs.scipy.org/doc/scipy/reference/linalg.html){target="_blank"}. I've covered selected functions below...


### Square Matrix Operations

These are functions available in the linear algebra module for working with square matrices.

#### Determinants

Determinants, a vital part of many operations centering around square matrices, are easy to calculate in SciPy using the `det` function.

```python
import scipy.linalg as sla
import numpy as np

matrix = np.array([[14, 4, 4],
                   [5, 6, 6],
                   [7, 6, 7]])
print(sla.det(matrix))
```
```output
64.0
```

If you try to use `det` on a non-square matrix, you will get an error:

```python
import scipy.linalg as sla
import numpy as np

matrix = np.array([[14, 4],
                   [5, 6],
                   [7, 6]])
print(sla.det(matrix))
```
```output
ValueError: expected square matrix
```

### Inversion

We can invert a square matrix using `inv`:

```python
import scipy.linalg as sla
import numpy as np

matrix = np.array([[14, 4, 4],
                   [5, 6, 6],
                   [7, 6, 7]])
print(sla.inv(matrix))
```
```output
[[ 0.09375  -0.0625   -0.      ]
 [ 0.109375  1.09375  -1.      ]
 [-0.1875   -0.875     1.      ]]
```

If the matrix is singular (i.e. $\text{det} A = 0$), then SciPy will raise an error.

```python
import numpy as np
import scipy.linalg as sla

# Create the 3x3 zero matrix
matrix = np.zeros((5, 5))

print(sla.inv(matrix))
```
```output
numpy.linalg.LinAlgError: singular matrix
```

Notice the type of the error is a bit odd here, it's `numpy.linalg.LinAlgError`, not `scipy.linalg.LinAlgError`, because we're working on a NumPy array.



## Linear Systems of Equations

Now we are somewhat aquainted with matrix operations, we can start to solve more complex problems. One of those you're likely to come across is the problem of good ol' fashioned "simultaneous equations". Consider this pair of equations:

$$ 
    \begin{align}
    2x + y &= 4 \\
    x + 2y &= 5
    \end{align}
$$

We have two equations with two unknowns and upon quick inspection you should be able to glean the answer ($x = 1, y = 2$)! Let's use this simple example as a way to build up how to solve such things in Python, however.

Remember the semantics of matrix multiplication, "row by column". Using this, we can convert this into a matrix equation of the form $A\vec{x} = \vec{b}$:

$$
\begin{pmatrix}
2 & 1 \\ 1 & 2
\end{pmatrix} 
\begin{pmatrix}
x \\ y
\end{pmatrix} 
=
\begin{pmatrix}
4 \\ 5
\end{pmatrix} 
$$

Alright - now to solve it! We're going to be using the method `scipy.linalg.solve` for this one. For what we're doing, it takes two parameters, the square $N\times N$ matrix ($A$), and the $N\times 1$ vector ($\vec{b}$) that represents the right hand side. So, let's set it up and give it a go!

```python
import scipy.linalg as sla

# Matrix A
a = np.array([[2, 1],
              [1, 2]])

# RHS (b)
b = np.array([4, 5])

# Returns a vector representing x
print(sla.solve(a, b))
```
```output
[1. 2.]
```

`solve` returns a 1D NumPy array that represents the variables in $\vec{x}$ in order - in this case, that would be `x` and `y`. We got the right answer - fantastic!


### Exercise 8.4 {: .exercise}

Try it yourself with more equations and more unknowns. The basic algorithm shouldn't change.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110256/solve-linear-system-of-equations/embed/?token=201d073a-d023-4d0e-9998-ba9313ba07a0" data-id="exercise-8-5" data-cta="Show Exercise"></numbas-embed>



### Curve fitting revisited: How does `polyfit` work?

In a bit of a flashback to curve fitting... 

Now that we've talked about solving a system of linear equations, we can actually talk a bit about how NumPy's `polyfit` works, by representing the problem as a vector-matrix system which it can solve for the coefficients - like we've just done. 

Suppose there are $m$ data points, each measured at a particular value of the independent variable $x$,

$$ y_1(x_1), y_2(x_2), \cdots , y_m(x_m).$$ 

We want a model for $y(x)$, a continuous function that fits this data. One way to do this is to use
a linear combination of simple functions, called basis functions, which are simply powers of $x$ for a polynomial,

$$ f(x) = \beta_nx^n + \beta_{n-1}x^{n-1} + \cdots + \beta_2x^2 + \beta_1x + \beta_0 $$

where $\beta_j$, with $j = 0, 1, \cdots , n$ are the coefficients of the $n$th degree polynomial.

The problem boils down to finding the best values for the coefficients (the free parameters in the model). The system of equations can be written in the form

$$ \textrm{X}\mathbf{\beta} = \mathbf{y} $$

where 

 * $\mathbf{y}$ is an $m$-element vector (one value for each datapoint $y_i$)
 * $\mathbf{\beta}$ is an $(n + 1)$-element vector (one value for each parameter in the model)
 * and $\textrm{X}$ is an $m$ by $(n + 1)$ matrix where each element is one of the basis functions $x^j$, evaluated at one of the values for $x_i$, $x^j(x_i)$

If $m = n + 1$ (the number of data points is equal to the number of free parameters in the quadratic) then $\textrm{X}$ is square, i.e. the number of data points is the same as the number of basis functions, and then this system of linear equations can be solved exactly.

Usually though, the degree of the polynomial $n$ is smaller than the number of datapoints $m$; in this case Python finds the best values of $\beta_j$ by minimising the sum of the squares of the residuals, the least-squares method. 

#### An example

This all might seem more complicated than it really is, so let’s have a look at a simple example (which should look familiar from basic linear algebra). There are three data points $(x, y): (1, 3), (2, 9), (3, 19)$. To fit a quadratic
function $y = ax^2 + bx + c$, we have $\beta_2 = a$, $\beta_1 = b$ and $\beta_0 = c$. We can write this as the matrix equation

$$
\begin{pmatrix}
1 & 1 & 1 \\
4 & 2 & 1 \\
9 & 3 & 1 
\end{pmatrix}
\begin{pmatrix}
a\\
b\\
c
\end{pmatrix}
=
\begin{pmatrix}
3 \\
9 \\
19
\end{pmatrix}
$$

which can be solved by hand or with Python:

```python
import numpy as np
import scipy.linalg as sla
A = [[1,1,1],[4,2,1],[9,3,1]]
y = [[3],[9],[19]]
beta = sla.solve(A,y)
print(beta)
```

to find $a = 2$, $b = 0$, $c = 1$ and therefore

$$y = 2x^2 + 1$$

This is the same result as we would get using `np.polyfit` (within computer precision):

```python
np.polyfit([1,2,3],[3,9,19],2)
```


## Eigenvalues and Eigenvectors

Eigenvalue problems generally come from differential equation problems, but are generally introduced as problems involving matrices. In general, an eigenvalue problem can be written in the following form:

$$ A\vec{x} = \lambda\vec{x} $$

where $\vec{x}$ is an eigenvector with corresponding eigenvalue $\lambda$. There may be, and generally are, multiple solutions to eigenvalue problems, with multiple eigenvectors possible with corresponding eigenvalues. Remember, an eigenvector/eigenvalue of a matrix indicates that said matrix will only change the magnitude of the vector, but not the direction - the eigenvalue is the scalar multiplier that the operation represents on the eigenvector.

We're going to use the SciPy function `eig`, which takes a square matrix as an argument, and returns two values: an array of eigenvalues, and an array of the corresponding eigenvectors. Here's an example:

```python
import scipy.linalg as sla
import numpy as np

a = np.array([[-4, 14, 16],
              [13,  4,  9],
              [ 3,  4, 18]])

# Solving Ax = lx, where A is known
# Unpack into eigenvalues and eigenvectors
eigenvalues, eigenvectors = sla.eig(a)

# Print the valid eigenvalues
print(eigenvalues)

# Print the corresponding eigenvectors
print(eigenvectors)
```
```output
[-14.09561797+0.j   6.71375286+0.j  25.38186511+0.j]
[[ 0.8129465  -0.44528258  0.58447437]
 [-0.58232839 -0.80010959  0.58987692]
 [-0.00341249  0.40193042  0.55716688]]
```

We have three eigenvalues with corresponding eigenvectors. It is very important to realise that the second output should not be treated like a matrix: it is a list of eigenvectors. We can write a loop to print out the eigenvector for each eigenvalue like so:

```python
# len gives the size, we want to go to one less than that - range is perfect here!
for i in range(0, len(eigenvalues)):
    print("Eigenvalue: {} - eigenvector {}".format(eigenvalues[i], eigenvectors[i]))
```
```output
Eigenvalue: (-14.095617972815791+0j) - eigenvector [ 0.8129465  -0.44528258  0.58447437]
Eigenvalue: (6.713752862836402+0j) - eigenvector [-0.58232839 -0.80010959  0.58987692]
Eigenvalue: (25.38186510997938+0j) - eigenvector [-0.00341249  0.40193042  0.55716688]
```

Notice how the eigenvalues are complex numbers. In this case, we provided a matrix that has only real eigenvalues. As the eigenvalues array is a NumPy array, we can just use the `real` attribute on the array to get real numbers out.

```python
print(eigenvalues.real)
```
```output
[-14.09561797   6.71375286  25.38186511]
```

The other big thing of note is that the eigenvectors are represented as $1\times 3$ matrices - if you were to use them in the future steps of a calculation, you'll want to use them as column vectors. We can use `reshape` to turn the vector into a column vector.

```
x = ([1,2,3])
np.reshape(x,[3,1])
```


### Exercise 8.5 {: .exercise}

Let's get the eigenvalues and eigenvectors of another matrix, this time a 4 by 4 matrix.

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110254/scipy-eigenvalues/embed/?token=08c11116-2af5-4109-8e47-042445e8b603" data-id="exercise-8-6" data-cta="Show Exercise"></numbas-embed>



