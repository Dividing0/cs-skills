# Domain guide: Build Compilers And Interpreters

## Pitfalls and boundaries

- LLVM poison/undef semantics must not be replaced by source-language assumptions.
- Reassociation can change floating-point and exceptional behavior.
- Interpreter agreement on samples is strong testing evidence but not a universal preservation proof.

## Worked task

Add constant folding and dead-code elimination to a small interpreter/compiler with side-effecting calls and checked integer overflow.

### Required reasoning and evidence

1. Preserve effects and checked-overflow semantics.
2. Specify pass invariants.
3. Use reference and unoptimized differential execution.

## Claim to challenge

Replace x/x with 1 for every integer and floating-point expression.

- Check zero, NaN, infinity and source arithmetic semantics.
- State valid restricted rewrite conditions.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
