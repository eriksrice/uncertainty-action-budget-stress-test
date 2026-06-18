from __future__ import annotations

import json
import shutil
from dataclasses import asdict
from pathlib import Path

from uncertainty_action.action_set_diff import diff_action_sets
from uncertainty_action.assertions import AssertionResult
from uncertainty_action.fixture_loader import PredictionRow
from uncertainty_action.formula_contract import FormulaContract, robust_score
from uncertainty_action.policy_runner import robust_score_table, select_robust, select_top_mean

PUBLIC_SAFE_NOTE = (
    "Synthetic/public-safe example only. This artifact contains no real WTCHP "
    "data, real people, operational thresholds, clinical guidance, staffing "
    "guidance, policy recommendation, or deployment claim."
)


def recreate_artifacts_dir(root: Path) -> Path:
    artifacts_dir = root / "artifacts"
    if artifacts_dir.exists():
        shutil.rmtree(artifacts_dir)
    artifacts_dir.mkdir(parents=True)
    return artifacts_dir


def selected_ids_text(ids: list[str]) -> str:
    return ", ".join(ids)


def write_top_mean_policy(
    artifacts_dir: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
) -> None:
    lines = [
        "# Top Mean Policy",
        "",
        PUBLIC_SAFE_NOTE,
        "",
        f"Budget: `{contract.budget}`",
        "",
        "Selection rule: descending `mean_score`, then ascending `case_id`.",
        "",
    ]
    for fixture_id, rows in fixtures.items():
        selected = select_top_mean(rows, contract.budget)
        lines.extend(
            [
                f"## {fixture_id}",
                "",
                f"Selected IDs: `{selected_ids_text(selected)}`",
                "",
            ]
        )
    (artifacts_dir / "top_mean_policy.md").write_text("\n".join(lines), encoding="utf-8")


def write_uncertainty_robust_policy(
    artifacts_dir: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
) -> None:
    lines = [
        "# Uncertainty-Robust Policy",
        "",
        PUBLIC_SAFE_NOTE,
        "",
        f"Formula: `{contract.expression}`",
        "",
        f"Lambda values: `{', '.join(f'{value:g}' for value in contract.lambda_values)}`",
        "",
    ]
    for fixture_id, rows in fixtures.items():
        lines.extend([f"## {fixture_id}", ""])
        for lambda_value in contract.lambda_values:
            selected = select_robust(rows, contract.budget, lambda_value)
            lines.append(f"- Lambda `{lambda_value:g}` selected IDs: `{selected_ids_text(selected)}`")
        lines.extend(["", "| Case | Mean | Uncertainty | " + " | ".join(f"Lambda {v:g}" for v in contract.lambda_values) + " |", "|---|---:|---:|" + "|".join("---:" for _ in contract.lambda_values) + "|"])
        for row in rows:
            scores = [
                f"{robust_score(row.mean_score, row.uncertainty_width, lambda_value):.3f}"
                for lambda_value in contract.lambda_values
            ]
            lines.append(
                f"| {row.case_id} | {row.mean_score:.3f} | {row.uncertainty_width:.3f} | "
                + " | ".join(scores)
                + " |"
            )
        lines.append("")
    (artifacts_dir / "uncertainty_robust_policy.md").write_text("\n".join(lines), encoding="utf-8")


def write_action_set_diff(
    artifacts_dir: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
) -> None:
    lines = [
        "# Uncertainty Action Budget Diff",
        "",
        PUBLIC_SAFE_NOTE,
        "",
        "The baseline action set is selected by top mean score. The robust action set uses lambda `0.5`.",
        "",
    ]
    for fixture_id, rows in fixtures.items():
        baseline = select_top_mean(rows, contract.budget)
        robust = select_robust(rows, contract.budget, 0.5)
        diff = diff_action_sets(baseline, robust)
        lines.extend(
            [
                f"## {fixture_id}",
                "",
                f"Baseline selected IDs: `{selected_ids_text(diff['baseline_selected_ids'])}`",
                f"Robust selected IDs: `{selected_ids_text(diff['robust_selected_ids'])}`",
                f"Removed IDs: `{selected_ids_text(diff['removed_ids'])}`",
                f"Added IDs: `{selected_ids_text(diff['added_ids'])}`",
                "",
                "Plain-English explanation: cases leave the fixed budget when their uncertainty width lowers their robust score enough for lower-uncertainty cases to enter.",
                "",
            ]
        )
    (artifacts_dir / "uncertainty_action_budget_diff.md").write_text("\n".join(lines), encoding="utf-8")


