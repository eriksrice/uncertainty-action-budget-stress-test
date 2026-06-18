# Reviewer Walkthrough

This project is synthetic and public-safe. It contains no real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendation, or deployment claim.

## The Question To Ask

If a model produces mean scores and uncertainty widths, should a fixed action budget simply take the top mean scores?

This repo shows a controlled counterexample. The top-score action set and the uncertainty-robust action set differ, and the difference survives a messier fixture while preserving a zero-uncertainty neutral control.

## Five-Minute Proof Path

1. Run `./scripts/demo.sh`.
2. Open `artifacts/uncertainty_action_budget_diff.md` and inspect the removed and added cases. This is the core reviewer artifact.
3. Open `artifacts/top_mean_policy.md` and note the baseline selected IDs.
4. Open `artifacts/uncertainty_robust_policy.md` and compare selected IDs at lambda `0.5` and `1.0`.
5. Open `artifacts/formula_sensitivity_table.md` and confirm lambda `0.0` plus zero-uncertainty controls.
6. Open `artifacts/assertion_results.json` and confirm `all_passed: true`.

## What To Notice

- The clean fixture changes from `A, B, C, D` to `C, D, E, F`.
- The messier fixture changes from `M01, M02, M03, M04` to `M01, M03, M05, M07`.
- `M01` survives in the messier fixture, so the robust policy is not simply dropping every high-mean case.
- Lambda `0.0` matches the top-mean policy.
- The zero-uncertainty control preserves the top-mean action set at nonzero lambda values.
- Assertion results separate expected values from computed values and include a self-comparison guard.

## Reviewer Takeaway

Top mean model score is not always the same thing as a robust fixed-budget action set. When uncertainty is treated as decision risk, the selected cases can change, and the change should be inspected with controls before scores become action queues.
