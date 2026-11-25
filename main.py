#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "The Funniest Office Joke, Judged Head to Head": A universal office truth built as an escalating triple - lost files, Friday errors, Finance paying regardless - with the surprise punchline word 'weather' held to the very end, and none of the brief's stock meeting/reply-all/printer material.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Our office calls it 'the cloud' because nobody knows where the files are, it rains errors every Friday, and Finance just keeps paying for the weather."
TEXT = LINE + "\n"
MAX_CHARS = 200
NLINES = 1


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if body.count("\n") != NLINES - 1:
        raise ValueError("wrong line count")
    if "\r" in body:
        raise ValueError("no carriage returns")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
