import unittest

from uncertainty_action.action_set_diff import diff_action_sets


class ActionSetDiffTests(unittest.TestCase):
    def test_clean_fixture_diff_removes_a_b_adds_e_f(self):
        diff = diff_action_sets(["A", "B", "C", "D"], ["C", "D", "E", "F"])
        self.assertEqual(diff["removed_ids"], ["A", "B"])
        self.assertEqual(diff["added_ids"], ["E", "F"])

    def test_messier_fixture_diff_removes_m02_m04_adds_m05_m07(self):
        diff = diff_action_sets(["M01", "M02", "M03", "M04"], ["M01", "M03", "M05", "M07"])
        self.assertEqual(diff["removed_ids"], ["M02", "M04"])
        self.assertEqual(diff["added_ids"], ["M05", "M07"])


if __name__ == "__main__":
    unittest.main()
