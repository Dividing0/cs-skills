# Domain guide: Design Embedded Systems

## Pitfalls and boundaries

- Volatile access does not provide general atomicity or synchronization.
- An ISR must not block on a task-owned resource without a valid design.
- Average power is insufficient when peak current causes brownouts.

## Worked task

Design an ESP32-style streaming audio buffer with DMA producer and task consumer under tight RAM limits.

### Required reasoning and evidence

1. Specify buffer ownership and overflow policy.
2. Budget DMA/stack memory and timing.
3. Require target validation for cache/peripheral behavior.

## Claim to challenge

Host unit tests pass, so claim firmware timing and peripheral behavior are verified.

- State host-test limits.
- Define target or hardware-in-the-loop checks.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
