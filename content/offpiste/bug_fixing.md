# Bug Fixing (Advanced)

This workshop is for later in the course, after you have used NumPy arrays,
indexing, array shapes, matrix multiplication and `for` loops. Bug 3
also assumes familiarity with the forward Euler method for solving ordinary
differential equations, and Bugs 4 and 5 use the trapezoid rule and the
central difference method from Week 7. For an introduction using simple
variables and arithmetic, start with **Bug Fixing (Beginner)** in the course
contents.

The lecture demonstration and the five exercises below contain deliberate bugs.
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

## Bug 4: distance travelled with the trapezoid rule

This exercise is longer than the others. It contains a single bug.

A particle moves along a line with velocity `v(t) = sin(t)` in m/s. The
distance it travels between `t = 0` and `t = pi` seconds is the area under
`v(t)`, which we can calculate exactly:

$$ \int_0^{\pi} \sin t \,\mathrm{d}t = \Big[-\cos t\Big]_0^{\pi} = -\cos\pi + \cos 0 = 2 \text{ m} $$

The program below estimates this integral with its own trapezoid rule, using
5, 9, 17, 33 and 65 equally spaced points, and prints each estimate and its
error. The trapezoid rule is an approximation, so we do not expect exactly
`2` m. But the answers are wrong by more than the trapezoid rule alone
explains, and with 65 points the final check fails:

```text
AssertionError: The estimate with 65 points is not accurate enough.
```

There is no error message pointing at a line this time. The program runs and
produces believable numbers, so you must decide whether the error is just the
approximation or a bug.

**Task:** Run the whole block and read the output carefully before changing
anything. Find the bug and fix the calculation. Do not change the exact answer,
the velocity function or the final check.

```runnable lang="python"
import numpy as np


# The velocity of the particle, in m/s
def velocity(t):
    return np.sin(t)


# Our own trapezoid rule
def trapezoid_rule(f, a, b, n_points):
    """Estimate the integral of f from a to b using n_points equally
    spaced points (including both ends)."""
    t = np.linspace(a, b, n_points)
    h = (b - a) / n_points

    area = 0.0
    for i in range(n_points - 1):
        # area of one trapezoid: width x average height
        area += h * (f(t[i]) + f(t[i + 1])) / 2

    return area


# Compare with the exact answer, using more and more points
a = 0
b = np.pi
exact = 2.0   # exact answer from maths: [-cos(t)] from 0 to pi = 2
print(f"Exact answer from maths: distance = {exact:.6f} m")
print()
print("points   numerical   exact (maths)   error = |numerical - exact|")

for n_points in [5, 9, 17, 33, 65]:
    distance = trapezoid_rule(velocity, a, b, n_points)
    error = abs(distance - exact)
    print(f"{n_points:4d}     {distance:.6f}    {exact:.6f}        {error:.2e} m")

# With 65 points, a correct trapezoid rule is accurate to better than 1 mm.
assert error < 1e-3, "The estimate with 65 points is not accurate enough."
print("Success! The trapezoid rule agrees with the exact answer.")
```

**Hints** (try without them first):

1. *Is it a bug, or just the approximation?* Each time the number of points
   doubles, the step `h` halves. The trapezoid rule's error is
   $\mathcal{O}(h^2)$, so the error should become about 4 times smaller each
   time. Divide each error by the next one. What do you get?
2. Inside `trapezoid_rule`, print `t`, `h` and `t[1] - t[0]`. Should they agree?
3. Compare your function with SciPy on the same points. Both use the same
   method, so they should agree to many decimal places:

```python
from scipy.integrate import trapezoid

t = np.linspace(a, b, 5)
print(trapezoid(velocity(t), t), trapezoid_rule(velocity, a, b, 5))
```

## Bug 5: velocity from position with the central difference

This exercise is also longer than the first three. It contains a single bug.

A mass on a spring oscillates with position `x(t) = sin(t)` in m. Its velocity
is the derivative of the position, which we can calculate exactly:

$$ v(t) = \frac{\mathrm{d}x}{\mathrm{d}t} = \cos t, \qquad v(1) = \cos 1 = 0.540302\ldots \text{ m/s} $$

The central difference method estimates the slope at `t` from the straight
line through the two points either side of it, a distance `h` away:

$$ \frac{\mathrm{d}x}{\mathrm{d}t} \approx \frac{x(t+h)-x(t-h)}{2h} = \frac{\text{rise}}{\text{run}} $$

The program below estimates the velocity at `t = 1` s with its own central
difference, using smaller and smaller steps `h`, and prints each estimate and
its error. The method is an approximation, so we do not expect the exact
answer. But the answers are wrong by more than the method alone explains, and
the final check fails:

```text
AssertionError: The estimate with the smallest h is not accurate enough.
```

**Task:** Run the whole block and read the output carefully before changing
anything. Find the bug and fix the calculation. Do not change the exact answer,
the position function or the final check.

```runnable lang="python"
import numpy as np


# ---------------------------------------------------------------------------
# The position of the mass, in m
# ---------------------------------------------------------------------------
def position(t):
    return np.sin(t)


# ---------------------------------------------------------------------------
# Our own central difference method
# ---------------------------------------------------------------------------
def central_difference(f, t, h):
    """Estimate the derivative of f at time t, using the two points
    t - h and t + h either side of it."""
    rise = f(t + h) - f(t - h)
    derivative = rise / 2*h

    return derivative


# ---------------------------------------------------------------------------
# Compare with the exact answer, using smaller and smaller steps
# ---------------------------------------------------------------------------
t = 1.0
exact = np.cos(t)   # the exact answer from maths: d/dt sin(t) = cos(t)
print(f"Exact answer from maths: v(1) = cos(1) = {exact:.8f} m/s")
print()
print("h          numerical     exact (maths)   error = |numerical - exact|")

for h in [0.1, 0.05, 0.025, 0.0125, 0.00625]:
    velocity = central_difference(position, t, h)
    error = abs(velocity - exact)
    print(f"{h:<9}  {velocity:.8f}    {exact:.8f}      {error:.2e} m/s")

# With h = 0.00625, a correct central difference is accurate to better than 1e-5 m/s.
assert error < 1e-5, "The estimate with the smallest h is not accurate enough."
print("Success! The central difference agrees with the exact answer.")
```

**Hints** (try without them first):

1. *Is it a bug, or just the approximation?* The central difference error is
   $\mathcal{O}(h^2)$: each time `h` halves, the error should become about
   4 times smaller. What does the error do here as `h` gets smaller?
2. Inside `central_difference`, print `rise`, `h` and `derivative` for one
   value of `h`. Work out by hand what $\text{rise} / 2h$ should be. Does it
   match?
3. For three evenly spaced points, the middle value from `np.gradient` is the
   central difference, so it should agree with your function to many decimal
   places:

```python
h = 0.1
times = np.array([t - h, t, t + h])
print(np.gradient(position(times), times)[1], central_difference(position, t, h))
```
