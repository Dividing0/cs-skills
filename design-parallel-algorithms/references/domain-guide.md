# Domain guide: Design Parallel Algorithms

## Pitfalls and boundaries

- Acyclic task graphs can still have costly scheduling overhead.
- Floating-point addition is not associative; reduction order can change output.
- More workers can reduce throughput when memory bandwidth is saturated.

## Worked task

Parallelize feature extraction across recordings of uneven duration and then reduce statistics.

### Required reasoning and evidence

1. Model load imbalance and critical path.
2. Specify reduction precision/determinism.
3. Measure throughput and memory by worker count.

## Claim to challenge

Run four threads on a task with a large serial phase and assume a fourfold speedup.

- Apply serial/work/span limits.
- Measure scheduling and bandwidth constraints.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
