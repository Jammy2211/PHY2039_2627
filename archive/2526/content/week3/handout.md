[Click here to open this handout in a new browser tab](#){target="_blank"}

# PHY2039 Handout 3

This week covers linear algebra, including matrix manipulation, solving systems of linear equations, and eigenvalue problems. We use NumPy and SciPy to acoomplish these goals.

## 3.1) Constructing vectors and matrices

We have made extensive use of defining 1D NumPy arrays in previous weeks. We can also use such arrays to describe vectors.

Specifically, the vector

$$ x = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix} $$

can be constructed in Python via the syntax

```python
import numpy as np
x = np.array([1, 2, 3])
```

The above syntax will construct a row vector representing $\mathbf{x}$. If we need a column vector instead, we can use the syntax

```python
x = np.array([[1],
              [2],
              [3]])
```

A column vector formed in this way is an example of a *matrix*, as constructed in Python. In general, we can construct an $(n,m)$ matrix $A$ as an array formed of a list of $n$ lists, each with $m$ elements. For example, to construct

$$ A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} $$

we use the syntax

```python
matrix = np.array([[1, 2], 
                   [3, 4]])
print(matrix)
```
```output
[[1 2]
 [3 4]]
```

*(Note: avoid using the functions `np.mat` or `np.matrix`, as they will be removed from NumPy in the near future.*

### Selecting matrix elements

Recall that we can extract elements of lists and arrays as follows

```python
L = [1,2,3,4]
L[0]
```
```output
1
```

The same can be done for matrices: the syntax `A[i,j]` extracts the element of `A` in the i-th row and j-th column, with `A[0,0]` corresponding to the top-left element. E.g.

```python
A = np.array([[1, 2], 
                   [3, 4]])
print(A[0,0])
print(A[0,1])
print(A[1,1])
```
```output
1
2
4
```

Further, recall that we can extract sections of an array using the syntax

```python
L = [1,2,3,4,5,6,7,8,9]
L[0:4]
```
```output
[1, 2, 3, 4]
```

We can do something similar for 2D arrays. For example,

```python
A = np.array([[-2,  1,  0],
[ 1, -2,  1],
[ 0,  1, -2]])
print(A[1:3,0:2])
```
```output
[[ 1 -2]
 [ 0  1]]

```

We can also use the syntax `start:stop:step`, and negative indices in the 2D setting.

### `np.zeros`, `np.ones`

The function `np.zeros` will be useful. In short, it produces an array of zeroes of the desired length. E.g.

```python
np.zeros(3)
```
```output
[0.0, 0.0, 0.0]
```

or 

```python
np.zeros([3, 4]) # 3 rows, 4 columns
```
```output
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```

There are similar functions to create an array of 1's:

```python
np.ones([2, 3])
```
```output
[[1., 1., 1.],
 [1., 1., 1.]]
```

or indeed an arbitrary value:

```python
np.full([2,3], np.pi)
```
```output
array([[3.14159265, 3.14159265, 3.14159265],
       [3.14159265, 3.14159265, 3.14159265]])
```

### Array data types

We can force a particular type for an array using the `dtype` option:

```python
x = np.ones([2,3])
type(x[1,1])
```
```output
numpy.float64
```

```python
x = np.ones([2,3],dtype=int)
type(x[1,1])
```
```output
numpy.int64
```

(The `64` represents the size of the data when stored on a computer.)

### Diagonal arrays

A diagonal array can be constructed using a combination of `np.zeros` and `np.fill_diagonal`:

```python
matrix = np.zeros([3, 3])
np.fill_diagonal(matrix, 1)
print(matrix)
```
```output
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

Note that `fill_diagonal` does not make a new copy of the array `matrix`, it alters the original permanently (similar to other methods such as `list.sort()`).

### Tridiagonal matrices

The elements of a tridiagonal matrix are zero except along the main diagonal and two diagonals either side of it. For example, the following tridiagonal matrix has 1's along the main diagonal and 2's along the subdiagonals

$$ 
\begin{pmatrix}
1 & 2 & 0 & 0 & 0 \\
2 & 1 & 2 & 0 & 0 \\
0 & 2 & 1 & 2 & 0 \\
0 & 0 & 2 & 1 & 2 \\
0 & 0 & 0 & 2 & 1
\end{pmatrix}
$$

We can use the SciPy function `scipy.sparse` to construct this in Python as follows

```python
import scipy.sparse as sparse
sparse.diags([1, -2, 1], [-1, 0, 1], [3, 3]).toarray()
```
```output
[[-2.  1.  0.]
 [ 1. -2.  1.]
 [ 0.  1. -2.]]
```

Let's unpack the command `sparse.diags([1, -2, 1], [-1, 0, 1], [3, 3]).toarray()`:

* The first array contains the values that are placed along the diagonals, in the order prescribed by the second array.
* The second array specifies the offsets for each diagonal: -1 represents the lower diagonal, 0  the leading diagonal, 1 the upper diagonal. 
* The third array specifies the size of the matrix in the form `[number of rows, number of columns]`.

If we did not include `toarray()` the object constructed in this way would not of array type (it would be a Python type known as a sparse matrix). This would cause issues with code later on.


<div class="interlude" markdown=true>

### What is a sparse matrix? 

The arrays we've been using in previous handouts are *dense*: this means that Python stores all of their elements, even if they are $0$. For small arrays this doesn't cause issues. However, when working with large arrays we would be wasting large amounts of (computer) memory keeping track of many zeroes.

In *sparse* matrix only the non-zero values are stored in memory. By not storing the majority of the elements (with value is $0$) we can write faster programs (often drastically faster). Hoever, we have to take care when passing from dense to sparse matrices. Happily SciPy [provides a package (`scipy.sparse.linalg`)](https://docs.scipy.org/doc/scipy/reference/sparse.linalg.html#module-scipy.sparse.linalg){target="_blank"} for performing operations on sparse matricies.

For the purposes of this week's content it is recommended to include `toarray()`, so that we have access to the standard array techniques we've been using in previous weeks. If you receive the error message

```
ValueError: Sparse matrices are not supported by this function. Perhaps one of the scipy.sparse.linalg functions would work instead.
```

the simplest solution is to include `toarray()`. However, in future modules or a final year project it may be necessary to use sparse matrices for memory or performance reasons.

</div>

<div class="exercise" markdown=true>


### Exercise 3.1

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110250/creating-vectors-and-matrices/embed/?token=98b1cf9b-e363-4f75-805d-df3909e8c9d7" data-id="exercise-8-1" data-cta="Show Exercise"></numbas-embed>

</div>

## 3.2) Vector Operations

NumPy's operations are **vectorised**: if you pass a NumPy array into most NumPy functions (or use standard Python operators with them) Python and NumPy will choose the appropriate operation to do on the array and carry it out element-wise.

For example, the syntax

```python
vec = np.array([1, 2, 3])
print(vec + 2)
```

causes a $2$ to be added to every element and a new array is returned

```
[3 4 5]
```

We can also do this with two arrays e.g.

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(vec1 + vec2)
```
```output
[5 7 9]
```

Notice that the size and shape of the two arrays must be the same for such an operation to work:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5])
print(vec1 + vec2)
```
```output
ValueError: operands could not be broadcast together with shapes (3,) (2,) 
```

Using any of the standard Python operators (such as `+`, `-`, `*` and `/`) on two arrays of the same size and shape will perform that operation element-wise. E.g.

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(vec1 * vec2)
```
```output
[ 4 10 18]
```

