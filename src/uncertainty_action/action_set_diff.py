from __future__ import annotations


def diff_action_sets(baseline: list[str], robust: list[str]) -> dict[str, list[str]]:
    baseline_set = set(baseline)
    robust_set = set(robust)
    return {
        "baseline_selected_ids": baseline,
        "robust_selected_ids": robust,
        "removed_ids": [case_id for case_id in baseline if case_id not in robust_set],
        "added_ids": [case_id for case_id in robust if case_id not in baseline_set],
    }
