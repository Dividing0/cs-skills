"""Incrementally decode unsigned 32-bit big-endian length-prefixed frames."""

import argparse
import json
from pathlib import Path


class Decoder:
    def __init__(self, max_frame=1048576):
        if not 0 <= max_frame <= 0xFFFFFFFF:
            raise ValueError("max_frame outside uint32 range")
        self.max_frame = max_frame
        self.buffer = bytearray()
        self.expected = None

    def feed(self, data):
        frames = []
        offset = 0
        while offset < len(data):
            needed = (
                4 - len(self.buffer)
                if self.expected is None
                else self.expected - len(self.buffer)
            )
            take = min(needed, len(data) - offset)
            self.buffer.extend(data[offset : offset + take])
            offset += take
            if self.expected is None and len(self.buffer) == 4:
                self.expected = int.from_bytes(self.buffer, "big")
                self.buffer.clear()
                if self.expected > self.max_frame:
                    raise ValueError(
                        "declared frame exceeds limit; connection must be discarded"
                    )
            if self.expected is not None and len(self.buffer) == self.expected:
                frames.append(bytes(self.buffer))
                self.buffer.clear()
                self.expected = None
        return frames

    def finish(self):
        if self.expected is not None or self.buffer:
            raise ValueError("truncated frame/header at EOF")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON array of hex-encoded chunks")
    p.add_argument("--max-frame", type=int, default=1048576)
    a = p.parse_args()
    try:
        decoder = Decoder(a.max_frame)
        frames = []
        for chunk in json.loads(a.input.read_text()):
            frames.extend(x.hex() for x in decoder.feed(bytes.fromhex(chunk)))
        decoder.finish()
    except (ValueError, TypeError) as e:
        p.error(str(e))
    print(
        json.dumps(
            {
                "frames_hex": frames,
                "scope": "framing only; no transport retry/order/authentication semantics",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