However, this last operation is not very geometric i.e. it does not correspond to operations we usually do with vectors in mathematics.


### Vector multiplication

We can use NumPy to take the dot and cross product of vectors.

#### The dot product a.k.a. scalar product

The dot product of two vectors of length $3$ is defined

$$ x = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \cdot \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = x_1 \times y_1 + x_2 \times y_2 + x_3 \times y_3 $$

This is implemented in Python as

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(np.dot(vec1, vec2))
```
```output
32
```

The dot product can be computed for arbitrary length vectors (as long as they are the same size). E.g.
```python
vec1 = np.array([1, 2, 3, 4, 5, 6])
vec2 = np.array([4, 5, 6, 7, 8, 9])
print(np.dot(vec1, vec2))
```
```output
154
```


#### The cross product

The cross product of two vectors of length $3$ is defined

$$ x = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \times \begin{pmatrix} y_1 \\ y_2 \\ y_3 \end{pmatrix} = 
\begin{pmatrix} (x_2 \times y_3) - (x_3 \times y_2) \\ (x_3 \times y_1) - (x_1 \times y_3) \\ (x_1 \times y_2) - (x_2 \times y_1) \end{pmatrix} $$

This is implemented in Python asrs:

```python
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
print(np.cross(vec1, vec2))
```
```output
[-3  6 -3]
```

Recall that the order of the arguments of `np.cross(vec1, vec2)` matters, so that

```python
print(np.cross(vec2, vec1))
```
```output
[3  -6  3]
```

The function `np.cross` can only be computed on a pair of length $3$ vectors. E.g.

```python
vec1 = np.array([1, 2, 3, 4])
vec2 = np.array([4, 5, 6, 7])
print(np.cross(vec1, vec2))
```
```output
ValueError: incompatible dimensions for cross product
(dimension must be 2 or 3)
```

<div class="interlude" markdown=true>

The cross product has the following defining properties: given vectors $\mathbf{u}$, $\mathbf{v}$ the cross product $\mathbf{u} \times \mathbf{v}$ is another vector, orthogonal to both $\mathbf{u}$ and $\mathbf{v}$.

Amazingly, it turns out that the only other dimension in which a cross product satisfying these properties exists is dimension $7$.

</div>

<div class="exercise" markdown=true>

### Exercise 3.2

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110252/numpy-scalar-and-vector-products/embed/?token=84c6d531-a3df-4ad5-ab8a-be7911f4c943" data-id="exercise-8-2" data-cta="Show Exercise"></numbas-embed>

</div>

## 3.3) Matrix operations

As we are using NumPy arrays to construct matrices we can rely on element-wise arithmetic for many common operations. E.g.

```python
mat1 = np.array([[1, 2, 3],
                 [4, 5, 6]])
