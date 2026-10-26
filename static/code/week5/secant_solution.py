"""Completed secant animation: run this file to see the solution.

Edit NUMBER_OF_STEPS and PAUSE_SECONDS below to change the animation.
Uses the same separate Tk window as the other root-finding demonstrations.
"""

import numpy as np
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt


# 1. SETTINGS ----------------------------------------------------------------

NUMBER_OF_STEPS = 5
PAUSE_SECONDS = 1.0

STARTING_X0 = 0.5
STARTING_X1 = 2.0

X_MIN = -0.25
X_MAX = 2.5


# 2. THE FUNCTION -------------------------------------------------------------

def f(x):
    return x**2 - 2


# 3. PREPARE THE FIGURE -------------------------------------------------------

if NUMBER_OF_STEPS < 1 or PAUSE_SECONDS <= 0:
    raise ValueError("Use at least one step and a positive pause time.")

plt.ion()
fig, ax = plt.subplots(figsize=(9, 6))
fig.subplots_adjust(bottom=0.22)
step_text = fig.text(0.12, 0.04, "", fontsize=11)


# 4. THE SECANT METHOD --------------------------------------------------------

x0 = STARTING_X0
x1 = STARTING_X1


for step in range(1, NUMBER_OF_STEPS + 1):

    # Evaluate the function at the two current estimates.
    f0 = f(x0)
    f1 = f(x1)

    if f0 == 0 or f1 == 0:
        if f0 == 0:
            x1 = x0
        print(f"Exact root found at x = {x1:.10f}", flush=True)
        break

    if x0 == x1 or f0 == f1:
        raise ValueError("Choose two different estimates with different function values.")

    # Secant update: find where the line through the two points meets y = 0.
    next_x = x1 - f1 * (x1 - x0) / (f1 - f0)

    if not np.isfinite(next_x):
        raise ValueError("The secant update must give a finite number.")

    f_next = f(next_x)

    # Print this step.
    print(f"\nStep {step}", flush=True)
    print(f"  x0 = {x0:.8f}, f(x0) = {f0:.6g}")
    print(f"  x1 = {x1:.8f}, f(x1) = {f1:.6g}")
    print(f"  next_x = {next_x:.8f}, f(next_x) = {f_next:.6g}", flush=True)

    # Draw the curve and the secant through the two points.
    plot_left = min(X_MIN, x0, x1, next_x) - 0.1
    plot_right = max(X_MAX, x0, x1, next_x) + 0.1
    plot_x = np.linspace(plot_left, plot_right, 500)

    slope = (f1 - f0) / (x1 - x0)
    secant_y = f1 + slope * (plot_x - x1)

    ax.clear()
    ax.plot(plot_x, f(plot_x), color="navy", label="f(x)")
    ax.axhline(0, color="black", linewidth=1)
    ax.plot(plot_x, secant_y, color="firebrick", label="secant")
    ax.scatter([x0, x1], [f0, f1], color="darkorange", label="current points")
    ax.scatter(next_x, 0, color="purple", marker="x", s=80,
               label="next estimate")

    ax.set_title(f"Secant method: step {step} of {NUMBER_OF_STEPS}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(alpha=0.2)

    step_text.set_text(
        f"x0 = {x0:.8f}     x1 = {x1:.8f}\n"
        f"next_x = {next_x:.8f}     f(next_x) = {f_next:.6g}"
    )

    fig.canvas.draw_idle()
    plt.pause(PAUSE_SECONDS)

    # Move the estimates along: discard the oldest one.
    x0 = x1
    x1 = next_x


print(f"\nLast root estimate: {x1:.10f}", flush=True)
print(f"Function value at this estimate: {f(x1):.6g}")

plt.ioff()
plt.show(block=True)
