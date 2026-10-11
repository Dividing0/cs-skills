# Domain guide: Design Data Structures

## Pitfalls and boundaries

- Expected hash-table bounds require hashing/load assumptions.
- Amortized O(1) does not bound individual-operation latency.
- Lock-free progress is not a memory-reclamation mechanism.

## Worked task

Design a deadline queue supporting insertion, cancellation and next-deadline retrieval for an event loop.

### Required reasoning and evidence

1. Specify cancellation ownership and handle identity.
2. Compare heap tombstones with indexed removal.
3. Test operation sequences and cleanup costs.

## Claim to challenge

Dynamic-array append is amortized constant time, so every append meets a fixed microsecond deadline.

- Distinguish amortized cost from worst-case latency.
- Account for resizing, allocation and allocator behavior.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
