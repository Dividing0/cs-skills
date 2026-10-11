# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/check_register.py assets/example-input.json
```

Values are JSON data compared by canonical JSON encoding. Writes mean successful completed register assignments; reads return result. Fields: unique string id, op, finite start/end and value or result. Optional status defaults to ok. Equal timestamps do not resolve event order; precedence uses end < start. Provide a totally ordered event clock or conservative intervals. Pending/failed operations return unknown. --max-ops default12 and --max-states default100000 bound search. Exit0 compatible with witness; exit1 violated; exit2 unknown or invalid input. This does not check transactions, multiple keys, crash durability or incomplete histories.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
