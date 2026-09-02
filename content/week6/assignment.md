---
toc: false
css:
  - custom.css
---

# MAS1801 Python Longer Questions


## Shopping

Create a class for a consumer who is going shopping.

The consumer should have the following attributes which are set in the `__init__` function:

* `name` - a string containing their name
* `balance` - the amount of money they have in the bank. Starts off at zero
* `shopping_list` - a list of items (strings) they need to buy. Starts off empty
* `shopping_trolley` - a list of items (strings) they have in their shopping trolley. Starts off empty
* `spend` - the value of the goods in the shopping trolley. Starts off at zero

Create a function (method) in the class for each of the following

* `__init__` - creates a new customer and takes a name argument.
* `deposit` - deposits money in their bank account balance
* `withdraw` - takes money off their bank account balance
* `init_balance` - sets the initial bank balance for the consumer
* `add_to_list` - adds an item (a string) to the consumer's shopping list (`append` should do it)
* `buy_item` - takes in an item string and a price. If the item is in the consumer's shopping list it removes it from the shopping list and adds it to their shopping trolley, as well as updating the value of `spend`
* `checkout` - empties the shopping trolley, updates the consumers bank balance by subtracting `spend` from it, and then zeros `spend`. Perhaps print a confirmatory message "Thank you for shopping at... " or similar.

It should run something like this:

```{.python}
c = Consumer("Chris")    # New consumer called Chris
c.init_balance(500)      # Chris' bank balance is £500

c.add_to_list("apples")  # Add apples to the shopping list
c.add_to_list(["bananas","cherries"])  # ideally you can add multiple things

c.buy_item("grapes",1.65)  # Does nothing as grapes aren't in shopping list
c.buy_item("apples", 1)    # Buy apples
c.buy_item("bananas",0.5)  # Buy bananas

print(c.shopping_trolley)  # Should show apples and bananas
print(c.spend)			   # Should show 1.50

c.checkout()  

print(c.balance)          # Should be 498.50
print(c.shopping_list)    # Should just have cherries in   
```


## Goat Grazing

A goat is tied, with a rope of length $x$, to the corner of a rectangular farm building with sides $a$ and $b$. The farmer is interested in what area of grass is available to the goat for grazing.

\begin{itemize}

\item Solve the problem (I recommend approaching it like you would have the problem solving exercises earlier in the module) to find how the grazing area depends on $a$, $b$ and $x$. You report should include some sort of sketch/image and an explanation of the problem.

\item Write a Python function which takes in $a$, $b$ and $x$ as input, and returns the area that the goat has to graze in. Your function should check for invalid input values and consider cases where $x\le a+b$ (the cases beyond that are much more difficult).

\item Consider the case where the farmer already has a building, which has dimensions 8m x 12m, and use your Python function to investigate how the available area changes with the rope length $x$. Include a plot to illustrate.

\item Consider the case where the farmer already has a rope of 15m in length, and is setting up a building for the goat to be attached to. The farmer has bricks to create a building with a 40m perimeter and would like to use them all. Use your MATLAB function to investigate how changing the proportions of the building (i.e. changing $a$ and $b$) will in turn change the grazing area. Include a plot to illustrate.