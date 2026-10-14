"""Generate every illustration used in the notes (vector SVG, matplotlib).

Run:  python3 figures.py        -> writes ../figs/*.svg
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch, Circle, Arc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "figs")
os.makedirs(OUT, exist_ok=True)

INDIGO = "#2b2d6e"
TEAL = "#0f9d8a"
AMBER = "#f2a900"
CORAL = "#e4572e"
PLUM = "#8e44ad"
GRAY = "#6b7280"
LIGHT = "#e5e7eb"
SKY = "#3b82c4"

plt.rcParams.update({
    "svg.fonttype": "path",
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "cm",
    "font.size": 10,
    "axes.linewidth": 1.0,
    "axes.edgecolor": "#374151",
    "axes.labelcolor": "#111827",
    "xtick.color": "#374151",
    "ytick.color": "#374151",
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "lines.linewidth": 2.0,
    "figure.dpi": 100,
})


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".svg"), format="svg", bbox_inches="tight", pad_inches=0.08)
    plt.close(fig)
    print("wrote", name)


def mathaxes(ax, xlim, ylim, xt=None, yt=None, grid=True, labels=True, aspect=None):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position(("data", 0) if xlim[0] < 0 < xlim[1] else ("data", xlim[0]))
    ax.spines["bottom"].set_position(("data", 0) if ylim[0] < 0 < ylim[1] else ("data", ylim[0]))
    if xt is not None:
        ax.set_xticks(xt)
    if yt is not None:
        ax.set_yticks(yt)
    if grid:
        ax.grid(True, color=LIGHT, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    ax.plot(1, ylim[0] if not (ylim[0] < 0 < ylim[1]) else 0, ">", color="#374151", ms=5,
            transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(xlim[0] if not (xlim[0] < 0 < xlim[1]) else 0, 1, "^", color="#374151", ms=5,
            transform=ax.get_xaxis_transform(), clip_on=False)
    if labels:
        ax.set_xlabel("x", loc="right", labelpad=-6, fontsize=10, style="italic")
        ax.set_ylabel("y", loc="top", rotation=0, labelpad=-8, fontsize=10, style="italic")
    if aspect:
        ax.set_aspect(aspect)
    # hide the "0" tick duplicate clutter
    ax.tick_params(length=3)


def dot(ax, x, y, filled=True, color=INDIGO, s=46, z=5):
    ax.scatter([x], [y], s=s, facecolor=color if filled else "white", edgecolor=color, linewidth=1.6, zorder=z)


# ---------------------------------------------------------------------------
# 0. Foundations
# ---------------------------------------------------------------------------
def fig_gallery():
    fig, axs = plt.subplots(2, 4, figsize=(9.2, 4.6))
    xs = np.linspace(-3, 3, 600)
    specs = [
        ("$y=x^2$  (parabola)", lambda x: x**2, (-3, 3), (-1, 6), INDIGO),
        ("$y=x^3$  (cubic)", lambda x: x**3, (-2, 2), (-6, 6), TEAL),
        ("$y=1/x$  (hyperbola)", None, (-4, 4), (-4, 4), CORAL),
        ("$y=|x|$  (V-shape)", np.abs, (-3, 3), (-1, 4), PLUM),
        ("$y=\\sqrt{x}$", None, (-1, 6), (-1, 3), AMBER),
        ("$y=\\sin x$", np.sin, (-2 * np.pi, 2 * np.pi), (-1.6, 1.6), SKY),
        ("$y=e^x$", np.exp, (-3, 3), (-1, 8), INDIGO),
        ("$y=\\ln x$", None, (-0.5, 6), (-3, 3), TEAL),
    ]
    for ax, (title, f, xl, yl, c) in zip(axs.ravel(), specs):
        mathaxes(ax, xl, yl, labels=False, grid=True)
        if "1/x" in title:
            for a, b in ((-4, -0.12), (0.12, 4)):
                x = np.linspace(a, b, 300)
                ax.plot(x, 1 / x, color=c)
        elif "sqrt" in title:
            x = np.linspace(0, 6, 300)
            ax.plot(x, np.sqrt(x), color=c)
        elif "ln x" in title:
            x = np.linspace(0.02, 6, 400)
            ax.plot(x, np.log(x), color=c)
        else:
            x = np.linspace(xl[0], xl[1], 500)
            ax.plot(x, f(x), color=c)
        ax.set_title(title, fontsize=9.5, color=INDIGO, pad=6)
        ax.set_xticks([])
        ax.set_yticks([])
    fig.tight_layout(h_pad=1.2, w_pad=0.8)
    save(fig, "fig_gallery")


def fig_unit_circle():
    fig, ax = plt.subplots(figsize=(5.6, 5.6))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=INDIGO, lw=2)
    ax.axhline(0, color="#374151", lw=1)
    ax.axvline(0, color="#374151", lw=1)
    for a in (30, 45, 60):
        r = np.deg2rad(a)
        ax.plot([0, np.cos(r)], [0, np.sin(r)], color=TEAL, lw=1.4)
        ax.scatter([np.cos(r)], [np.sin(r)], color=TEAL, s=34, zorder=5)
    for a in (0, 90, 180, 270):
        r = np.deg2rad(a)
        ax.scatter([np.cos(r)], [np.sin(r)], color=CORAL, s=34, zorder=5)
    # outside labels, pushed radially away from the circle
    for a, lab in ((0, "0\u00b0"), (30, "30\u00b0"), (45, "45\u00b0"), (60, "60\u00b0"), (90, "90\u00b0"),
                   (180, "180\u00b0"), (270, "270\u00b0")):
        r = np.deg2rad(a)
        off = 1.17 if a not in (0, 180) else 1.2
        ax.text(off * np.cos(r), off * np.sin(r), lab, ha="center", va="center", fontsize=9.5,
                color=TEAL if a in (30, 45, 60) else "#111827")
    # exact coordinates in a side key (no overlap)
    key = [("30\u00b0", "$(\\frac{\\sqrt{3}}{2},\\ \\frac{1}{2})$"),
           ("45\u00b0", "$(\\frac{\\sqrt{2}}{2},\\ \\frac{\\sqrt{2}}{2})$"),
           ("60\u00b0", "$(\\frac{1}{2},\\ \\frac{\\sqrt{3}}{2})$")]
    ax.text(-1.55, 1.42, "Point on the circle at angle $\\theta$:  $(\\cos\\theta,\\ \\sin\\theta)$", fontsize=10.5,
            color=INDIGO, ha="left")
    for i, (a, c) in enumerate(key):
        ax.text(-1.55, 1.22 - 0.2 * i, f"{a}  \u2192  {c}", fontsize=9.5, color=TEAL, ha="left", va="center")
    ax.text(0.5, -0.09, "x = cos", fontsize=8.5, color=GRAY, ha="center", va="top")
    ax.text(0.04, -0.5, "y = sin", fontsize=8.5, color=GRAY, rotation=90, ha="left", va="center")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.6)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "fig_unit_circle")


def fig_inverse_trig():
    fig, axs = plt.subplots(1, 3, figsize=(9.4, 3.2))
    x = np.linspace(-1, 1, 400)
    mathaxes(axs[0], (-1.6, 1.6), (-2, 2), xt=[-1, 1], yt=[-np.pi/2, np.pi/2], labels=False)
    axs[0].set_yticklabels(["$-\\pi/2$", "$\\pi/2$"])
    axs[0].plot(x, np.arcsin(x), color=INDIGO)
    axs[0].set_title("$\\sin^{-1}x$:  domain $[-1,1]$\nrange $[-\\frac{\\pi}{2},\\frac{\\pi}{2}]$", fontsize=9, color=INDIGO)
    mathaxes(axs[1], (-1.6, 1.6), (-0.5, 3.6), xt=[-1, 1], yt=[np.pi/2, np.pi], labels=False)
    axs[1].set_yticklabels(["$\\pi/2$", "$\\pi$"])
    axs[1].plot(x, np.arccos(x), color=TEAL)
    axs[1].set_title("$\\cos^{-1}x$:  domain $[-1,1]$\nrange $[0,\\pi]$", fontsize=9, color=TEAL)
    xx = np.linspace(-6, 6, 400)
    mathaxes(axs[2], (-6.5, 6.5), (-2, 2), xt=[-4, -2, 2, 4], yt=[-np.pi/2, np.pi/2], labels=False)
    axs[2].set_yticklabels(["$-\\pi/2$", "$\\pi/2$"])
    axs[2].plot(xx, np.arctan(xx), color=CORAL)
    axs[2].axhline(np.pi/2, color=GRAY, ls="--", lw=1)
    axs[2].axhline(-np.pi/2, color=GRAY, ls="--", lw=1)
    axs[2].set_title("$\\tan^{-1}x$:  domain $\\mathbb{R}$\nrange $(-\\frac{\\pi}{2},\\frac{\\pi}{2})$", fontsize=9, color=CORAL)
    fig.tight_layout()
    save(fig, "fig_inverse_trig")


def fig_exp_log():
    fig, ax = plt.subplots(figsize=(4.6, 4.2))
    mathaxes(ax, (-3, 4.5), (-3, 4.5), xt=range(-3, 5), yt=range(-3, 5), labels=True)
    x = np.linspace(-3, 1.55, 300)
    ax.plot(x, np.exp(x), color=INDIGO, label="$y=e^x$")
    x2 = np.linspace(0.05, 4.5, 300)
    ax.plot(x2, np.log(x2), color=TEAL, label="$y=\\ln x$")
    ax.plot([-3, 4.5], [-3, 4.5], "--", color=GRAY, lw=1.2)
    ax.text(3.2, 3.55, "$y=x$ (mirror)", fontsize=9, color=GRAY, rotation=38)
    dot(ax, 0, 1, color=INDIGO)
    dot(ax, 1, 0, color=TEAL)
    ax.text(0.12, 1.15, "(0, 1)", fontsize=8.5, color=INDIGO)
    ax.text(1.1, -0.45, "(1, 0)", fontsize=8.5, color=TEAL)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    ax.set_aspect("equal")
    save(fig, "fig_exp_log")


def fig_growth():
    fig, ax = plt.subplots(figsize=(5.8, 3.8))
    x = np.linspace(0, 6, 400)
    mathaxes(ax, (0, 6), (0, 120), labels=True, xt=range(0, 7), yt=[0, 40, 80, 120])
    for f, lab, c in ((lambda t: t, "$y=x$", GRAY), (lambda t: t**2, "$y=x^2$", TEAL),
                      (lambda t: t**3, "$y=x^3$", AMBER), (np.exp, "$y=e^x$", CORAL)):
        ax.plot(x, f(x), color=c, label=lab)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    ax.set_title("Exponentials eventually beat every power of $x$", fontsize=10, color=INDIGO)
    save(fig, "fig_growth")


# ---------------------------------------------------------------------------
# Unit II: limits, continuity, derivatives
# ---------------------------------------------------------------------------
def fig_limit_sinx():
    fig, ax = plt.subplots(figsize=(5.4, 3.2))
    mathaxes(ax, (-10, 10), (-0.4, 1.3), xt=[-9.4248, -3.1416, 3.1416, 9.4248], yt=[0, 1], labels=True)
    ax.set_xticklabels(["$-3\\pi$", "$-\\pi$", "$\\pi$", "$3\\pi$"])
    x = np.linspace(-10, 10, 2001)
    x = x[np.abs(x) > 1e-3]
    ax.plot(x, np.sin(x) / x, color=INDIGO)
    dot(ax, 0, 1, filled=False, color=CORAL)
    ax.annotate("hole at x = 0\n(undefined),\nyet the curve\naims at 1", xy=(0, 1), xytext=(3.2, 0.95), fontsize=8.5,
                color=CORAL, arrowprops=dict(arrowstyle="->", color=CORAL))
    ax.set_title("$\\dfrac{\\sin x}{x}$ is undefined at 0 but $\\to 1$", fontsize=10, color=INDIGO, pad=8)
    save(fig, "fig_limit_sinx")


def fig_onesided():
    fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.0))
    ax = axs[0]
    mathaxes(ax, (-3, 3), (-0.5, 3), xt=[-2, -1, 1, 2], yt=[1, 2], labels=False)
    ax.plot([-3, 0], [1, 1], color=INDIGO)
    ax.plot([0, 3], [2, 2], color=INDIGO)
    dot(ax, 0, 1, True)
    dot(ax, 0, 2, False)
    ax.set_title("Jump: left limit 1, right limit 2\n(limit does not exist)", fontsize=9, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (-3, 3), (-0.5, 3), xt=[-2, -1, 1, 2], yt=[1, 2], labels=False)
    ax.plot([-3, 3], [1, 1], color=TEAL)
    dot(ax, 0, 1, False, color=TEAL)
    dot(ax, 0, 2, True, color=CORAL)
    ax.set_title("Hole: both limits are 1, but $f(0)=2$\n(limit exists, not continuous)", fontsize=9, color=TEAL)
    fig.tight_layout()
    save(fig, "fig_onesided")


def fig_discontinuities():
    fig, axs = plt.subplots(1, 4, figsize=(11, 2.9))
    # continuous
    ax = axs[0]
    mathaxes(ax, (-3, 3), (-1, 5), labels=False, xt=[], yt=[])
    x = np.linspace(-2.2, 2.2, 200)
    ax.plot(x, x**2 * 0.9 + 0.2, color=TEAL)
    ax.set_title("Continuous\n(draw without lifting pen)", fontsize=9, color=TEAL)
    # removable
    ax = axs[1]
    mathaxes(ax, (-3, 3), (-1, 5), labels=False, xt=[], yt=[])
    x = np.linspace(-2.5, 2.5, 200)
    ax.plot(x, 0.3 * x + 2, color=INDIGO)
    dot(ax, 0, 2, False, color=INDIGO)
    dot(ax, 0, 3.5, True, color=CORAL)
    ax.set_title("Removable\n(hole; $f(c)\\neq\\lim f$)", fontsize=9, color=INDIGO)
    # jump
    ax = axs[2]
    mathaxes(ax, (-3, 3), (-1, 5), labels=False, xt=[], yt=[])
    ax.plot([-2.7, 0], [1.2, 1.2 + 0.0], color=AMBER)
    ax.plot([0, 2.7], [3.4, 3.4], color=AMBER)
    ax.plot([-2.7, 0], [1.2, 1.2], color=AMBER)
    dot(ax, 0, 1.2, True, color=AMBER)
    dot(ax, 0, 3.4, False, color=AMBER)
    ax.set_title("Jump\n(left limit $\\neq$ right limit)", fontsize=9, color="#b07d00")
    # infinite
    ax = axs[3]
    mathaxes(ax, (-3, 3), (-4, 4), labels=False, xt=[], yt=[])
    for a, b in ((-3, -0.15), (0.15, 3)):
        x = np.linspace(a, b, 300)
        ax.plot(x, 1 / x, color=CORAL)
    ax.axvline(0, color=CORAL, ls=":", lw=1)
    ax.set_title("Infinite\n(shoots off to $\\pm\\infty$)", fontsize=9, color=CORAL)
    fig.tight_layout()
    save(fig, "fig_discontinuities")


def fig_floor():
    fig, ax = plt.subplots(figsize=(4.8, 3.4))
    mathaxes(ax, (-3.3, 4.3), (-3.4, 4.3), xt=range(-3, 5), yt=range(-3, 5), labels=True)
    for n in range(-3, 4):
        ax.plot([n, n + 1], [n, n], color=INDIGO)
        dot(ax, n, n, True, s=30)
        dot(ax, n + 1, n, False, s=30)
    ax.set_title("$f(x)=[x]$ : jumps at every integer", fontsize=10, color=INDIGO)
    save(fig, "fig_floor")


def fig_secant():
    fig, ax = plt.subplots(figsize=(5.8, 4.4))
    mathaxes(ax, (-0.3, 3.4), (-0.5, 9.5), xt=[0, 1, 2, 3], yt=[0, 2, 4, 6, 8], labels=True)
    x = np.linspace(-0.3, 3.2, 300)
    ax.plot(x, x**2, color=INDIGO, lw=2.4)
    x0 = 1.0
    cols = [AMBER, "#d98a00", CORAL]
    for h, c in zip((2.0, 1.0, 0.4), cols):
        slope = (x0 + h)**2 - x0**2
        slope /= h
        xs = np.array([-0.2, 3.3])
        ax.plot(xs, x0**2 + slope * (xs - x0), color=c, lw=1.3, alpha=0.9)
        dot(ax, x0 + h, (x0 + h)**2, color=c, s=28)
        ax.text(x0 + h + 0.07, (x0 + h)**2 - 0.55, f"h={h:g}", fontsize=8, color=c)
    xs = np.array([-0.2, 3.3])
    ax.plot(xs, 1 + 2 * (xs - 1), color=TEAL, lw=2.4)
    dot(ax, 1, 1, color=TEAL, s=60)
    ax.text(0.15, 5.7, "tangent: slope $=f'(1)=2$", fontsize=9, color=TEAL)
    ax.text(0.15, 7.3, "secants: slope $=\\dfrac{f(1+h)-f(1)}{h}=2+h$", fontsize=9, color="#b07d00")
    ax.set_title("Secant lines swing into the tangent as $h\\to 0$", fontsize=10, color=INDIGO)
    save(fig, "fig_secant")


def fig_nondiff():
    fig, axs = plt.subplots(1, 4, figsize=(11, 2.9))
    x = np.linspace(-2, 2, 400)
    ax = axs[0]
    mathaxes(ax, (-2, 2), (-0.5, 2.5), labels=False, xt=[], yt=[])
    ax.plot(x, np.abs(x), color=INDIGO)
    ax.set_title("Corner: $|x|$ at 0\nslopes $-1$ and $+1$", fontsize=9, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (-2, 2), (-2, 2), labels=False, xt=[], yt=[])
    ax.plot(x, np.cbrt(x), color=TEAL)
    ax.set_title("Vertical tangent: $x^{1/3}$\nslope $\\to\\infty$", fontsize=9, color=TEAL)
    ax = axs[2]
    mathaxes(ax, (-2, 2), (-0.5, 2.5), labels=False, xt=[], yt=[])
    ax.plot(x, np.cbrt(x**2), color=CORAL)
    ax.set_title("Cusp: $x^{2/3}$\nslopes $\\to\\mp\\infty$", fontsize=9, color=CORAL)
    ax = axs[3]
    mathaxes(ax, (-2, 2), (-0.5, 2.5), labels=False, xt=[], yt=[])
    ax.plot([-2, 0], [0.4, 0.4], color=AMBER)
    ax.plot([0, 2], [1.7, 1.7], color=AMBER)
    dot(ax, 0, 0.4, True, color=AMBER)
    dot(ax, 0, 1.7, False, color=AMBER)
    ax.set_title("Jump: not even continuous\n(so no derivative)", fontsize=9, color="#b07d00")
    fig.tight_layout()
    save(fig, "fig_nondiff")


def fig_rolle_mvt():
    fig, axs = plt.subplots(1, 2, figsize=(9.4, 3.5))
    f = lambda x: 1 + 2.2 * np.sin(x * 0.9)  # arbitrary smooth bump
    # Rolle: f(x)=x^2-4x+3 on [1,3]
    ax = axs[0]
    mathaxes(ax, (0, 4), (-1.6, 3.4), xt=[1, 2, 3], yt=[0], labels=True)
    x = np.linspace(0.2, 3.9, 300)
    ax.plot(x, x**2 - 4 * x + 3, color=INDIGO)
    ax.plot([1, 3], [0, 0], color=GRAY, lw=1, ls="--")
    dot(ax, 1, 0), dot(ax, 3, 0)
    dot(ax, 2, -1, color=CORAL, s=60)
    ax.plot([1.2, 2.8], [-1, -1], color=CORAL, lw=2)
    ax.text(2.1, -1.45, "$c=2$:  $f'(c)=0$ (flat tangent)", fontsize=8.5, color=CORAL, ha="center")
    ax.set_title("Rolle: $f(1)=f(3)$ forces a flat tangent", fontsize=9.5, color=INDIGO)
    # MVT: f(x)=x^2 on [0,2]; c=1
    ax = axs[1]
    mathaxes(ax, (-0.3, 2.6), (-0.6, 5.4), xt=[0, 1, 2], yt=[0, 2, 4], labels=True)
    x = np.linspace(-0.2, 2.4, 300)
    ax.plot(x, x**2, color=INDIGO)
    ax.plot([0, 2], [0, 4], color=AMBER, lw=2)
    ax.plot([0.2, 1.8], [1 + 2 * (0.2 - 1), 1 + 2 * (1.8 - 1)], color=CORAL, lw=2)
    dot(ax, 0, 0), dot(ax, 2, 4)
    dot(ax, 1, 1, color=CORAL, s=60)
    ax.text(0.05, 4.4, "chord slope = (4 - 0)/(2 - 0) = 2", fontsize=8.5, color="#b07d00")
    ax.text(1.12, 0.45, "$c=1$: tangent slope $2$", fontsize=8.5, color=CORAL)
    ax.set_title("Mean Value: some tangent is parallel to the chord", fontsize=9.5, color=INDIGO)
    fig.tight_layout()
    save(fig, "fig_rolle_mvt")


def fig_taylor_sin():
    from math import factorial
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    mathaxes(ax, (-7, 7), (-2.6, 2.6), xt=[-2 * np.pi, -np.pi, np.pi, 2 * np.pi], yt=[-2, -1, 1, 2], labels=True)
    ax.set_xticklabels(["$-2\\pi$", "$-\\pi$", "$\\pi$", "$2\\pi$"])
    x = np.linspace(-7, 7, 800)
    ax.plot(x, np.sin(x), color="black", lw=3, label="$\\sin x$", zorder=6)

    def P(n):
        return sum((-1)**k * x**(2 * k + 1) / factorial(2 * k + 1) for k in range((n + 1) // 2))
    for n, c in ((1, GRAY), (3, AMBER), (5, TEAL), (7, SKY), (9, CORAL)):
        y = P(n)
        y = np.where(np.abs(y) <= 2.6, y, np.nan)
        ax.plot(x, y, color=c, lw=1.8, label=f"degree {n}")
    ax.legend(loc="upper right", frameon=True, fontsize=8, ncol=2, facecolor="white", edgecolor=LIGHT)
    ax.set_title("More terms $\\Rightarrow$ a better copy of $\\sin x$ (centred at 0)", fontsize=10, color=INDIGO)
    save(fig, "fig_taylor_sin")


def fig_taylor_ln():
    from math import factorial
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.6))
    ax = axs[0]
    mathaxes(ax, (-3.2, 3.2), (-1, 12), xt=[-3, -2, -1, 1, 2, 3], yt=[0, 4, 8, 12], labels=True)
    x = np.linspace(-3.2, 3.2, 600)
    ax.plot(x, np.exp(x), color="black", lw=3, label="$e^x$")
    for n, c in ((1, GRAY), (2, AMBER), (3, TEAL), (4, CORAL)):
        y = sum(x**k / factorial(k) for k in range(n + 1))
        ax.plot(x, np.where((y > -1) & (y < 12), y, np.nan), color=c, lw=1.8, label=f"degree {n}")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_title("$e^x$: converges for every $x$", fontsize=9.5, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (-1.2, 2.2), (-3, 2), xt=[-1, 1, 2], yt=[-2, -1, 1], labels=True)
    x = np.linspace(-0.97, 2.1, 600)
    ax.plot(x, np.log(1 + x), color="black", lw=3, label="$\\ln(1+x)$")
    for n, c in ((2, AMBER), (4, TEAL), (8, CORAL)):
        y = sum((-1)**(k + 1) * x**k / k for k in range(1, n + 1))
        ax.plot(x, np.where((y > -3) & (y < 2), y, np.nan), color=c, lw=1.8, label=f"degree {n}")
    ax.axvline(1, color=GRAY, ls=":", lw=1)
    ax.legend(frameon=False, fontsize=8, loc="lower right")
    ax.set_title("$\\ln(1+x)$: only trustworthy for $-1<x\\leq 1$", fontsize=9.5, color=INDIGO)
    fig.tight_layout()
    save(fig, "fig_taylor_ln")


def fig_incdec():
    fig, axs = plt.subplots(2, 1, figsize=(6.0, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.25, 1]})
    x = np.linspace(-2.3, 2.3, 400)
    f = x**3 - 3 * x
    fp = 3 * x**2 - 3
    ax = axs[0]
    mathaxes(ax, (-2.5, 2.5), (-3.5, 3.5), xt=[-2, -1, 1, 2], yt=[-2, 2], labels=False)
    for a, b, c in ((-2.3, -1, TEAL), (-1, 1, CORAL), (1, 2.3, TEAL)):
        m = (x >= a) & (x <= b)
        ax.plot(x[m], f[m], color=c, lw=2.6)
    dot(ax, -1, 2, color=INDIGO), dot(ax, 1, -2, color=INDIGO)
    ax.text(-1.0, 2.55, "local max", fontsize=8.5, ha="center", color=INDIGO)
    ax.text(1.0, -2.95, "local min", fontsize=8.5, ha="center", color=INDIGO)
    ax.text(0.3, 3.0, "$f(x)=x^3-3x$", fontsize=9.5, color=INDIGO)
    ax.text(-2.35, -2.9, "rising", color=TEAL, fontsize=8.5)
    ax.text(0.25, 1.1, "falling", color=CORAL, fontsize=8.5)
    ax.text(1.75, 0.9, "rising", color=TEAL, fontsize=8.5)
    ax = axs[1]
    mathaxes(ax, (-2.5, 2.5), (-4, 8), xt=[-2, -1, 1, 2], yt=[-3, 0, 3, 6], labels=False)
    ax.plot(x, fp, color=INDIGO)
    ax.fill_between(x, fp, 0, where=fp > 0, color=TEAL, alpha=0.25)
    ax.fill_between(x, fp, 0, where=fp < 0, color=CORAL, alpha=0.25)
    ax.text(-0.5, 6.6, "$f'(x)=3x^2-3$", fontsize=9.5, color=INDIGO, ha="center")
    ax.text(-2.1, 1.0, "$f'>0$", color="#0b7a6a", fontsize=9)
    ax.text(-0.35, -2.2, "$f'<0$", color=CORAL, fontsize=9)
    ax.text(1.5, 1.0, "$f'>0$", color="#0b7a6a", fontsize=9)
    ax.text(2.4, -0.3, "x", fontsize=9, style="italic")
    fig.tight_layout(h_pad=0.6)
    save(fig, "fig_incdec")


def fig_tangent_normal():
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    mathaxes(ax, (-1.2, 3.2), (-1, 5), xt=[-1, 0, 1, 2, 3], yt=[0, 1, 2, 3, 4], labels=True)
    x = np.linspace(-1.1, 2.2, 300)
    ax.plot(x, x**2, color=INDIGO, lw=2.4)
    xs = np.array([-0.9, 3])
    ax.plot(xs, 1 + 2 * (xs - 1), color=TEAL, lw=2)
    xn = np.array([-0.9, 3.1])
    ax.plot(xn, 1 - 0.5 * (xn - 1), color=CORAL, lw=2)
    dot(ax, 1, 1, color=INDIGO, s=60)
    ax.text(2.0, 3.35, "tangent\n$y-1=2(x-1)$", color=TEAL, fontsize=9)
    ax.text(1.6, 0.0, "normal  $y-1=-\\frac{1}{2}(x-1)$", color=CORAL, fontsize=9)
    ax.text(-1.1, 4.2, "$y=x^2$ at $(1,1)$", color=INDIGO, fontsize=9.5)
    ax.set_aspect("equal")
    save(fig, "fig_tangent_normal")


def fig_differential():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    f = lambda x: x**2
    x0, dx = 1.0, 0.8
    mathaxes(ax, (0.3, 2.4), (0.2, 3.6), xt=[], yt=[], labels=False, grid=False)
    x = np.linspace(0.4, 2.3, 300)
    ax.plot(x, f(x), color=INDIGO, lw=2.4)
    ax.plot([0.5, 2.3], [1 + 2 * (0.5 - 1), 1 + 2 * (2.3 - 1)], color=TEAL, lw=1.6)
    ax.plot([x0, x0 + dx], [f(x0)] * 2, color=GRAY, ls="--")
    ax.plot([x0 + dx] * 2, [f(x0), f(x0 + dx)], color=CORAL, lw=2.4)
    ax.plot([x0 + dx] * 2, [f(x0), 1 + 2 * dx], color=TEAL, lw=3.2)
    dot(ax, x0, f(x0)), dot(ax, x0 + dx, f(x0 + dx)), dot(ax, x0 + dx, 1 + 2 * dx, color=TEAL, s=32)
    ax.text(x0 - 0.12, f(x0) - 0.1, "P", fontsize=10, ha="right", color=INDIGO)
    ax.text(x0 + dx + 0.05, f(x0 + dx) + 0.05, "Q", fontsize=10, color=INDIGO)
    ax.text(1.4, 0.95, "$dx=\\Delta x$", fontsize=9.5, color=GRAY, ha="center")
    ax.text(x0 + dx + 0.07, 2.35, "$\\Delta y$ (true change)", fontsize=9, color=CORAL)
    ax.text(x0 + dx + 0.07, 2.25 - 0.4, "", fontsize=9)
    ax.text(x0 + dx + 0.07, 1.78, "$dy=f'(x)\\,dx$\n(tangent-line change)", fontsize=9, color="#0b7a6a")
    ax.text(0.45, 3.3, "$dy\\approx\\Delta y$ when $dx$ is small", fontsize=9.5, color=INDIGO)
    ax.set_xlabel("x", loc="right")
    ax.set_ylabel("y", loc="top", rotation=0)
    save(fig, "fig_differential")


def fig_extrema():
    fig, axs = plt.subplots(1, 2, figsize=(10.2, 3.6), gridspec_kw={"width_ratios": [1.7, 1]})
    ax = axs[0]
    mathaxes(ax, (-0.2, 8.2), (-0.8, 5.4), xt=[], yt=[], labels=False, grid=False)
    x = np.linspace(0.3, 7.7, 600)
    y = 2.4 + 1.5 * np.sin(1.25 * x - 0.6) + 0.12 * x - 0.35 * np.cos(2.9 * x) * 0
    ax.plot(x, y, color=INDIGO, lw=2.4)
    # locate local extrema numerically
    dy = np.gradient(y, x)
    idx = np.where(np.diff(np.sign(dy)) != 0)[0]
    for i in idx:
        mx = dy[i] > 0
        dot(ax, x[i], y[i], color=CORAL if mx else TEAL)
        ax.text(x[i], y[i] + (0.28 if mx else -0.5), "local max" if mx else "local min", ha="center",
                fontsize=8.5, color=CORAL if mx else TEAL)
    ax.axvline(x[0], color=GRAY, ls=":", lw=1)
    ax.axvline(x[-1], color=GRAY, ls=":", lw=1)
    ax.text(x[0], -0.55, "a", ha="center", fontsize=10, style="italic")
    ax.text(x[-1], -0.55, "b", ha="center", fontsize=10, style="italic")
    ymax, ymin = y.max(), y.min()
    ax.axhline(ymax, color=CORAL, ls="--", lw=0.8)
    ax.axhline(ymin, color=TEAL, ls="--", lw=0.8)
    ax.text(0.2, ymax + 0.08, "absolute max on [a, b]", fontsize=8, ha="left", color=CORAL)
    ax.text(0.2, ymin - 0.32, "absolute min on [a, b]", fontsize=8, ha="left", color=TEAL)
    ax.set_title("Local (hill-top / valley) vs absolute (highest / lowest overall)", fontsize=9.5, color=INDIGO, pad=14)
    ax = axs[1]
    mathaxes(ax, (-2, 2), (-3, 3), xt=[], yt=[], labels=False)
    x = np.linspace(-1.4, 1.4, 200)
    ax.plot(x, x**3, color=PLUM, lw=2.4)
    dot(ax, 0, 0, color=PLUM)
    ax.text(0.15, -0.8, "$f'(0)=0$ but not an extremum:\npoint of inflection", fontsize=8.5, color=PLUM)
    ax.set_title("$f(x)=x^3$: flat spot, no hill", fontsize=9.5, color=PLUM, pad=14)
    fig.tight_layout()
    save(fig, "fig_extrema")


def fig_box():
    fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.8), gridspec_kw={"width_ratios": [1, 1.25]})
    ax = axs[0]
    ax.add_patch(Rectangle((0, 0), 18, 18, fc="#eef2ff", ec=INDIGO, lw=2))
    s = 3
    for (cx, cy) in ((0, 0), (15, 0), (0, 15), (15, 15)):
        ax.add_patch(Rectangle((cx, cy), s, s, fc="#fecaca", ec=CORAL, lw=1.6, hatch="////"))
    ax.plot([3, 3], [0, 18], ls="--", color=GRAY, lw=1)
    ax.plot([15, 15], [0, 18], ls="--", color=GRAY, lw=1)
    ax.plot([0, 18], [3, 3], ls="--", color=GRAY, lw=1)
    ax.plot([0, 18], [15, 15], ls="--", color=GRAY, lw=1)
    ax.text(1.5, -1.6, "x", ha="center", color=CORAL, fontsize=10, style="italic")
    ax.text(9, -1.9, "18 cm", ha="center", color=INDIGO, fontsize=9)
    ax.text(9, 9, "base side\n$18-2x$", ha="center", va="center", fontsize=10, color=INDIGO)
    ax.set_xlim(-2, 20)
    ax.set_ylim(-3, 19.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Cut a square $x$ from each corner,\nfold up the flaps", fontsize=9.5, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (0, 9.5), (0, 500), xt=range(0, 10), yt=[0, 100, 200, 300, 400], labels=False)
    x = np.linspace(0, 9, 300)
    ax.plot(x, x * (18 - 2 * x)**2, color=INDIGO)
    dot(ax, 3, 432, color=CORAL, s=60)
    ax.text(3.3, 445, "$x=3$, $V=432$ cm$^3$ (max)", fontsize=9, color=CORAL)
    ax.set_title("$V(x)=x\\,(18-2x)^2$", fontsize=9.5, color=INDIGO)
    ax.set_xlabel("x (cm)", loc="right")
    fig.tight_layout()
    save(fig, "fig_box")


def fig_ladder():
    fig, ax = plt.subplots(figsize=(4.4, 3.8))
    ax.plot([0, 0], [0, 5.6], color="#374151", lw=5)
    ax.plot([0, 6], [0, 0], color="#374151", lw=3)
    ax.plot([0, 4], [3, 0], color=INDIGO, lw=4)
    ax.plot([0, 0], [0, 3], color=CORAL, lw=2.5)
    ax.plot([0, 4], [0, 0], color=TEAL, lw=2.5)
    ax.text(-0.35, 1.5, "y", color=CORAL, fontsize=12, style="italic", ha="center")
    ax.text(2, -0.55, "x", color=TEAL, fontsize=12, style="italic", ha="center")
    ax.text(2.3, 1.9, "5 m", color=INDIGO, fontsize=10, rotation=-37, ha="center")
    ax.annotate("", xy=(5.4, 0.28), xytext=(4.2, 0.28), arrowprops=dict(arrowstyle="->", color=TEAL, lw=2))
    ax.text(4.8, 0.58, "$dx/dt=2$", fontsize=8.5, color=TEAL, ha="center")
    ax.annotate("", xy=(0.28, 2.0), xytext=(0.28, 3.0), arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.4, ls="--"))
    ax.text(0.55, 2.35, "$dy/dt=?$", fontsize=8.5, color=CORAL)
    ax.set_xlim(-0.9, 6.3)
    ax.set_ylim(-1, 5.8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "fig_ladder")


def fig_cone_cyl():
    fig, ax = plt.subplots(figsize=(4.0, 3.6))
    ax.add_patch(Polygon([[-3, 0], [3, 0], [0, 5.5]], fc="#eef2ff", ec=INDIGO, lw=2))
    xr = 1.5
    hy = 5.5 * (1 - xr / 3)
    ax.add_patch(Rectangle((-xr, 0), 2 * xr, hy, fc="#bbf7d0", ec=TEAL, lw=2))
    ax.plot([0, 0], [0, 5.5], color=GRAY, ls="--", lw=1)
    ax.plot([0, 3], [-0.35, -0.35], color=INDIGO, lw=1.5)
    ax.text(1.5, -0.95, "$r$", ha="center", color=INDIGO, fontsize=11)
    ax.plot([0, xr], [hy + 0.3, hy + 0.3], color=TEAL, lw=1.5)
    ax.text(xr / 2, hy + 0.55, "$x$", ha="center", color=TEAL, fontsize=11)
    ax.text(3.35, 2.7, "cone height $h$", rotation=90, va="center", fontsize=9, color=INDIGO)
    ax.text(0.25, 1.1, "cylinder", fontsize=9, color="#0b7a6a")
    ax.set_xlim(-3.6, 4.3)
    ax.set_ylim(-1.5, 6.2)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "fig_cone_cyl")


# ---------------------------------------------------------------------------
# Unit III: integration
# ---------------------------------------------------------------------------
def fig_constants():
    fig, ax = plt.subplots(figsize=(5.2, 3.7))
    mathaxes(ax, (-2.5, 2.5), (-2, 6), xt=[-2, -1, 1, 2], yt=[-1, 1, 3, 5], labels=True)
    x = np.linspace(-2.4, 2.4, 300)
    cols = [GRAY, AMBER, TEAL, INDIGO, CORAL, PLUM]
    for C, c in zip(range(-1, 5), cols):
        ax.plot(x, x**2 + C, color=c, lw=1.8)
        ax.text(2.42, 2.4**2 + C - 0.05, f"C={C}", fontsize=7.5, color=c, va="center")
    for C in range(-1, 5):
        ax.plot([1, 1], [1 + C - 0.14, 1 + C + 0.14], color="black", lw=1)
    ax.plot([1, 1], [-2, 6], color=GRAY, ls=":", lw=1)
    ax.set_title("Every curve $y=x^2+C$ has slope $2x$; at $x=1$ they are all parallel", fontsize=9.2, color=INDIGO)
    save(fig, "fig_constants")


def fig_riemann():
    fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.2))
    f = lambda x: x**2
    xx = np.linspace(0, 2, 300)
    for ax, n in zip(axs[:2], (4, 12)):
        mathaxes(ax, (-0.2, 2.3), (-0.3, 4.6), xt=[0, 1, 2], yt=[0, 2, 4], labels=False)
        ax.plot(xx, f(xx), color=INDIGO, lw=2.2)
        w = 2 / n
        total = 0
        for i in range(n):
            xl = i * w
            h = f(xl + w)  # right endpoints (upper sum for increasing f)
            total += h * w
            ax.add_patch(Rectangle((xl, 0), w, h, fc=TEAL, alpha=0.30, ec=TEAL, lw=0.8))
        ax.set_title(f"{n} rectangles: total area $\\approx${total:.2f}", fontsize=9.5, color=INDIGO)
    ax = axs[2]
    mathaxes(ax, (-0.2, 2.3), (-0.3, 4.6), xt=[0, 1, 2], yt=[0, 2, 4], labels=False)
    ax.plot(xx, f(xx), color=INDIGO, lw=2.2)
    ax.fill_between(xx, 0, f(xx), color=TEAL, alpha=0.35)
    ax.text(1.0, 0.8, "$\\int_0^2 x^2\\,dx=\\dfrac{8}{3}\\approx 2.67$", fontsize=10, color=INDIGO, ha="center")
    ax.set_title("infinitely many, infinitely thin", fontsize=9.5, color=INDIGO)
    fig.tight_layout()
    save(fig, "fig_riemann")


def fig_even_odd():
    fig, axs = plt.subplots(1, 2, figsize=(8.8, 3.2))
    x = np.linspace(-2, 2, 400)
    ax = axs[0]
    mathaxes(ax, (-2.4, 2.4), (-0.5, 4.8), xt=[-2, -1, 1, 2], yt=[], labels=False)
    ax.plot(x, x**2, color=INDIGO)
    ax.fill_between(x, 0, x**2, where=x <= 0, color=TEAL, alpha=0.35)
    ax.fill_between(x, 0, x**2, where=x >= 0, color=AMBER, alpha=0.35)
    ax.set_title("Even ($x^2$): mirror image, so\n$\\int_{-a}^{a}=2\\int_0^a$", fontsize=9.5, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (-2.4, 2.4), (-4.2, 4.2), xt=[-2, -1, 1, 2], yt=[], labels=False)
    ax.plot(x, x**3 / 2, color=CORAL)
    ax.fill_between(x, 0, x**3 / 2, where=x <= 0, color=TEAL, alpha=0.35)
    ax.fill_between(x, 0, x**3 / 2, where=x >= 0, color=AMBER, alpha=0.35)
    ax.text(1.0, -2.6, "area above $+$", fontsize=8.5, color="#b07d00", ha="center")
    ax.text(-1.0, 2.2, "area below $-$", fontsize=8.5, color="#0b7a6a", ha="center")
    ax.set_title("Odd ($x^3$): cancels, so\n$\\int_{-a}^{a}=0$", fontsize=9.5, color=CORAL)
    fig.tight_layout()
    save(fig, "fig_even_odd")


def fig_king():
    fig, axs = plt.subplots(1, 2, figsize=(8.6, 3.2))
    x = np.linspace(0, 2, 300)
    for ax, g, col, ttl in ((axs[0], lambda t: t**2, INDIGO, "$f(x)=x^2$"),
                            (axs[1], lambda t: (2 - t)**2, CORAL, "$f(a-x)=(2-x)^2$")):
        mathaxes(ax, (-0.2, 2.3), (-0.3, 4.6), xt=[0, 1, 2], yt=[], labels=False)
        ax.plot(x, g(x), color=col, lw=2.2)
        ax.fill_between(x, 0, g(x), color=col, alpha=0.25)
        ax.text(1.0, 1.0, "area $=\\frac{8}{3}$", color=col, ha="center", fontsize=10)
        ax.set_title(ttl, fontsize=10, color=col)
    fig.suptitle("Reflecting the graph left-right leaves the area unchanged ($a=2$)", fontsize=10, color=INDIGO, y=1.03)
    fig.tight_layout()
    save(fig, "fig_king")


def fig_abs_integral():
    fig, ax = plt.subplots(figsize=(5.0, 3.1))
    mathaxes(ax, (-2.6, 2.6), (-0.4, 3.8), xt=[-2, -1, 1, 2], yt=[1, 2, 3], labels=True)
    x = np.linspace(-2, 2, 400)
    ax.plot(x, np.abs(x - 1), color=INDIGO, lw=2.2)
    ax.fill_between(x, 0, np.abs(x - 1), where=x <= 1, color=TEAL, alpha=0.3)
    ax.fill_between(x, 0, np.abs(x - 1), where=x >= 1, color=AMBER, alpha=0.35)
    ax.text(-0.5, 0.7, "area 9/2", fontsize=9.5, color="#0b7a6a", ha="center")
    ax.text(1.55, 0.18, "1/2", fontsize=9.5, color="#b07d00", ha="center")
    ax.set_title("$\\int_{-2}^{2}|x-1|\\,dx = \\frac{9}{2}+\\frac{1}{2} = 5$", fontsize=10, color=INDIGO)
    save(fig, "fig_abs_integral")


# ---------------------------------------------------------------------------
# Unit I
# ---------------------------------------------------------------------------
def fig_eigen():
    fig, axs = plt.subplots(1, 2, figsize=(8.8, 4.0))
    A = np.array([[2, 1], [1, 2]], float)
    t = np.linspace(0, 2 * np.pi, 400)
    circ = np.vstack([np.cos(t), np.sin(t)])
    img = A @ circ
    for ax in axs:
        ax.set_aspect("equal")
        ax.set_xlim(-3.7, 3.7)
        ax.set_ylim(-3.7, 3.7)
        ax.axhline(0, color="#9ca3af", lw=0.8)
        ax.axvline(0, color="#9ca3af", lw=0.8)
        ax.grid(True, color=LIGHT, lw=0.8)
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.set_xticks(range(-3, 4))
        ax.set_yticks(range(-3, 4))
    ax = axs[0]
    ax.plot(circ[0], circ[1], color=INDIGO)
    ax.annotate("", xy=(0.707, 0.707), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.4))
    ax.annotate("", xy=(0.707, -0.707), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=CORAL, lw=2.4))
    ax.plot([-3.3, 3.3], [-3.3, 3.3], color=TEAL, ls=":", lw=1)
    ax.plot([-3.3, 3.3], [3.3, -3.3], color=CORAL, ls=":", lw=1)
    ax.set_title("Before: the unit circle", fontsize=10, color=INDIGO)
    ax = axs[1]
    ax.plot(img[0], img[1], color=INDIGO)
    ax.annotate("", xy=(2.121, 2.121), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=TEAL, lw=2.4))
    ax.annotate("", xy=(0.707, -0.707), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=CORAL, lw=2.4))
    ax.plot([-3.3, 3.3], [-3.3, 3.3], color=TEAL, ls=":", lw=1)
    ax.plot([-3.3, 3.3], [3.3, -3.3], color=CORAL, ls=":", lw=1)
    ax.text(1.35, 2.85, "stretched $\\times3$\n($\\lambda=3$)", color=TEAL, fontsize=9)
    ax.text(1.0, -1.7, "unchanged $\\times1$\n($\\lambda=1$)", color=CORAL, fontsize=9)
    ax.set_title("After applying $A$ (rows $(2,1)$ and $(1,2)$)", fontsize=10, color=INDIGO)
    fig.tight_layout()
    save(fig, "fig_eigen")


def fig_linear_systems():
    fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.1))
    x = np.linspace(-3, 3, 100)
    ax = axs[0]
    mathaxes(ax, (-3, 3), (-3, 3), xt=[], yt=[], labels=False)
    ax.plot(x, x, color=INDIGO)
    ax.plot(x, -0.5 * x + 1.5, color=TEAL)
    dot(ax, 1, 1, color=CORAL, s=60)
    ax.set_title("Unique solution\n(lines cross once)\nrank $A$ = rank $[A|B]$ = $n$", fontsize=9, color=INDIGO)
    ax = axs[1]
    mathaxes(ax, (-3, 3), (-3, 3), xt=[], yt=[], labels=False)
    ax.plot(x, x, color=INDIGO)
    ax.plot(x, x + 1.4, color=TEAL)
    ax.set_title("No solution\n(parallel lines)\nrank $A$ < rank $[A|B]$", fontsize=9, color=INDIGO)
    ax = axs[2]
    mathaxes(ax, (-3, 3), (-3, 3), xt=[], yt=[], labels=False)
    ax.plot(x, x, color=INDIGO, lw=5, alpha=0.5)
    ax.plot(x, x, color=TEAL, lw=1.6)
    ax.set_title("Infinitely many solutions\n(same line)\nrank $A$ = rank $[A|B]$ < $n$", fontsize=9, color=INDIGO)
    fig.tight_layout()
    save(fig, "fig_linear_systems")


def fig_big_picture():
    """Roadmap graphic for the three units."""
    fig, ax = plt.subplots(figsize=(9.6, 2.7))
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 8.6)
    ax.axis("off")
    boxes = [
        (0.3, "UNIT I", "Matrices &\nLinear Systems", "organise numbers,\nsolve many equations\nat once", INDIGO),
        (10.3, "UNIT II", "Differential\nCalculus", "how fast things\nchange (slopes)", TEAL),
        (20.3, "UNIT III", "Integral\nCalculus", "adding up tiny pieces\n(areas, totals)", CORAL),
    ]
    for x0, tag, title, sub, c in boxes:
        ax.add_patch(plt.matplotlib.patches.FancyBboxPatch((x0, 0.6), 9.2, 7.4, boxstyle="round,pad=0.02,rounding_size=0.5",
                                                           fc="white", ec=c, lw=2.6))
        ax.text(x0 + 4.6, 7.0, tag, ha="center", fontsize=11, color=c, weight="bold")
        ax.text(x0 + 4.6, 5.1, title, ha="center", va="center", fontsize=12.5, color="#111827", weight="bold")
        ax.text(x0 + 4.6, 2.1, sub, ha="center", va="center", fontsize=9.2, color=GRAY)
    for xa in (9.7, 19.7):
        ax.annotate("", xy=(xa + 0.55, 4.2), xytext=(xa - 0.1, 4.2),
                    arrowprops=dict(arrowstyle="-|>", color="#374151", lw=2))
    save(fig, "fig_big_picture")


def fig_function_machine():
    fig, ax = plt.subplots(figsize=(7.2, 1.9))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.annotate("", xy=(5.5, 2.5), xytext=(1.3, 2.5), arrowprops=dict(arrowstyle="-|>", color=INDIGO, lw=2.2))
    ax.add_patch(plt.matplotlib.patches.FancyBboxPatch((5.6, 0.8), 8.6, 3.4, boxstyle="round,pad=0.05,rounding_size=0.6",
                                                       fc="#eef2ff", ec=INDIGO, lw=2.4))
    ax.text(9.9, 2.5, "$f(x)=x^2+1$", ha="center", va="center", fontsize=13, color=INDIGO)
    ax.annotate("", xy=(18.7, 2.5), xytext=(14.4, 2.5), arrowprops=dict(arrowstyle="-|>", color=INDIGO, lw=2.2))
    ax.text(0.4, 2.5, "input\n$x=3$", ha="center", va="center", fontsize=10, color=GRAY)
    ax.text(19.4, 2.5, "output\n$10$", ha="center", va="center", fontsize=10, color=GRAY)
    save(fig, "fig_function_machine")


def fig_ln_series_dummy():
    pass


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("fig_") and callable(fn) and name != "fig_ln_series_dummy":
            fn()
