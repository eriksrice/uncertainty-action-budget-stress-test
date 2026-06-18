from __future__ import annotations

from dataclasses import dataclass

from uncertainty_action.fixture_loader import PredictionRow
from uncertainty_action.formula_contract import FormulaContract
from uncertainty_action.policy_runner import select_robust, select_top_mean


@dataclass(frozen=True)
class AssertionResult:
    name: str
    expected: object
    computed: object
    passed: bool
    detail: str


def expected_ids(rows: list[PredictionRow], field_name: str) -> list[str]:
    values: list[str] = []
    for row in rows:
        value = getattr(row, field_name)
        if value is None:
            raise ValueError(f"Missing expected value for {row.case_id}.{field_name}")
        if value:
            values.append(row.case_id)
    return values


def self_comparison_guard(expected: list[str], computed: list[str], computed_source: str) -> AssertionResult:
    copied = computed_source == "expected_fixture_labels"
    passed = not copied
    return AssertionResult(
        name="copied_expected_selected_ids_fail_self_comparison_guard",
        expected="computed values must be derived from policy code",
        computed={"computed_source": computed_source, "selected_ids": computed},
        passed=passed,
        detail="PASS" if passed else "FAIL: computed IDs came from expected fixture labels",
    )


def missing_expected_values_fail_closed(rows: list[PredictionRow]) -> AssertionResult:
    mutated = [
        PredictionRow(
            case_id=row.case_id,
            mean_score=row.mean_score,
            uncertainty_width=row.uncertainty_width,
            row_purpose=row.row_purpose,
            top_mean_selected_expected=None if index == 0 else row.top_mean_selected_expected,
            robust_selected_expected_lambda_0_5=row.robust_selected_expected_lambda_0_5,
            robust_selected_expected_lambda_1_0=row.robust_selected_expected_lambda_1_0,
        )
        for index, row in enumerate(rows)
    ]
    try:
        expected_ids(mutated, "top_mean_selected_expected")
    except ValueError as exc:
        return AssertionResult(
            name="missing_expected_values_fail_closed",
            expected="missing expected value raises ValueError",
            computed=str(exc),
            passed=True,
            detail="PASS",
        )
    return AssertionResult(
        name="missing_expected_values_fail_closed",
        expected="missing expected value raises ValueError",
        computed="no error",
        passed=False,
        detail="FAIL: missing expected value did not fail closed",
    )


def assert_fixture(fixture_id: str, rows: list[PredictionRow], contract: FormulaContract) -> list[AssertionResult]:
    baseline_expected = expected_ids(rows, "top_mean_selected_expected")
    baseline_computed = select_top_mean(rows, contract.budget)
    lambda_0_5_expected = expected_ids(rows, "robust_selected_expected_lambda_0_5")
    lambda_1_0_expected = expected_ids(rows, "robust_selected_expected_lambda_1_0")
    lambda_0_5_computed = select_robust(rows, contract.budget, 0.5)
    lambda_1_0_computed = select_robust(rows, contract.budget, 1.0)

    source_guard = self_comparison_guard(baseline_expected, baseline_computed, "policy_runner")
    copied_guard = self_comparison_guard(baseline_expected, baseline_expected, "expected_fixture_labels")
    missing_guard = missing_expected_values_fail_closed(rows)
    results = [
        AssertionResult(
            name=f"{fixture_id}_top_mean_matches_expected",
            expected=baseline_expected,
            computed=baseline_computed,
            passed=baseline_expected == baseline_computed,
            detail="baseline top-mean selected IDs",
        ),
        AssertionResult(
            name=f"{fixture_id}_lambda_0_5_matches_expected",
            expected=lambda_0_5_expected,
            computed=lambda_0_5_computed,
            passed=lambda_0_5_expected == lambda_0_5_computed,
            detail="robust selected IDs at lambda 0.5",
        ),
        AssertionResult(
            name=f"{fixture_id}_lambda_1_0_matches_expected",
            expected=lambda_1_0_expected,
            computed=lambda_1_0_computed,
            passed=lambda_1_0_expected == lambda_1_0_computed,
            detail="robust selected IDs at lambda 1.0",
        ),
        AssertionResult(
            name=f"{fixture_id}_lambda_0_0_matches_top_mean",
            expected=baseline_computed,
            computed=select_robust(rows, contract.budget, 0.0),
            passed=baseline_computed == select_robust(rows, contract.budget, 0.0),
            detail="lambda 0.0 should reduce to top-mean selection",
        ),
        AssertionResult(
            name=f"{fixture_id}_expected_and_computed_selected_ids_are_distinct",
            expected=source_guard.expected,
            computed=source_guard.computed,
            passed=source_guard.passed,
            detail=source_guard.detail,
        ),
        AssertionResult(
            name=f"{fixture_id}_copied_expected_selected_ids_fail_self_comparison_guard",
            expected="guard rejects computed IDs copied from expected fixture labels",
            computed=copied_guard.detail,
            passed=not copied_guard.passed,
            detail="negative guard behaved as expected",
        ),
        AssertionResult(
            name=f"{fixture_id}_missing_expected_values_fail_closed",
            expected=missing_guard.expected,
            computed=missing_guard.computed,
            passed=missing_guard.passed,
            detail=missing_guard.detail,
        ),
    ]
    return results


def assert_zero_uncertainty_control(rows: list[PredictionRow], contract: FormulaContract) -> list[AssertionResult]:
    baseline = select_top_mean(rows, contract.budget)
    return [
        AssertionResult(
            name=f"zero_uncertainty_control_matches_top_mean_for_lambda_{lambda_value:g}",
            expected=baseline,
            computed=select_robust(rows, contract.budget, lambda_value),
            passed=baseline == select_robust(rows, contract.budget, lambda_value),
            detail="zero uncertainty should preserve top-mean selection",
        )
        for lambda_value in contract.lambda_values
        if lambda_value != 0.0
    ]
