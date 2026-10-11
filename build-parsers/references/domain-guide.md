# Domain guide: Build Parsers

## Pitfalls and boundaries

- A successful prefix parse is not acceptance of the full document.
- PEG ordered choice differs from CFG ambiguity semantics.
- Round-trip tests need normalization rules for comments and formatting.

## Worked task

Build a Pratt parser for arithmetic with unary minus, right-associative exponentiation and source-span errors.

### Required reasoning and evidence

1. Specify precedence with examples such as unary versus exponentiation.
2. Reject trailing tokens.
3. Test truncated and deeply nested input.

## Claim to challenge

The parser accepts 1+2garbage because it parsed a valid prefix. Treat the document as valid.

- Require full-input consumption.
- Emit a location-aware trailing-token error.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
