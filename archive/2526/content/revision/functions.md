[Click here to open this handout in a new browser tab](#){target="_blank"}

# Functions

## Creating your own function

Python makes it possible to write your own functions, which take some input and return a value or values, in just the same way as Python's built-in functions. This helps to keep your Python code as modular as possible.

<iframe src="https://campus.recap.ncl.ac.uk/Panopto/Pages/Embed.aspx?id=241bac1c-77b9-4a64-a952-ada000d4f4eb&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&start=0&interactivity=none" width=720 height=405 style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

The syntax for creating a function is as follows:

```python
def my_func():
	print("My function prints this")
```

Note a similar syntax as for control flow: the function begins with the keyword `def` and then the function name "my_func". This is followed by input arguments inside brackets - for this function there are none, and finally a colon. The contents of the function are then indented. 

We can call the function with

```python
my_func()
```

either from the same file or the Console.

Now let's add an input parameter to our function and a more descriptive name:

```python
def zoo_visit(animal):
	print("I went to the zoo and saw a {}".format(animal))

zoo_visit("koala")
zoo_visit("panda")
zoo_visit("sun bear")
```

Did I mention that I like bears?

We can also set a default value by using parameter = ... in the parentheses. This default is used if the input parameter is not set.

```python
def zoo_visit(animal = "bear"):
  print("I went to the zoo and saw a {}".format(animal))

zoo_visit("koala")
zoo_visit("panda")
zoo_visit("sun bear")
zoo_visit()
```

Any data type can be sent to a function. Here's a list, with a for loop to print each value - pay careful attention to the indenting:

```python
def print_my_list(list):
	for x in list:
		print(x)

print_my_list([1,5,2,6])
```

And a simple one with a number

```python
def square_a_number(x):
	print(x**2)

square_a_number(2)
```

All of the above examples print something. The functions we have been using however return a value which can be assigned to a variable. For example at the moment this does not do what we might like

```python
x = square_a_number(2)
```

To return a value (or values) from a function we need to use a `return` statement. This is done as follows:

```python
def square_a_number(x):
	return x**2

x = square_a_number(5)
print(x)
```

Note that the `x` in the function argument and the `x` outside the function are completely unrelated. This is known as the scope of a variable.

Now let's extend this by accepting two input arguments:

```python
def show_me_the_bigger(a,b):
	print(max([a,b]))

show_me_the_bigger(4,5)
```





## Adding help to your function

A comment contained within three quotes ```"""``` at the start of our custom function is used to display help. It is known as a *docstring* (documentation string)

```python
import numpy as np
import matplotlib.pyplot as plt

def sin_plus_cos(x):
   """ Takes in a value x and 
       returns cos(x)+sin(x) """
   return np.cos(x)+np.sin(x)

```

Test your help with

```
help(sin_plus_cos)
```
