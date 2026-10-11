# Domain guide: Design Backpressure

## Pitfalls and boundaries

- Use Little's law only for a stable, consistently defined system; burst sizing requires distributional evidence.
- An item-count limit does not bound memory when item sizes vary.
- Unbounded retry buffers can invalidate an otherwise bounded design.

## Worked task

A crawler accepts 1000 URLs/s but persists 600/s. Design behavior for a ten-minute overload and a stalled database.

### Required reasoning and evidence

1. Calculate unbounded backlog growth before choosing capacity.
2. Specify byte limits and a loss/admission contract.
3. Verify shutdown and permit release.

## Claim to challenge

Add a queue capacity of 1000 and claim the complete pipeline now has bounded memory.

- Inspect hidden/in-flight buffers and payload sizes.
- Explain what resource bound is actually established.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
