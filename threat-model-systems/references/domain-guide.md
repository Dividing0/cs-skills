# Domain guide: Threat Model Systems

## Pitfalls and boundaries

- Authentication does not imply authorization or tenant isolation.
- Encrypted transport does not prevent application business-logic attacks.
- The absence of identified threats is not a security certification.

## Worked task

Threat-model a legal assistant that accepts uploaded documents, searches tenant data and calls external tools.

### Required reasoning and evidence

1. Trace upload/storage/retrieval/tool boundaries.
2. Assess tenant isolation and malicious document influence.
3. Prioritize testable mitigations.

## Claim to challenge

TLS is enabled, so the application is secure.

- Reject the unsupported conclusion.
- Examine authorization, data handling and business invariants.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
