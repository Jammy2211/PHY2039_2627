
# Python Cheat Sheet

<div style="float: right; max-width: 300px; width: 50%; margin-left: 30px; text-align: center; border-bottom: 4px solid #c23abb; padding: 10px; background: #FAFAFA;">
<a href="/static/pdf/python-cheat.pdf" target="_blank">
	<img src="/static/images/cheatsheet.png" style="width: 100%;">
</a>
<h4 style="margin-top: 10px;"><a href="/static/pdf/python-cheat.pdf" target="_blank">Cheat Sheet (PDF version)</a></h4>
</div>

This is a cheat sheet of commands from the stage 1 Python module PHY2039, provided as a useful reference.

Click the image to download a PDF copy to stick on your wall!

Below is a useful online/accessible version of the same thing.


<br style="clear: both;">

## Good practice

<table class="table">
<tr>
<td markdown="true">
```python
# A comment
```
</td>	
<td>Don't forget to comment your code</td>
</tr>
<tr>
<td markdown="true">
```python
""" A doc string """
```
</td>
<td>Use a docstring for module/function help</td>
</tr>
<tr>
<td colspan="2">Have a sensible way of organising your files, such as a folder structure by week. Never use untitled.py as a filename (!)</td>
<td>
</td>
</tr>
</table>

## Importing modules

(Later cheat sheet entries will use these short names)


<table class="table">
<tr>
<td markdown="true">
```python
import numpy as np
```
</td>
<td>
	Import NumPy module (<a href="https://numpy.org/" target="_blank">Documentation</a>)
</td>
</tr>
<tr>
<td markdown="true">
```python
import matplotlib.pyplot as plt
```
</td>
<td>
	Import PyPlot from Matplotlib module (<a href="https://matplotlib.org/" target="_blank">Documentation</a>)
</td>
</tr>
<tr>
</table>


## Data types

* Text:	`str`
* Numeric:	`int`, `float`, `complex`
* Sequence:	`list`, `range`, `tuple`, `dict`
* Boolean:	`bool`
* Maths-specific: `np.ndarray` (NumPy array)

<table class="table">
<tr>
<td markdown="true">
```python
type(x)
```
</td>
<td>
	Query the type of `x`
</td>
</tr>
<tr>
<td markdown="true">
```python
str(x)
```
</td>
<td>
	Convert `x` to type `str` (similar for other types `bool(x)` etc)
</td>
</tr>
</table>



## Printing and formatting numbers


<table class="table">
<tr>
<td markdown="true">
```python
print(x)
```
</td>
<td>
	Print any variable
</td>
</tr>
<tr>
<td markdown="true">
```python
print("Values x = {} and y = {}".format(x,y))
```
</td>
<td>
	Print a string with variables
</td>
</tr>
<tr>
<td markdown="true">
```python
str(x)
```
</td>
<td>
	Convert variable x to a string
</td>
</tr>

<tr>
<td markdown="true">
```python
round(x,n)
```
</td>
<td>
	Round x to n decimal places
</td>
</tr>
</table>


## Creating lists and arrays

<table class="table">
<tr>
<td markdown="true">
```python
[3,10,7,4]
```
</td>
<td>Create a list with specific values</td>
</tr>
<tr>
<td markdown="true">
```python
range(1,11)
```
</td>
<td>A range of values 1,2,3...10 (not 11)</td>
</tr>
<tr>
<td markdown="true">
```python
range(1,11,2)
```
</td>
<td>A range of values 1,3,5...9 (not 11)</td>
</tr>
<tr>
<td markdown="true">
```python
np.linspace(0,5,10)
```
</td>
<td>Create a linearly spaced NumPy array of 10 values between 0 and 5</td>
</tr>
<tr>
<td markdown="true">
```python
np.arange(1,11)
```
</td>
<td>Create a NumPy array with values 1,2,3...10</td>
</tr>
<tr>
<td markdown="true">
```python
np.arange(1,11,2)
```
</td>
<td>Create a NumPy array with values 1,3,5,7,9</td>
</tr>
<tr>
<td markdown="true">
```python
np.zeros(10)
```
</td>
<td>Create a NumPy array with ten values, each with value 0</td>
</tr>
</table>


## Querying list values

<table class="table">
<tr>
<td markdown="true">
```python
x[2]
```
</td>
<td>
	Returns the **third** value in a list or array x
</td>
</tr>
<tr>
<td markdown="true">
```python
x[a:b]
```
</td>
<td>
	Return values in x with index a through to (b-1)
</td>
</tr>
<tr>
<td markdown="true">
```python
x[a:]
```
</td>
<td>
	Return values in x with index a through to the end of the array
