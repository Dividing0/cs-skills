"""Sort UTF-8 newline records lexicographically using bounded chunks and merge fan-in."""

import argparse
import heapq
import json
import tempfile
from contextlib import ExitStack
from pathlib import Path


def sort_file(source, target, chunk_bytes=1048576, fan_in=16, max_record_bytes=65536):
    source, target = Path(source), Path(target)
    if source.resolve() == target.resolve() or target.exists():
        raise ValueError("output must be a new path distinct from input")
    if chunk_bytes <= 0 or max_record_bytes <= 0 or fan_in < 2:
        raise ValueError("positive byte limits and fan_in>=2 required")
    count = passes = 0
    with tempfile.TemporaryDirectory(prefix="external-sort-") as temp:
        temp = Path(temp)
        runs = []
        records = []
        byte_count = 0

        def flush():
            path = temp / f"run-{len(runs)}.txt"
            with path.open("w", encoding="utf-8", newline="\n") as out:
                for record in sorted(records):
                    out.write(record + "\n")
            runs.append(path)
            records.clear()

        with source.open("rb") as inp:
            while True:
                raw = inp.readline(max_record_bytes + 1)
                if not raw:
                    break
                if len(raw) > max_record_bytes:
                    raise ValueError(
                        "record exceeds maximum encoded size including newline"
                    )
                record = raw.decode("utf-8").removesuffix("\n")
                if records and byte_count + len(raw) > chunk_bytes:
                    flush()
                    byte_count = 0
                records.append(record)
                byte_count += len(raw)
                count += 1
        if records:
            flush()
        initial_runs = len(runs)
        while len(runs) > 1:
            merged = []
            passes += 1
            for i in range(0, len(runs), fan_in):
                group = runs[i : i + fan_in]
                dest = temp / f"merge-{passes}-{i}.txt"
                with ExitStack() as stack:
                    readers = [
                        stack.enter_context(p.open(encoding="utf-8", newline=""))
                        for p in group
                    ]
                    with dest.open("w", encoding="utf-8", newline="\n") as out:
                        out.writelines(
                            heapq.merge(
                                *readers, key=lambda line: line.removesuffix("\n")
                            )
                        )
                merged.append(dest)
                for path in group:
                    path.unlink()
            runs = merged
        created = False
        try:
            with target.open("xb") as out:
                created = True
                if runs:
                    with runs[0].open("rb") as inp:
                        while block := inp.read(chunk_bytes):
                            out.write(block)
        except BaseException:
            if created:
                target.unlink(missing_ok=True)
            raise
    return {
        "records": count,
        "initial_runs": initial_runs,
        "merge_passes": passes,
        "scope": "lexicographic text records; bounded encoded chunks, not exact Python RSS; max merge readers=fan_in; temp spill is not durable recovery",
        "output": str(target),
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("source", type=Path)
    p.add_argument("target", type=Path)
    p.add_argument("--chunk-bytes", type=int, default=1048576)
    p.add_argument("--fan-in", type=int, default=16)
    p.add_argument("--max-record-bytes", type=int, default=65536)
    a = p.parse_args()
    try:
        r = sort_file(a.source, a.target, a.chunk_bytes, a.fan_in, a.max_record_bytes)
    except (ValueError, OSError, UnicodeError) as e:
        p.error(str(e))
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
