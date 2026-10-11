# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/retention_probe.py --factory asyncio:new_event_loop --count 100
```

Import only a trusted module:callable returning a new event loop. The probe retains all handles and keeps an earlier timer active. Read callback/argument/context live counts at each phase; different runtimes may have different context-release contracts. It does not test cyclic payloads, destructor reentrancy, native allocations or RSS. A nonzero count is reachability evidence at that phase, not automatically a leak.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
