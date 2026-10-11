# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/count_min.py assets/example-input.json --width 16 --depth 4
```

Insertion-only string keys; width/depth positive. --seed selects deterministic SHA-256 row salts. Sketch.add supports nonnegative integer counts; Sketch.merge requires matching width/depth/seed. The CLI retains exact counts to assess a bounded fixture, so it is not itself a bounded-memory production stream. No hash-independence theorem or exact byte-memory budget is claimed. Python integers avoid counter overflow here but production fixed-width counters need explicit handling.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
