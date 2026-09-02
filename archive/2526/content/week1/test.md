---
toc: false
css:
  - custom.css
---

# MAS1801 Python Practical 1

Welcome to the handout for the first week of Python material.

#### To Hand in this week: {.handin}

Upload your solutions to:

* Exercise 1.8

to NESS by midnight this **Sunday 18th Neverember**. [Click here to view instructions on how to upload to NESS](../introduction_and_handouts/uploading_to_ness.html){target="_blank"}. 


## Using these handouts

In the practical sessions you will be working through one of these (virtual) handouts. If you want a printable version then hit the link "Download chapter as PDF".

You might need some scrap paper for some of the exercises. If you don't have any then let me know.

You should try out commands: I suggest copying the bits of code like this one

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = 2
```

into the Spyder and exploring them by changing variables and so on. When you see text formatted like this: `x`, I am referring to variables or other bits of code.

I suggest you set up your windows like this: 

** pic/vid **

Whilst you are working through, I'll wander round, as will my fab postgraduate helpers; just stick your hand up or give me a shout if you'd like any assistance. Don't be afraid to ask questions, no matter how silly they might seem.

My handouts have some items in them along the way. They go like this...


### Interlude {.interlude}
This is an interlude, which contains something either totally off-topic, usually not assessed and just there for a bit of fun. Yes, programming can be fun! :-)


### Exercise {.exercise}
This is an exercise. Sometimes there'll be an answer, sometimes they are just to get you thinking. I'll release solutions and comments for each of these next week. I suggest that you try them as you reach them in the notes and that you save your answers into a script file (which we'll find out about later in this handout).


### Exercise* {.handin}
This is an exercise that you need to hand in this week (there may be more than one, though not this week). 



## Python and Spyder

### About Python

A bit of blurb to go in here

We are going to be using the the integrated development environment (IDE) Spyder to run our Python code. Spyder is open source and cross-platform, so you can **insert link re installing on own machine**

#### Python 2 and Python 3

Quick explanation

### Launching Spyder

How to launch spyder

### Spyder windows

A bit of info about the various windows in Spyder


<!-- Python as a calculator -->


## Python as a calculator
 The simplest way to use Python is to enter a command in the *Console* and allow Python to execute it and return the result. I'm showing you the command and output here, but feel free to copy and paste or write commands in Python to follow along. The *>>>* represents the Python prompt, which varies with IDE. Copy and paste, or enter, the code after the prompt into Spyder.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
2+2
```


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
2/3
```


Note that you can access the value of any previous output using `Out[n]`. This is a little bit like the `Ans` on your calculator (well, on my calculator at least).


<!-- Variable assignment -->

## Variable Assignment

You can assign values to variables, in the Console again, we're going to set a variable `x` equal to -3:


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = -3
```

Note that Python is pretty quiet - it doesn't make a lot of fuss. You can see that `x` has definitely been set in the *Variable explorer*, but if you want to display its value in the Console:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x
```


or as we'll do later from scripts using the funtion `print()`

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
print(x)
```



Let's let $y=x^2$. This can be done like this:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
y = x**2
```

Take a look again at the *Variable explorer*. Here you can keep an eye on the type and value of variables. 


There are some rules to follow when naming and using variables:

* Python is case sensitive, so the variable `x` is not the same as `X`.
* variable names can contain numbers, but cannot start with a number.
* variable names cannot contain spaces (however you can use an underscore if you like).
* when we do more extensive code, descriptive variable names will help when you come back to look at your code.


### Arithmetic operators

You might have expected to use `^` in place of `**`. Here are Python's arithmetic operators in a useful table

Operator           Example input      Example Output
--------           -------------      --------------
   +                `2 + 2`              4
   -                `3 - 2`              1
   *                `2 * 3`              6
   /                `4 / 2`              2
   **               `2 ** 3`             8
   % (modulus)      `10 % 3`             1

Go ahead and play around with some of these commands in the Console. 

*Note that an alternative to ** is the function `pow()`. Let's talk about functions next, after an interlude...


### Interlude 1.1 {.interlude}
You can use modular arithmetic to figure out if a year is a leap year (year divides by 4). Like next year:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
2020 % 4
```


But did you also know that keeping our (Gregorian) calendar in line with the time required for the Earth to revolve about the Sun requires more correction than this? As an additional fix, a year that is divisible by 100 is a leap year only if it is also divisible by 400. I won't make it to 2100, but you might... and you may be surprised to find it isn't a leap year. 


