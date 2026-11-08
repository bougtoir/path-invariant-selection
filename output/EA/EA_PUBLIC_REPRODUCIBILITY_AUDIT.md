# EA_PUBLIC_REPRODUCIBILITY_AUDIT

Genuine clean-clone test of the public repository, run outside the private working tree.

- Public repository: https://github.com/bougtoir/path-invariant-selection
- Branch: `main` (default)
- Commit tested: `dbf2b4babc30e1b0201088c5dfc959ecd80859c3`
- First attempt (commit `74bb4b9`, before this QC pass): figures were generated, but the repository had **no README or dependency file**. A user following only the public files could not know the command or the dependencies, so the test was judged FAIL. Fix: added `README.md` (instructions) and `requirements.txt` (pinned dependencies), mirrored, and re-ran.

## Procedure (final run)

```bash
T=$(mktemp -d -p ~ eaclone.XXXX); cd $T
git clone https://github.com/bougtoir/path-invariant-selection.git pub && cd pub
rm -f figures/EA/*                      # ensure outputs are regenerated, not pre-existing
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # matplotlib==3.10.9, numpy==2.2.6, Pillow==12.3.0 (Python 3.10.12)
.venv/bin/python scripts/make_figures_EA.py   # as documented in README.md
```

No file was copied from the private tree into the clone. The comparison against the submission figures was done after generation.

## Results

| Figure | Generated | Size / mode / dpi | Pixel comparison with submission file | Content check | Result |
|---|---|---|---|---|---|
| Figure 1 (PNG, TIFF) | yes | 5400×3000 L 600 dpi; 10800×6000 L 1200 dpi | identical pixels (PNG and TIFF) | Opportunity → experience → target attribute → direct evidence → decision. Four role arrows labeled developmental/evidential/contextual/credential, as in the caption | PASS |
| Figure 2 (PNG, TIFF) | yes | 5760×2640 L 600 dpi; 11520×5280 L 1200 dpi | identical pixels | Panel A path-invariant vs Panel B path-dependent with dashed pathway→evaluation arrow, as in the caption | PASS |
| Figure 3 (PNG, TIFF) | yes | 5400×2640 L 600 dpi; 10800×5280 L 1200 dpi | identical pixels | Qualitative proximal–distal continuum, no numerical axis. In-figure note: "Positions are conceptual and illustrative; they are not empirically estimated" | PASS |

Subsequent mirror commits after `dbf2b4b` changed documentation/audit files only. `scripts/make_figures_EA.py`, `requirements.txt` and `README.md` are verified unchanged by `git diff` before the final handoff (see FINAL_HANDOFF_EA_FINAL.md).

Result: PASS. The Data Availability Statement ("code that generates the three conceptual figures ... is openly available") is accurate.
