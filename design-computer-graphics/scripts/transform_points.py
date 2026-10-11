"""Compose 4x4 matrices and transform column-vector homogeneous points."""

import argparse
import json
import math
from pathlib import Path


def validate(matrix):
    if len(matrix) != 4 or any(len(row) != 4 for row in matrix):
        raise ValueError("matrix must be 4x4")
    if any(
        isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
        for row in matrix
        for x in row
    ):
        raise ValueError("matrix entries must be finite")


def multiply(a, b):
    validate(a)
    validate(b)
    return [
        [sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)
    ]


def point(matrix, p, epsilon=1e-12):
    validate(matrix)
    if len(p) != 3 or any(
        isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x)
        for x in p
    ):
        raise ValueError("point must have 3 finite coordinates")
    v = list(p) + [1]
    out = [sum(matrix[i][j] * v[j] for j in range(4)) for i in range(4)]
    if any(not math.isfinite(x) for x in out) or abs(out[3]) <= epsilon:
        raise ValueError("nonfinite result or homogeneous w too close to zero")
    return [x / out[3] for x in out[:3]]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "input",
        type=Path,
        help="JSON {matrices:[firstApplied,...],points:[[x,y,z],...]}",
    )
    a = p.parse_args()
    try:
        data = json.loads(a.input.read_text())
        matrix = [[int(i == j) for j in range(4)] for i in range(4)]
        for m in data["matrices"]:
            matrix = multiply(m, matrix)
        r = {
            "composite": matrix,
            "points": [point(matrix, v) for v in data["points"]],
            "convention": "column vectors; matrices listed in order of application; no clipping, normals or viewport transform",
        }
    except (ValueError, KeyError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
