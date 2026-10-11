# Domain guide: Design Storage Engines

## Pitfalls and boundaries

- Process crash, OS crash and power loss are different failure models.
- An fsync guarantee depends on the stack and configured hardware behavior.
- Compaction and deletion need snapshot/reader lifetime accounting.

## Worked task

Design a log-backed key-value store and define whether an acknowledged write survives a crash between data append and manifest update.

### Required reasoning and evidence

1. State acknowledgement and flush ordering.
2. Enumerate crash windows.
3. Verify recovery with a reference map.

## Claim to challenge

Atomically rename a manifest and assume both manifest and newly created data files are durable.

- Check file/directory flush requirements.
- Avoid equating atomic visibility with crash durability.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
