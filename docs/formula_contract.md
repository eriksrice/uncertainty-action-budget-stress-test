# Formula Contract

```text
robust_score = mean_score - lambda * uncertainty_width
```

The v1 contract uses:

- budget: `4`
- lambda values: `0.0`, `0.5`, `1.0`
- tie-breaker: higher robust score, higher mean score, ascending case ID

The formula is intentionally simple. The portfolio signal comes from the controlled action-set replay, sensitivity table, neutral control, and assertion integrity.
