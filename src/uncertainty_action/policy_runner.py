from __future__ import annotations

from uncertainty_action.fixture_loader import PredictionRow
from uncertainty_action.formula_contract import robust_score


def select_top_mean(rows: list[PredictionRow], budget: int) -> list[str]:
    ranked = sorted(rows, key=lambda row: (-row.mean_score, row.case_id))
    return [row.case_id for row in ranked[:budget]]


def select_robust(rows: list[PredictionRow], budget: int, lambda_value: float) -> list[str]:
    ranked = sorted(
        rows,
        key=lambda row: (
            -robust_score(row.mean_score, row.uncertainty_width, lambda_value),
            -row.mean_score,
            row.case_id,
        ),
    )
    return [row.case_id for row in ranked[:budget]]


def robust_score_table(rows: list[PredictionRow], lambda_values: tuple[float, ...]) -> list[dict[str, object]]:
    table: list[dict[str, object]] = []
    for row in rows:
        record: dict[str, object] = {
            "case_id": row.case_id,
            "mean_score": row.mean_score,
            "uncertainty_width": row.uncertainty_width,
            "row_purpose": row.row_purpose,
        }
        for lambda_value in lambda_values:
            record[f"lambda_{lambda_value:g}"] = round(
                robust_score(row.mean_score, row.uncertainty_width, lambda_value),
                6,
            )
        table.append(record)
    return table
