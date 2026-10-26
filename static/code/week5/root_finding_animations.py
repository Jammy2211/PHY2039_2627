"""Animate the bisection and Newton--Raphson root-finding methods.

Original timed prototype. For the reviewed, Enter-controlled teaching versions,
run bisection_steps.py or newton_raphson_steps.py in this directory instead.

Run this file in Spyder, or from a terminal with:

    python root_finding_animations.py

The default display compares both methods.  To show just one method, use:

    python root_finding_animations.py --method bisection
    python root_finding_animations.py --method newton

Press the space bar while the figure is selected to pause or resume it.

To try another function, edit the functions and starting values in the
"Student settings" section below.  Use NumPy functions such as np.sin(x),
rather than functions from the math module, so that plotting still works.

In Spyder, animations work best with an interactive graphics backend.  If the
plot appears only as a still image, select an Automatic or Qt backend in
Tools > Preferences > IPython console > Graphics.
"""

import argparse
from pathlib import Path

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Student settings: this is the main section to edit
# =============================================================================

def function(x):
    """The function whose root we want to find."""
    return x**2 - 2


def derivative(x):
    """The derivative of function(x), needed by Newton--Raphson."""
    return 2 * x


# Range displayed on the horizontal axis.
X_MIN = -0.25
X_MAX = 2.50

# Starting interval [a, b] for bisection.  The function must change sign.
BISECTION_A = 0.0
BISECTION_B = 2.0

# Starting estimate for Newton--Raphson.
NEWTON_X0 = 2.25

TOLERANCE = 1e-5
MAX_ITERATIONS = 30
FRAME_INTERVAL_MS = 900


# =============================================================================
# Root-finding algorithms
# =============================================================================

def bisection(f, a, b, tolerance=1e-5, max_iterations=100):
    """Return a root estimate and a record of every bisection step."""
    fa = float(f(a))
    fb = float(f(b))

    if not np.isfinite([fa, fb]).all():
        raise ValueError("The function must be finite at both interval ends.")
    if fa == 0:
        return a, [{"iteration": 0, "a": a, "b": a, "mid": a, "f_mid": fa}]
    if fb == 0:
        return b, [{"iteration": 0, "a": b, "b": b, "mid": b, "f_mid": fb}]
    if fa * fb > 0:
        raise ValueError(
            "Bisection needs function(a) and function(b) to have opposite signs."
        )

    history = []

    for iteration in range(max_iterations):
        mid = (a + b) / 2
        f_mid = float(f(mid))

        history.append(
            {"iteration": iteration, "a": a, "b": b, "mid": mid, "f_mid": f_mid}
        )

        if abs(f_mid) < tolerance or (b - a) / 2 < tolerance:
            return mid, history

        if fa * f_mid < 0:
            b = mid
            fb = f_mid
        else:
            a = mid
            fa = f_mid

    raise RuntimeError("Bisection did not converge within max_iterations.")


def newton_raphson(f, dfdx, x0, tolerance=1e-5, max_iterations=100):
    """Return a root estimate and a record of every Newton--Raphson step."""
    x = float(x0)
    history = []

    for iteration in range(max_iterations):
        fx = float(f(x))
        gradient = float(dfdx(x))

        if not np.isfinite([fx, gradient]).all():
            raise ValueError("The function and derivative must remain finite.")
        if abs(fx) < tolerance:
            history.append(
                {
                    "iteration": iteration,
                    "x": x,
                    "f_x": fx,
                    "gradient": gradient,
                    "next_x": x,
                }
            )
            return x, history
        if abs(gradient) < 1e-14:
            raise ZeroDivisionError(
                f"The derivative is too close to zero at x = {x:.6g}."
            )

        next_x = x - fx / gradient
        history.append(
            {
                "iteration": iteration,
                "x": x,
                "f_x": fx,
                "gradient": gradient,
                "next_x": next_x,
            }
        )

        if abs(next_x - x) < tolerance:
            return next_x, history
        x = next_x

    raise RuntimeError("Newton--Raphson did not converge within max_iterations.")


# =============================================================================
# Animation code
# =============================================================================

def _set_up_axes(ax, x_values, y_values, title):
    """Draw the parts of a graph shared by both animations."""
    ax.plot(x_values, y_values, color="navy", linewidth=2, label="$f(x)$")
    ax.axhline(0, color="black", linewidth=1)
    ax.axvline(0, color="black", linewidth=1)
    ax.set_xlim(X_MIN, X_MAX)

    finite_y = y_values[np.isfinite(y_values)]
    if finite_y.size == 0:
        raise ValueError("The function is not finite anywhere in the plot range.")
    low = min(float(finite_y.min()), 0.0)
    high = max(float(finite_y.max()), 0.0)
    padding = 0.12 * max(high - low, 1.0)
    ax.set_ylim(low - padding, high + padding)

    ax.set_xlabel("$x$")
    ax.set_ylabel("$f(x)$")
    ax.set_title(title)
    ax.grid(alpha=0.2)


