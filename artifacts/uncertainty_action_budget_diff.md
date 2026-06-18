# Uncertainty Action Budget Diff

Synthetic/public-safe example only. This artifact contains no real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendation, or deployment claim.

The baseline action set is selected by top mean score. The robust action set uses lambda `0.5`.

## clean_fixture

Baseline selected IDs: `A, B, C, D`
Robust selected IDs: `C, D, E, F`
Removed IDs: `A, B`
Added IDs: `E, F`

Plain-English explanation: cases leave the fixed budget when their uncertainty width lowers their robust score enough for lower-uncertainty cases to enter.

## messier_fixture

Baseline selected IDs: `M01, M02, M03, M04`
Robust selected IDs: `M01, M03, M05, M07`
Removed IDs: `M02, M04`
Added IDs: `M05, M07`

Plain-English explanation: cases leave the fixed budget when their uncertainty width lowers their robust score enough for lower-uncertainty cases to enter.
