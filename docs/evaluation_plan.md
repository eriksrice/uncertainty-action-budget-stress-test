# Evaluation Plan

The demo must pass these checks:

- clean fixture top-mean selection is `A, B, C, D`
- clean fixture robust selection is `C, D, E, F` at lambda `0.5` and `1.0`
- messier fixture top-mean selection is `M01, M02, M03, M04`
- messier fixture robust selection is `M01, M03, M05, M07` at lambda `0.5` and `1.0`
- zero-uncertainty control preserves top-mean selection at nonzero lambda values
- expected and computed selected IDs are separated
- copied expected selections fail the self-comparison guard
- missing expected values fail closed