def make_animation(method="both", interval_ms=FRAME_INTERVAL_MS):
    """Create and return the figure and Matplotlib animation."""
    bisection_root, bisection_history = bisection(
        function,
        BISECTION_A,
        BISECTION_B,
        tolerance=TOLERANCE,
        max_iterations=MAX_ITERATIONS,
    )
    newton_root, newton_history = newton_raphson(
        function,
        derivative,
        NEWTON_X0,
        tolerance=TOLERANCE,
        max_iterations=MAX_ITERATIONS,
    )

    if method == "both":
        figure, axes = plt.subplots(1, 2, figsize=(13, 5.5))
        axes = list(axes)
        frame_count = max(len(bisection_history), len(newton_history))
    elif method == "bisection":
        figure, axis = plt.subplots(figsize=(7, 5.5))
        axes = [axis]
        frame_count = len(bisection_history)
    else:
        figure, axis = plt.subplots(figsize=(7, 5.5))
        axes = [axis]
        frame_count = len(newton_history)

    x_values = np.linspace(X_MIN, X_MAX, 600)
    y_values = np.asarray(function(x_values), dtype=float)
    if y_values.shape != x_values.shape:
        raise ValueError("function(x) must return one value for every input x.")

    def draw_bisection(ax, frame):
        step = bisection_history[min(frame, len(bisection_history) - 1)]
        a = step["a"]
        b = step["b"]
        mid = step["mid"]

        _set_up_axes(ax, x_values, y_values, "Bisection method")
        ax.axvspan(a, b, color="cornflowerblue", alpha=0.18, label="bracket")
        ax.vlines([a, b], 0, [function(a), function(b)], colors="grey", linestyles="--")
        ax.scatter(
            [a, b],
            [function(a), function(b)],
            color=["forestgreen", "firebrick"],
            s=55,
            zorder=3,
        )
        ax.vlines(mid, 0, function(mid), color="darkorange", linestyle="--")
        ax.scatter(mid, function(mid), color="darkorange", s=70, zorder=4)
        ax.scatter(mid, 0, color="darkorange", marker="x", s=70, zorder=4)
        ax.text(
            0.03,
            0.97,
            f"iteration {step['iteration']}\n"
            f"a = {a:.6f}\n"
            f"b = {b:.6f}\n"
            f"midpoint = {mid:.6f}\n"
            f"f(midpoint) = {step['f_mid']:.3e}",
            transform=ax.transAxes,
            va="top",
            bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "0.8"},
        )
        ax.legend(loc="lower right")

    def draw_newton(ax, frame):
        step_number = min(frame, len(newton_history) - 1)
        step = newton_history[step_number]
        x = step["x"]
        next_x = step["next_x"]
        tangent = step["f_x"] + step["gradient"] * (x_values - x)

        _set_up_axes(ax, x_values, y_values, "Newton--Raphson method")
        ax.plot(x_values, tangent, color="firebrick", linewidth=1.8, label="tangent")
        ax.vlines(x, 0, step["f_x"], color="grey", linestyle="--")
        ax.scatter(x, step["f_x"], color="darkorange", s=70, zorder=4)
        ax.scatter(next_x, 0, color="purple", marker="x", s=80, zorder=4)

        previous_estimates = [item["x"] for item in newton_history[: step_number + 1]]
        ax.scatter(
            previous_estimates,
            np.zeros(len(previous_estimates)),
            color="purple",
            s=25,
            alpha=0.45,
            label="estimates",
        )
        ax.text(
            0.03,
            0.97,
            f"iteration {step['iteration']}\n"
            f"x_n = {x:.6f}\n"
            f"f(x_n) = {step['f_x']:.3e}\n"
            f"x_(n+1) = {next_x:.6f}",
            transform=ax.transAxes,
            va="top",
            bbox={"facecolor": "white", "alpha": 0.88, "edgecolor": "0.8"},
        )
        ax.legend(loc="lower right")

    def update(frame):
        for ax in axes:
            ax.clear()
        if method == "both":
            draw_bisection(axes[0], frame)
            draw_newton(axes[1], frame)
        elif method == "bisection":
            draw_bisection(axes[0], frame)
        else:
            draw_newton(axes[0], frame)
        return axes

    figure.suptitle("Finding a root: press SPACE to pause or resume", fontsize=14)
    figure.tight_layout(rect=(0, 0, 1, 0.95))

    movie = animation.FuncAnimation(
        figure,
        update,
        frames=frame_count,
        interval=interval_ms,
        repeat=True,
        repeat_delay=1500,
        blit=False,
        cache_frame_data=False,
    )

    paused = {"value": False}

    def toggle_pause(event):
        if event.key == " ":
            if paused["value"]:
                movie.event_source.start()
            else:
                movie.event_source.stop()
            paused["value"] = not paused["value"]

    figure.canvas.mpl_connect("key_press_event", toggle_pause)

    print(f"Bisection estimate:      {bisection_root:.10f}")
    print(f"Bisection iterations:    {len(bisection_history)}")
    print(f"Newton--Raphson estimate: {newton_root:.10f}")
    print(f"Newton iterations:        {len(newton_history)}")

    return figure, movie


def parse_arguments():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--method",
        choices=("both", "bisection", "newton"),
        default="both",
        help="which animation to display (default: both)",
    )
    parser.add_argument(
        "--interval",
        type=int,
        default=FRAME_INTERVAL_MS,
        help="milliseconds between animation frames",
    )
    parser.add_argument(
        "--save",
        type=Path,
        help="optionally save the animation as a GIF",
    )
    parser.add_argument(
        "--no-show",
        action="store_true",
        help=argparse.SUPPRESS,
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    figure, movie = make_animation(args.method, args.interval)

    if args.save is not None:
        if args.save.suffix.lower() != ".gif":
            raise ValueError("The --save filename must end in .gif")
        print(f"Saving animation to {args.save} ...")
        movie.save(args.save, writer="pillow", dpi=100)
        print("Animation saved.")

    if not args.no_show:
        plt.show()
    else:
        plt.close(figure)


if __name__ == "__main__":
    main()
