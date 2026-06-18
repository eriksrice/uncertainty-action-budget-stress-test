#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

export PYTHONPATH="$ROOT_DIR/src"

python3 -m unittest discover -s tests
python3 -m uncertainty_action --root "$ROOT_DIR"

printf '\nReviewer artifacts:\n'
printf '  artifacts/top_mean_policy.md\n'
printf '  artifacts/uncertainty_robust_policy.md\n'
printf '  artifacts/uncertainty_action_budget_diff.md\n'
printf '  artifacts/formula_sensitivity_table.md\n'
printf '  artifacts/assertion_results.json\n'
printf '  artifacts/incident_summary.json\n'
