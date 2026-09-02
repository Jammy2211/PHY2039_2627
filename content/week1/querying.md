

## Querying and manipulating arrays

Consider the following array set up using `np.arange()`

```python
x = np.arange(0,15)
```

We saw earlier that, for example, the element with index 5 (6th in the list) can be found with 

```python
x[0]
```

And we can also use this to set a value 

```python
x[0] = 5
```

Using a similar idea, we can find the values greater than 

```python
x[x>10]
```

We could also find the number of values 

```python
len(x[x>10])
```

Note that the command `x>10` returns an array of logicals

```python
x>10
```
i.e. a `True` or `False` for each element in the array. We'll come back to logical expressions next week.

### Exercise 1.6 {: .exercise}

Look up the help for the *numpy* function `zeros()` to create a vector

$$[0, 0, 0, 0, 1, 0, 0, 0, 0, 0]$$

(i.e. don't just add the elements individually)

It's likely that your array will contain floating point numbers. Take another look at the help for `zeros` and see if you set up the array with integers instead

