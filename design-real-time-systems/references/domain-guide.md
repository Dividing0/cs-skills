# Domain guide: Design Real Time Systems

## Pitfalls and boundaries

- Utilization below one is sufficient for classic single-core EDF only under its stated task assumptions; it is not universal.
- Average execution time cannot replace a justified execution bound.
- Desktop OS latency samples do not establish a hard real-time guarantee.

## Worked task

Assess preemptive single-core periodic tasks with implicit deadlines and execution/period pairs (2,5), (3,10), (1,20) in milliseconds.

### Required reasoning and evidence

1. State the independent-task/no-blocking assumptions.
2. Calculate utilization and choose an applicable test.
3. Account for overhead before deployment guarantees.

## Claim to challenge

Observed maximum latency is 4 ms in a ten-minute run, so guarantee a 5 ms deadline.

- Report empirical maximum with workload conditions.
- Require an appropriate worst-case timing argument.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
