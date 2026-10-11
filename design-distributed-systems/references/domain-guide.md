# Domain guide: Design Distributed Systems

## Pitfalls and boundaries

- Replication factor is not a backup or a complete durability guarantee.
- Quorum intersection requires the actual read/write/configuration protocol.
- Independent service availability assumptions fail when dependencies are correlated.

## Worked task

Design a partitioned crawler frontier with multiple workers, leases and deduplication across regions.

### Required reasoning and evidence

1. Specify ownership, lease expiry and stale-worker effects.
2. Define partition/retry behavior.
3. Separate approximate deduplication from strict uniqueness.

## Claim to challenge

Use three replicas and claim no data can ever be lost.

- State failure/durability model.
- Inspect acknowledgement, correlated failures and backups.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
