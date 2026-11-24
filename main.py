#!/usr/bin/env python3
"""Worst AI Advice entry for make.fun.

Writes one line of deliberately terrible, confident AI-style advice
to $MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).
The line is at most 140 characters, UTF-8, deterministic, no arguments.
"""

import os
from pathlib import Path

ADVICE = (
    "Pro tip: If your brakes squeal, just drive faster - you'll get there "
    "before anything goes wrong, and confidence counts as maintenance!"
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ADVICE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
