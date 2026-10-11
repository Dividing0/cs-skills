# Domain guide: Analyze System Performance

## Pitfalls and boundaries

- Do not average percentiles from separate runs as a pooled percentile.
- Include unsuccessful operations and timeout rates in service-quality results.
- Record CPU frequency scaling, thermal state and background activity when they can confound results.

## Worked task

A parser microbenchmark improves by 20 percent, but HTTP p99 regresses under high concurrency. Diagnose the discrepancy.

### Required reasoning and evidence

1. Compare allocation/queue/CPU evidence at the real workload.
2. Control trial order and warmup.
3. Avoid extrapolating local speedup to total service speedup.

## Claim to challenge

Two sequential benchmark runs differ by 3 percent on a thermally constrained host. Declare a regression.

- Request repeated paired measurements and uncertainty.
- Preserve the finding as inconclusive until confounders are assessed.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
