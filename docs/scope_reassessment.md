# Scope Reassessment

Status: stop and reassess after CI, reviewer positioning, README expected output, and artifact polish.

## Decision

Do not expand v1 scope.

The project already has the proof path it needs:

- deterministic demo command;
- synthetic fixtures;
- top-mean baseline policy;
- uncertainty-robust policy;
- action-set diff;
- lambda sensitivity table;
- zero-uncertainty control;
- assertion-integrity checks;
- generated reviewer artifacts;
- CI proof path.

## Why Stop Here

The next likely additions would weaken the project if added too early:

- dashboard UI would distract from the proof artifact;
- model training would shift attention away from action-policy evaluation;
- LLM or agent layers would look decorative;
- real WTCHP framing would create public-safety and overclaim risk;
- broader optimization language would make the project less precise.

## Next Valid Moves

- Let CI run on GitHub.
- Confirm README renders cleanly.
- Use the repo as a portfolio artifact.
- Only add new scope if a reviewer identifies a concrete missing proof.

## Current Boundary

```yaml
add_dashboard: false
add_model_training: false
add_llm_or_agent_layer: false
add_real_wtchp_data: false
add_operational_recommendations: false
current_state: v1_scope_complete_pending_external_review
```