Same was true for 1900: not a leap year. Though here's an even weirder fact: Microsoft Excel has a known bug that it thinks 29/2/1900 was an actual day. They can't fix it because they need to maintain backwards compatibility!

Off...topic...



<!-- Using functions -->

## Using Functions

The function `pow` can also be used to square a number, or in fact to raise any number to a power.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
pow(x,2)
```

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
pow(x,3)
```


The function  `pow()` is known as a built-in function - it is one that is part of Python's standard library. To do more with Python we need to find out how to use more of these...

Much like a mathematical function, a function on a computer takes some input, does some stuff and returns some output.

In the command

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
pow(x, 2)
```

The `x` and `2` are the input *arguments* to the function. `pow()` computes $x^2$ and returns its value. The output from a function could be assigned to a new variable:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
y = pow(x, 2)
```

Here are some functions that we'll use from the Python standard library

function             Description
---------            ---------------------------------------------------
`abs()`				 Return the absolute value of a number
`len()`              Return the length of an object
`max()`              Find the largest value in a list or similar object
`min()` 			 Find the smallest value in a list or similar object
`print()`			 Print the value of an object
`round()`            Round a number to a specified precision
`sum()`              Sum the values in a list or similar object

Lets take a look at a couple of examples

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
abs(-3)
```


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
round(2.555,2)
```


So we can square a number, find its absolute value - good start - but as physicists we are going to want to do a lot more. We might expect to be able to do

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
cos(0)
```

But this returns an error message. Why? Python is very modular, and its standard library only contains common, but fairly limited functions. 

## Getting help

You can find out what a function does, and what it expects as input arguments using another function: `help`

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
help(pow)
```

You can even do 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
help(help)
```

if you like!

There is an alternative interactive way of getting help in Spyder. Click on the Help tab on the right and you will prompted to explore your code using CTRL-I - this can be in the Console or the Editor window when we use that later. Move your cursor, say to the `print()` function a couple of commands ago, and press that button combination to get some nicely formatted information.

** animation here **

To get more information you can also consult the online documentation. Click on *Help* nad then *online documentation* and choose the *Python 3 documentation* item.

** image or animation here **

## Python modules

Modules are Python files which can contain function definitions (and possibly other stuff) that can be imported into your code. Later we will see how we can create our own modules, but for now we'll learn how to import an existing one using the `import statement`. Try this out in the Editor:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import math
```

This imports the `math` module and will be imported quietly (successfully). Try running the same command with a different name and you will see what happens when a module cannot be found by Python, e.g.


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import maths
```

gives the error *ModuleNotFoundError: No module named 'maths'*.

Returning to our correct `math` module, the reference guide https://docs.code .python.org/3/library/math.html contains a full list of the functions and definitions contained in the `math` module and we note that there is a function `cos`.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import math
y = math.cos(0)
```

Note the syntax to use the `cos` function from the `math` package. This is important, because there may be (are in fact any seond) other modules which also have a `cos` function. 


### The `numpy` module

The *numpy* module declares itself "the fundamental package for scientific computing with Python". It is a key module that we will use a lot.

Load the module with

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy
```

Just like the `math` module it also has a `cos` function

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
numpy.cos(0)
```

And an awful lot more

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
numpy.sqrt(numpy.pi)
```

It's pretty laborious writing out "numpy" every time you run a command, so Python has a shortcut. You can do this:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
```

and then

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
np.cos(np.pi)
```

Let's use some functions from the *numpy* module to do our first exercise...


### Exercise 1.1 {.exercise}
The hyperbolic sine function $\sinh(x)$ can be defined in terms of exponentials as:

$$ \sinh(x)=\frac{e^x-e^{-x}}{2}. $$

* Use the function `exp` to calculate $\sinh(\pi)$ using the expression on the right of the above equation. 
* Verify that you get the same answer with the command `sinh(pi)`. 

Note that the above documentation tells us that there is both a function `math.exp` as well as a mathematical constant `math.e`. Either could be used here.



## Data Types

An understanding of different data types is important for any programming language. 

Following on from some of the trigonometry in the previous section, have a go at this:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
z = np.sin(np.pi/3)
```

