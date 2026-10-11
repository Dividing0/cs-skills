# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/compare_dfa.py assets/example-input.json
```

Input has left/right DFAs with states, alphabet (string tokens), start, accept and transitions (state -> token -> state). Alphabets must match. Missing transitions enter an implicit rejecting sink. word is a token list; [] denotes epsilon. --limit caps product states. Exit0 equivalent, exit1 different with shortest distinguishing word, exit2 unknown or invalid. Only finite deterministic automata are accepted; do not pass NFA or grammar objects.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
