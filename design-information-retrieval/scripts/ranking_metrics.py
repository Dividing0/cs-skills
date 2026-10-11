"""Compute per-query and macro retrieval metrics with explicit conventions."""

import argparse
import json
import math
from pathlib import Path


def evaluate(data, k=10):
    if k <= 0:
        raise ValueError("k must be positive")
    qrels, rankings = data["qrels"], data["rankings"]
    if not qrels:
        raise ValueError("at least one judged query is required")
    if set(rankings) - set(qrels):
        raise ValueError("ranking query missing judgments")
    rows = {}
    for query, grades in qrels.items():
        if any(
            isinstance(g, bool)
            or not isinstance(g, (int, float))
            or not math.isfinite(g)
            or not 0 <= g <= 30
            for g in grades.values()
        ):
            raise ValueError("grades must be finite numbers between 0 and 30")
        ranking = rankings.get(query, [])
        if len(set(ranking)) != len(ranking):
            raise ValueError("duplicate document in ranking")
        top = ranking[:k]
        relevant = {d for d, g in grades.items() if g > 0}
        hits = [d in relevant for d in top]
        retrieved = sum(hits)
        dcg = sum(
            (2 ** grades.get(d, 0) - 1) / math.log2(i + 2) for i, d in enumerate(top)
        )
        ideal = sorted(grades.values(), reverse=True)[:k]
        idcg = sum((2**g - 1) / math.log2(i + 2) for i, g in enumerate(ideal))
        rows[query] = {
            "precision_at_k": retrieved / k,
            "recall_at_k": retrieved / len(relevant) if relevant else 0.0,
            "reciprocal_rank_at_k": next(
                (1 / (i + 1) for i, h in enumerate(hits) if h), 0.0
            ),
            "ndcg_at_k": dcg / idcg if idcg else 0.0,
            "judged_fraction_at_k": sum(d in grades for d in top) / len(top)
            if top
            else 0.0,
        }
    metrics = ("precision_at_k", "recall_at_k", "reciprocal_rank_at_k", "ndcg_at_k")
    return {
        "k": k,
        "queries": rows,
        "macro": {m: sum(r[m] for r in rows.values()) / len(rows) for m in metrics},
        "conventions": "unjudged=grade0; binary relevant=grade>0; gain=2^grade-1; no relevant gives recall/nDCG0; precision denominator=k; missing ranking=empty",
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("input", type=Path)
    p.add_argument("--k", type=int, default=10)
    a = p.parse_args()
    try:
        result = evaluate(json.loads(a.input.read_text()), a.k)
    except (ValueError, KeyError, TypeError) as e:
        p.error(str(e))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
