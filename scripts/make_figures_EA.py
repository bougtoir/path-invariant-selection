"""Generate Educational Assessment Figures 1-3 (conceptual, non-quantitative; grayscale line art).

Outputs figures/EA/Figure{1,2,3}.png (600 dpi) and .tif (1200 dpi, LZW, grayscale).
No figure contains data, axes values or estimated positions.
"""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from PIL import Image

OUT = os.path.join(os.path.dirname(__file__), "..", "figures", "EA")
os.makedirs(OUT, exist_ok=True)
plt.rcParams.update({"font.family": "DejaVu Sans"})
K, G = "#000000", "#555555"
BOX = dict(boxstyle="round,pad=0.35", fc="white", ec=K, lw=1.4)
BOX_B = dict(boxstyle="round,pad=0.35", fc="#e6e6e6", ec=K, lw=1.4)


def box(ax, x, y, t, style=BOX, fs=10):
    ax.text(x, y, t, ha="center", va="center", fontsize=fs, bbox=style, zorder=3)


def arrow(ax, a, b, ls="-", lw=1.5, color=K, rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle="-|>", mutation_scale=14, lw=lw, color=color,
                                 linestyle=ls, zorder=2, connectionstyle=f"arc3,rad={rad}"))


def save(fig, name):
    png = os.path.join(OUT, name + ".png")
    fig.savefig(png, dpi=600)
    fig.savefig(os.path.join(OUT, name + "_tmp.png"), dpi=1200)
    plt.close(fig)
    im = Image.open(os.path.join(OUT, name + "_tmp.png")).convert("L")
    im.save(os.path.join(OUT, name + ".tif"), compression="tiff_lzw", dpi=(1200, 1200))
    os.remove(os.path.join(OUT, name + "_tmp.png"))
    Image.open(png).convert("L").save(png, dpi=(600, 600))


# Figure 1: three roles of biographical evidence in a selection decision
fig, ax = plt.subplots(figsize=(9.0, 5.0))
ax.set_xlim(0, 10); ax.set_ylim(-0.2, 6.0); ax.axis("off")
box(ax, 0.95, 4.6, "Opportunity\nand context (R)")
box(ax, 2.95, 4.6, "Experience (E)")
box(ax, 5.0, 4.6, "Target\nattribute (Z)")
box(ax, 7.2, 4.6, "Direct evidence (D)\nsampled performance")
box(ax, 9.25, 2.9, "Decision\n(A)")
box(ax, 5.0, 1.3, "Biographical record (B)\nof the experience", style=BOX_B)
arrow(ax, (1.75, 4.6), (2.25, 4.6))
arrow(ax, (3.65, 4.6), (4.35, 4.6))
arrow(ax, (5.65, 4.6), (6.05, 4.6))
arrow(ax, (8.0, 4.25), (9.0, 3.3))
arrow(ax, (2.95, 4.25), (4.2, 1.75))
arrow(ax, (6.1, 1.3), (8.95, 2.6), ls="--", lw=1.7)
arrow(ax, (5.0, 1.75), (5.0, 4.15), ls=":", color=G)
arrow(ax, (0.95, 4.1), (8.3, 3.7), ls="-.", color=G, rad=0.25)
ax.text(3.2, 5.4, "(1) developmental pathway: E builds Z", fontsize=9.2, style="italic")
ax.text(5.15, 3.05, "(2) evidential role:\nB indicates Z", fontsize=9.0, color=G, style="italic")
ax.text(1.0, 2.75, "(3) contextual role:\nR informs the\ninterpretation of D", fontsize=9.0, color=G, style="italic")
ax.text(7.0, 0.35, "(4) credential role: B weighted\nindependently of Z", fontsize=9.0, style="italic")
fig.tight_layout(); save(fig, "Figure1")

# Figure 2: path-invariant vs path-dependent weighting
fig, axes = plt.subplots(1, 2, figsize=(9.6, 4.4))
for ax, t in zip(axes, ["A. Path-invariant evaluation", "B. Path-dependent evaluation"]):
    ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off"); ax.set_title(t, fontsize=11)
ax = axes[0]
for i, lab in enumerate(["Pathway 1\n(e.g., summer program)", "Pathway 2\n(e.g., coursework)",
                         "Pathway 3\n(e.g., self-study)"]):
    box(ax, 1.65, 4.8 - 1.8 * i, lab, fs=8.8)
    arrow(ax, (2.95, 4.8 - 1.8 * i), (4.6, 3.0), lw=1.3)
box(ax, 6.0, 3.0, "Equivalent directly\nevidenced attribute")
arrow(ax, (7.25, 3.0), (8.25, 3.0))
box(ax, 9.1, 3.0, "Equivalent\nevaluation", fs=9.5)
ax = axes[1]
for i, lab in enumerate(["Pathway A\n(prestigious)", "Pathway B\n(less visible)"]):
    box(ax, 1.65, 4.3 - 2.6 * i, lab, fs=8.8)
    arrow(ax, (2.85, 4.3 - 2.6 * i), (4.6, 3.0), lw=1.3)
box(ax, 6.0, 3.0, "Equivalent directly\nevidenced attribute")
arrow(ax, (7.25, 3.0), (8.25, 3.0))
box(ax, 9.1, 3.0, "Different\nevaluations", fs=9.5)
arrow(ax, (2.0, 4.85), (8.85, 3.45), ls="--", lw=1.6, rad=-0.25)
ax.text(3.6, 5.45, "pathway record weighted directly", fontsize=9, style="italic")
fig.tight_layout(); save(fig, "Figure2")

# Figure 3: evidence-proximity continuum (no values, no estimated positions)
fig, ax = plt.subplots(figsize=(9.0, 4.4))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis("off")
ax.plot([1.0, 9.0], [3.3, 3.3], color=K, lw=1.4)
arrow(ax, (8.6, 3.3), (9.5, 3.3), lw=1.4)
arrow(ax, (1.4, 3.3), (0.5, 3.3), lw=1.4)
ax.text(0.5, 3.65, "more distal", fontsize=10, ha="left")
ax.text(9.5, 3.65, "more proximal", fontsize=10, ha="right")
ex = [(1.9, "records of\nparticipation"), (3.95, "narratives and\nreferences"),
      (6.05, "grades and\nexaminations"), (8.1, "structured performance\nsamples")]
for x, t in ex:
    ax.plot([x], [3.3], marker="o", ms=8, color="white", mec=K, mew=1.5, zorder=3)
    ax.text(x, 4.3, t, ha="center", fontsize=9.5)
ax.text(5.0, 5.45, "Proximity of evidence to the target attribute (relative, construct-specific)",
        ha="center", fontsize=10.5)
arrow(ax, (2.2, 2.35), (7.8, 2.35), ls="--", color=G)
ax.text(5.0, 1.8, "as proximal evidence of the target improves, the warrant for proxy weight on biography weakens",
        ha="center", fontsize=9.3, style="italic", color=G)
ax.text(5.0, 0.7, "Placement is illustrative and depends on the construct; it is not empirically estimated.",
        ha="center", fontsize=9, style="italic", color=G)
fig.tight_layout(); save(fig, "Figure3")
print("written:", sorted(os.listdir(OUT)))