def write_formula_sensitivity_table(
    artifacts_dir: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
) -> None:
    lines = [
        "# Formula Sensitivity Table",
        "",
        PUBLIC_SAFE_NOTE,
        "",
        "| Fixture | Lambda | Selected IDs | Changed From Top Mean |",
        "|---|---:|---|---|",
    ]
    for fixture_id, rows in fixtures.items():
        baseline = select_top_mean(rows, contract.budget)
        for lambda_value in contract.lambda_values:
            selected = select_robust(rows, contract.budget, lambda_value)
            changed = selected != baseline
            lines.append(
                f"| {fixture_id} | {lambda_value:g} | {selected_ids_text(selected)} | {str(changed).lower()} |"
            )
    lines.extend(
        [
            "",
            "The zero-uncertainty control should not change the selected IDs at nonzero lambda values.",
            "",
        ]
    )
    (artifacts_dir / "formula_sensitivity_table.md").write_text("\n".join(lines), encoding="utf-8")


def write_assertion_results(artifacts_dir: Path, results: list[AssertionResult]) -> None:
    payload = {
        "all_passed": all(result.passed for result in results),
        "assertion_names": [result.name for result in results],
        "expected_values": {result.name: result.expected for result in results},
        "computed_values": {result.name: result.computed for result in results},
        "pass_fail_results": {result.name: result.passed for result in results},
        "results": [asdict(result) for result in results],
        "self_comparison_guard_result": [
            asdict(result)
            for result in results
            if "self_comparison_guard" in result.name
        ],
    }
    (artifacts_dir / "assertion_results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def write_incident_summary(
    artifacts_dir: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
) -> None:
    payload = {
        "fixture_ids": list(fixtures),
        "budget": contract.budget,
        "formula": contract.expression,
        "lambda_values": list(contract.lambda_values),
        "selected_ids_by_policy": {
            fixture_id: {
                "top_mean": select_top_mean(rows, contract.budget),
                **{
                    f"robust_lambda_{lambda_value:g}": select_robust(rows, contract.budget, lambda_value)
                    for lambda_value in contract.lambda_values
                },
            }
            for fixture_id, rows in fixtures.items()
        },
        "action_set_changed": {
            fixture_id: select_top_mean(rows, contract.budget) != select_robust(rows, contract.budget, 0.5)
            for fixture_id, rows in fixtures.items()
        },
        "public_safe_boundary": PUBLIC_SAFE_NOTE,
    }
    (artifacts_dir / "incident_summary.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def write_all_artifacts(
    root: Path,
    fixtures: dict[str, list[PredictionRow]],
    contract: FormulaContract,
    assertion_results: list[AssertionResult],
) -> None:
    artifacts_dir = recreate_artifacts_dir(root)
    report_fixtures = {
        key: value for key, value in fixtures.items() if key != "zero_uncertainty_control"
    }
    write_top_mean_policy(artifacts_dir, report_fixtures, contract)
    write_uncertainty_robust_policy(artifacts_dir, report_fixtures, contract)
    write_action_set_diff(artifacts_dir, report_fixtures, contract)
    write_formula_sensitivity_table(artifacts_dir, fixtures, contract)
    write_assertion_results(artifacts_dir, assertion_results)
    write_incident_summary(artifacts_dir, fixtures, contract)
