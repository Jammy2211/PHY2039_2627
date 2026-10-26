Week 5 root-finding challenges
=============================

Run any script directly in PyCharm, Spyder, or a terminal. Each is standalone
and uses the same separate Tk plot window as the working demonstrations.
Requires numpy, matplotlib and Tk. Set NUMBER_OF_STEPS to 5, then try 10.
PAUSE_SECONDS controls the time between updates. Close the plot to finish.

From this folder:
    python flat_root_bisection.py
    python flat_root_newton_raphson.py
    python apparent_root_bisection.py
    python apparent_root_newton_raphson.py

Flat root: (x - 1)**7
    Bisection interval: [0, 3]. Newton initial estimate: 2.25.
    True root: 1. Compare distance from 1 with the function value.
    Newton's error decreases by a factor of 6/7 each update.
    Bisection continues halving its bracket normally.
    Function values use scientific notation so tiny values do not look like zero.

Apparent root: 1/x
    Bisection interval: [-1, 2]. Newton initial estimate: 1.
    There is NO root. Bisection approaches the discontinuity at zero;
    Newton doubles its estimate while its function value halves.
    The bisection plot separates the branches at zero and limits the vertical
    axis to [-12, 12]; later midpoint values can lie outside the visible plot.
    Read the console values too. This intentionally violates the continuity
    assumption needed for bisection; a sign change alone is insufficient.
