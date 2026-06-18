from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PredictionRow:
    case_id: str
    mean_score: float
    uncertainty_width: float
    row_purpose: str
    top_mean_selected_expected: bool | None
    robust_selected_expected_lambda_0_5: bool | None
    robust_selected_expected_lambda_1_0: bool | None


def parse_bool(value: str) -> bool | None:
    cleaned = value.strip().lower()
    if cleaned in {"true", "1", "yes"}:
        return True
    if cleaned in {"false", "0", "no"}:
        return False
    if cleaned == "":
        return None
    raise ValueError(f"Unsupported boolean value: {value!r}")


def load_fixture(path: Path) -> list[PredictionRow]:
    rows: list[PredictionRow] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        required = {
            "case_id",
            "mean_score",
            "uncertainty_width",
            "row_purpose",
            "top_mean_selected_expected",
            "robust_selected_expected_lambda_0_5",
            "robust_selected_expected_lambda_1_0",
        }
        missing = required.difference(reader.fieldnames or [])
        if missing:
            raise ValueError(f"{path} is missing required columns: {sorted(missing)}")
        for raw in reader:
            rows.append(
                PredictionRow(
                    case_id=raw["case_id"],
                    mean_score=float(raw["mean_score"]),
                    uncertainty_width=float(raw["uncertainty_width"]),
                    row_purpose=raw["row_purpose"],
                    top_mean_selected_expected=parse_bool(raw["top_mean_selected_expected"]),
                    robust_selected_expected_lambda_0_5=parse_bool(raw["robust_selected_expected_lambda_0_5"]),
                    robust_selected_expected_lambda_1_0=parse_bool(raw["robust_selected_expected_lambda_1_0"]),
                )
            )
    if not rows:
        raise ValueError(f"{path} has no rows")
    return rows
