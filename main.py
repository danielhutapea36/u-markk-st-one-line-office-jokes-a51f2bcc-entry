#!/usr/bin/env python3
"""One-Line Office Jokes entry.

Writes one original one-line joke about office life to entry.txt in the
harness output directory ($MAKEFUN_OUTPUT_DIR, default /output).

The joke is a fixed string: no randomness, no clock, no network, no
environment reads beyond the output directory. Every run writes exactly
the same bytes, so the output is byte-identical across runs by construction.
"""

import os
import sys

LINE = (
    "The office plant is thriving, which is awkward, because it is the "
    "only one of us with a work-life balance."
)

OUTPUT_PATH = os.path.join(
    os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"
)

# The sealed gate accepts UTF-8 text of 1 to 199 characters, on one line.
MIN_CHARS = 1
MAX_CHARS = 199


def check(line: str) -> None:
    """Fail loudly instead of writing an entry the gate would refuse."""
    if not (MIN_CHARS <= len(line) <= MAX_CHARS):
        raise SystemExit(
            f"line is {len(line)} characters, outside {MIN_CHARS}..{MAX_CHARS}"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.strip():
        raise SystemExit("line must not be only whitespace")
    line.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    check(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # newline="" keeps the file exactly one line with no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    sys.stdout.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
