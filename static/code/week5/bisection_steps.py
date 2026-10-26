"""Edit NUMBER_OF_STEPS, then run the whole file. No keypresses are needed.

For a moving plot, use an external plot window in Spyder or PyCharm.
An inline plot viewer may show only the final image.
"""

import numpy as np
import matplotlib.pyplot as plt


# 1. SETTINGS ----------------------------------------------------------------

NUMBER_OF_STEPS = 5
PAUSE_SECONDS = 1.0

X_MIN = -0.25
X_MAX = 2.5

LEFT = 0.0
RIGHT = 2.0


# 2. THE FUNCTION -------------------------------------------------------------

def f(x):
    return x**2 - 2


# 3. PREPARE THE FIGURE -------------------------------------------------------

if not isinstance(NUMBER_OF_STEPS, int) or NUMBER_OF_STEPS < 1:
    raise ValueError("NUMBER_OF_STEPS must be a positive integer.")

if not np.isfinite(PAUSE_SECONDS) or PAUSE_SECONDS <= 0:
    raise ValueError("PAUSE_SECONDS must be positive.")

plot_x = np.linspace(X_MIN, X_MAX, 500)

fig, ax = plt.subplots(figsize=(9, 6))
fig.subplots_adjust(bottom=0.22)
step_text = fig.text(0.12, 0.04, "", fontsize=11)


# 4. BISECTION ---------------------------------------------------------------
# Assume f is continuous between left and right.

left = LEFT
right = RIGHT

if not np.isfinite([left, right, f(left), f(right)]).all():
    raise ValueError("The endpoints and function values must be finite.")

if left >= right or f(left) * f(right) > 0:
    raise ValueError("Choose LEFT < RIGHT with opposite function signs.")


for step in range(1, NUMBER_OF_STEPS + 1):

    # Calculate the midpoint.
    midpoint = (left + right) / 2

    # An endpoint may already be an exact root.
    if f(left) == 0:
        midpoint = left
    elif f(right) == 0:
        midpoint = right

    f_midpoint = f(midpoint)

    if not np.isfinite(f_midpoint):
        raise ValueError("The function is not finite at the midpoint.")

    # Decide which half to keep.
    if f_midpoint == 0:
        decision = "Exact root found."
    elif f(left) * f_midpoint < 0:
        decision = "Keep the left half: replace right with midpoint."
    else:
        decision = "Keep the right half: replace left with midpoint."

    # Print this step.
    print(f"\nStep {step}", flush=True)
    print(f"  left = {left:.8f}, right = {right:.8f}")
    print(f"  midpoint = {midpoint:.8f}, f(midpoint) = {f_midpoint:.8f}")
    print(f"  {decision}", flush=True)

    # Draw the curve, current interval and midpoint.
    ax.clear()
    ax.plot(plot_x, f(plot_x), color="navy", label="f(x)")
    ax.axhline(0, color="black", linewidth=1)

    ax.axvspan(left, right, color="cornflowerblue", alpha=0.2,
               label="current interval")
    ax.scatter([left, right], [f(left), f(right)], color="green",
               label="endpoints")
    ax.plot([midpoint, midpoint], [0, f_midpoint], "--", color="darkorange")
    ax.scatter(midpoint, f_midpoint, color="darkorange", label="midpoint")

    ax.set_title(f"Bisection: step {step} of {NUMBER_OF_STEPS}")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(alpha=0.2)

    step_text.set_text(
        f"midpoint = {midpoint:.8f}     f(midpoint) = {f_midpoint:.8f}\n"
        + decision
    )

    # Show the graph and pause briefly before the next step.
    plt.pause(PAUSE_SECONDS)

    if f_midpoint == 0 or not plt.fignum_exists(fig.number):
        break

    # Update the interval.
    if f(left) * f_midpoint < 0:
        right = midpoint
    else:
        left = midpoint


print(f"\nLast root estimate: {midpoint:.10f}", flush=True)
print("Increase NUMBER_OF_STEPS to investigate the accuracy.")

# Keep the final graph available.
plt.show()
