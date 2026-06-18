# Project Summary

`Uncertainty-to-Action Budget Stress Test` is a deterministic Applied AI portfolio project about action policy under prediction uncertainty.

It tests whether a fixed action budget should simply take the highest mean model scores.

The answer in the synthetic fixtures is no: once uncertainty width is treated as decision risk, the selected action set changes.

The clean fixture moves from `A, B, C, D` to `C, D, E, F`.

The messier fixture moves from `M01, M02, M03, M04` to `M01, M03, M05, M07`.

The zero-uncertainty control preserves the baseline action set, which keeps the demo from being a formula trick.

The project demonstrates senior signal around model-score interpretation, fixed-budget decision policy, uncertainty controls, and assertion integrity.

Run it with `./scripts/demo.sh`.

The demo is synthetic/public-safe and makes no real WTCHP, clinical, staffing, policy, or deployment claims.