mat2 = np.array([[6, 5, 4],
                 [3, 2, 1]])

print(mat1 + mat2)
```
```output
[[7 7 7]
 [7 7 7]]
```

Notice that the operator `*` will also apply element-wise to matrices, so that

```python
print(mat1 * mat2)
```
```output
[[ 6 10 12]
 [12 10  6]]
```

This behaviour is often useful, but it does not correctly capture matrix multiplication.

### Matrix multiplication

Matrix multiplication is implemented via the operator `@`. Let $A$ be an $(n,m)$ matrix, and $B$ an $(k,l)$ matrix. Recall that the matrix product $AB$ exists if and only if $m=k$, and that $AB$ is an $(n,l)$ matrix (if it exists).

In the example above `mat1` and `mat2` are both $(2,3)$ matrices, so their product does not exist and we obtain

```python
print(mat1 @ mat2)
```
```output
ValueError: matmul: Input operand 1 has a mismatch...
```

Let `mat3` be the matrix

```python
mat3 = np.array([[6, 5],
                 [4, 3],
                 [2, 1]])
```

We can then compute both `mat1@mat2` and `mat2@mat1`. We have

```python
print(mat1@mat3)
print(mat3@mat1)
```

Notice that `mat1@mat3` is a $(2,2)$ matrix but `mat3@mat2` is a $(3,3)$ matrix. This highlights the *noncommutativity* of matrix multiplication: $AB$ is not equal to $BA$, in general.

### Transpose

We can convert a matrix to its transpose using the following syntax

```python
mat1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(mat1.T)
```
```output
[[1 4]
 [2 5]
 [3 6]]
