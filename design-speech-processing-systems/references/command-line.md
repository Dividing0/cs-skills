# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/audio_budget.py assets/example-input.json
```

Positive integer sample_rate/channels/sample_bytes; positive finite frame_ms. Stages have name and optional nonnegative buffer_ms, lookahead_ms, processing_ms, queue_ms, network_ms, endpoint_ms. The calculator adds one initial frame plus serial stage components. Avoid double-counting frame/lookahead when supplying values. It does not infer pipelined overlap or end-to-end percentiles from per-stage percentiles. Frame size may be fractional; integral_frame flags that issue.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
