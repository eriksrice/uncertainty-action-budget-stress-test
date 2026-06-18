from __future__ import annotations

from dataclasses import dataclass

from uncertainty_action.fixture_loader import PredictionRow
from uncertainty_action.formula_contract import FormulaContract
from uncertainty_action.policy_runner import select_robust, select_top_mean


@dataclass(frozen=True)
class FixtureSensitivity:
    fixture_id: str
    baseline_selected_ids: list[str]
    selected_ids_by_lambda: dict[str, list[str]]


def build_fixture_sensitivity(
    fixture_id: str,
    rows: list[PredictionRow],
    contract: FormulaContract,
) -> FixtureSensitivity:
    return FixtureSensitivity(
        fixture_id=fixture_id,
        baseline_selected_ids=select_top_mean(rows, contract.budget),
        selected_ids_by_lambda={
            f"{lambda_value:g}": select_robust(rows, contract.budget, lambda_value)
            for lambda_value in contract.lambda_values
        },
    )
