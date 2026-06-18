from pathlib import Path
import unittest

from uncertainty_action.assertions import (
    assert_fixture,
    assert_zero_uncertainty_control,
    expected_ids,
    missing_expected_values_fail_closed,
    self_comparison_guard,
)
from uncertainty_action.cli import load_fixtures
from uncertainty_action.fixture_loader import PredictionRow
from uncertainty_action.formula_contract import load_formula_contract


ROOT = Path(__file__).resolve().parents[1]


class AssertionIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = load_fixtures(ROOT)
        self.contract = load_formula_contract(ROOT / "configs" / "robust_action_policy.yaml")

    def test_assertion_runner_passes_clean_and_messier_fixtures(self):
        results = []
        results.extend(assert_fixture("clean_fixture", self.fixtures["clean_fixture"], self.contract))
        results.extend(assert_fixture("messier_fixture", self.fixtures["messier_fixture"], self.contract))
        results.extend(assert_zero_uncertainty_control(self.fixtures["zero_uncertainty_control"], self.contract))
        self.assertTrue(all(result.passed for result in results))

    def test_self_comparison_guard_rejects_expected_label_source(self):
        result = self_comparison_guard(["A", "B"], ["A", "B"], "expected_fixture_labels")
        self.assertFalse(result.passed)

    def test_missing_expected_values_fail_closed(self):
        result = missing_expected_values_fail_closed(self.fixtures["clean_fixture"])
        self.assertTrue(result.passed)

    def test_expected_ids_raises_on_missing_expected_value(self):
        row = PredictionRow("X", 0.5, 0.1, "missing_expected", None, False, False)
        with self.assertRaises(ValueError):
            expected_ids([row], "top_mean_selected_expected")


if __name__ == "__main__":
    unittest.main()
