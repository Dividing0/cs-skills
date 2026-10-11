# Domain guide: Test Distributed Systems

## Pitfalls and boundaries

- Use isolated local/test deployments by default; no production fault injection without explicit scope authorization.
- Lost client replies require uncertain-completion modeling.
- An oracle that sorts by completion time can invent false linearizability violations.

## Worked task

Test a three-node key-value service through leader crash, partition and recovery while recording reads and writes.

### Required reasoning and evidence

1. Define the register/transaction oracle.
2. Keep pending operations and fault timeline.
3. Replay and minimize a violation.

## Claim to challenge

Kill a production node to obtain more realistic evidence without explicit authorization.

- Stay within authorized isolated test scope.
- Provide a reproducible safe fault plan.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
