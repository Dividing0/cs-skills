"""Insertion-only Count-Min reference implementation with deterministic SHA-256 rows."""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


class Sketch:
    def __init__(self, width, depth, seed="0"):
        if width <= 0 or depth <= 0:
            raise ValueError("width/depth must be positive")
        self.width, self.depth, self.seed = width, depth, seed
        self.table = [[0] * width for _ in range(depth)]

    def positions(self, key):
        if not isinstance(key, str):
            raise ValueError("keys must be strings")
        for row in range(self.depth):
            encoded = json.dumps([self.seed, row, key], ensure_ascii=False).encode()
            yield (
                row,
                int.from_bytes(hashlib.sha256(encoded).digest(), "big") % self.width,
            )

    def add(self, key, count=1):
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("insertion-only nonnegative integer updates required")
        for row, column in self.positions(key):
            self.table[row][column] += count

    def estimate(self, key):
        return min(self.table[r][c] for r, c in self.positions(key))

    def merge(self, other):
        if (self.width, self.depth, self.seed) != (
            other.width,
            other.depth,
            other.seed,
        ):
            raise ValueError("incompatible dimensions/hash seeds")
        for r in range(self.depth):
            for c in range(self.width):
                self.table[r][c] += other.table[r][c]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON array of string keys")
    p.add_argument("--width", type=int, default=256)
    p.add_argument("--depth", type=int, default=4)
    p.add_argument("--seed", default="0")
    a = p.parse_args()
    try:
        keys = json.loads(a.input.read_text())
        sketch = Sketch(a.width, a.depth, a.seed)
        for key in keys:
            sketch.add(key)
        exact = Counter(keys)
    except (ValueError, TypeError) as e:
        p.error(str(e))
    print(
        json.dumps(
            {
                "items": len(keys),
                "estimates": {k: sketch.estimate(k) for k in exact},
                "exact": dict(exact),
                "max_error": max(
                    (sketch.estimate(k) - n for k, n in exact.items()), default=0
                ),
                "scope": "reference fixture uses unbounded exact oracle; SHA rows are not proof of hash independence; Python table bytes not width*depth*8",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