```

Notice that this has changed the original matrix permanently, rathen than created a new object.

<div class="exercise" markdown=true>

### Exercise 3.3 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110251/numpy-matrix-operations/embed/?token=264a53a6-9df6-4fef-982c-7ef30bda75e5" data-id="exercise-8-3" data-cta="Show Exercise"></numbas-embed>

</div>

## 3.4) Linear algebra with SciPy

Now that we can create and manipulate matrices themselves, we can use futher functionality of Python to solve linear alegbra problems. There are a number of packages suited to this task; we'll be using SciPy's `linalg` package, imported as

```python
import scipy.linalg as sla
```

Notice the shorthand `sla` (similar to `import matplotlib.pyplot as plt`).

[The official documentation for `linalg` can be found here.](https://docs.scipy.org/doc/scipy/reference/linalg.html){target="_blank"}


### Square matrix operations

A matrix is *square* if it has the same number of rows as columns e.g. it is an $(n,n)$ matrix. The following functions are provided by `linalg` for use with square matrices.

#### Determinants

Determinants are straightforward to calculate in SciPy using the `det` function:

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

Attempting to use `det` on a non-square matrix yields the following error

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

This is as expected, as it does not make mathematical sense to compute the determinant of a non-square matrix.

<div class="interlude" markdown=true>

### Why SciPy over NumPy for linear algebra?

NumPy also provides many functions for working with matrices. E.g. we can compute the determinant as follows

```python
import numpy.linalg as la
import numpy as np

matrix = np.array([[14, 4, 4],
                   [5, 6, 6],
                   [7, 6, 7]])
print(la.det(matrix))
```
```output
63.99999999999998
```

While there result is very similar (and the error is small), it's not the same as that computed by SciPy. In general, SciPy is more accurate. [More details can be found here.](https://www.scipy.org/scipylib/faq.html#why-both-numpy-linalg-and-scipy-linalg-what-s-the-difference){target="_blank"} Basically, use SciPy if you can and use NumPy as a backup.

</div>

### Inversion

We can invert a square matrix using `sla.inv`:

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

If the matrix is singular (i.e. $\text{det} A = 0$) SciPy will raise an error:

```python
import numpy as np
import scipy.linalg as sla

# Create the 5x5 zero matrix
matrix = np.zeros((5, 5))

print(sla.inv(matrix))
```
```output
numpy.linalg.LinAlgError: singular matrix
```

Again, this is as expected: a square matrix possesses an inverse if and only if it is not singular.

(Notice that the error refers to NumPy not SciPy, as we're working on a NumPy array.)

<div class="interlude" markdown=true>

#### Machine precision 

Let's verify that this does indeed produce the inverse of a matrix. Given a matrix $A$, recall that the inverse, $A^{-1}$, is the unique matrix satisfying $A A^{-1} = A^{-1} A = I$, for $I$ the identify matrix.

```python
import numpy as np
import scipy.linalg as sla

matrix = np.array([[14, 4, 4],
                   [5, 6, 6],
                   [7, 6, 7]])
inverse = sla.inv(matrix)
# A A^-1
print(matrix @ inverse)
print("---")
# A^-1 A
print(inverse @ matrix)
```
```output
[[1.00000000e+00 0.00000000e+00 0.00000000e+00]
 [1.11022302e-16 1.00000000e+00 0.00000000e+00]
 [5.55111512e-17 0.00000000e+00 1.00000000e+00]]
---
[[ 1.0000000e+00  0.0000000e+00  0.0000000e+00]
 [ 8.8817842e-16  1.0000000e+00  0.0000000e+00]
 [-8.8817842e-16  0.0000000e+00  1.0000000e+00]]
