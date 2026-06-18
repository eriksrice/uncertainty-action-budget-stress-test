# Reviewer Walkthrough

This project is synthetic and public-safe. It contains no real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendation, or deployment claim.

## Five-Minute Proof Path

1. Run `./scripts/demo.sh`.
2. Open `artifacts/top_mean_policy.md` and note the baseline selected IDs.
3. Open `artifacts/uncertainty_robust_policy.md` and compare selected IDs at lambda `0.5` and `1.0`.
4. Open `artifacts/uncertainty_action_budget_diff.md` and inspect which cases were removed and added.
5. Open `artifacts/formula_sensitivity_table.md` and confirm lambda `0.0` plus zero-uncertainty controls.
6. Open `artifacts/assertion_results.json` and confirm `all_passed: true`.

## Reviewer Takeaway

Top mean model score is not always the same thing as a robust fixed-budget action set. When uncertainty is treated as decision risk, the selected cases can change, and the change should be inspected with controls.
