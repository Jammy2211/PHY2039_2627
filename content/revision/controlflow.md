[Click here to open this handout in a new browser tab](#){target="_blank"}

# Control Flow

Before we get on to control flow there are a couple of topics to upskill in first: using the `print()` function and a reminder of logical operators.


## The print function

We're going to be using a bit more of the `print` function today in our scripts, to help us to see what's happening in our code.

Recall that `print()` can be used with a value (of any type) inserted directly

```python
print(5)
print("Hello")
```

It can also print more than one thing at once:

```python
print("Hello", "World")
```

It can be used to print a variable

```python
x = [1,5,7]
print(x)
```

But what if we want the output to be something like this, where the 5 is a variable?

```python
The value is 5
```

this is going to be a string with a variable value injected into it. The way this is done is as follows:

```python
a = 5
print("The value is {}".format(a))
``` 

`{}` is a placeholder for the variable that is specified inside `format()`. If we need to insert more than one variable then we can add them, comma-separated, inside `format()` as follows

```python
a = 5
b = 6
print("The values are {} and {}".format(a,b))
```

The placeholders can be labelled so that a variable can be inserted twice in the same string:

```python
a = 5
b = 6
print("The values are {0} and {1}. Here's the first one again...{0}".format(a,b))
```


Things start to get a little complicated if you want to specify the format of the values you are inserting. Here's an example which prints $\pi$ and $e$ to 2 decimal places:

```python
import numpy as np
print("Some stuff to 2 decimal places... pi = {:.2f} and e = {:.2f}".format(np.pi,np.e))
# or including the labels 
print("Some stuff to 2 decimal places... pi = {0:.2f} and e = {1:.2f}".format(np.pi,np.e))

```
 
In `{0:.2f}`, the `0` is the label (so `np.pi` is inserted here), the `:` separates the label from the format specification, `.2` is for 2 decimal places and `f` is for float.

We could spend all day talking about string formatting, and at this stage it will be easier to look up what you want to do when you get to it; here's a [guide](https://docs.python.org/3.4/library/string.html#string-formatting){target="_blank"} for reference and or keen beans.


## Logical operators

Recall from handout 1 that we use logical operators to determine whether a statement is true or false

```python
x == 2
x > 2
```

Others which can be used to make up such an expression are as follows:

**Operator**   |    **Description** 
---------------|-------------------------------
<              |    Less than 
>              |    Greater than 
<=             |    Less than or equal to 
>=             |    Greater than or equal to 
==             |    Equal to 
!=             |     Not equal to
a and b        |      is a AND b 
a or b         |     is a OR b 

Here are some more examples

```python
a = 3
print(a <= 3)        # True
print(a < 5 or a > 25)   # True
print(a < 5 and a > 25)  # False
print(a % 2 == 0)  # False (is the remainder when divided by 2 zero - in other words is a even)
```

These will form an important part of the next section on control flow.

## Control Flow

This section introduces loops and if statements, part of a family of tools used by programmers and referred to generically as control flow.


### For Loops

A 'for loop' is used when we would like to repeat a piece of code many times, usually incrementing a value so that something slightly different happens at each iteration. 

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=87f6568b-c449-4ffa-8561-ada000d4f5ce&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

The basic construction of a for loop is as follows:

```python
for n in range(1,6):
    # do something with n
```

Notice the syntax, importantly the colon at the end of the `for` line, and the indentation. It doesn't really matter what the indentation is, a tab or some spaces - a Python enthusiast will tell you that 4 spaces is best - the important thing is that you are consistent!

Go on try it without...

```python
for n in range(1,6):
# do something with n
```
Yep, you get an error!

The comment labelled "do something with n" indicates exactly that, usually you would do something with the current value of $n$. The loop, in this case, runs 5 times, the first time $n=1$, then $n=2$ and so on until $n=5$, and then it stops. 


So here my choice of "doing something" is to print the value of $n^2$:

```python
for n in range(1,6):
	print(n**2)
```

We could get fancy and print some text alongside the value:

```python
for n in range(1,6):
    print("The value squared is {}".format(n**2))
```

The `range(1,6)` could be any list, so we can do this, for example

```python
for n in [4,1,5,6]:
    print(n)
```
Or even other data types,

```python
bears = ["koala", "panda", "sun"]
for x in bears:
	print(x)
```

The loop could do pretty much anything with `n`. For example here I add the values of n by initialising a variable s, and then adding n to it at each step of the loop:

```python
# Intitialise a variable
s = 0

# Loop through adding n each time
for n in range(1,6):
    s += n

# print final value
print(s)
```

Notice that the line break and subsequent unindent marks the end of the for loop contents.

The `s += n` adds `n` to the current `s` value and is equivalent to `s = s + n`. 

`+=` is known as an assignment operator, and there are others such as `*=` e.g. `s *= n` equivalent to `s = s * n`.


### While Loops

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=4f60e7c9-6693-4981-b102-ada000d4f442&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

Loops aren't always faster, but can offer a lot of flexibility. For example a `while` loop can run whilst a certain condition is satisfied, e.g.

```python
s = 0   # some value we'll add to
n = 0   # this is my counter

while s < 1000:
   n += 1    # increment the counter
   s += n    # add to s  

# Output the results
print("s is equal to {}".format(s))
```

Here, the `s < 1000` is a logical expression, it returns either true or false, and so the while loop can be read "while s < 1000 is true". Note that you might expect the final value of `s` to be less than 1000. Have a read through the code logic to convince yourself that it is sensible that its value should be greater than 1000.

Note that it's easy to get stuck in an infinite while loop, if the condition that is set happens to never be satisfied. If this happens to you then the stop button in the Console, or CTRL-C will stop your code!


### If statements

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=b6f9035c-95cf-43be-ad1a-ada000d4f573&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

An `if` statement ensures that a bit of code is only executed if a condition is met:
```python
x = 2
if x >= 2:
   print("that is true")
```
The `print` command is only executed "if x >= 2" is true. On the other hand here,

```python
x = 1
if x >= 2:
   print("that is true")
```
the `print` command in the if statement is not executed.

That isn't the whole story: we can use `if`...`else`..., with the command after `else` acting as a fall back, for example,

```python
x = 2
if x < 2:
  print("x is less than 2")
else:
  print("x is not less than 2")
```

Or, for even more options, `if`...`elif`...`else`...
```python
x = 2
if x < 2:
    print("x is less than 2")
elif x == 2:
    print("x is equal to 2")
else:
    print("x is greater than 2")
```


Take note again of the indenting. This is particularly important for nested clauses. The following is an alternative to the `while` loop above:

```python
s = 0
for n in range(100):
    n += 1    # increment the counter
    s += n    # calculate the new sum  
    if s > 1000:
        break

# Output the results
print(s)
```

Here the command `break` ends the for loop when `s > 1000`. Of course this wasn't as good as our while loop as we had to guess how many iterations to use (i.e. that 100 was large enough). Notice how we can see which commands go with the `if` and `for` respectively, thanks to the indenting.




### Control flow and array elements

Recall that we can query a single element of a list or array like this:

```python
x = [2,5,8,5]
print(x[2])
```

We can also update the value inside a list:
```python
x = [2,5,8,5]
x[2] = 4
print(x)
```

We could use this inside a for loop. Remember earlier how we filled a list with values from a series using elementwise arithmetic? Suppose we try to fill an array t with values. We might expect that we could do this to update the n-th element of `t` at each iteration, but not quite. Python is happy over-writing array values, but isn't happy if they don't yet exist. So this doesn't work:

```python
t = []
for n in range(0,10):
	t[n] = n**2
```
The solution is to either append

```python
t = []
for n in range(0,10):
  t.append(n**2)
```

or, using NumPy, initialise `t` as an empty array first using the `np.zeros()` function

```python
import numpy as np
t = np.zeros(10)
for n in range(0,10):
	t[n] = n**2
```

then the code works perfectly. Check with

```python
print(t)
```

Note this is the same as
```python
n = np.arange(0,10)
t = n**2
```
and that this way (using vector arithmetic) is much more efficient; using for loops is not always the best solution. I take a look at the performance of the above two options in an interlude shortly.

### For loops plot example


```python
import matplotlib.pyplot as plt
import numpy as np

# Array of x values
x = np.linspace(0,8,100)

# Plot f(x)=xe^(ax) for a from 1 to 5
for a in range(1,6):
    f = x*np.exp(-a*x)
    plt.plot(x,f)


plt.show()

# make it pretty...
```

Which produces this plot:

![Five curves plotted on the same axes, each one using a different value of a inside the function.](/static/images/week3/lecture_multiplot.png){width="90%"}

*[Download the full source code for this plot](/static/code/week3/lecture_multiplot.py){target="_blank"}*



## List comprehension

List comprehension is the fancy name for another way to iterate through lists (or NumPy arrays). The syntax is as follows

```python
[expression for item in list]
```

and it's a really neat way to do things like query which elements in a list satisfy a certain condition. Here's an example

```python 
a = [1,2,3,4,5,6]
[x > 2 for x in a]
```
```output
[False, False, True, True, True, True]
```

or, with a slightly different syntax, return values that satisfy a condition. `%` is the modulo operator, so `x % 2` gives the remainder when `x` is divided by 2.

```python
even_numbers = [ x for x in a if x % 2 == 0]
print(even_numbers)
```
```output
[2, 4, 6]
```


