# Domain guide: Evaluate Machine Learning Systems

## Pitfalls and boundaries

- Fit preprocessing on training data only and keep final evaluation out of hyperparameter selection.
- Bootstrapping correlated frames independently can severely understate uncertainty.
- WER, F1 and accuracy do not replace deployment-specific failure analysis.

## Worked task

Compare two Ukrainian ASR models on recordings from speakers also present in training; redesign the evaluation.

### Required reasoning and evidence

1. Identify speaker and near-duplicate leakage.
2. Define independent held-out evaluation.
3. Report paired quality and inference conditions.

## Claim to challenge

Bootstrap 10000 frames from ten recordings as independent samples and claim a narrow confidence interval.

- Choose the independent resampling unit.
- Explain dependence and sample-size limits.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
