# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/check_safety.py assets/example-input.json
```

All states are unique strings. Initial must be nonempty. Every transition endpoint and forbidden state must be declared. Exit 0: property holds in the supplied reachable finite graph; 1: forbidden state reached with trace; 2: exploration capped; invalid input uses argparse exit 2. Terminal states are listed, not automatically classified as deadlocks. No fairness or liveness is checked. Set --limit explicitly for large graphs.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
