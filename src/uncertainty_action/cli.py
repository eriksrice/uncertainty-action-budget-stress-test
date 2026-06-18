from __future__ import annotations

import argparse
from pathlib import Path

from uncertainty_action.artifact_writer import write_all_artifacts
from uncertainty_action.assertions import assert_fixture, assert_zero_uncertainty_control
from uncertainty_action.fixture_loader import load_fixture
from uncertainty_action.formula_contract import load_formula_contract


def load_fixtures(root: Path):
    data_dir = root / "data" / "synthetic"
    return {
        "clean_fixture": load_fixture(data_dir / "clean_uncertainty_cases.csv"),
        "messier_fixture": load_fixture(data_dir / "messier_uncertainty_cases.csv"),
        "zero_uncertainty_control": load_fixture(data_dir / "zero_uncertainty_control.csv"),
    }


def run(root: Path) -> int:
    contract = load_formula_contract(root / "configs" / "robust_action_policy.yaml")
    fixtures = load_fixtures(root)

    assertion_results = []
    assertion_results.extend(assert_fixture("clean_fixture", fixtures["clean_fixture"], contract))
    assertion_results.extend(assert_fixture("messier_fixture", fixtures["messier_fixture"], contract))
    assertion_results.extend(assert_zero_uncertainty_control(fixtures["zero_uncertainty_control"], contract))

    write_all_artifacts(root, fixtures, contract, assertion_results)

    failed = [result for result in assertion_results if not result.passed]
    print("Uncertainty-to-Action Budget Stress Test")
    print(f"Artifacts written to: {root / 'artifacts'}")
    print(f"Assertions: {len(assertion_results) - len(failed)}/{len(assertion_results)} passed")
    if failed:
        for result in failed:
            print(f"FAIL {result.name}: {result.detail}")
        return 1
    print("PASS: top-mean and uncertainty-robust action policies behave as expected.")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run the uncertainty-to-action stress test.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path.cwd(),
        help="Project root. Defaults to the current working directory.",
    )
    args = parser.parse_args(argv)
    return run(args.root.resolve())
