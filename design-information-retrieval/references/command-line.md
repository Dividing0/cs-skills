# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/ranking_metrics.py assets/example-input.json --k 2
```

qrels maps query IDs to document grades in [0,30]; rankings maps query IDs to ordered unique document IDs. Grades>0 are binary relevant. nDCG uses 2^grade-1; unjudged=0. Precision denominator is k even if fewer results exist. Queries without relevant judgments get recall/nDCG0, included in macro mean. Missing ranking is empty; ranking queries without qrels are rejected. Report judged_fraction before interpreting incomplete judgments.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
