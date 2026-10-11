# Domain guide: Design Stream Processing

## Pitfalls and boundaries

- A watermark is a progress policy under source assumptions, not a guarantee that future older events cannot arrive.
- Exactly-once operator state does not automatically make external effects exactly once.
- Define half-open versus closed window boundaries explicitly.

## Worked task

Count sensor readings in five-second event-time windows; events arrive out of order, one partition idles and a sink write succeeds before checkpoint completion.

### Required reasoning and evidence

1. Specify boundaries, idleness and late-event handling.
2. Account for replay duplicate effects.
3. Use offline expected counts.

## Claim to challenge

Enable framework checkpoints and advertise exactly-once HTTP notifications.

- Identify the external side-effect gap.
- Require idempotency or a transactional output protocol.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
