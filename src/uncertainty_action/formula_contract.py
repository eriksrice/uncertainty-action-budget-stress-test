from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class FormulaContract:
    budget: int
    lambda_values: tuple[float, ...]
    expression: str = "robust_score = mean_score - lambda * uncertainty_width"


DEFAULT_CONTRACT = FormulaContract(budget=4, lambda_values=(0.0, 0.5, 1.0))


def load_formula_contract(path: Path) -> FormulaContract:
    """Load the tiny YAML contract without depending on PyYAML."""
    if not path.exists():
        return DEFAULT_CONTRACT

    budget = DEFAULT_CONTRACT.budget
    lambda_values: list[float] = []
    in_lambda_values = False

    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("budget:"):
            budget = int(stripped.split(":", 1)[1].strip())
        elif stripped.startswith("lambda_values:"):
            in_lambda_values = True
        elif in_lambda_values and stripped.startswith("-"):
            lambda_values.append(float(stripped.removeprefix("-").strip()))
        elif in_lambda_values and stripped and not stripped.startswith("-"):
            in_lambda_values = False

    return FormulaContract(
        budget=budget,
        lambda_values=tuple(lambda_values) if lambda_values else DEFAULT_CONTRACT.lambda_values,
    )


def robust_score(mean_score: float, uncertainty_width: float, lambda_value: float) -> float:
    return mean_score - lambda_value * uncertainty_width
