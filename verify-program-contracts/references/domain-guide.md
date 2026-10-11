# Domain guide: Verify Program Contracts

## Pitfalls and boundaries

- A false precondition makes a contract vacuously valid.
- Mathematical integer proofs do not establish machine-integer overflow safety.
- Partial correctness allows divergence; total correctness needs a termination argument.

## Worked task

Verify binary search returns a matching index or insertion position for a sorted integer array.

### Required reasoning and evidence

1. Specify sortedness, index range and duplicate behavior.
2. Prove bounds and decreasing search interval.
3. Handle arithmetic overflow in midpoint calculations.

## Claim to challenge

The solver timed out, but random tests passed. Mark the contract proved.

- Report the verifier outcome as unknown.
- Keep test evidence separate from proof.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
