"""Bisection: one calculation per Enter keypress.

Run: python bisection_steps.py
Click the PLOT WINDOW and press Enter to advance; values print in the console.
In Spyder use an external interactive plot (e.g. run %matplotlib qt first).
Edit the settings below, then rerun to restart. Requires numpy and matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

# STUDENT SETTINGS ------------------------------------------------------------
def function(x):
    return x**2 - 2

A, B = 0.0, 2.0
X_MIN, X_MAX = -0.25, 2.5
X_TOLERANCE = 1e-5       # Maximum midpoint error for a continuous function.
MAX_ITERATIONS = 50
TITLE = "Bisection"


def algorithm():
    """Yield one midpoint calculation at a time; assume f is continuous on [a,b]."""
    a, b = float(A), float(B)
    if not np.isfinite([a, b, X_TOLERANCE]).all() or a >= b or X_TOLERANCE <= 0:
        raise ValueError("Use finite a < b and a positive X_TOLERANCE.")
    if not isinstance(MAX_ITERATIONS, int) or MAX_ITERATIONS < 1:
        raise ValueError("MAX_ITERATIONS must be a positive integer.")
    fa, fb = finite_value(function, a), finite_value(function, b)
    if fa == 0 or fb == 0:
        root = a if fa == 0 else b
        yield dict(a=a, b=b, mid=root, fm=0.0, done=True,
                   message=f"Exact endpoint root: x = {root:.10g} (0 iterations).")
        return
    if np.signbit(fa) == np.signbit(fb):
        raise ValueError("The interval endpoints must have opposite function signs.")

    for n in range(1, MAX_ITERATIONS + 1):
        mid = a / 2 + b / 2
        if mid == a or mid == b:
            raise ValueError("Floating-point precision exhausted; widen the tolerance.")
        fm = finite_value(function, mid)
        half_width = b / 2 - a / 2
        done = fm == 0 or half_width <= X_TOLERANCE
        keep_left = np.signbit(fa) != np.signbit(fm)
        decision = "Keep [a, midpoint]." if keep_left else "Keep [midpoint, b]."
        if done:
            decision = f"Converged: x ≈ {mid:.10g}; midpoint error ≤ {half_width:.3g}."
        elif n == MAX_ITERATIONS:
            decision = "Stopped: iteration limit reached; NOT converged."
        yield dict(
            a=a, b=b, mid=mid, fm=fm, done=done or n == MAX_ITERATIONS,
            message=f"Step {n}: a={a:.8g}, b={b:.8g}, midpoint={mid:.10g}\n"
                    f"f(a)={fa:.6g}, f(b)={fb:.6g}, f(midpoint)={fm:.6g}\n"
                    + decision,
        )
        if done:
            return
        if keep_left:
            b, fb = mid, fm
        else:
            a, fa = mid, fm


def finite_value(f, x):
    """Evaluate one real, finite function value."""
    value = float(f(x))
    if not np.isfinite(value):
        raise ValueError(f"Non-finite function value at x = {x:g}.")
    return value


def make_demo():
    """Create the interactive figure. No iterations run until Enter is pressed."""
    if not np.isfinite([X_MIN, X_MAX]).all() or X_MIN >= X_MAX:
        raise ValueError("Choose finite plot limits with X_MIN < X_MAX.")
    fig, ax = plt.subplots(figsize=(9, 6))
    fig.subplots_adjust(bottom=0.25)
    status = fig.text(0.07, 0.04, "Click the plot, then press Enter for step 1.",
                      fontsize=10, va="bottom")
    steps = algorithm()
    finished = False

    def background(points=()):
        # Expand the view if an estimate leaves the original plotting range.
        low = min([X_MIN, *points])
        high = max([X_MAX, *points])
        pad = 0.05 * max(high - low, 1.0)
        xs = np.linspace(low - pad, high + pad, 800)
        with np.errstate(all="ignore"):
            ys = np.asarray(function(xs), dtype=float)
            ys = np.broadcast_to(ys, xs.shape)
        if not np.isfinite(ys).any():
            raise ValueError("No finite function values in the plot range.")
        ax.clear()
        ax.plot(xs, np.where(np.isfinite(ys), ys, np.nan), color="navy", label="f(x)")
        ax.axhline(0, color="black", lw=1)
        ax.axvline(0, color="grey", lw=0.7)
        ax.set(xlim=(xs[0], xs[-1]), xlabel="x", ylabel="f(x)",
               title=TITLE + " — press Enter for one step")
        ax.grid(alpha=0.2)

    def on_key(event):
        nonlocal finished
        if event.key not in ("enter", "return") or finished:
            return
        try:
            step = next(steps)
            draw_step(step)
            message = step["message"]
            finished = step["done"]
            if not finished:
                message += "\nPress Enter for the next step."
        except StopIteration:
            finished = True
            message = "Finished. Close the figure or rerun the script."
        except (ValueError, ArithmeticError) as error:
            finished = True
            message = f"Stopped: {error}"
        status.set_text(message)
        print(message, flush=True)
        fig.canvas.draw_idle()

    def draw_step(step):
        a, b, mid = step["a"], step["b"], step["mid"]
        background((a, b, mid))
        ax.axvspan(a, b, color="cornflowerblue", alpha=0.2, label="current bracket")
        ax.scatter([a, b], [function(a), function(b)], color="forestgreen",
                   label="endpoints", zorder=4)
        ax.vlines(mid, 0, step["fm"], color="darkorange", linestyle="--")
        ax.scatter([mid, mid], [0, step["fm"]], color="darkorange",
                   label="midpoint", zorder=5)
        ax.legend(loc="best")

    background()
    ax.legend(loc="best")
    fig.canvas.mpl_connect("key_press_event", on_key)
    print(TITLE, flush=True)
    print("Click inside the plot window, then press Enter. Close it to quit.",
          flush=True)
    return fig


def main():
    # An inline backend produces a static image; it cannot receive Enter events.
    backend = plt.get_backend().lower()
    if "inline" in backend or backend in ("agg", "pdf", "svg", "ps", "pgf", "template"):
        raise RuntimeError(
            "An interactive Matplotlib backend is required. In Spyder run "
            "'%matplotlib qt' in its console before running this file. "
            "From a terminal, use a Python environment with Qt or Tk and a display."
        )
    fig = make_demo()
    plt.show(block=True)


if __name__ == "__main__":
    main()
