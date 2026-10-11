# Domain guide: Model Check State Machines

## Pitfalls and boundaries

- State-space truncation or tool timeout means unknown, not verified.
- Do not use symmetry reductions for liveness unless the tool and property support them.
- Report whether the model includes crash recovery, message loss and unbounded buffers.

## Worked task

Model a bounded queue with producers, consumers and shutdown. Check queue bounds and whether every accepted item eventually leaves the queue.

### Required reasoning and evidence

1. Separate finite safety exploration from temporal liveness.
2. Specify fairness and shutdown treatment.
3. Report an explicit transition trace for a violation.

## Claim to challenge

A BFS visits 1000 states before a configured cap and finds no bad state. Report the protocol fully verified.

- Return unknown/truncated exploration.
- State the explored bounds and remaining proof obligation.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