```

This isn't the identity matrix, but it is close. The two non-zero entries are very close to zero. This is due to a known problem with floating point arithmetic: because computers cannot store an infinite number of decimal places (and packages such as SciPy do not attempt to store numbers as fractions) some precision is inevitably lost. However, in general the error is extremely small in magnitude. 

There are a number of ways to mitigate this, as we'll see in the coming weeks.

</div>


### Systems of linear equations

Consider the system of linear equations (a.k.a. simultaneous equations)

$$ 
    \begin{align}
    2x + y &= 4 \\
    x + 2y &= 5
    \end{align}
$$

This is a system of two equations in two unknowns, and we can rewrite it in terms of matrices as follows

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

That is, we have expressed the system in the form $A\mathbf{x} = \mathbf{b}$, for $A$ a matrix and $\mathbf{x}$, $\mathbf{b}$ vectors.

We can solve this system using `linalg` as follows

```python
import scipy.linalg as sla
import numpy as np

# matrix A
a = np.array([[2, 1],
              [1, 2]])

# vector b
b = np.array([[4],[5]])

# Returns a vector representing x
print(sla.solve(a, b))
```
```output
[[1.]
 [2.]]
```

The function `solve` returns a NumPy array that represents the variables in $\mathbf{x}$.

Note that defining `b` as a row vector would not cause any problems: it would simply cause the output vector to be a row vector also.

<div class="exercise" markdown=true>

### Exercise 3.4 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110256/solve-linear-system-of-equations/embed/?token=201d073a-d023-4d0e-9998-ba9313ba07a0" data-id="exercise-8-5" data-cta="Show Exercise"></numbas-embed>
</div>


### Curve fitting via linear algebra

In certain circumstances the function `polyfit` we encountered in previous weeks uses techniques like those described above to fit curves to data. 

Consider a collection of datapoints $y_i (x_i)$

$$ y_0(x_0), y_1(x_1), \cdots , y_m(x_m).$$ 

Our task is to obtain a model, $f(x)$, of this dataset. One way to do so is to build $f(x)$ as a combination of simple functions, known as *basis functions*. When fitting a polynomial to a dataset the basis functions are simply powers of $x$ e.g. $\beta_nx^n, \beta_{n-1}x^{n-1}, \ldots$. That is,

$$ f(x) = \beta_nx^n + \beta_{n-1}x^{n-1} + \ldots + \beta_2x^2 + \beta_1x + \beta_0 $$

where $\beta_j$, with $j = 0, 1, \ldots , n$ are parameters.

We must therefore find the optimal values of the parameters $\beta_j$. We can express this as the matrix equation

$$ \textbf{X}\mathbf{\beta} = \mathbf{y} $$

where 

 * $\mathbf{y}$ is an $(m + 1)$-length vector containing the datapoints $y_i$.
 * $\mathbf{\beta}$ is an $(n + 1)$-length vector containing the parameters $\beta_j$.
 * $\textbf{X}$ is an $(m + 1, n + 1)$ matrix, with $(i,j)$-the element equal to $(x_i)^{n-j}$
 
The matrix $\mathbf{X}$ is known as a Vandermode matrix.

If the number of data points is equal to the number of free parameters in the quadratic, then $\textrm{X}$ is square, i.e. the number of data points is the same as the number of basis functions. In this case the system can be solved exactly.

If the degree of the polynomial $n$ is smaller than the number of datapoints $m$ then the system cannot be solved exactly. However, linear algebra is still very useful as it can be used to find relationships between the variables, so that they do not all need to be computed explicitly. 

#### Worked example

Consider the three data points $(x, y): (1, 3), (2, 9), (3, 19)$. In the notation above fitting a quadratic function $y = ax^2 + bx + c$ requires us to compute $\beta_2 = a$, $\beta_1 = b$, $\beta_0 = c$. 

Recall that the $(i,j)$-the element equal to $(x_i)^{n-j}$. In this case $n=2$ and $x_1 = (1,3)$, so that the $(0,0)$-th entry is $1^{2-0}$, and so on. The complete matrix is

$$ X = \begin{pmatrix}
1^2 & 1^1 & 1^0 \\
2^2 & 2^1 & 2^0 \\
3^2 & 3^1 & 3^0 
\end{pmatrix} = 
\begin{pmatrix}
1 & 1 & 1 \\
4 & 2 & 1 \\
9 & 3 & 1 
\end{pmatrix} $$

that that the equation is

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

We solve this as follows

```python
import numpy as np
import scipy.linalg as sla
A = np.array([[1,1,1],[4,2,1],[9,3,1]])
y = np.array([[3],[9],[19]])
beta = sla.solve(A,y)
print(beta)
```
```output
[[ 2.00000000e+00]
 [-8.32667268e-16]
 [ 1.00000000e+00]]
