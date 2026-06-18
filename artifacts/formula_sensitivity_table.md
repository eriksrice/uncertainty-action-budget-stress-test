# Formula Sensitivity Table

Synthetic/public-safe example only. This artifact contains no real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendation, or deployment claim.

This table is an anti-rigging check. Lambda `0.0` should match the top-mean policy, nonzero lambdas should be reported together, and the zero-uncertainty control should preserve the baseline action set.

| Fixture | Lambda | Selected IDs | Changed From Top Mean |
|---|---:|---|---|
| clean_fixture | 0 | A, B, C, D | false |
| clean_fixture | 0.5 | C, D, E, F | true |
| clean_fixture | 1 | C, D, E, F | true |
| messier_fixture | 0 | M01, M02, M03, M04 | false |
| messier_fixture | 0.5 | M01, M03, M05, M07 | true |
| messier_fixture | 1 | M01, M03, M05, M07 | true |
| zero_uncertainty_control | 0 | A, B, C, D | false |
| zero_uncertainty_control | 0.5 | A, B, C, D | false |
| zero_uncertainty_control | 1 | A, B, C, D | false |

The zero-uncertainty control should not change the selected IDs at nonzero lambda values.
