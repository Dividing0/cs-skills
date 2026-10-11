# Domain guide: Design Robotics Software

## Pitfalls and boundaries

- A numerically valid matrix may encode the wrong transform direction.
- Low residuals do not prove absolute-position accuracy without a reference and observability.
- Covariance comparisons require consistent frame/unit transformations.

## Worked task

Integrate IMU and GPS data where GPS time is measurement time and IMU time comes from a different clock; design alignment and replay.

### Required reasoning and evidence

1. Define clock mapping and transform conventions.
2. Handle delayed/reordered measurements.
3. Separate simulated and device trajectory evidence.

## Claim to challenge

Mix ENU positions and NED velocities because both have three coordinates.

- Identify the frame/unit mismatch.
- Specify and test explicit transforms including covariance handling.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
