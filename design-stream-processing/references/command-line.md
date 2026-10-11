# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/window_oracle.py assets/example-input.json --width 5 --deduplicate
```

Input is an array of events with finite numeric time and string key. With --deduplicate also require a string id; repeated IDs with differing event payloads are errors. Windows are [start,end), origin0; negative timestamps use mathematical floor. Deduplication is global only over this finite input and uses memory proportional to unique events. This is an offline oracle, not a bounded streaming processor, watermark simulation or checkpoint checker.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
