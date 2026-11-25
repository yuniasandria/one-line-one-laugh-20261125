#!/usr/bin/env python3
"""One Line, One Laugh — writes a single funny line to /output/entry.txt.

Pure stdlib. The line is assembled from two parts so the punchline lands
in one clean pass: a concrete kitchen mechanism, exact numbers, and a
low-risk measurable closer.
"""

import os
from pathlib import Path

# PART_A: the setup — a concrete mechanism with exact numbers.
LINE_A = "My microwave beeps 3 times when it's done, "

# PART_B: the turn — the punchline, and the guard that proves the line.
LINE_B = (
    "then again every 30 seconds until I open it \u2014 the only "
    "appliance in my house that files a noise complaint against me."
)

LINE = LINE_A + LINE_B


def main() -> None:
    # Guard: the assembled line is exactly the two parts, one line, in gate.
    assert LINE == LINE_A + LINE_B
    assert "\n" not in LINE and "\r" not in LINE
    assert LINE.strip() == LINE
    assert 1 <= len(LINE) <= 200, len(LINE)
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
