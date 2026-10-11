# Domain guide: Design Human Computer Interaction

## Pitfalls and boundaries

- Automated accessibility checks cannot certify complete accessibility conformance.
- Visual attractiveness is not evidence of task success.
- Responsive scaling must preserve readability and interaction, not only fit pixels.

## Worked task

Improve navigation and log viewing in an Android app across small phones, tablets and large font settings.

### Required reasoning and evidence

1. Cover state/layout/focus transitions.
2. Check accessibility and scrolling behavior.
3. Define observable task-based acceptance checks.

## Claim to challenge

A screenshot looks good, so declare the app accessible and usable.

- Separate visual inspection from interaction validation.
- Specify keyboard/assistive and task-based checks.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
