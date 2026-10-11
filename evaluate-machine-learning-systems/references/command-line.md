# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/grouped_bootstrap.py assets/example-input.json --trials 2000 --seed 0
```

Unique string id per independent group; nonnegative integer error counts and positive integer units. A/B must cover identical units. Resample paired groups and compute the pooled error-rate difference B-A; negative favors B for error metrics. errors may exceed units (e.g. WER insertions). Output is an empirical percentile95 interval; few groups, selection bias and dependent groups limit reliability. Do not reinterpret this as frame-independent bootstrap, a formal significance test or population guarantee.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
