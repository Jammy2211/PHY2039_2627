
![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 3 - Linear algebra

---

## Reminder

Assessment 1 is open. See the page on the Canvas course *Preparing for Assessment 1*, and Exercise 2.7 from the Week 2 Handout.

Deadline: 16:00 on the 17th of October.

Questions: during practical, via email.

Office hours: email to make an appointment, or just see if I'm in (Herschel 2.12, door has "Dr Colin Woods" written on it currently).

---

## Python functions

Used functions with SciPy `curve_fit`. However, they are much more flexible than we saw in this context

```runnable lang="python"
def cube_and_add(x,y):
    return x**3 + y**3

print(cube_and_add(2,3))
```

---

## Linear algebra: motivation

We used `polyfit` without thinking deeply about how it works. To fit a quadratic to the data
```python
x = [1,2,3]
y = [5,8,10]
```

`polyfit` solves the system of equations

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
5 \\
8 \\
10
\end{pmatrix}
$$

where the fitting parameters are $a$,$b$, $c$.

---

In weeks to come we'll see further examples of systems that can be converted into linear algebra. E.g.

\begin{align}
\frac{\mathrm{d}x}{\mathrm{d}t} &=\alpha x-\beta xy, \\[0.7em] 
\frac{\mathrm{d}y}{\mathrm{d}t} &=\delta xy-\gamma y
\end{align}

is equivalent to

$$ \frac{\mathrm{d}}{\mathrm{d}t} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} \alpha  & - \beta x \\ \delta y & -\gamma \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$


---

Eigenvalue problems are ubiquitious across science:

* Principal axes of rotating object $\mathbf{L} = I \mathbf{\omega}$
* Time-independent Schrödinger equation $\mathbf{\hat{H}}\mathbf{\psi} = E\mathbf{\psi}$
* ...

It's extremely useful to be able to solve them using Python.

---

## Vectors in Python


$$ 
\mathbf{v} = \begin{pmatrix} 1  & 2  & 3 \end{pmatrix}
$$

NumPy arrays allow us to easily work with (row) vectors

```python
np.array([1, 2, 3])
```

We can use **matrices** to work with column vectors when necessary.

---

There are many array operations available out of the box e.g. `a*b`, `np.dot(a,b)`, `np.cross(a,b)`

```runnable lang="python"
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
```

---

## Matrices in Python

$$ 
A = \begin{pmatrix} 1 & 2 \\ 2 & 3 \\ 3 & 4 \end{pmatrix}
$$


```runnable lang="python"
import numpy as np
A = np.array([[1, 2],
              [2, 3],
              [3, 4]])

# element in i-th row, j-th column is A[i,j]
print(A[1, 1])
```

---

As before, there are many useful operations available e.g. `A*B`, `A@B`

```runnable lang="python"
import numpy as np
A = np.array([[1, 2],
              [2, 3],
              [3, 4]])
B = np.array([[4, 5],
              [5, 6],
              [6, 7]])
```


---


## Column vectors


$$ 
\vec{v} = \begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}
$$

We can construct a column vector in Python as an $(n,1)$ matrix:

```python
np.array([[1], 
          [2], 
          [3]])
```

(It turns out that we don't often need column vectors explicitly.)

---

## Example: working with arrays

Consider a matrix $A$ and an element $A_{ij}$ that does not lie along an edge.

$$ 
A = \begin{pmatrix} 1 & 2 & 3 & 4 & 5 \\ 6 & 7 & 8 & 9 & 10 \\ 11 & 12 & 13 & 14 & 15 \\ 16 & 17 & 18 & 19 & 20 \end{pmatrix}
$$

How can we return a $(3,3)$ matrix with $A_{ij}$ at its centre?

---

```runnable lang="python"
import numpy as np

# Create the matrix
A = np.arange(1,21).reshape(4,5)

i = 1 
j = 1
Aij = A[i-1:i+2,j-1:j+2]

# Print centre and surround
print(A[i,j])
print(Aij)
```

---

As a function:

```runnable lang="python"
import numpy as np

def surround(A,i,j):
    return A[i-1:i+2,j-1:j+2]

A = np.arange(1,21).reshape(4,5)

i = 2
j = 3

print(A[i,j])
print(surround(A,i,j))
```

---

## Scipy `linalg`

This package gives us access to matrix operations such as determinant and inverse

```runnable lang="python"
import numpy as np
import scipy.linalg as sla
A = np.array([[1, 0, 3],
              [2, 1, 1],
              [1, 0, 1]])
```

---

`linalg` can be used to solve systems of linear equations. To solve $\mathbf{A} \mathbf{x} = \mathbf{b}$ we invoke `sla.solve(A, b)`.

$$
\begin{matrix}
x + 2y = 5 \\
2x + y = 7
\end{matrix} \quad \rightarrow \quad
\begin{pmatrix}
1 & 2 \\ 2 & 1
\end{pmatrix}
\begin{pmatrix}
x \\ y
\end{pmatrix}
=
\begin{pmatrix}
5 \\ 7
\end{pmatrix}
$$

---

`linalg` can also be used to compute eigenvalues and eigenvectors. Recall that eigenvalues are solutions for $\lambda$ in

$$ \mathbf{A}\mathbf{x} = \lambda\mathbf{x} $$

while eigenvectors are solutions for $\mathbf{x}$.

The function `sla.eig(A)` returns an array containing the eigenvalues and eigenvectors of $A$ e.g.

```python
eigenvalues, eigenvectors = sla.eig(A)
```

---

## Example: 2D rotation
The following matrix describes rotation by $\theta$ in the $(x,y)$-plane:

$$ R=\begin{pmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{pmatrix} $$

Specifically, the rotated vector $(x',y')$ is given by

$$ \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix}\cos \theta &-\sin \theta \\\sin \theta &\cos \theta \end{pmatrix}\begin{pmatrix} x \\ y \end{pmatrix} $$

---

```python
import numpy as np
import scipy.linalg as sla

# Rotate by
theta = np.pi/2

# rotation matrix
R = np.array([[np.cos(theta), -np.sin(theta)],
             [np.sin(theta), np.cos(theta)]])

# Construct x and xdash
x = np.array([[1],
              [0]])
xdash = R @ x
```

---

![The Herschel Cluster](/static/images/intro/cluster.jpg){width="60%"}

The material sketched in this lecture is covered in greater detail in Handout 3.

