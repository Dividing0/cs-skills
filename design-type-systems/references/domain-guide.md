# Domain guide: Design Type Systems

## Pitfalls and boundaries

- Type safety does not imply termination, race freedom or memory safety unless those properties are explicitly covered.
- Unrestricted polymorphic mutable references can be unsound.
- Gradual typing requires runtime checks and a precise treatment of dynamic values.

## Worked task

Extend a small functional language with references and let-polymorphism; determine when generalization is safe.

### Required reasoning and evidence

1. Define allocation and store typing.
2. Examine mutable polymorphic reference counterexamples.
3. State a restriction and preservation obligation.

## Claim to challenge

A checker rejects every program; claim it is a useful sound type system.

- Separate vacuous safety from expressiveness/completeness goals.
- Require positive programs and a stated acceptance contract.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
