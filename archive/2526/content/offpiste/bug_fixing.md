##  Bug Lecture Demo

This script is meant to extract the first column of a 2D numpy array A
and double its values.

However, it contains a bug and does not given the expected result.

In the lecture I will show how to use print() statements to debug and fix this code.

**Intended behaviour**.

A is:

    [[1 1 1]
    [2 2 2]
    [3 3 3]]

The first column is: 

    [[1].
     [2], 
     [3]].

Doubling it inside A gives the array:

    [[2 1 1]
    [4 2 2]
    [6 3 3]]


```runnable lang="python"
import numpy as np

A = np.array([[1,1,1],
              [2,2,2],
              [3,3,3]])

A[0, :] = 2 * A[0, :]

expected = np.array([[2,1,1],
                     [4,2,2],
                     [6,3,3]])

assert np.array_equal(A, expected), "Column extraction is incorrect!"
```


##  Bug 1

This script creates two 1D numpy arrays, and computes:

    1) Their sum.
    2) It then tries to perform a matrix multiplicaiton, assuming one is 3 x 1 and the other is 1 x 3, but it fails.

The goal is to get a 3 x 3 matrix as the result of the matrix multiplication.

**Intended behaviour**

A and B are both 1D arrays of shape (3,) with all elements equal to 1:

    A = [1, 1, 1]
    B = [1, 1, 1]

The sum C_sum = A + B is:

    C_sum = [2, 2, 2]

If A is a 3 x 1 matrix, and B is a 1 x 3 matrix, their matrix multiplication should be a 3x3 matrix with all elements equal to 1:

    C = [[1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]]

However, the code below does not produce the expected 3 x 3 matrix.

What do you need to do with the shapes of C to make it output a 3 x 3 matrix?

**Task:**

Use print statements, in particular printing the shape of the numpy arrays, to identify and fix the bug(s) in the code.

Here is how you print the shape of a numpy array:

    print(A.shape)
    print(B.shape)

```runnable lang="python"
import numpy as np

A = np.ones(3)
B = np.ones(3)

C_sum = A + B

expected_sum = np.array([2,2,2])

assert np.array_equal(C_sum, expected_sum), "Sum is Incorrect!"

C = np.matmul(A, B)

expected = np.array([[1,1,1],
                     [1,1,1],
                     [1,1,1]]
                    )

assert np.array_equal(C, expected), "Matrix Multiplication Incorrect!"
```

##  Bug 2

This script demonstrates basic NumPy array operations and the use of for loops
to manipulate specific rows of a matrix.

It is intended to:

    1. Create two matrices, A (3×3) and B (3×2), and prepare an empty 3×2 result matrix.
    2. Add the square of the first row of A to the first row of the result matrix.
    3. Double the values in the second row of the result matrix using a for loop.

**Bug**

The code below when run gives the error:

    File "bug_fix_1.py", line 29, in <module>
    sum_matrix[0, i] += A[0, i]**2
    ~~~~~~~~~~^^^^^^

    IndexError: index 2 is out of bounds for axis 1 with size 2

**Task**

Use print statements to diagnose the bug and fix the code.

In particular, print the shape of a numpy array to absolutely confirm why the bug occurs. An example of
printing the shape of numpy arrays was used in the previous example.

Reading the error message above is particularly helpful, as it directly points to where the code breaks.

**Description of the bug**

Lets break down what an IndexError is telling us here:

    Traceback (most recent call last):
        File "/mnt/c/Users/Jammy/Code/PHY2039/bug_fix_1.py", line 50, in <module>
            sum_matrix[0, i] += A[0, i]**2
            ~~~~~~~~~~^^^^^^
    IndexError: index 2 is out of bounds for axis 1 with size 2

This is telling us that for the numpy array `sum_matrix`, we are: 

    - Trying to access to its first axis (axis 1, where the input is the `i` in [0, i]) 
    - Trying to access index 2 of axis 1 (e.g the value of `i` is 2).
    - But axis 1 only has size 2 (meaning the only valid indices are 0 and 1).

An equivalent way to produce this bug would be simply to run:

    import numpy as np
    sum_matrix = np.zeros((3,2)) # Second axis has size 2
    print(A[0,2])  # This will give the same IndexError, because 2 is out of bounds for axis 1 with size 2

```runnable lang="python"
import numpy as np

# Step 1: Create a 3x3 array
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Shape of A:", A.shape)  # Debug print to check the shape of A

# Step 2: Define another array
B = np.array([[9, 8],
              [6, 5],
              [3, 2]])

# Step 3: Initialize a summed matrix with zeros
sum_matrix = np.zeros((3,2))

# Step 4: Add the square of the first row of A to the summed matrix
for i in range(3):
    sum_matrix[0, i] += A[0, i]**2

# Step 4: Add the second row of the summed matrix to itself
for i in range(3):
    sum_matrix[1, i] += sum_matrix[1, i]

# Step 5: Validate the result
assert (sum_matrix == np.array([[1, 4],
                               [0, 0],
                               [0, 0]])).all()
```

##  Bug 3

This script attempts to solve the ODE

    dy/dt = -2y + sin(t),      y(0) = 0

using the forward Euler method.

**Intended behaviour**

The code should:

    1. Create a time array t of length 10 (0 to 1 in steps of 0.1).
    2. Use Euler's formula: y[n+1] = y[n] + h * f(y[n], t[n])
    3. Return all values of y.

**Bug**

The loop runs correctly for the first few iterations, but then crashes with:

    IndexError: index 10 is out of bounds for axis 0 with size 10

Your job is to use print() statements to diagnose why the code crashes, and then fix the bug so that the code runs
successfully to completion.

Think carefully about what this IndexError means given what we learned in the previous bug.

```runnable lang="python"
import numpy as np

# Step 1: ODE function
def f(y, t):
    return -2*y + np.sin(t)

# Step 2: Time array and initialization
t = np.linspace(0, 1, 10)
h = t[1] - t[0]

y = np.zeros(10)

# Step 3: Euler loop
for n in range(len(t)):
    y[n+1] = y[n] + h * f(y[n], t[n])

print("Success! All iterations completed.")

assert np.round(y[-1], 8) == 0.25141333

print("Success! Final assertion passed.")
```