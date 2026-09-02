### Exercise 1.5 {: .exercise}

A scientist measures the weight of an unstable isotope over a number of days and records the results.


Day       |   1  |  2   |  3   |  4  |  5  |  6  |  7  |  8  |  9  |  10
----------|------|------|------|-----|-----|-----|-----|-----|-----|-----
Weight(g) | 24.3 | 18.1 | 11.7 | 7.3 | 4.9 | 2.9 | 2.6 | 1.5 | 1.0 | 0.5


* Set up some variables and make a plot.

* Fit an exponential function of the form $y=a\exp(bx)$ to the data by using the transformed equation you obtained in the first part of the last exercise (if you didn't get that done, see the hint to that exercise!). In doing so, you should verify that a lin-log (linear $x$ axis and log $y$ axis) looks like a straight line, by using the plotting function `semilogy`.

* Use `polyfit` to obtain values for $a$ and $b$.

* Verify that on day 0 there was around 40 g of the isotope.

* Make a lin-lin plot (linear $x$ axis and linear $y$ axis - just the normal `plot` command) to illustrate the fit.