```

Thus $a = 2$, $b = 0$, $c = 1$ and the quadratic of best fit is

$$y = 2x^2 + 1$$

Notice that `np.polyfit` yields the same result (within computer precision):

```python
np.polyfit([1,2,3],[3,9,19],2)
```
```output
array([ 2.00000000e+00, -4.09473026e-15,  1.00000000e+00])
```


## 3.5) Transformation matrices

For our purposes a *transformation* of 2- or 3-dimensional space is a rotation, rescaling, shearing, or a combination of these operations.

Perhaps counterintuitively, all transformations can be encoded using matrices. The following example illustrates how they can be studied using Python.


<div class="exercise" markdown=true>


### Exercise 3.5: Transformation matrix worked example 

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/147465/transformation-matrices/embed/?token=22edd273-572a-4342-ac7d-51a65eb31a06" data-id="exercise-3-5" data-cta="Show Exercise"></numbas-embed>

</div>


## 3.6) Eigenvalues and eigenvectors

Given a square matrix $A$, the eigenvalues of $A$ are solutions for $\lambda$ in the equation

$$ A\mathbf{x} = \lambda\mathbf{x} $$

and the eigenvectors of $A$ are solutions for $\mathbf{x}$.

The computation of eigenvalues and eigenvectors is at the heart of a huge amount of mathematics (both pure and applied) and science (across physics, biology, economics, and more).

We can use the `linalg` function `eig` to return an array of eigenvalues and an array of the corresponding eigenvectors. E.g.

```python
import scipy.linalg as sla
import numpy as np

A = np.array([[-4, 14, 16],
              [13,  4,  9],
              [ 3,  4, 18]])

# Solve Ax = lx and unpack into eigenvalues and eigenvectors
eigenvalues, eigenvectors = sla.eig(a)

# Print the eigenvalues
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

There are three eigenvalues, each with a corresponding eigenvector. It is very important to note that the second array should not be treated like a matrix: it is a list of the eigenvectors. That is, each row of `eigenvectors` is a single eigenvector. 

We could use a loop to print the eigenvector associated to each eigenvalue like so:

```python
for i in range(0, len(eigenvalues)):
    print("Eigenvalue: {}, Eigenvector {}".format(eigenvalues[i], eigenvectors[i]))
```
```output
Eigenvalue: (-14.095617972815791+0j), Eigenvector [ 0.8129465  -0.44528258  0.58447437]
Eigenvalue: (6.713752862836402+0j), Eigenvector [-0.58232839 -0.80010959  0.58987692]
Eigenvalue: (25.38186510997938+0j), Eigenvector [-0.00341249  0.40193042  0.55716688]
```

Notice that the eigenvalues are complex numbers, albeit with zero imaginary component as denoted by the `+0j` syntax. We can use the following syntax to simplify the outpud

```python
print(eigenvalues.real)
```
```output
[-14.09561797   6.71375286  25.38186511]
```

<div class="exercise" markdown=true>

### Exercise 3.6

<numbas-embed data-url="https://numbas.mathcentre.ac.uk/question/110254/scipy-eigenvalues/embed/?token=08c11116-2af5-4109-8e47-042445e8b603" data-id="exercise-8-6" data-cta="Show Exercise"></numbas-embed>

</div>

## Next week

Next week:

 * Control flow and alogorithms
 * Root finding

