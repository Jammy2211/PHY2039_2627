### Matrices in `numpy`

From a programming point of view, a matrix is a two-dimensional array, and can also be set up using the *numpy* `array` function. The syntax is as follows

```python
A = np.array([[2,1,3],[2,3,3],[1,2,0]])
```

As for lists, the *numpy* array class of objects has methods. You can view these for our object `A` with

```python
dir(A)
```

The shape of a *numpy* array can be queried with the shape method

```python
A.shape
```

The methods for a numpy array include some common tasks used when working with matrices, for example

```python
A.transpose()
```

*numpy* also has functions which operate on matrices, such as `np.linalg.inv()`, to calculate the inverse of a matrix.

```python
np.linalg.inv(A)
```

The function `np.linalg.solve(A,b)` solves an equation in the matrix form $Ax=b$ for matrix $A$ and column vector $b$. For example, let's solve the system of linear equations

$$ 
x +  y + z = 6 \\
2y + 5z = -4   \\
2x + 5y - z = 27   \\
$$

We'll write the system in the form

$$ Ax = b $$

$$
\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 3 \\ 2 & 5 & -1 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ z\end{pmatrix} = \begin{pmatrix} 6 \\ -4 \\ 27\end{pmatrix}
$$

and create `A` and `b` in Python using *numpy*

```python
A = np.array([[1,1,1],[0,2,3],[2,5,-1]])
```
```python
b = np.array([[6],[0],[27]])
```

Then $x$ is then given by

```python
x = np.linalg.solve(A,b) 
print(x)
```
```output
array([[ 5.],
       [ 3.],
       [-2.]])
```

A matrix element can be accessed as `A[i][j]` where `i` is the row index and `j` the column index

```python
A[1][2]
```
```output
5
```

Or alternatively

```python
A[1,2]
```
```output
5
```

A colon on its own acts as a 'wilcard', so this returns the first column (remember the first column has index 0),

```python
A[:,0]
```
```output
array([1, 0, 2])
```
 
Read this as "show me the any row and the first column". Similarly,

```python
A[0,:]
```
```output
array([1, 1, 1])
```

gives the "first row and any column".


### Exercise 1.7 {: .exercise}

Create the matrix 

$$
\begin{pmatrix} 1 & 2 & 3 & 4 & 5  \\ 6 & 7 & 8 & 9 & 10 \\ 11 & 12 & 13 & 14 & 15 \end{pmatrix}
$$

There are three levels of sophistication here:

* Create the matrix entering individual elements.
* Create the matrix from the 3 sequences. You'll need the *numpy* functions `arange()` and `column_stack()` (see `help(np.column_stack)`)
* Create the matrix from 1 sequence. Take a look at help(np.reshape).

