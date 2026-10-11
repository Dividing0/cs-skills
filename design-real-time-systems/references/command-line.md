# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/implicit_deadlines.py assets/example-input.json
```

Task counts/times must use consistent units; execution>=0, period>0. Optional deadline must equal period; nonzero blocking/jitter is rejected. EDF U<=1 is evaluated only for the stated classic single-core preemptive independent implicit-deadline model. The rate-monotonic Liu-Layland bound is sufficient only; exceeding it yields undecided, not infeasible. Execution inputs must be justified bounds, not averages. No OS timing or overhead validation is performed.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
