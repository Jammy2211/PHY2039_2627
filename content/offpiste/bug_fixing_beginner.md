# Bug Fixing (Beginner)

A bug is a mistake in a program. Finding and fixing bugs is a normal part of
writing Python: you do not need to understand everything before you start!

These three examples are for lecture 2. They start with variables and `print()`,
then introduce choosing with `if` and repeating with `for`. Each example
contains **one deliberate bug**.

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

## Example 2: choosing the right thermostat message

Work through this example together.

An `if` checks a condition: it is either `True` or `False`. The indented lines
under it run only when the condition is `True`. An `else` provides an alternative
when its condition is `False`. A conditional chooses what to do; it is not a
loop, which repeats instructions.

The thermostat should print **exactly one** message:

- `Heating` below 18°C.
- `Cooling` above 24°C.
- `Comfortable` from 18°C to 24°C, including both boundaries.

At 16°C, the expected output is **Heating only**.

```runnable lang="python"
temperature = 16
if temperature < 18:
    print('Heating')
if temperature > 24:
    print('Cooling')
else:
    print('Comfortable')
```

The current program prints **Heating and Comfortable on separate lines**.

- Before the branches, add `print('Below 18:', temperature < 18)` and
  `print('Above 24:', temperature > 24)`. Which condition is `True`?
- Follow the code from top to bottom. Which `if` does the `else` belong to?
- The two `if` statements make separate decisions. Use `elif` ("else if") to
  link the second condition to the first: it is checked only when the first
  condition was false.
- Remove the diagnostic prints and rerun. Check temperatures 16, 21 and 26°C:
  expect `Heating`, `Comfortable` and `Cooling`, respectively, one message each.
- Test the boundaries too: 18 and 24°C should both print `Comfortable`, once.

## Example 3: keeping a running total

Try this example yourself.

A `for` loop takes each value from a list in turn. Here `distance` is first 2,
then 3, then 4 metres. The indented lines repeat for each distance. An unindented
line after the loop runs when the loop finishes.

`total = total + distance` adds the current distance to the running total. The
program should add all three distances and print **9 once**, after the loop.

```runnable lang="python"
for distance in [2, 3, 4]:
    total = 0
    total = total + distance
print(total)
```

The current program prints **4**.

- Inside the loop, immediately after the addition, add
  `print('distance:', distance, 'total:', total)` with the same indentation.
- Trace each repetition. The diagnostic totals are 2, 3 and 4; they should be
  2, 5 and 9. Where does the program lose the distances already added?
- Which statement resets the total? Should it run before every addition, or
  just once before the loop?
- Move the initialisation to run once before the loop, checking the indentation
  of the lines that should still repeat.
- Remove your diagnostic print and rerun the whole block. Does the program
  print the expected total, 9, once?

## What did you learn from the bug?

For each example, explain briefly:

- What caused the problem?
- What evidence helped you find it?
- What did you change?
- How did you check the correction?

An error message is useful evidence. A program that runs without an error can
still give the wrong answer: always compare its output with what it should do.