</td>
</tr>
<tr>
<td markdown="true">
```python
x[:b]
```
</td>
<td>
	Return values in x with from the start of the array through to index b
</td>
</tr>
<tr>
<td markdown="true">
```python
[a for a in x if a > 0]
```
</td>
<td>
	Return the values in x greater than zero
</td>
</tr>
</table>


## Variable management

Note these commands will work in Spyder and other "iPython" consoles.

<table class="table">
<tr>
<td markdown="true">
```python
%reset
```
</td>
<td>
	Clear all variables 
</td> 
</tr>
<tr>
<td markdown="true">
```python
%whos
```
</td>
<td>
	View all variables (or use the variables tab)
</td> 
</tr>
</table>

## Some Functions

that do pretty much what you'd expect them to

<table class="table">
<tr>
<td markdown="true">
```python
sum(x)
```
</td>
</tr>
<tr>
<td markdown="true">
```python
min(x)
```
</td>
</tr>
<tr>
<td markdown="true">
```python
max(x)
```
</td>
</tr>
<tr>
<td markdown="true">
```python
len(x)   # (length)
```
</td>
</tr>
<tr>
<td markdown="true">
```python
sorted(x)
```
</td>
</tr>
</table>


## Logical operators

<table class="table">
<tr>
<td markdown="true">
```python
==
```
</td>
<td>
	Equal to
</td> 
</tr>
<tr>
<td markdown="true">
```python
!=
```
</td>
<td>
	Not equal to
</td> 
</tr>
<tr>
<td markdown="true">
```python
>
```
</td>
<td>
	Greater than
</td> 
</tr>
<tr>
<td markdown="true">
```python
>=
```
</td>
<td>
	Greater than or equal to
</td> 
</tr>
<tr>
<td markdown="true">
```python
<
```
</td>
<td>
	Less than
</td> 
</tr>
<tr>
<td markdown="true">
```python
<=
```
</td>
<td>
	Less than or equal to
</td> 
</tr>
<tr>
<td markdown="true">
```python
and
```
</td>
<td>
	And
</td> 
</tr>
<tr>
<td markdown="true">
```python
or
```
</td>
<td>
	Or
</td> 
</tr>
</table>



## Random numbers


<table class="table">
<tr>
<td markdown="true">
```python
np.random.rand() 
```
</td>
<td>
	Random number in [0,1]
</td>
</tr>
<tr>
<td markdown="true">
```python
np.random.rand(2,2)  
```
</td>
<td>
	Random numbers in [0,1], distributed in a 2 x 2 array
</td>
</tr>
<tr>
<td markdown="true">
```python
np.random.randint(0,10)   
```
</td>
<td>
	Random integer between 0 and 9
</td>
</tr>
<tr>
<td markdown="true">
```python
np.random.normal(0,1)  
```
</td>
<td>
	Random number from the normal distribution with mean 0 and s.d. 1
</td>
</tr>
</table>


## Plotting example

Sample plot

```python
import numpy as np
import matplotlib.pyplot as plt

# Set up an array
x = np.linspace(0,10,100)

# Create a figure (optional if you need only one)
plt.figure()

plt.plot(x,np.sin(x))
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Plot of sin(x) versus x")

```

## Function example

```python
def add_one(x):
	""" Adds one to the input """
	return x + 1
```


<table class="table">
<tr>
<td markdown="true">
```python
add_one(2)
```
</td>
<td>
	Call the function
</td> 
</tr>
<tr>
<td markdown="true">
```python
help(add_one)
```
</td>
<td>
Get function help
</td> 
</tr>

</table>


## For loop example

```python
for n in range(5):
	print(n)
```

## While loop example

```python
x = 0
while x < 5:
	x += 1
```

## if statement example

```python
x = 2
if x > 0:
	print("positive!")
```


## List comprehension example
```python
[x**2 for x in range(5)]
```

## Exception handling

```python
try:
	add_one("2")
except:
	print("an exception occured")
```
Handling a specific error type:
```python
try:
    add_one("2")
except TypeError:
    print("It's a type error")
except:
    print("It's another error")
```

## Miscellaneous tips

* CTRL-C will stop execution of an infinite loop.

* Be consistent with your indenting in control flow and functions.

* Seek help! If you’ve got a problem then someone, somewhere has also had it! Look for solutions on sites like stackoverflow (though do not post exam questions!), or ask your friendly lecturer!

* Have fun and if you find something that interests you, roll with it!


<style>
.highlight pre {
	margin-bottom: 1px;
}
table {
    border-top: none;
    border-bottom: 1px solid #dee2e6;
}</style>

