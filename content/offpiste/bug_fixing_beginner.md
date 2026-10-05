# Bug Fixing (Beginner)

A bug is a mistake in a program. Finding and fixing bugs is a normal part of
writing Python: you do not need to understand everything before you start!

The first three examples are for lecture 2. They use variables, arithmetic and
`print()`. Leave the optional fourth example until you have studied `for` loops.
Each example contains **one deliberate bug**.

## A routine for finding bugs

1. **Predict:** read what the program should do and work out the expected result.
2. **Run:** run the code and compare what happens with your prediction.
3. **Read:** if Python reports an error, read the final line of the error message
   first. It names the error and gives a clue. Then look for the line of your
   code identified in the error report.
4. **Inspect:** use `print()` to check intermediate values. Put these checks
   before a failing line: Python stops at the error, so later prints will not run.
5. **Change one thing:** use the evidence to choose a correction.
6. **Rerun:** run the whole block again and check the output against the intended
   result. Remove temporary diagnostic prints when you finish.

Treat each code block as a separate program. Rerun it from its initial state,
including the starting assignments, rather than running only the lines you
changed. If you use a notebook, do not rely on variables left over from other
examples.

## Example 1: a name Python does not recognise

We will work through this example in the lecture.

The program should calculate the area of a rectangle with length 5 and width 3,
then print **15**.

```runnable lang="python"
length = 5
width = 3
area = lenght * width
print(area)
```

Run the code and read the error message. A `NameError` means Python has reached
a name that has not been defined. The error report identifies the name and the
line where Python encountered it; the displayed line number may depend on where
you run the code.

- Which name does the error mention?
- Compare it carefully with the names in the first two lines. Are their spellings
  identical?
- Put `print(length, width)` before the area calculation. What does this tell
  you about the values available before the error?
- Correct the name, remove your diagnostic print and rerun the whole block.
  Does it print the expected area?

## Example 2: it runs, but is the answer right?

Work through this example together.

The program should calculate the perimeter of a rectangle with length 5 and
width 3, then print **16**. The perimeter is the sum of all four sides.

```runnable lang="python"
length = 5
width = 3
perimeter = 2 * length + width
print(perimeter)
```

The current program prints **13**, without an error message.

- Calculate the perimeter by hand. How many lengths and how many widths must
  you include?
- Python performs multiplication before addition. Which value does the current
  expression double?
- Print `2 * length` and `width` separately to see the two contributions.
- Where could parentheses make Python add the length and width before doubling?
  Change the calculation, remove diagnostic prints and check that the output is
  now 16.

## Example 3: printing the wrong value

Try this example yourself.

Each item costs 4 pounds and you buy 3 items. The program should calculate the
total cost and print **12**.

```runnable lang="python"
price = 4
quantity = 3
total = price * quantity
print(price)
```

The current program prints **4**.

- Add a temporary `print(total)` immediately after the calculation. Is the
  calculated total correct?
- Follow the value from the calculation to the original final line. Which
  variable does that line actually print?
- Change the original output line, remove your diagnostic print and rerun.
  Does the program print the total once?

## Optional extension: when does a line run?

**Attempt this only after you have learned about `for` loops.**

The program should add 1, 2 and 3, then print **only the final total, 6**, once.

```runnable lang="python"
total = 0
for number in [1, 2, 3]:
    total = total + number
    print(total)
```

The current program prints **1, 3 and 6 on separate lines**. In Python,
indentation determines which lines belong to the loop. An indented line in this
loop runs once for each value of `number`.

- Trace the loop on paper. Make a table with columns for `number`, `total` after
  the addition, and what gets printed.
- Should the print happen during every repetition, or after the loop finishes?
- Change **only the indentation** of the print line. Rerun the whole block,
  starting with `total = 0`, and check that the only output is 6.

## What did you learn from the bug?

For each example, explain briefly:

- What caused the problem?
- What evidence helped you find it?
- What did you change?
- How did you check the correction?

An error message is useful evidence. A program that runs without an error can
still give the wrong answer: always compare its output with what it should do.
