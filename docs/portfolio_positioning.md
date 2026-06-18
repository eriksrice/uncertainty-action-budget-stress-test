# Portfolio Positioning

This project is a compact Applied AI decision-support proof, not a dashboard or modeling showcase.

## One-Line Positioning

I built a deterministic stress test showing that a fixed action budget selected by top mean model scores can change when prediction uncertainty is treated as decision risk.

## Senior Signal

- Translates model output into an action-policy question.
- Separates score ranking from decision readiness.
- Uses lambda sensitivity and a zero-uncertainty control to reduce formula-rigging risk.
- Includes a messier fixture where the robust policy does not simply drop every high-mean case.
- Preserves expected/computed separation and a self-comparison guard.
- Produces reviewer-readable artifacts from one deterministic command.

## Interview Talk Track

The project starts with a common failure mode: a team has a model score and a fixed action budget, so the obvious move is to take the top scores. I built a synthetic stress test where that top-score action set changes once uncertainty width is treated as decision risk. The point is not that my formula is universal. The point is that action policies need reproducible controls before model scores become work queues.

## Best-Fit Roles

- Senior Applied AI Scientist
- AI Analytics Engineer
- AI Evaluation and Reliability Engineer
- Decision-support analytics lead
- Analytics engineering lead working near model outputs

## What To Emphasize

- The action-set diff is the center artifact.
- The project is deterministic and reproducible.
- The controls are there to make the formula harder to rig.
- The scope is intentionally narrow: fixed budget, synthetic fixtures, no real operational claims.

## What Not To Emphasize

- Do not pitch this as a real WTCHP action tool.
- Do not pitch it as model training.
- Do not pitch it as an optimizer.
- Do not pitch it as a dashboard.
- Do not imply clinical, staffing, policy, or deployment validity.
