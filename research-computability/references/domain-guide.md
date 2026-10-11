# Domain guide: Research Computability

## Pitfalls and boundaries

- An unsuccessful search is not a nonexistence proof.
- Bounded-state termination can be decidable even when arbitrary-program termination is undecidable.
- Undecidability does not imply every concrete instance is difficult or unresolvable.

## Worked task

Can an analyzer decide whether any arbitrary Python program terminates? Contrast a finite transition system with bounded memory.

### Required reasoning and evidence

1. Define model and input encoding.
2. Give a valid halting reduction.
3. Explain why finite-state reachability differs.

## Claim to challenge

A parser always finishes on tested inputs, so membership in any grammar is decidable by that implementation.

- Reject sample-based decidability claims.
- Require a terminating procedure over all legal inputs and a sound/correct recognition argument.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
