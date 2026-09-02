[Click here to open this handout in a new browser tab](#){target="_blank"}

# Python Basics

## Using these handouts

<iframe class="recap" src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=234e3cad-7502-4ec9-b0a6-ada000d4f742&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" style="max-width: 720; width: 100%; height: 405px; border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>


You should try out commands: I suggest copying the bits of code like this one

```python
x = 2
```

into Spyder and exploring them by changing variables and so on. When you see text formatted like this: `x`, I am referring to variables or other bits of code.



## Python and Spyder

### About Python

Python was first developed in the late 1980s by Guido van Rossum, a Dutch programmer who was also a fan of [Monty Python's Flying Circus](https://www.dailymotion.com/video/x2hwqn9){target="_blank"}. It is [one the most popular coding languages in the world](https://www.wired.com/story/python-language-more-popular-than-ever/#:~:text=Python%20is%20one%20of%20the,by%20the%20analyst%20firm%20RedMonk.){target="_blank"} and has wide-ranging applications from data science to web frameworks. It helps to power these very lecture notes. 

To name just a few other bits of software powered by Python, that you've probably used today: Google, Instagram, Spotify, Dropbox, Wikipedia and Amazon...

We are going to be using the integrated development environment (IDE) Spyder to run our Python code. Spyder is open source and cross-platform, so you can install it for free on your own machine - see the information section of our Canvas course.

#### Python 2 and Python 3

Versions 2 and 3 of Python were released in 2000 and 2008 respectively. Because Python 3 was not entirely backward compatible, this caused a bit of a fork in usage. The result is that both are actively used, and the official "end-of-life" for Python 2 was 1st January 2020. It's a no-brainer for us to use Python 3, but this is worth bearing in mind e.g. when you are browsing for documentation, that Python 2 is still widely used.

### Launching Spyder

Let's start by launching Anaconda:

![The Anaconda Navigator menu item](/static/images/week1/launchanaconda.png){width=80%}

You should be presented with a number of applications. You are welcome to explore these, but we are really only interested in *Spyder* at this stage.

![The choice of options inside Anaconda Navigator](/static/images/week1/anaconda.png){width=90%}

Launch Spyder by clicking on the "Launch" button in that block. 

If you are on a laptop or desktop then I suggest that you set up your windows so that the handout and Spyder are side by side, so that you can copy and paste commands across from one to the other (see the video at the start of this section). 

### Spyder windows

On opening Spyder, you will be presented with the following:

![Default oientation of Spyder windows](/static/images/week1/spyder.png){width=90%}

The pane on the left is the *Editor* window. We'll use this space to write scripts once we get going. 

For the moment we will insert code in the *Console* window in the bottom right corner.

The window in the top right has some tabs, which can be used to access "Help", the "File explorer" (to open files etc) and the "Variable explorer" (view the currently active variables). In the latest version of Spyder (Spyder 4), this is also where plots will appear, in a "plots" tab.


## Python as a calculator
 The simplest way to use Python is to enter a command in the *Console* and allow Python to run it and return the result. I'm showing you the command and output here, but feel free to copy and paste or write commands in Python to follow along. The *prompt* is the place where the Spyder console is waiting for code; on first launch it will read `In [1]`. Copy and paste, or enter, the below code after the prompt. I've included both the input and output in much of this handout.

```python
2+2
```
```output
4
```

```python
2/3
```
```output
0.6666666666666666
```

Note that you can access the value of any previous output using `Out[n]`. This is a little bit like the `Ans` on your calculator (well, on my calculator at least).


<!-- Variable assignment -->

## Variable Assignment

It is usual to assign values to *variables* when we write longer pieces of code. In the Console again, we're going to set a variable `x` equal to -3:


```python
x = -3
```

Note that Python is pretty quiet - it doesn't make a lot of fuss. You can see that `x` has definitely been set in the *Variable explorer*, but if you want to display its value in the Console:

```python
x
```
```output
-3
```

or as we'll do later from scripts using the function `print()`

```python
print(x)
```
```output
-3
```


Let's let $y=x^2$. This can be done like this:

```python
y = x**2
print(y)
```
```output
9
```

Take a look again at the *Variable explorer*. Here you can keep an eye on the type and value of variables. 


There are some rules to follow when naming and using variables:

* Python is case sensitive, so the variable `x` is not the same as `X`.
* variable names can contain numbers, but cannot start with a number.
* variable names cannot contain spaces (however you can use an underscore if you like).
* when we do more extensive code, descriptive variable names will help you to come back to try and understand what old code does.


### Arithmetic operators

You might have expected to use `^` in place of `**`, but that's not the case. Here are Python's arithmetic operators in full, in a useful table

Operator       |     Example input   |   Example Output
---------------|---------------------|--------------------
   +           |     `2 + 2`         |     4
   -           |     `3 - 2`         |     1
   *           |     `2 * 3`         |     6
   /           |     `4 / 2`         |     2
   **          |     `2 ** 3`        |     8
   % (modulo)  |     `10 % 3`        |     1

Go ahead and play around with some of these commands in the Console. 

An alternative to ** is the function `pow()`. Let's talk about functions next, after an interlude...


### Interlude 1.1 {: .interlude}
You can use modular arithmetic to figure out if a year is a leap year (year divides by 4). Like this year:

```python
2020 % 4
```
```output
0
```

`a % b` finds the remainder of `a` divided by `b`. 

You will be familiar with leap years, but did you also know that keeping our (Gregorian) calendar in line with the time required for the Earth to revolve about the Sun requires more correction than this? As an additional fix, a year that is divisible by 100 is a leap year only if it is also divisible by 400. 

I was here (literally, at the university), "meeting up in the year 2000"... and it was a leap year. I won't make it to 2100, but you might, and you may be surprised to find it isn't a leap year. 

Back on topic...


<!-- Using functions -->

## Using Functions

The function `pow()` can also be used to square a number, or in fact to raise any number to a power.

```python
x = -3
pow(x,2)
```
```output
9
```
```python
pow(x,3)
```
```output
-27
```

The function  `pow()` is known as a built-in function - it is one that is part of Python's [*standard library*](https://docs.python.org/3/library/){target="_blank"}. 

To do more with Python we need to find out how to use more of these functions.

Much like a mathematical function, a function on a computer takes some input, does some stuff and returns some output. In the command

```python
pow(x, 2)
```

The `x` and `2` are the input *arguments* to the function. `pow()` computes $x^2$ and returns its value. The output from a function could also be assigned to a new variable:

```python
y = pow(x, 2)
```

Here are some "mathsy" functions that we might use from the Python standard library

function      |       Description
--------------|---------------------------------------------------------
`abs()`		  |		 Return the absolute value of a number
`len()`       |       Return the length of an object
`max()`       |       Find the largest value in a list or similar object
`min()` 	  |		 Find the smallest value in a list or similar object
`print()`	  |		 Print the value of an object
`round()`     |       Round a number to a specified precision
`sum()`       |       Sum the values in a list or similar 

Lets take a look at a couple of examples

```python
abs(-3)
```
```output
3
```

```python
round(2.555,2)
```
```output
2.56
```


So we can square a number, find its absolute value - good start - but as physicists we are going to want to do a lot more. We might expect to be able to do the following, but this returns an error message:

```python
cos(0)
```

Why? Well Python is very *modular*, and its standard library only contains common, but fairly limited functions. We'll see how to extend Python using *modules* shortly.

### Getting help

You can find out what a function does, and what it expects as input arguments using another function: `help`

```python
help(pow)
```

There is an alternative interactive way of getting help in Spyder. Click on the Help tab and you will prompted to explore your code using CTRL-I (capital I for indigo) - this can be in the Console or the Editor window when we use that later. Move your cursor immediately before a command, -  say to the `print()` function a couple of commands ago - and press that button combination to get some nicely formatted information.


To get more help you can also consult the online documentation. In the toolbar at the top of Spyder, click on *Help* and then *online documentation* and choose the *Python 3 documentation* item.

![The Python 3 documentation is found at "Help", and then "online documentation", then "Python 3 documentation"](/static/images/week1/help.png){width=70%}




## Data Types

An understanding of different data types is important for any programming language. 

Consider creating a variable `z` 

```python
z = 1/3
```

When we do this, Python does not store `z` as the fraction 1/3. We know that if we write 1/3 as a decimal it can be written as $0.333333\ldots$ to some arbitrary precision and you can always be more precise. Similarly, your computer does not store values like this precisely. That's why this sort of thing happens

```python
0.1+0.2
```
```output
0.30000000000000004
```
We won't dwell on this, but [here is a link to some info in the Python docs if you are interested](https://docs.python.org/3/tutorial/floatingpoint.html){target="_blank"}. There are  mathematics packages for Python which allow for symbolic storing of something like 1/3, but we aren't interested in those for the moment. 

In the variable explorer you will find that the type of the variable `z` is a *float*. You might also have some integers with type *int* still in your workspace. Let's now find out more about these and other data types...


### Integers

Python stores integers as a separate data type which it calls *int*. Why? Well there's no point in storing a load of decimal places in your computer if you have integer numbers. 

The function `type` can tell us the data type of a variable.


```python
type(2)
```
```output
int
```
 
Other data types can be converted to integers using the function `int()` (the technical term is *casting*). Here `x` is a decimal number:

```python
x = 2.0
int(x)
```
```output
2
```

Note that the intended use is not rounding or formatting numbers. We'll come back to that later.


### Floating point numbers

On a computer, "decimal numbers" are called floating-point numbers, and Python refers to them as a *float*. 

```python
type(2.0)
```
```output
float
```

The function `float` will take a different data type and turn it into a float. Here `x` is an integer.
```python
x = 2
float(x)
```
```output
2.0
```


### Complex numbers

You may or may not have already come across complex numbers, but this is as good a place as any to mention them:

You can define a complex number as follows, with the imaginary part written with a j suffix:
```python
z = 2+3j
type(z)
```
```output
complex
```

and easily query its real and imaginary parts
```python
z.real
```
```output
2.0
```
```python
z.imag
```
```output
3.0
```

Note it is `z.real` not `real(z)`. This is called an attribute of `z`. We'll come back to that.  


### Booleans

A boolean is an object that is either true or false and is referred to as type *bool* in Python. There are only two values for this data type: `True` and `False`
```python
type(True)
```
```output
bool
```

Note that computers store boolean values as 0s (for false) and 1s (for true), so the result of this sort of conversion is not surprising:

```python
int(True)
```
```output
1
```
```python
bool(1)
```
```output
True
```

We will use these extensively later on in the course, when we want to compare values:

```python
5 < 0
```
```output
False
```

this is called a logical comparison, and `<` a logical operator. More on these in week 3...


### Strings

*Strings* (words), sometimes called character strings, could be used as part of data that we are working with, or when naming files, and so on. Python calls this type of data *str*.

You can define a string as follows:

```python
s = "orange juice"
type(s)
```
```output
str
```

You can use either single or double quotes to enclose a string. Unlike other languages, there is no real precedent for using one over the other, but it's best to stick with one and be consistent. In that spirit, I'm going for... double quotes.

We are about to talk about lists, and actually strings themselves are lists of individual characters, as we will see in the next section.


## Lists (Collections)

Lists and arrays are used by Python to store data in a vector-like structure. There are actually several list type structures in Python, and together they are known as *collections*, and have different applications.

We are going to concentrate on lists, which are very straightforward to set up: place a comma-separated list of any data type inside square brackets as follows:

```python
x = [3,8,5,6]
```

An element of the list can be accessed using an index number as follows,

```python
x[3]
```
```output
6
```

And individual elements can be set with,

```python
x[3] = 10
print(x)
```

Note - **very important** - Python 'indexing' begins at 0, not 1, i.e. the element with index 3 above is the fourth in the list! There are long and boring reasons why, which I won't waste pixels with, but importantly this is different in other languages (including R, which you will learn next semester), so take care!

To retrieve a section of the list, say the first 3 element we can also use the colon notation
```python
x[0:3]
```
```output
[3, 8, 5]
```
Note that this displays the elements up to, but not including 3 (which would be the fourth element). This behaviour is something you will get used to in the next section when we look at ranges.


Lists can be used with other data types too. For example strings:

```python
y = ["oranges","apples","bananas"]
y[1]
```
```output
'apples'
```

Note that, as mentioned above, strings are themeselves lists of characters, so this returns a single letter:

```python
y = ["oranges","apples","bananas"]
x = y[1]
x[4]
```
```output
'e'
```

and can also be written as
```python
y = ["oranges","apples","bananas"]
y[1][4]
```
```output
'e'
```

`y` is effectively a multidimensional list of strings!

### List functions

We are now in a position to use some more of the built-in functions that were introduced earlier in the handout. Try each of the following functions out:

```python
x = [1,5,7,2,4,6,3,9,1,-1]
```
```python
len(x)
min(x)
max(x)
sum(x)
sorted(x)
```

### The `range` function

The range function creates a sequence of integer numbers. We will use this a lot!

With one argument, `range(stop)` for some integer `stop`, the function returns the sequence from 0 up to **but not including** `stop`.  

```python
range(10)
```

creates a sequence of numbers $0,1,2\ldots 9$. It does not return a list though, it returns an object of type *range*, as you can see with

```python
x = range(10)
type(x)
```
```output
range
```

You can display these numbers as a list using the `list` function:

```{.python}
list(range(10))
```

If `range` is given two arguments, it treats them as `range(start,stop)` and returns the sequence from `start` up to **but not including** `stop`.  

```{.python}
list(range(2,10))
```

returns the sequence $2,3,4\ldots 9$.

If range has a third argument: `range(start,stop,step)`, it returns the sequence from `start` up to **but not including** `stop` in step sizes of `step`.

```{.python}
list(range(2,10,2))
```

returns the sequence $2,4,6,8$.

Just like before, we can query elements in a sequence

```{.python}
x = list(range(2,10,2))
x[3]
```
```output
8
```



### List methods

*methods* in Python are tasks associated with a particular *type* of object. In this case there are a number of methods associated with lists. Note that these change the list itself:

```python
x = [2,7,3,8]
x.reverse()
print(x)
```
```output
[8,3,7,2]
```

```python
x.sort()
print(x)
```
```output
[2, 3, 7, 8]
```

```python
x = ["oranges","bananas"]
x.append("apples")
print(x)
```
```output
['oranges', 'bananas', 'apples']
```

or if appending a list to an existing list:
```python
x = ["oranges","bananas"]
x.extend(["apples","kiwis"])
print(x)
```
```output
['oranges', 'bananas', 'apples', 'kiwis']
```

Here is a [reference page for more list methods](https://docs.python.org/3/tutorial/datastructures.html){target="_blank"}. You can also view methods available for any object using the `dir()` function.

```python
dir(x)
```



### Limitation of lists

This is all very neat and don't forget about lists, as they are great! However, they are not ideal for arithmetic operations. I might wish to do something like the following

```python
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

Because we're physicists, we are likely to want to do this sort of thing. And you will also recall that, earlier on, we couldn't use mathematical functions such as $\cos$.

```python
cos(0)
```
```{.output}
NameError: name 'cos' is not defined
```

To proceed we need to extend Python's standard library with modules. Let's see how they work, and then get stuck in to one that we will use extensively, *NumPy*.


## Python modules

Modules are Python files which can contain function definitions and variables that can be imported into your code. Later we will see how we can create our own modules, but for now we'll learn how to import an existing one using the `import` command. Try this out:

```python
import math
```


This imports the `math` module and will be imported quietly (successfully). You can view its contents with

```python
help(math)
```



Try running the import command with a different name and you will see what happens when a module cannot be found by Python, e.g.


```python
import maths
```
```{.output}
ModuleNotFoundError: No module named 'maths'.
```

Using the module involves using the module name `math`, then a dot, and then a function name, for example `cos`, like this:

```python
import math
math.cos(0)
```

Note that this syntax of including the module name in front of the function is extremely important, because there may be (and are in fact) other modules which also have a `cos` function, such as:


### The NumPy module

The *NumPy* module declares itself "the fundamental package for scientific computing with Python". That sounds quite useful. It is a key module that we will use a lot, and includes the functionality of the math module and much more, so we will now put that behind us.

Load the NumPy module with

```python
import numpy
```

Just like the `math` module it also has a `cos` function

```python
numpy.cos(0)
```

And an awful lot more:

```python
numpy.sqrt(numpy.pi)
```

In other words, NumPy has a variable `pi` as part of the module.

It's pretty laborious writing out `numpy` every time you run a command, so Python has a shortcut. You can do this:

```python
import numpy as np
```

and then

```python
np.cos(np.pi)
```

I have not chosen np arbitrarily, though I guess I could have done. `import numpy as np` is the convention used my millions of other Python coders, so we may as well go with the flow!



## Arrays in NumPy

Setting up a list-like object using NumPy goes like this:

```python
import numpy as np
a = np.array([3,6,9])
print(a)
```

Go ahead and use `type` to take a look at it's type. It isn't a list as such, it has type `numpy.ndarray`.

NumPy also has support for sequences of numbers, similar to `range`, with the function `np.arange()`.

```python
np.arange(3,6)
```

```python
np.arange(1,10,2)
```

Note that `np.arange` gives the same type of object as `np.array`.


## Vector arithmetic

We can now do some vector arithmetic. Hoorah! In the following command

```python
import numpy as np
x = np.array([3,6,9])
y = x/3
```

each term in `x` is divided by 3, so that `y` is an array of length 3 containing the values 1,2,3. In other words, the division is done 'element-wise'.

Similarly we can do vector multiplication

```python
3*x
```
```output
array([ 9, 18, 27])
```

and addition and subtraction

```python
x = np.array([1,2,3])
y = np.array([4,5,6])
x + y
```
```output
array([5, 7, 9])
```

Similarly, functions which would normally be used for a scalar number operate element-wise. Consider for example `np.deg2rad()` which converts degrees to radians:

```python
a = np.array([0,90,180])
np.deg2rad(a)
```
```output
array([0.        , 1.57079633, 3.14159265])
```

Let's see how vector arithmetic can be used to do some clever stuff, by constructing the triangular numbers

$$t_n = \frac{n(n+1)}{2}$$

Say we are interested in $n$ from 1 to 10. Let's set up an array using `np.arange()`

```python
n = np.arange(1,11)
```

Because all of the arithmetic is element-wise, the triangular numbers are simply given by 

```python
t = n*(n+1)/2
```


## Python Scripts

Whilst the console window is an important part of the environment, especially as it contains the output to our code, it's not a convenient place to put multiple lines of code. And of course we're going to need more code if we want to do amazing things with Python.

You'll have noticed that big space on the left of Spyder. This is the *Editor* and is used to edit files. We'll use files to store our code, so that we can edit, save, re-open and re-use code.

### Opening a blank file

Hit the "New file" button or go to *File -> New file..*. 

<!--** pic to add **-->

You'll have a file with a bunch of stuff at the top. The first two lines are comments (actually the first is known as a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)){target="_blank"}) and the bit in green is a multiline comment. You can delete these bits for the moment if you like - we'll come back to commenting.


Let's go ahead and put some code into our file from earlier.

```python
import numpy as np
x = np.arange(0,10)
y = np.cos(x)
```
Click the play button, or hit f5 to run the file. You may be prompted to save your file. It's a good idea to give it a sensible name and location, maybe even think about creating a folder for today's session.


You'll then get a load of other options in a window the first time you run a script: this is just Spyder setting up your configuration and you can go ahead and hit "Run".

In the console you'll see a line something like 

```
runfile('H:/python/my_file.py', wdir='H:/python/')
```

Hitting the run button basically called a function `runfile()`, with two arguments: the first is the file location, the second the "working directory". The latter is very important when it comes to working with multiple files later in the module.

You won't see any other output in the Console though; I did say that Python is quiet! Let's use the `print` function to print out the value of y. Change your code in the editor to 

```python
import numpy as np
x = np.arange(0,10)
y = np.cos(x)
print(y)
```

and you will see the value of `y` printed in the Console. Notice the beauty of not needing to enter the other lines again, you can just add the print command at the bottom of your script.

Next week we'll talk about best practices for commenting your files, which is very important. In brief, lines beginning with a `#` are treated as comments:

```python
# import numpy
import numpy as np

# do some stuff
x = np.arange(0,10)
y = np.cos(x)

# print y
print(y)
```



