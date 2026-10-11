# Executable helper

Run from the skill directory, or use absolute paths. Requires Python 3.10+ and the standard library only.

```bash
python scripts/frame_decoder.py assets/example-input.json --max-frame 1024
```

Input is a JSON array of hexadecimal byte chunks. Decoder uses a four-byte unsigned big-endian payload length; empty frames are allowed. It buffers only the currently needed header/frame, rejects oversized declarations before payload allocation and raises on truncated EOF. Frames are output as hex. Discard the decoder/connection after malformed input. Framing does not validate authentication, semantic schemas or retries; caller must bound chunk/output retention.

Read `--help` for options. Invalid input exits nonzero. Preserve the input and exact output for task evidence; never present a demonstration fixture as a production verification.
