# Uncertainty-to-Action Budget Stress Test

This project is a deterministic stress test for fixed-budget action policies under prediction uncertainty.

It shows that a fixed action budget selected by top mean model scores can differ from an uncertainty-robust action set. The difference is inspectable through formula sensitivity, neutral controls, action-set diffs, and assertion results.

All data is synthetic and public-safe. This repository does not use real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendations, or deployment claims.

## What It Proves

The baseline policy selects cases by top mean score. The robust policy computes:

```text
robust_score = mean_score - lambda * uncertainty_width
```

For the synthetic fixtures, the selected action set changes at nonzero lambda values while the zero-uncertainty control preserves the baseline. That means the project is not simply changing decisions for every input; the change is tied to uncertainty width.

## One-Command Demo

```bash
./scripts/demo.sh
```

The demo is deterministic. It does not call external services, download data, train a model, require credentials, or depend on network access.

Generated artifacts:

- `artifacts/top_mean_policy.md`
- `artifacts/uncertainty_robust_policy.md`
- `artifacts/uncertainty_action_budget_diff.md`
- `artifacts/formula_sensitivity_table.md`
- `artifacts/assertion_results.json`
- `artifacts/incident_summary.json`

## Reviewer Path

1. Open `artifacts/top_mean_policy.md` to see the baseline fixed-budget action set.
2. Open `artifacts/uncertainty_robust_policy.md` to see robust selections by lambda.
3. Open `artifacts/uncertainty_action_budget_diff.md` to inspect removed and added cases.
4. Open `artifacts/formula_sensitivity_table.md` to verify lambda `0.0`, `0.5`, `1.0`, and the zero-uncertainty control.
5. Open `artifacts/assertion_results.json` to confirm expected/computed separation and the self-comparison guard.

## Out Of Scope

- Real WTCHP data
- Real operational thresholds
- Real triage or action recommendations
- Model training
- Live model calls
- Dashboard UI
- Live integrations
- Clinical, staffing, policy, or deployment claims
- General decision optimization platform
