# Career Blurbs

Use these as external-facing summaries for the project. Keep the framing synthetic, method-centered, and action-policy focused.

## Resume Bullet

- Built a deterministic Applied AI stress test showing that fixed-budget action sets selected by top mean model scores can change when prediction uncertainty is treated as decision risk; implemented synthetic fixtures, robust-score policy replay, lambda sensitivity, zero-uncertainty controls, assertion-integrity guards, CI, and reviewer artifacts.

## Short Resume Variant

- Built a reproducible uncertainty-to-action stress test with synthetic fixtures, robust policy replay, neutral controls, assertion-integrity checks, and CI-backed reviewer artifacts.

## LinkedIn / Portfolio Card

`Uncertainty-to-Action Budget Stress Test` is a compact Applied AI project about a common decision-support failure mode: top model scores are not automatically the right action queue under a fixed budget. The repo uses synthetic fixtures to compare a top-mean baseline against an uncertainty-robust policy, then produces reviewer artifacts showing exactly which cases leave and enter the action set. It is deterministic, public-safe, CI-backed, and intentionally narrow: no real WTCHP data, no dashboard, no model training, and no operational recommendations.

## Interview Explanation

I built this to show that model scores need decision-policy controls before they become work queues. The baseline policy takes the four highest mean scores. The robust policy uses the same budget but penalizes uncertainty width. In both synthetic fixtures, the action set changes; in the zero-uncertainty control, it does not. That gives a reviewer a small but concrete proof: the change is tied to uncertainty, not just to a formula that always rearranges cases. The repo includes generated artifacts, assertion results, and CI so the proof is reproducible rather than just described.

## 30-Second Spoken Version

This is a small Applied AI reliability project. It asks whether a fixed action budget should simply take the top model scores. In my synthetic fixtures, once uncertainty is treated as decision risk, the selected action set changes. The important part is not the formula itself; it is the controlled proof path: lambda sensitivity, a zero-uncertainty neutral control, a messier fixture, assertion-integrity checks, and generated reviewer artifacts.

## What Not To Say

- "I built a WTCHP intervention optimizer."
- "This recommends real public health actions."
- "This is a production triage system."
- "This proves the robust formula is universally correct."
- "This uses real WTCHP data."
