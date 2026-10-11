# Domain guide: Analyze Programs Statically

## Pitfalls and boundaries

- Missing exceptional/control-flow edges can make a purported conservative analysis unsound.
- Widening improves convergence by sacrificing precision, not by proving absence of errors automatically.
- Taint sanitizers must be context-specific and validated against the sink semantics.

## Worked task

Design an interval analysis for loops and integer division, including possible division by zero and unknown function calls.

### Required reasoning and evidence

1. Define lattice and transfer semantics.
2. Specify widening and overflow model.
3. Handle unknown calls conservatively.

## Claim to challenge

Ignore reflection and FFI, find no warnings and call the entire application safe.

- Expose unsupported regions.
- Limit guarantees to analyzed semantics.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
