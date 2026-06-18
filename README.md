# Uncertainty-to-Action Budget Stress Test

This project is a deterministic stress test for fixed-budget action policies under prediction uncertainty. It demonstrates a common decision-support failure mode: the cases with the highest mean model scores are not always the same cases a robust action policy should choose when prediction uncertainty matters.

The proof is intentionally small. A baseline policy selects four synthetic cases by top mean score. An uncertainty-robust policy applies the same fixed budget after penalizing uncertainty width. The selected action set changes, and the change is checked against lambda sensitivity, a zero-uncertainty neutral control, a messier fixture, and assertion-integrity guards.

All data is synthetic and public-safe. This repository does not use real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendations, or deployment claims.

## What It Proves

The baseline policy asks:

> Which four cases have the highest mean model scores?

The robust policy asks:

> Which four cases still look strongest after uncertainty is treated as decision risk?

The robust policy computes:

```text
robust_score = mean_score - lambda * uncertainty_width
```

For both synthetic fixtures, the selected action set changes at nonzero lambda values. The zero-uncertainty control preserves the baseline. That distinction matters: the policy is not changing decisions for every input; the change is tied to uncertainty width.

## Why It Matters

In applied AI decision support, model scores are often treated as a ranked work queue. This repo shows why that can be unsafe under a fixed action budget: uncertainty can change which cases deserve scarce attention. The project is not claiming one universal formula. It is a reproducible proof that action policies need controls before top scores become action queues.

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

## Expected Output

The demo should show this action-set change:

| Fixture | Top-Mean Policy | Uncertainty-Robust Policy |
|---|---|---|
| Clean | `A, B, C, D` | `C, D, E, F` |
| Messier | `M01, M02, M03, M04` | `M01, M03, M05, M07` |

The zero-uncertainty control should preserve the top-mean selection at nonzero lambda values.

## Reviewer Path

1. Run `./scripts/demo.sh`.
2. Open `artifacts/uncertainty_action_budget_diff.md` first. This is the main proof: the fixed budget selects different cases after uncertainty is penalized.
3. Open `artifacts/top_mean_policy.md` to see the baseline action set.
4. Open `artifacts/uncertainty_robust_policy.md` to see robust selections and score tables by lambda.
5. Open `artifacts/formula_sensitivity_table.md` to verify lambda `0.0`, `0.5`, `1.0`, and the zero-uncertainty control.
6. Open `artifacts/assertion_results.json` to confirm expected/computed separation, fail-closed missing expected values, and the self-comparison guard.

## What Good Looks Like

- The top-mean policy selects `A, B, C, D` on the clean fixture.
- The robust policy selects `C, D, E, F` at lambda `0.5` and `1.0`.
- The messier fixture preserves one high-mean moderate-uncertainty case while replacing higher-uncertainty cases.
- The zero-uncertainty control keeps the same selected IDs at nonzero lambda values.
- All assertions pass without copying expected labels into computed results.

## Portfolio Notes

- [Portfolio positioning](docs/portfolio_positioning.md)
- [Reviewer walkthrough](docs/reviewer_walkthrough.md)
- [Scope reassessment](docs/scope_reassessment.md)

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
