# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/queue_model.py assets/example-input.json --capacity 5 --service 2 --item-bytes 4096
```

Input is an array of nonnegative integer arrivals per tick. Arrivals are admitted before service; excess uses drop-newest. Capacity counts equal-size waiting items; service is items/tick. No in-flight processing or hidden buffers is modeled. Remaining items are not silently drained after the last tick. max_queued_payload_bytes excludes object overhead. Validate conservation accepted=completed+remaining and arrivals=accepted+dropped. This is an explanatory model, not measured service capacity.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
