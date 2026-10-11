# Domain guide: Analyze Memory Models

## Pitfalls and boundaries

- A release store and acquire load synchronize only through the relevant observed value/release sequence under the selected model.
- Sequential consistency does not repair a use-after-free or incorrect algorithm.
- Separate compiler barriers, CPU barriers and device/DMA ordering.

## Worked task

A producer writes data then stores ready with Release; a consumer loads ready with Acquire and reads data only if true. Analyze assumptions and allowed outcomes.

### Required reasoning and evidence

1. State initialization, writer count and lifetime assumptions.
2. Explain the conditional synchronizes-with edge.
3. Distinguish publication from subsequent unsynchronized mutation.

## Claim to challenge

Use SeqCst on an atomic pointer, free the old pointee immediately, and claim all readers are safe.

- Identify reclamation as a separate lifetime obligation.
- Provide a reader/free schedule and suitable reclamation options.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