We all know that $\sin(\pi/3)=\sqrt{3/2}$, but we don't get a nicely answer like this (try it and you will get 0.8660254037844386). Python makes its computations in what is known as floating point arithmetic (by default); when it makes its calculation it thinks of pi as a decimal, hence the decimal output. There are symbolic mathematics packages for Python but we won't use those in this module. 

In the variable explorer you will find that the type of the variable `z` is a *float*. You might also have some integers with type *int* still in your workspace. Let's find out more about these and other data types...



The function `type` can tell us the data type of a variable.

### Integers

Python stores integers as a separate data type which it calls *int*. Why? Well there's no point in storing a load of decimal places if you have whole numbers. 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
type(2)
```

 
Other data types can be converted to integers using the function `int`. Here `x` is a decimal number.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = 2.0
int(x)
```


Note that the intended use is not rounding or formatting numbers. We'll come back to that later.


### Floating point numbers

In the last section we dealt with some decimal numbers... strictly speaking these were really what are called floating-point numbers, and Python refers to them as a *float*. 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
type(math.pi)
```


The function `float` will take a different data type and turn it into a float. Here `x` is an integer.
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = 2
float(x)
```



### Complex numbers

You may or not have already come across complex numbers. Well, this is as good a place as any to mention them, even if we don't really use them in this bit of course.

You can define a complex number as follows
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
z = 2+3j
type(z)
```


and easily query its real and imaginary parts
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
z.real
```

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
z.imaj
```


### Booleans

A boolean is an object that is either true or false and is referred to as type *bool* in Python. There are only two values for this data type: `True` and `False`
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
type(True)
```


Note that computers store boolean values as 0s (for false) and 1s (for true), so the result of this sort of conversion is not surprising:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
int(True)
```

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
bool(1)
```


### Strings

*Strings* (words!), sometimes called character strings, could be used as part of data that we are working with, or when naming files, and so on. Python calls this type of data *str*.

You can define a complex number as follows
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
type("a string")
```


You can use either single or double quotes to enclose a string. Unlike other languages, there is no real precedent for using one over the other, but it's best to stick with one and being consistent. In that spirit, I'm going for double quotes...



### Exercise 1.2 {.exercise}

Assign some strings to two variables, preferably two words or phrases that when put together will be hilarious. 

* Look up a function or method to join the two strings into one. What is the technical name for this operation? When I say look up, Google is your friend! *Other search engines are available.*
* Use the function `len` to find out how many characters are in your masterpiece.

Note that there are several ways to do this, some more sophisticated than others. What happens if you use your method to join a string and an integer? The simplest method of joining strings doesn't allow this and returns an error. If you wanted to do such a thing then you may need another way.



## Lists and arrays

Lists and arrays are used by Python to store data in a vector- or matrix-like structure. 

### Lists

Lists are very straightforward to set up. Place a comma-separated list of any variable type inside square brackets.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = [3,8,5,6]
```

An element of the list can be accessed, or *indexed*, as follows,

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x[3]
```


And individual elements can be set with,

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x[3] = 10
```


Note - **very important** - Python indexing begins at 0, not 1, i.e. the element with index 3 above is the fourth in the list! There are long and boring reasons why, which I won't waste pixels with, but importantly this is different in other languages (including R, which you will learn next semester), so take care!

Lists can be used with other data types too. For example strings:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
y = ["oranges","apples","bananas"]
y[1]
```


We are now in a position to use some more of the built-in functions that were introduced earlier in the handout.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = [1,5,7,2,4,6,3,9,1,-1]
```
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
len(x)
```
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
min(x)
```
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
max(x)
```
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
sum(x)
```

### The `range` function

The range function creates a sequence of integer numbers. We will use this a lot!

With one argument, `range(stop)` for some integer `stop`, the function returns the sequence from 0 up to **but not including** `stop`.  

```{.code .python}
range(10)
```

creates a sequence of numbers $0,1,2\cdots 9$.

You can display these numbers in a list using the `list` function:

```{.code .python}
list(range(10))
```

If `range` is given two arguments, it treats them as `range(start,stop)` and returns the sequence from `start` up to **but not including** `stop`.  

```{.code .python}
list(range(2,10))
```

returns the sequence $2,3,4\cdots 9$.

If range has a third argument then it does 'list(start,stop,step)'

```{.code .python}
list(range(2,10,2))
```

returns the sequence $2,4,6,8$.

Just like before, we can query elements in a sequence

```{.code .python}
x = range(2,10,2)
x[3]
```

### Exercise 1.3 {.exercise}
Run the following command:

