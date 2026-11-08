"""Generate Figures 1-3 for the path-invariant selection manuscript (600 dpi PNG, greyscale-safe)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import os

OUT = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(OUT, exist_ok=True)

C_MAIN = "#1f3a5f"   # deep blue (reads in greyscale)
C_CRED = "#b5542a"   # burnt orange
C_GREY = "#555555"
BOX = dict(boxstyle="round,pad=0.35", fc="white", ec=C_MAIN, lw=1.6)
BOX_CRED = dict(boxstyle="round,pad=0.35", fc="#fdf0ea", ec=C_CRED, lw=1.6)


def box(ax, x, y, text, style=BOX, fs=11):
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, bbox=style, zorder=3)


def arrow(ax, x1, y1, x2, y2, color=C_MAIN, lw=1.8, style="-|>", ls="-"):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=16, lw=lw, color=color,
                                 linestyle=ls, zorder=2))


# ---------------- Figure 1 ----------------
fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

box(ax, 1.0, 4.2, "Resources and\nopportunities (R)")
box(ax, 3.1, 4.2, "Experience (E)")
box(ax, 5.3, 4.2, "Competence (K)")
box(ax, 7.5, 4.2, "Direct evidence\n(D)")
box(ax, 9.2, 4.2, "Selection\nevaluation (A)")
box(ax, 5.3, 1.6, "Credential signal", style=BOX_CRED)
box(ax, 5.3, 5.5, "Later outcome (Y)", fs=10)

arrow(ax, 1.9, 4.2, 2.35, 4.2)
arrow(ax, 3.85, 4.2, 4.5, 4.2)
arrow(ax, 6.1, 4.2, 6.6, 4.2)
arrow(ax, 8.35, 4.2, 8.6, 4.2)
arrow(ax, 5.3, 3.85, 5.3, 2.45, color=C_CRED)
arrow(ax, 6.05, 1.6, 9.0, 3.55, color=C_CRED, ls="--")
arrow(ax, 5.3, 4.55, 5.3, 5.15, color=C_GREY, lw=1.4)
arrow(ax, 5.65, 5.5, 9.0, 4.75, color=C_GREY, lw=1.4, ls=":")

ax.text(3.7, 5.0, "developmental pathway", fontsize=10, color=C_MAIN, style="italic")
ax.text(6.35, 2.2, "credential pathway:\nexperience rewarded\nindependently of K", fontsize=9.5,
        color=C_CRED, style="italic")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "Figure1.png"), dpi=600)
plt.close(fig)

# ---------------- Figure 2 ----------------
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.4))
for ax, title in zip(axes, ["Panel A — path-invariant selection",
                            "Panel B — path-dependent selection"]):
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
    ax.set_title(title, fontsize=11.5)

ax = axes[0]
for i, lab in enumerate(["Pathway 1\n(e.g. study abroad)", "Pathway 2\n(e.g. coursework)",
                         "Pathway 3\n(e.g. self-study)"]):
    box(ax, 1.6, 4.8 - 1.8 * i, lab, fs=9.5)
    arrow(ax, 2.8, 4.8 - 1.8 * i, 4.6, 3.0, lw=1.5)
box(ax, 5.9, 3.0, "Equivalent relevant\ncapability (K)")
arrow(ax, 7.2, 3.0, 8.3, 3.0)
box(ax, 9.15, 3.0, "Equivalent\nevaluation", fs=10)

ax = axes[1]
for i, lab in enumerate(["Pathway A\n(high-status)", "Pathway B\n(low-status)"]):
    box(ax, 1.6, 4.3 - 2.6 * i, lab, fs=9.5)
    arrow(ax, 2.8, 4.3 - 2.6 * i, 4.6, 3.0, lw=1.5)
box(ax, 5.9, 3.0, "Equivalent relevant\ncapability (K)")
arrow(ax, 7.2, 3.0, 8.3, 3.0)
box(ax, 9.15, 3.0, "Different\nevaluations", fs=10)
arrow(ax, 1.6, 1.35, 8.9, 2.35, color=C_CRED, ls="--", lw=1.6)
ax.text(4.6, 1.35, "pathway affects A directly", fontsize=9.5, color=C_CRED, style="italic")

fig.tight_layout()
fig.savefig(os.path.join(OUT, "Figure2.png"), dpi=600)
plt.close(fig)

# ---------------- Figure 3 (non-quantitative conceptual continuum) ----------------
fig, ax = plt.subplots(figsize=(8.8, 4.2))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")

# horizontal continuum band (gradient from credential-heavy to direct-evidence)
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
cmap = LinearSegmentedColormap.from_list("cont", ["#e8eef5", "#1f3a5f"])
grad = np.linspace(0, 1, 256).reshape(1, -1)
ax.imshow(grad, extent=[1.0, 9.0, 3.1, 3.9], aspect="auto", cmap=cmap, zorder=1)
rect = mpatches.FancyBboxPatch((1.0, 3.1), 8.0, 0.8, boxstyle="round,pad=0.02",
                               fc="none", ec=C_MAIN, lw=1.4, zorder=2)
ax.add_patch(rect)

# directional arrows + end labels (no axis values)
arrow(ax, 9.0, 4.4, 9.7, 4.4, color=C_MAIN)
arrow(ax, 1.0, 2.6, 0.3, 2.6, color=C_CRED)
ax.text(5.0, 4.55, "feasibility / validity of direct assessment  increases", fontsize=10.5,
        ha="center", color=C_MAIN, style="italic")
ax.text(5.0, 2.45, "residual reliance on biography  increases", fontsize=10.5,
        ha="center", color=C_CRED, style="italic")

# illustrative environment labels
labels = [("Political candidacy", 1.9), ("University admissions", 5.0), ("Employment selection", 8.0)]
for name, x in labels:
    ax.plot([x], [3.5], marker="o", ms=9, color="white", mec=C_MAIN, mew=1.8, zorder=3)
    ax.text(x, 5.35, name, ha="center", fontsize=11, color="#222222")

ax.text(5.0, 0.8, "Positions are conceptual and illustrative; they are not empirically estimated.",
        fontsize=9.5, color=C_GREY, style="italic", ha="center")
fig.tight_layout()
fig.savefig(os.path.join(OUT, "Figure3.png"), dpi=600)
plt.close(fig)
print("figures written:", os.listdir(OUT))
