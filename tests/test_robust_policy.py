from pathlib import Path
import unittest

from uncertainty_action.cli import load_fixtures
from uncertainty_action.formula_contract import load_formula_contract
from uncertainty_action.policy_runner import select_robust, select_top_mean


ROOT = Path(__file__).resolve().parents[1]


class RobustPolicyTests(unittest.TestCase):
    def setUp(self):
        self.fixtures = load_fixtures(ROOT)
        self.contract = load_formula_contract(ROOT / "configs" / "robust_action_policy.yaml")

    def test_clean_fixture_nonzero_lambda_selects_c_d_e_f(self):
        self.assertEqual(select_robust(self.fixtures["clean_fixture"], self.contract.budget, 0.5), ["C", "D", "E", "F"])
        self.assertEqual(select_robust(self.fixtures["clean_fixture"], self.contract.budget, 1.0), ["C", "D", "E", "F"])

    def test_messier_fixture_nonzero_lambda_selects_m01_m03_m05_m07(self):
        expected = ["M01", "M03", "M05", "M07"]
        self.assertEqual(select_robust(self.fixtures["messier_fixture"], self.contract.budget, 0.5), expected)
        self.assertEqual(select_robust(self.fixtures["messier_fixture"], self.contract.budget, 1.0), expected)

    def test_lambda_zero_matches_top_mean(self):
        for fixture_id in ["clean_fixture", "messier_fixture"]:
            rows = self.fixtures[fixture_id]
            self.assertEqual(
                select_robust(rows, self.contract.budget, 0.0),
                select_top_mean(rows, self.contract.budget),
            )

    def test_zero_uncertainty_control_preserves_baseline(self):
        rows = self.fixtures["zero_uncertainty_control"]
        baseline = select_top_mean(rows, self.contract.budget)
        self.assertEqual(select_robust(rows, self.contract.budget, 0.5), baseline)
        self.assertEqual(select_robust(rows, self.contract.budget, 1.0), baseline)


if __name__ == "__main__":
    unittest.main()
