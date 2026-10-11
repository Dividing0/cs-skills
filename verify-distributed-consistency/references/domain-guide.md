# Domain guide: Verify Distributed Consistency

## Pitfalls and boundaries

- Acyclic dependency graphs prove only the property captured by the graph and conflict definitions.
- Wall-clock skew can invalidate cross-node real-time ordering; preserve client-monotonic evidence.
- A single-register checker cannot validate multi-key transaction isolation.

## Worked task

A completed write of 1 precedes a read returning 0 on a register initially 0. Assess a linearizability claim.

### Required reasoning and evidence

1. Reject the complete history under the register contract.
2. Use invocation/completion precedence.
3. Contrast a read overlapping the write.

## Claim to challenge

All reads overlap writes, but a completion-time sort rejects the history. Conclude a violation.

- Search other legal linearizations.
- Avoid treating completion-time ordering as mandatory for overlapping operations.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
