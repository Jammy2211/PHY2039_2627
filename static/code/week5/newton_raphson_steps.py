"""Newton–Raphson: one calculation per Enter keypress.

Run: python newton_raphson_steps.py
Click the PLOT WINDOW and press Enter to advance; values print in the console.
In Spyder use an external interactive plot (e.g. run %matplotlib qt first).
Edit the settings below, then rerun to restart. Requires numpy and matplotlib.
"""

import matplotlib.pyplot as plt
import numpy as np

# STUDENT SETTINGS ------------------------------------------------------------
def function(x):
    return x**2 - 2


def derivative(x):
    return 2 * x

X0 = 2.25
X_MIN, X_MAX = -0.25, 2.5
F_TOLERANCE = 1e-5       # Stop when abs(f(x)) is this small.
MAX_ITERATIONS = 30
TITLE = "Newton–Raphson"


def algorithm():
    """Yield one tangent update at a time; no iterations are precomputed."""
    x = float(X0)
    if not np.isfinite([x, F_TOLERANCE]).all() or F_TOLERANCE <= 0:
        raise ValueError("Use a finite starting estimate and a positive F_TOLERANCE.")
    if not isinstance(MAX_ITERATIONS, int) or MAX_ITERATIONS < 1:
        raise ValueError("MAX_ITERATIONS must be a positive integer.")
    fx = finite_value(function, x)
    if abs(fx) <= F_TOLERANCE:
        yield dict(x=x, fx=fx, slope=None, next_x=x, next_f=fx, done=True,
                   message=f"Initial estimate already meets tolerance: x={x:.10g}, "
                           f"f(x)={fx:.6g} (0 updates).")
        return

    for n in range(1, MAX_ITERATIONS + 1):
        slope = finite_value(derivative, x)
        if slope == 0:
            raise ValueError(f"Zero derivative at x={x:.10g}; choose another start.")
        next_x = x - fx / slope
        if not np.isfinite(next_x):
            raise ValueError("The Newton update is non-finite; choose another start.")
        next_f = finite_value(function, next_x)
        done = abs(next_f) <= F_TOLERANCE
        decision = "Use this new estimate for the next tangent."
        if done:
            decision = f"Converged: x ≈ {next_x:.10g}, |f(x)| ≤ {F_TOLERANCE:g}."
        elif next_x == x:
            decision = "Stopped: estimate stagnated; residual is still too large."
        elif n == MAX_ITERATIONS:
            decision = "Stopped: iteration limit reached; NOT converged."
        yield dict(
            x=x, fx=fx, slope=slope, next_x=next_x, next_f=next_f,
            done=done or next_x == x or n == MAX_ITERATIONS,
            message=f"Step {n}: x={x:.10g}, f(x)={fx:.6g}, f'(x)={slope:.6g}\n"
                    f"new x = x - f(x)/f'(x) = {next_x:.10g}; "
                    f"f(new x)={next_f:.6g}\n" + decision,
        )
        if done or next_x == x:
            return
        x, fx = next_x, next_f


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
        x, next_x = step["x"], step["next_x"]
        background((x, next_x))
        if step["slope"] is not None:
            xs = np.array(ax.get_xlim())
            ax.plot(xs, step["fx"] + step["slope"] * (xs - x),
                    color="firebrick", label="tangent at current estimate")
        ax.vlines(x, 0, step["fx"], color="grey", linestyle="--")
        ax.scatter(x, step["fx"], color="darkorange", label="current point", zorder=5)
        ax.scatter(next_x, 0, color="purple", marker="x", s=80,
                   label="next estimate", zorder=5)
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
