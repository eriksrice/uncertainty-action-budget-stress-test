from pathlib import Path
import unittest

from uncertainty_action.cli import load_fixtures
from uncertainty_action.formula_contract import load_formula_contract
from uncertainty_action.sensitivity_report import build_fixture_sensitivity


ROOT = Path(__file__).resolve().parents[1]


class FormulaSensitivityTests(unittest.TestCase):
    def test_clean_and_messier_fixtures_change_at_nonzero_lambda(self):
        fixtures = load_fixtures(ROOT)
        contract = load_formula_contract(ROOT / "configs" / "robust_action_policy.yaml")
        for fixture_id in ["clean_fixture", "messier_fixture"]:
            sensitivity = build_fixture_sensitivity(fixture_id, fixtures[fixture_id], contract)
            self.assertEqual(sensitivity.selected_ids_by_lambda["0"], sensitivity.baseline_selected_ids)
            self.assertNotEqual(sensitivity.selected_ids_by_lambda["0.5"], sensitivity.baseline_selected_ids)
            self.assertNotEqual(sensitivity.selected_ids_by_lambda["1"], sensitivity.baseline_selected_ids)


if __name__ == "__main__":
    unittest.main()
