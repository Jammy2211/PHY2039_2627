"""Flat root: f(x) = (x - 1)**7.

Edit NUMBER_OF_STEPS, then run the whole file. No keypresses are needed.

The animation opens in a separate Tk window, including when run in PyCharm.
If PyCharm still captures it, disable 'Show plots in tool window' in settings.
"""

import numpy as np
import matplotlib

# Use a real plot window rather than the IDE's static plot viewer.
# This must come BEFORE importing pyplot. Tk is included with standard Python.
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


# 1. SETTINGS ----------------------------------------------------------------

NUMBER_OF_STEPS = 5
PAUSE_SECONDS = 1.0

X_MIN = -0.25
X_MAX = 3.25

STARTING_X = 2.25


# 2. THE FUNCTION AND ITS DERIVATIVE ------------------------------------------

def f(x):
    return (x - 1)**7


def derivative(x):
    return 7 * (x - 1)**6


# 3. PREPARE THE FIGURE -------------------------------------------------------

# Raise an error if the settings would prevent the animation from running.
if NUMBER_OF_STEPS < 1 or PAUSE_SECONDS <= 0:
    raise ValueError("Use at least one step and a positive pause time.")

plot_x = np.linspace(X_MIN, X_MAX, 500)

plt.ion()
fig, ax = plt.subplots(figsize=(9, 6))
fig.subplots_adjust(bottom=0.22)
step_text = fig.text(0.12, 0.04, "", fontsize=11)


# 4. NEWTON–RAPHSON -----------------------------------------------------------

x = STARTING_X


for step in range(1, NUMBER_OF_STEPS + 1):

    # Calculate the function value and slope at the current estimate.
    f_x = f(x)
    slope = derivative(x)

    if f_x == 0:
        print(f"Exact root found at x = {x:.10f}", flush=True)
        break

    # We cannot divide by a zero or undefined slope.
    if slope == 0 or not np.isfinite(slope):
        raise ValueError("The derivative must be finite and non-zero. Try another starting x.")

    # The tangent meets the x-axis at the next estimate.
    next_x = x - f_x / slope
    f_next = f(next_x)

    if not np.isfinite([next_x, f_next]).all():
        raise ValueError("The new estimate or function value is not finite.")

    # Print this step.
    print(f"\nStep {step}", flush=True)
    print(f"  x = {x:.8f}, f(x) = {f_x:.3e}, derivative = {slope:.8f}")
    print(f"  next_x = x - f(x) / derivative = {next_x:.8f}")
    print(f"  f(next_x) = {f_next:.3e}", flush=True)

    # Expand the view if the new estimate leaves the original plot range.
    plot_left = min(X_MIN, x, next_x) - 0.1
    plot_right = max(X_MAX, x, next_x) + 0.1
    plot_x = np.linspace(plot_left, plot_right, 500)
    tangent_y = f_x + slope * (plot_x - x)

    # Draw the curve, tangent and next estimate.
    ax.clear()
    ax.plot(plot_x, f(plot_x), color="navy", label="f(x)")
    ax.axhline(0, color="black", linewidth=1)
    ax.plot(plot_x, tangent_y, color="firebrick", label="tangent")

    ax.plot([x, x], [0, f_x], "--", color="grey")
    ax.scatter(x, f_x, color="darkorange", label="current point")
    ax.scatter(next_x, 0, color="purple", marker="x", s=80,
               label="next estimate")

    ax.set_title(f"Newton–Raphson: step {step} of {NUMBER_OF_STEPS}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(alpha=0.2)

    step_text.set_text(
        f"x = {x:.8f}     next_x = {next_x:.8f}\n"
        f"f(next_x) = {f_next:.3e}"
    )

    # Show the graph and pause briefly before the next step.
    fig.canvas.draw_idle()
    plt.pause(PAUSE_SECONDS)

    # Update the estimate.
    previous_x = x
    x = next_x

    if x == previous_x:
        print("Stopped: the estimate no longer changes at this precision.", flush=True)
        break


print(f"\nLast root estimate: {x:.10f}", flush=True)
print(f"Function value at this estimate: {f(x):.10g}")

print(f"Distance from the true root x=1: {abs(x - 1):.8g}")

# Keep the final graph available.
plt.ioff()
plt.show(block=True)
