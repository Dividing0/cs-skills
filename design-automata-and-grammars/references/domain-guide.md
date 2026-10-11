# Domain guide: Design Automata And Grammars

## Pitfalls and boundaries

- Tokenization choices can change the language being recognized.
- Exponential subset growth requires explicit state/resource bounds.
- Determinism of a parser does not prove the source grammar unambiguous.

## Worked task

Construct a DFA over a,b for words with an even number of a characters and ending in b; compare it to a proposed four-state machine.

### Required reasoning and evidence

1. Define state meanings and empty-word outcome.
2. Check a shortest distinguishing word if unequal.
3. Make all transitions explicit.

## Claim to challenge

Enumerate words up to length 8 and claim two arbitrary context-free grammars are equivalent.

- Label bounded evidence only.
- Explain the limits of grammar equivalence testing.

## Review rubric

Require the declared model and assumptions to match the claim. Check boundary cases and alternative explanations. Require reproducible evidence for empirical results and an actual proof obligation for universal claims. A counterexample refutes the property it violates; absence of a counterexample in a bounded search does not establish an unbounded guarantee. If a selected tool cannot express the required model, change the method or state the unresolved obligation.
