"""Deadpan forecast for Quilmbury, a city that does not exist.

Writes one single-line weather forecast (158 characters) to
/output/entry.txt, or to $MAKEFUN_OUTPUT when set for local testing.
Deterministic, stdlib only, no network.
"""

import os

FORECAST = (
    "In Quilmbury, snow falls upward at 3 inches an hour, the sun is "
    "delayed until Thursday pending forms, and lows hit minus 12 in "
    "the town's one heated argument."
)


def main() -> None:
    output = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output) or ".", exist_ok=True)
    with open(output, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(FORECAST)


if __name__ == "__main__":
    main()
