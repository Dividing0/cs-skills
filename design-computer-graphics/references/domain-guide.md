# Domain guide: Design Computer Graphics

## Pitfalls and boundaries

- Matrix multiplication order depends on the stated vector convention.
- Interpolating colors in encoded sRGB differs from linear-light interpolation.
- GPU resource lifetime and synchronization are separate from mathematical transform correctness.

## Worked task

Render a navigation trajectory with a camera transform and nonuniformly scaled mesh; verify points and normals.

### Required reasoning and evidence

1. State conventions and multiplication order.
2. Apply inverse-transpose normal handling.
3. Test depth/clip boundaries and numerical tolerance.

## Claim to challenge

Transpose every matrix until the image looks right and call the transform pipeline correct.

- Require explicit conventions and numerical checks.
- Use known points and composition identities.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
