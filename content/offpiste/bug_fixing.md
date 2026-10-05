# Bug Fixing (Advanced)

This workshop is for later in the course, after you have used NumPy arrays,
indexing, array shapes, matrix multiplication and `for` loops. The final
exercise also assumes familiarity with the forward Euler method for solving
ordinary differential equations. For an introduction using simple variables
and arithmetic, start with **Bug Fixing (Beginner)** in the course contents.

The lecture demonstration and the three exercises below contain deliberate bugs.
Each runnable block is a separate program: an assertion failure or an
`IndexError` on the first run is expected.

Read the intended result before changing the code. Use `print()` statements to
inspect array values, shapes and loop indices immediately before the line that
fails. After each change, rerun the whole block from its initial state so that
previous changes to arrays do not affect your diagnosis.

Fix the code that produces the result. Do not remove the assertions or change
the expected values to make the checks pass. An assertion checks that a condition
is true; if it is false, Python stops with an `AssertionError` and the supplied
message.

## Bug lecture demo: rows and columns

This program should double the first column of a two-dimensional NumPy array
`A` in place, leaving the other columns unchanged. In the lecture, we will use
`print()` statements to diagnose why it changes the wrong entries.

Initially, `A` is:

```text
[[1 1 1]
 [2 2 2]
 [3 3 3]]
```

The first column, selected by `A[:, 0]`, is the one-dimensional array
`[1, 2, 3]` with shape `(3,)`. Selecting a column this way does not produce a
two-dimensional array of shape `(3, 1)`.

After doubling that column, `A` should be:

```text
[[2 1 1]
 [4 2 2]
 [6 3 3]]
```

Which entries does `A[0, :]` select? Print the selection and the updated array
to check your prediction.

```runnable lang="python"
import numpy as np

A = np.array([[1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])

A[0, :] = 2 * A[0, :]

expected = np.array([[2, 1, 1],
                     [4, 2, 2],
                     [6, 3, 3]])

assert np.array_equal(A, expected), "Double only the first column of A."
print("Success! Only the first column was doubled.")
```

## Bug 1: array shapes and matrix multiplication

This program first adds two one-dimensional arrays `A` and `B`, each with shape
`(3,)` and values `[1, 1, 1]`. Their sum, `C_sum`, should remain a
one-dimensional array `[2, 2, 2]` with shape `(3,)`.

After calculating and checking the sum, the program should treat `A` as a
column with shape `(3, 1)` and `B` as a row with shape `(1, 3)`. Multiplying
these two-dimensional arrays should produce a matrix `C` with shape `(3, 3)`:

```text
[[1 1 1]
 [1 1 1]
 [1 1 1]]
```

The current call to `np.matmul(A, B)` succeeds, but with two one-dimensional
inputs it computes their dot product: the scalar `3.0`, whose shape is `()`.
The assertion then fails because this is not the intended matrix.

**Task:** Use print statements to inspect `A.shape`, `B.shape`, `C` and
`C.shape`. Change the shapes of the operands **after** the sum check and
**before** the multiplication. Do not try to reshape the scalar result `C`.

```runnable lang="python"
import numpy as np

A = np.ones(3)
B = np.ones(3)

C_sum = A + B
expected_sum = np.array([2, 2, 2])

assert np.array_equal(C_sum, expected_sum), "The sum must be [2, 2, 2] with shape (3,)."

C = np.matmul(A, B)

expected = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])

assert np.array_equal(C, expected), "The matrix product must be a 3 x 3 array of ones."
print("Success! The sum and matrix product are correct.")
```

## Bug 2: loop bounds and array axes

This program should square the **first two entries** of the first row of `A`
and put them in the first row of a result array, `sum_matrix`, with shape
`(3, 2)`. The other two rows of the result should remain zero:

```text
[[1 4]
 [0 0]
 [0 0]]
```

On its first run, the program stops with:

```text
IndexError: index 2 is out of bounds for axis 1 with size 2
```

For a two-dimensional array, axis 0 is the first axis (rows) and axis 1 is the
second axis (columns). In `sum_matrix[0, i]`, `0` selects the first row and
`i` selects a column. There are two columns, so the valid column indices are
`0` and `1`. Index `2` would select a third column, which does not exist.

This short example produces the same error independently:

```python
import numpy as np

sum_matrix = np.zeros((3, 2))
print(sum_matrix[0, 2])  # No third column: this raises IndexError.
```

**Task:** Print `A.shape`, `sum_matrix.shape` and the value of `i` immediately
before the assignment inside the loop. Why is `i = 2` valid for `A` but invalid
for `sum_matrix`? Fix the loop so its bound comes from the **number of columns
in the result array**, rather than a hard-coded number. Keep the result shape
`(3, 2)` and leave its other rows zero.

```runnable lang="python"
import numpy as np

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

sum_matrix = np.zeros((3, 2))

# Fill the first row using the corresponding squared entries of A.
for i in range(3):
    sum_matrix[0, i] += A[0, i]**2

expected = np.array([[1, 4],
                     [0, 0],
                     [0, 0]])

assert np.array_equal(sum_matrix, expected), "The first row must be [1, 4]; the other rows must stay zero."
print("Success! The result has the intended values and shape.")
```

## Bug 3: time samples and Euler steps

This program approximates the solution of the ordinary differential equation

```text
dy/dt = -2y + sin(t),      y(0) = 0
```

using the forward Euler method:

```text
y[n + 1] = y[n] + h * f(y[n], t[n])
```

The time array `np.linspace(0, 1, 10)` contains **10 sample times**, including
both endpoints `0` and `1`. There are **9 intervals** between them, so the step
size is `h = 1/9`, approximately `0.111111`, not `0.1`.

The array `y` stores one value per time sample. Its first entry holds the
initial value `y[0] = 0`; nine Euler updates should fill its remaining entries.
The final entry should be approximately `0.25141332912489534`. This is the
forward Euler approximation on this particular time grid, not the exact
solution of the differential equation at `t = 1`.

The current loop attempts one update too many and stops with:

```text
IndexError: index 10 is out of bounds for axis 0 with size 10
```

**Task:** Print `len(t)`, `len(y)` and `h`, then print `n` and `n + 1`
immediately before the update inside the loop. What is the largest valid
index in `y`? What is the largest value of `n` for which both `y[n]` and
`y[n + 1]` exist? Use these answers to fix the loop bound. Keep the time grid,
initial condition and Euler update unchanged.

The final check uses a small absolute tolerance because the result is a
floating-point calculation.

```runnable lang="python"
import numpy as np


def f(y, t):
    return -2 * y + np.sin(t)


t = np.linspace(0, 1, 10)
h = t[1] - t[0]
y = np.zeros(10)

for n in range(len(t)):
    y[n + 1] = y[n] + h * f(y[n], t[n])

assert y.shape == t.shape, "Store one y value for each time sample."
assert y[0] == 0, "Keep the initial condition y(0) = 0."
assert np.isclose(y[-1], 0.25141332912489534, rtol=0, atol=1e-8), "The final value does not match the Euler approximation on this grid."

print("Success! All Euler checks passed.")
print("Euler approximation at t = 1:", y[-1])
```
