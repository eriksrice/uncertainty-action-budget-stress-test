# Uncertainty-Robust Policy

Synthetic/public-safe example only. This artifact contains no real WTCHP data, real people, operational thresholds, clinical guidance, staffing guidance, policy recommendation, or deployment claim.

Formula: `robust_score = mean_score - lambda * uncertainty_width`

Lambda values: `0, 0.5, 1`

## clean_fixture

- Lambda `0` selected IDs: `A, B, C, D`
- Lambda `0.5` selected IDs: `C, D, E, F`
- Lambda `1` selected IDs: `C, D, E, F`

| Case | Mean | Uncertainty | Lambda 0 | Lambda 0.5 | Lambda 1 |
|---|---:|---:|---:|---:|---:|
| A | 0.930 | 0.300 | 0.930 | 0.780 | 0.630 |
| B | 0.900 | 0.250 | 0.900 | 0.775 | 0.650 |
| C | 0.870 | 0.050 | 0.870 | 0.845 | 0.820 |
| D | 0.850 | 0.040 | 0.850 | 0.830 | 0.810 |
| E | 0.830 | 0.020 | 0.830 | 0.820 | 0.810 |
| F | 0.810 | 0.010 | 0.810 | 0.805 | 0.800 |
| G | 0.800 | 0.000 | 0.800 | 0.800 | 0.800 |
| H | 0.780 | 0.000 | 0.780 | 0.780 | 0.780 |
| I | 0.760 | 0.000 | 0.760 | 0.760 | 0.760 |
| J | 0.740 | 0.000 | 0.740 | 0.740 | 0.740 |

## messier_fixture

- Lambda `0` selected IDs: `M01, M02, M03, M04`
- Lambda `0.5` selected IDs: `M01, M03, M05, M07`
- Lambda `1` selected IDs: `M01, M03, M05, M07`

| Case | Mean | Uncertainty | Lambda 0 | Lambda 0.5 | Lambda 1 |
|---|---:|---:|---:|---:|---:|
| M01 | 0.910 | 0.070 | 0.910 | 0.875 | 0.840 |
| M02 | 0.900 | 0.240 | 0.900 | 0.780 | 0.660 |
| M03 | 0.890 | 0.050 | 0.890 | 0.865 | 0.840 |
| M04 | 0.880 | 0.180 | 0.880 | 0.790 | 0.700 |
| M05 | 0.860 | 0.030 | 0.860 | 0.845 | 0.830 |
| M06 | 0.850 | 0.140 | 0.850 | 0.780 | 0.710 |
| M07 | 0.840 | 0.020 | 0.840 | 0.830 | 0.820 |
| M08 | 0.830 | 0.010 | 0.830 | 0.825 | 0.820 |
| M09 | 0.820 | 0.000 | 0.820 | 0.820 | 0.820 |
| M10 | 0.810 | 0.000 | 0.810 | 0.810 | 0.810 |
