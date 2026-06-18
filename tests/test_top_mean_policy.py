from pathlib import Path
import unittest

from uncertainty_action.cli import load_fixtures
from uncertainty_action.formula_contract import load_formula_contract
from uncertainty_action.policy_runner import select_top_mean


ROOT = Path(__file__).resolve().parents[1]


class TopMeanPolicyTests(unittest.TestCase):
    def test_clean_fixture_top_mean_selects_a_b_c_d(self):
        fixtures = load_fixtures(ROOT)
        contract = load_formula_contract(ROOT / "configs" / "robust_action_policy.yaml")
        self.assertEqual(select_top_mean(fixtures["clean_fixture"], contract.budget), ["A", "B", "C", "D"])

    def test_messier_fixture_top_mean_selects_m01_m02_m03_m04(self):
        fixtures = load_fixtures(ROOT)
        contract = load_formula_contract(ROOT / "configs" / "robust_action_policy.yaml")
        self.assertEqual(
            select_top_mean(fixtures["messier_fixture"], contract.budget),
            ["M01", "M02", "M03", "M04"],
        )


if __name__ == "__main__":
    unittest.main()
