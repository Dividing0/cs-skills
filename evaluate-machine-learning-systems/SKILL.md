---
name: evaluate-machine-learning-systems
description: "Evaluate ML systems with reproducible quality and deployment evidence. Use for baseline design, leakage, grouped/temporal splits, distribution shifts, confidence intervals, inference cost and production-quality tradeoffs."
---

# Evaluate Machine Learning Systems

## Scope and routing

Assess whole-system empirical claims. Use statistical-learning theory for generalization theorems and framework skills for training/inference implementation.

Use the user's chosen language, framework and target platform. Reuse existing specifications and evidence before asking for missing information. If a missing assumption changes the conclusion, state the alternatives and continue work that is independent of it.

## Workflow

1. Define task, target population, label policy, decision threshold, failure costs and production latency/memory/compute budgets.
2. Split by independent units such as speaker, patient, document family or time; identify preprocessing, tuning and near-duplicate leakage paths.
3. Choose simple strong baselines and task-appropriate metrics; preserve class/subgroup distributions and label uncertainty.
4. Compare models on the same held-out units with paired statistics or grouped bootstrap as appropriate; document sample size and dependence.
5. Measure preprocessing, model and postprocessing together on stated hardware, precision, batch sizes, sequence lengths and concurrency.
6. Report quality/cost tradeoffs, calibration, failure slices and distribution-shift evidence; do not generalize beyond evaluated languages, conditions or populations.

## Executable helper

Read [command-line contract](references/command-line.md) before running `scripts/grouped_bootstrap.py`. Use its example fixture for an initial check, then supply task-specific input. The helper's declared scope and bounds constrain any conclusion.

## Evidence and completion

- Inspect actual code, configuration, schemas or traces before diagnosing a concrete system; give artifact/function references for findings.
- Read [domain guide](references/domain-guide.md) for domain pitfalls and a worked task; consult it before making a guarantee.
- Read [primary sources](references/sources.md) for authoritative starting points. Check current version-specific documentation when APIs, standards or tool behavior matter. Never fabricate tool availability, source citations or measurements.
- Run the relevant available checks after changes and preserve the command, versions, input, outcome and reproducibility conditions. If execution is unavailable, say which validation remains unperformed and give the runnable check.
- Distinguish a mathematical proof, tool proof under assumptions, finite/bounded exploration, passing tests, simulation and measured observations. Report timeouts, unsupported models and incomplete data as unknown, not success.
- Complete the requested artifact or fix within the authorized scope; use the smallest change supported by evidence. Validate the user's acceptance criteria as well as the model's internal properties.

## Deliverable

Use [report template](assets/report-template.md) as a checklist, adapting length to the task. Lead with the result, then give assumptions, the concrete model/design/change, evidence, limitations and remaining checks. Include a minimal counterexample for a refuted claim. For a design, include implementation-ready contracts and acceptance criteria.

## Related skills

`analyze-data-with-statsmodels`, `research-statistical-learning-theory`, `compute-with-monte-carlo`. Invoke only the subset required for the actual task; these are optional capabilities, not mandatory installation dependencies.

For maintenance, use [evaluation cases](assets/evaluation-cases.json) as task prompts and scoring criteria. They are evaluation fixtures, not evidence that this skill has been validated on production systems.
