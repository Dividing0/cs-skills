"""Deterministic discrete-tick FIFO admission model for equal-size items."""

import argparse
import json
from collections import deque
from pathlib import Path


def simulate(arrivals, capacity, service, item_bytes=1):
    if capacity <= 0 or service < 0 or item_bytes <= 0:
        raise ValueError(
            "capacity/item_bytes positive and service nonnegative required"
        )
    if any(isinstance(n, bool) or not isinstance(n, int) or n < 0 for n in arrivals):
        raise ValueError("arrivals must contain nonnegative integers")
    queue = deque()
    accepted = completed = dropped = highwater = 0
    ages = []
    timeline = []
    for tick, n in enumerate(arrivals):
        admitted = min(n, capacity - len(queue))
        queue.extend([tick] * admitted)
        accepted += admitted
        dropped += n - admitted
        highwater = max(highwater, len(queue))
        served = min(service, len(queue))
        for _ in range(served):
            ages.append(tick - queue.popleft())
        completed += served
        timeline.append(
            {
                "tick": tick,
                "arrivals": n,
                "admitted": admitted,
                "completed": served,
                "queued": len(queue),
            }
        )
    return {
        "accepted": accepted,
        "completed": completed,
        "dropped": dropped,
        "remaining": len(queue),
        "max_queued_items": highwater,
        "max_queued_payload_bytes": highwater * item_bytes,
        "max_completed_age_ticks": max(ages, default=0),
        "timeline": timeline,
        "assumptions": "arrivals then service each tick; drop-newest; equal-size payloads; excludes object overhead, hidden buffers and in-flight stages",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON array of arrivals per tick")
    p.add_argument("--capacity", type=int, required=True)
    p.add_argument("--service", type=int, required=True)
    p.add_argument("--item-bytes", type=int, default=1)
    a = p.parse_args()
    try:
        r = simulate(
            json.loads(a.input.read_text()), a.capacity, a.service, a.item_bytes
        )
    except (ValueError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
