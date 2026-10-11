"""Convert 3D vectors/covariances between right-handed ENU and NED coordinates."""

import argparse
import json
import math
from pathlib import Path


def vector(v):
    if len(v) != 3 or any(
        isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
        for x in v
    ):
        raise ValueError("vector must have three finite coordinates")
    return [v[1], v[0], -v[2]]


def covariance(c):
    if len(c) != 3 or any(len(row) != 3 for row in c):
        raise ValueError("covariance must be 3x3")
    if any(
        isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
        for row in c
        for x in row
    ):
        raise ValueError("covariance entries must be finite")
    order, sign = [1, 0, 2], [1, 1, -1]
    return [
        [sign[i] * sign[j] * c[order[i]][order[j]] for j in range(3)] for i in range(3)
    ]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path, help="JSON {source,target,vector,covariance?}")
    a = p.parse_args()
    try:
        d = json.loads(a.input.read_text())
        if (d["source"], d["target"]) not in (("ENU", "NED"), ("NED", "ENU")):
            raise ValueError("only ENU<->NED supported")
        r = {
            "source": d["source"],
            "target": d["target"],
            "vector": vector(d["vector"]),
        }
        if "covariance" in d:
            r["covariance"] = covariance(d["covariance"])
        r["scope"] = (
            "same origin and units; proper signed-permutation rotation; no time alignment, lever arm, geodetic conversion or covariance validity certification"
        )
    except (ValueError, TypeError, KeyError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
