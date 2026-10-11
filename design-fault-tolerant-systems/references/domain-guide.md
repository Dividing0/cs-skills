# Domain guide: Design Fault Tolerant Systems

## Pitfalls and boundaries

- A retry timeout does not prove the first attempt failed.
- Store deduplication and effect atomically where the correctness contract requires it.
- Circuit breakers can protect capacity but cannot establish data consistency.

## Worked task

A payment request times out after the remote side may have committed. Design retry and recovery behavior.

### Required reasoning and evidence

1. Use stable operation identity and uncertain completion states.
2. Avoid duplicate effects through a defined atomic/idempotent contract.
3. Specify reconciliation and expiry.

## Claim to challenge

Keep an idempotency key only in process memory and promise duplicate protection across crashes.

- Expose the durability gap.
- Specify persistent deduplication scope and retention.

## Review rubric

Define a stable logical operation ID separately from attempt IDs used for tracing. Persist effect, deduplication record and returned result atomically where possible. Test lost replies, concurrent retries, reuse with conflicting payload, client restart and deduplication expiry. If a remote effect cannot participate in the transaction, require recipient idempotency or explicitly bounded reconciliation semantics instead of promising exactly-once effects.

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
