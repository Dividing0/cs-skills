# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/work_span.py assets/example-input.json --processors 2
```

Input is a list of unique string task IDs, finite nonnegative cost and optional deps. Dependencies must exist and the graph must be acyclic. Work=sum(cost); span=longest weighted path. Output bounds apply to ideal processors with no communication/dispatch overhead. --processors must be positive. A cost-zero DAG has null average_parallelism; do not interpret that as infinite measured scalability.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
