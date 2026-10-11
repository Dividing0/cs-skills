"""Observe timer-owned callback/args/context lifetimes; not an RSS leak detector."""

import argparse
import asyncio
import contextvars
import gc
import importlib
import json
import weakref


class Payload:
    def callback(self, *args):
        pass


def probe(factory, count=100):
    loop = factory()
    marker = contextvars.ContextVar("retention_probe_marker")
    refs, handles = [], []
    active = loop.call_later(20, lambda: None)
    try:
        for _ in range(count):
            callback_owner, argument, context_owner = Payload(), Payload(), Payload()
            ctx = contextvars.Context()
            ctx.run(marker.set, context_owner)
            refs.append(
                tuple(weakref.ref(x) for x in (callback_owner, argument, context_owner))
            )
            handle = loop.call_later(
                3600, callback_owner.callback, argument, context=ctx
            )
            handles.append(handle)
            del callback_owner, argument, context_owner, ctx, handle

        def alive():
            gc.collect()
            return dict(
                zip(
                    ("callback", "argument", "context"),
                    (sum(row[i]() is not None for row in refs) for i in range(3)),
                )
            )

        scheduled = alive()
        for h in handles:
            h.cancel()
            h.cancel()
        cancelled = alive()
        loop.run_until_complete(asyncio.sleep(0))
        ticked = alive()
        active.cancel()
        loop.close()
        closed = alive()
        return {
            "count": count,
            "scheduled": scheduled,
            "after_cancel": cancelled,
            "after_tick": ticked,
            "after_close_handles_retained": closed,
            "scope": "weakref reachability for acyclic payloads; handles remain referenced",
        }
    finally:
        if not loop.is_closed():
            active.cancel()
            loop.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--factory",
        default="asyncio:new_event_loop",
        help="module:callable returning a new loop",
    )
    parser.add_argument("--count", type=int, default=100)
    args = parser.parse_args()
    if args.count <= 0:
        parser.error("count must be positive")
    module, sep, attribute = args.factory.partition(":")
    if not sep or not attribute:
        parser.error("factory must be module:callable")
    factory = getattr(importlib.import_module(module), attribute)
    print(json.dumps(probe(factory, args.count), indent=2))


if __name__ == "__main__":
    main()