```{.octave data-gutter-symbol=">>" data-code-dir="input"}
list(range(2, -3))
```

* What do you think was the intended sequence of numbers? 
* What is the result instead?
* Can you figure out how to 'fix' it. 

### List methods

*methods* in Python are similar to a little bit like a function: they are tasks associated with a particular type (technically class, we'll come back to that later in the module) of object. In this case there are a number of methods associated with lists. Note that these change the list itself:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = range(0,10)
x.reverse()
print(x)
```


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = [2,7,3,8]
x.sort()
print(x)
```


```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = ["oranges","bananas"]
x.append("apples")
print(x)
```


Here is a [https://docs.code .python.org/3/tutorial/datastructures.html](reference page for more list methods). You can also view all of the methods available for any object using the `dir()` function.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
dir(x)
```

### Exercise 1.4 {.exercise}

Consider the following:
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
fizzy_drinks = ["Cola", "Lemonade", "Sparkling Water"] 
stll_drinks = ["Orange Juice", "Still Water"]
```
Find a way to combine the two lists into one list named `all_drinks` (hint: use the method `copy()` followed by `extend()`) and then sort it alphabetically using `sort()`.


### Limitation of lists

This is all very neat and don't forget about lists, as they are great! However, they are not ideal for arithmetic operations. I might well like to do something like the following

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = [3,6,9]
x/3
```
and hope to get back 
```
[1,2,3]
```
however what I get back is
```
TypeError: unsupported operand type(s) for /: 'list' and 'int'
```
Because we're physicists, we are likely to want to do this sort of thing. Fortunately *numpy* is brilliant at this...


## Arrays in *numpy*

Setting up a vector using numpy goes like this:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
a = np.array([3,6,9])
```


*numpy* also has support for sequences of numbers with a function `arange`.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
np.arange(3,6)
```

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
np.arange(1,10,2)
```


## Vector arithmetic

We can now do some vector arithmetic. In the following command

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
x = np.array([3,6,9])
y = x/3
```

each term in `x` is divided by 3, so that `y` is an array of length 3 containing the values 1,2,3. The division is done 'element-wise'.

Similarly we can do vector multiplication

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
3*x
```


and addition and subtraction

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = np.array([1,2,3])
y = np.array([4,5,6])
x + y
```

Similarly, functions which would normally be used for a scalar number operate element-wise. Consider for example `np.deg2rad()` which converts degrees to radians:

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
a = np.array([0,90,180])
np.deg2rad(a)
```


Let's see how this works in practice by constructing some triangular numbers

$$t_n = \frac{n(n+1)}{2}$$

Say we are interested in $n$ from 1 to 10. Let's set up an array using `arange()`

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
n = np.arange(1,11)
```

Because all of the arithmetic is element-wise, the triangular numbers are simply given by 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
t = n*(n+1)/2
```

### Exercise 1.5 {.exercise}

Using the above, find the sum of the first 100 triangle numbers.


## Querying and manipulating arrays

Consider the following array set up using `arange`

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = np.arange(0,15)
```

We saw earlier that, for example, the element with index 5 (6th in the list) can be found with 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x[0]
```

And we can also use this to set a value 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x[0] = 5
```

Using a similar idea, we can find the values greater than 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x[x>10]
```

We could also find the number of values 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
len(x[x>10])
```

Note that the command `x>10` returns an array of logicals

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x>10
```
i.e. a `True` or `False` for each element in the array. We'll come back to logical expressions next week.

### Exercise 1.6 {.exercise}

Look up the help for the *numpy* function `zeros()` to create a vector

$$[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]$$

(i.e. don't just add the elements individually)

It's likely that your array will contain floating point numbers. Take another look at the help for `zeros` and see if you set up the array with integers instead

### Matrices in `numpy`

From a programming point of view, a matrix is a two-dimensional array, and can also be set up using the *numpy* `array` function. The syntax is as follows

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A = np.array([[2,1,3],[2,3,3],[1,2,0]])
```

As for lists, the *numpy* array class of objects has methods. You can view these for our object `A` with

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
dir(A)
```

The shape of a *numpy* array can be queried with the shape method

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A.shape
```

The methods for a numpy array include some common tasks used when working with matrices, for example

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A.transpose()
```

*numpy* also has functions which operate on matrices, such as `numpy.linalg.inv()`, to calculate the inverse of a matrix.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
numpy.linalg.inv(A)
```

The function `np.linalg.solve(A,b)` solves an equation in the matrix form $Ax=b$ for matrix $A$ and columb nector $b$. For example, let's solve the system of linear equations

$$ 
x +  y + z = 6 \\
2y + 5z = −4   \\
2x + 5y − z = 27   \\
$$

We'll write the system in the form

$$ Ax = b $$

$$
\begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 5 \\ 2 & 5 & -1 \\ \end{pmatrix} \begin{pmatrix} x \\ y \\ z\end{pmatrix} = \begin{pmatrix} 6 \\ -4 \\ 27\end{pmatrix}
$$

and create `A` and `b` in Python using *numpy*

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A = np.array([[1,1,1],[0,2,3],[2,5,-1]])
```
```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
B = np.array([[6],[0],[27]])
```

Then $x$ is then given by

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
x = np.linalg.solve(A,b) 
print(x)
```


A matrix element can be accessed as `A[i][j]` where `i` is the row index and `j` the column index

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A[1][2]
```


Or alternatively

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A[1,2]
```


A colon acts as a 'wilcard', so this returns the first column (remember the first column has index 0),

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A[:,0]
```

 
Read this as "show me the any row and the first column". Similarly,

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
A[0,:]
```


gives the "first row and any column".


### Exercise 1.7 {.exercise}

Create the matrix 

$$
\begin{pmatrix} 1 & 2 & 3 & 4 & 5  \\ 6 & 7 & 8 & 9 & 10 \\ 11 & 12 & 13 & 14 & 15 \end{pmatrix}
$$

There are three levels of sophistication here:

* Create the matrix entering individual elements.
* Create the matrix from the 3 sequences. You'll need the *numpy* functions `arange()` and `column_stack()` (see `help(np.column_stack)`)
* Create the matrix from 1 sequence. Take a look at help(np.reshape).


<!-- Working with files -->

## Python Scripts

Whilst the Console window is an important part of the environment, especially as it contains the output to our code, it's not a convenient place to put multiple lines of code. And of course we're going to need more code if we want to do amazing things with Python.

You'll have noticed that big space on the left of Spyder. This is the *Editor* and is used to edit files. We'll use files to store our code, so that we can edit, save, re-open and re-use code.

### Opening a blank file

Hit the `New file` button or go to *File -> New file..*. 

** pic **

You'll have a file with a bunch of stuff at the top. The first two lines are comments (actually the first is known as a *shebang*) and the but in green is a multiline string. You can delete this bit if you like.


Let's go ahead and put some code into our file from earlier.

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
x = np.arange(0,10)
y = np.cos(x)
```
Click the play button, or hit f5 to run the file. You will be prompted to save your file. It's a good idea to give it a sensible name and location, maybe even think about creating a folder for today's session.

In the console you'll see a line like 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
runfile('/Users/chris/.spyder-py3/myfile.py', wdir='/Users/chris/.spyder-py3')
```

but not much else. I did say that Python is quiet! Let's use the `print` function to print out the value of y. Change your code in the editor to 

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
import numpy as np
x = np.arange(0,10)
y = np.cos(x)
print(y)
```

and you will see the value of `y` printed in the Console.

Next week we'll talk about best practices for commenting your files, which is very important. In brief, lines with a # are treated as comments

```{.code .python data-gutter-symbol=">>>" data-code-dir="input"}
# import numpy
import numpy as np

# do some stuff
x = np.arange(0,10)
y = np.cos(x)

# print y
print(y)
```

<!-- Hand In exercise -->

### Exercise 1.8* {.handin}


In the 14th century, the Indian astronomer and mathematician, Madhava of Sangamagrama, proposed the following method for computing the value of the number $\pi$:

$$ \pi = \sqrt{12}\sum_{k=0}^{n}\frac{(-3)^{-k}}{2k+1} $$

Madhava computed the first 21 terms in the series.  

* Create a vector `k` containing the integers $0$ to $20$ using a *numpy* array.
* Use `k` to create a new vector which contains the terms in the series (*Hint: see the vector arithmetic section*).
* Use your vector to calculate $\pi$ using Madhava's method.
* To how many decimal places was Madhava correct?

Put your commands into a .py script and upload it to NESS before Neversday at midnight.


## Next Time
In the next session we will look at Python's impressive plotting capabilities and my teaching materials will be a whole load more colourful! 

** image to go in **

------------------------------