![PHY2039](/static/images/phy2039-logo.png){style="width: 600px;"}

# Lecture 2 - Good Python Practice

---

## Today

* Finding and fixing bugs
* Inspecting values with `print()`
* Defining a simple function
* Writing scripts and comments

---

## Finding bugs

A **bug** is a mistake in a program. Finding and fixing bugs is a normal part of writing Python.

1. **Predict** the intended result, then **run** the code.
2. **Read** the error, if there is one; **inspect** values with `print()`.
3. **Change one thing**, then **rerun** and check your prediction.

---

## Spot the bug: rectangle area

A rectangle has length 5 and width 3. This program should print its area: **15**.

**Before running:** predict what will happen. Can you spot the bug?

```runnable lang="python"
length = 5
width = 3
area = lenght * width
print(area)
```

---

## Diagnose: rectangle area

```runnable lang="python"
length = 5
width = 3
print(length, width)
area = lenght * width
print(area)
```

---

## What the error tells us

* Read the last line of the error: `NameError` means an undefined name. Compare spellings on the failing line and the assignments.
* Why put the diagnostic print **before** the failing line?
* Edit the correction live, remove the diagnostic print and rerun. Expected: **15**.

---

## Choosing with `if`

* An `if` checks a condition, such as `temperature < 18`: it is either `True` or `False`.
* Its indented lines run only when the condition is `True`.
* An `else` provides an alternative when its condition is `False`.
* A conditional **chooses** what to do; a loop **repeats** instructions.

---

## Spot the bug: thermostat

Print **one** message: `Heating` below 18°C, `Cooling` above 24°C, or `Comfortable` from 18°C to 24°C inclusive.

At 16°C, expect **Heating only**. Predict what happens, then run.

```runnable lang="python"
temperature = 16
if temperature < 18:
    print('Heating')
if temperature > 24:
    print('Cooling')
else:
    print('Comfortable')
```

---

## Diagnose: thermostat

Inspect both conditions, then follow the branches.

```runnable lang="python"
temperature = 16
print('Below 18:', temperature < 18)
print('Above 24:', temperature > 24)
if temperature < 18:
    print('Heating')
if temperature > 24:
    print('Cooling')
else:
    print('Comfortable')
```

---

## Which `if` owns the `else`?

* At 16°C, the first condition is `True`; the second is `False`. Which messages appear?
* The `else` belongs to the **second** `if`. The two `if` statements make separate decisions.
* Use `elif` ("else if") to link the second condition to the first. It is checked only if the first condition was false.
* Edit live and remove the diagnostic prints. Test 16, 21 and 26°C: expect `Heating`, `Comfortable` and `Cooling`, respectively.
* Also test the boundaries: 18 and 24°C should both print `Comfortable`, once.

---

## Repeating with `for`

* `for distance in [2, 3, 4]:` takes each distance in turn: 2, then 3, then 4 metres.
* The indented lines repeat for each distance; an unindented line after the loop runs when it finishes.
* `total = total + distance` adds the current distance to the running total.
* The running total must retain the distances already added.

---

## Spot the bug: total distance

Add three distances: 2, 3 and 4 metres. Print **9 once**, after the loop.

Predict the output, then run. Which lines repeat?

```runnable lang="python"
for distance in [2, 3, 4]:
    total = 0
    total = total + distance
print(total)
```

---

## Diagnose: total distance

Inspect the running total after each addition.

```runnable lang="python"
for distance in [2, 3, 4]:
    total = 0
    total = total + distance
    print('distance:', distance, 'total:', total)
print(total)
```

---

## What should run only once?

* The diagnostic totals are **2, 3, 4**. We expected **2, 5, 9**. Where is the earlier distance lost?
* Which statement resets the total? Should it run before every addition, or just once before the loop?
* Move the initialisation to run once before the loop. Check the indentation of the lines that should still repeat.
* Remove the diagnostic print and rerun the whole block. Expected: **9**, once.

---

## Debugging habits

* An error message is **evidence**: use it to locate the problem.
* Code that runs can still be wrong: compare with an expected result.
* Rerun the **whole block**, including its starting assignments, after a correction.

---

## Printing variables

Print intermediate values to check what your code is doing. Arrays can be inspected too.

```runnable lang="python"
import numpy as np
arr = np.linspace(-5.0, 5.0, 5)
print(arr)
```

---

## Check the printed values

```text
[-5.  -2.5  0.   2.5  5. ]
```

Does the output match the values you expected?

---

## Defining Python functions

`x` and `y` are inputs; `return` sends the result back to the caller.

Predict the output before running:

```runnable lang="python"
def my_function(x, y):
    return x**2 + y**2

print(my_function(2, 3))
```

---

## Scripts

From here on we'll be writing longer and more complicated code. I recommend that you use *scripts* from this point on.

* Scripts are text files containing code. They can be saved for ease of editing and reuse. 

* They have the extension **.py**.

* It is good practice to *comment* your scripts.

---

### Components of a script

A **module docstring** at the start describes the script. Use `#` for comments.

```python
"""A short description of what this script does."""

# Set the starting value
x = 2  # Comments can also go at the end of a line
```

---

### Commenting

View:  <button onclick="showCode()">Comments and code</button> <button onclick="hideCode()">Comments only</button> 

<div id="content1" style="font-size: 0.8em; margin-top:-10px;" markdown=true>

```python
""" 
Script to calculate pi using Madhava's approximation
"""
import numpy as np

# Set up an array of k values
k = np.arange(21)

# pk array containing series contributions for each k
pk = 1/((2*k+1)*(-3)**k)

# Find the pi approximation, using the sum of pk
pi_approx = np.sqrt(12)*sum(pk)
```

</div>
<div id="content2" style="display: none; font-size: 0.8em; margin-top:-10px;"  markdown=true>

```python
""" 
Script to calculate pi using Madhava's approximation
"""

# Set up an array of k values


# pk array containing series contributions for each k


# Find the pi approximation, using the sum of pk

```

</div>


<script>
    function hideCode() {
        document.getElementById('content1').style.display = 'none';
        document.getElementById('content2').style.display = 'block';
    }
    function showCode() {
        document.getElementById('content1').style.display = 'block';
        document.getElementById('content2').style.display = 'none';
    }    
    
</script>

---

### Suggestions for scripts

* Organise your code in folders e.g. Top-level folder *Stage 2 Python*, then subfolders for each week.
* Consider using your Newcastle University Onedrive to ensure your scripts are backed up.
* Comment your code: even quick shorthand comments are better than nothing.

---

## Good Python habits

* Inspect values with `print()` when something is unclear.
* Test your code against an expected output.
* Put reusable calculations in functions.
* Save readable scripts and explain their purpose with comments.
