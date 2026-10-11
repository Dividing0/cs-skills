# Domain guide: Design Streaming Algorithms

## Pitfalls and boundaries

- Insertion-only sketch guarantees need not survive arbitrary deletions.
- An empirical confidence interval is not the algorithm's worst-case probability bound.
- Reservoir sampling needs correct inclusion probabilities across the entire prefix.

## Worked task

Estimate URL frequencies using 2 MiB of memory with an insertion-only Count-Min sketch and compare to exact prefix counts.

### Required reasoning and evidence

1. State epsilon/delta and hash assumptions.
2. Check overestimation and merge parameters.
3. Handle counter overflow and empty streams.

## Claim to challenge

Subtract arbitrary deletes from an insertion-only sketch and retain its original overestimation guarantee.

- Identify the changed stream model.
- Require a valid turnstile guarantee or reject the claimed bound.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
