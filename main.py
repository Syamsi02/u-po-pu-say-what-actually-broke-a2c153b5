"""Say What Actually Broke — one line of honest error copy.

Writes a single-line software error message (at most 200 characters)
to /output/entry.txt. The line names the real failure in plain words,
tells the user what to do next, and lands the joke in one read.

The line is 141 characters: a server out-of-memory failure mid-save,
no data stored, retry in a minute, and the blame placed where it
belongs when the retry fails too.
"""

import os
import sys

LINE = (
    "Our server ran out of memory mid-save and dropped your work \u2014 "
    "nothing was stored. Try again in a minute; "
    "if it fails twice, it\u2019s us, not you."
)


def main() -> int:
    text = LINE.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
