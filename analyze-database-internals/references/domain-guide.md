# Domain guide: Analyze Database Internals

## Pitfalls and boundaries

- EXPLAIN ANALYZE executes the statement; use safe isolated data for mutating statements.
- Do not transfer isolation details or index capabilities between engines without checking their documentation.
- A larger connection pool can worsen contention instead of increasing throughput.

## Worked task

An hourly query scans recent calls while long transactions prevent cleanup. Investigate high CPU and rising storage.

### Required reasoning and evidence

1. Examine actual plans and snapshot/transaction age.
2. Evaluate indexing and cleanup independently.
3. Measure write overhead and concurrent behavior.

## Claim to challenge

PostgreSQL Read Committed means every statement in a transaction sees the same snapshot.

- Correct the isolation premise using version-specific documentation.
- Demonstrate statement-level snapshot changes.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
