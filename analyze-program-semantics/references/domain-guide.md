# Domain guide: Analyze Program Semantics

## Pitfalls and boundaries

- Big-step rules without divergence machinery may not distinguish divergence from absent derivations.
- Integer overflow and floating-point semantics can invalidate algebraic rewrites.
- Substitution must avoid variable capture in nested binders.

## Worked task

Assess whether replacing f()+g() with g()+f() preserves behavior when both functions mutate shared state.

### Required reasoning and evidence

1. Specify sequencing and observable state.
2. Give a counterexample or sufficient effect assumptions.
3. Avoid pure algebraic reasoning for effects.

## Claim to challenge

Both programs return 3 on ten inputs. Prove contextual equivalence.

- Reject a universal conclusion from samples.
- Define observables and either prove refinement or present bounded results.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
