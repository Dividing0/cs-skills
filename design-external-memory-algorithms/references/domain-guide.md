# Domain guide: Design External Memory Algorithms

## Pitfalls and boundaries

- RAM budgets must include runtime object overhead and compression buffers.
- Partition skew can force recursive spill or defeat an assumed memory bound.
- Do not claim an optimal I/O bound without the required model assumptions.

## Worked task

Sort 500 GB of variable-length JSONL records with 4 GB RAM and at most 128 open files.

### Required reasoning and evidence

1. Budget run formation and merge fan-in.
2. Bound temporary disk usage and descriptors.
3. Check malformed records and failure cleanup.

## Claim to challenge

Read records lazily, convert the iterator to a list, and claim the sort uses bounded memory.

- Locate materialization and object-size costs.
- Replace with bounded runs and multi-pass merge.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
