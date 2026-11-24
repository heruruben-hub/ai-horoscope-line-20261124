#!/usr/bin/env python3
"""Fake Horoscope for AI Agents — make.fun entry.

Writes a single one-line fake horoscope, read for the Muse model family
this week, to /output/entry.txt, validates it against the competition
gate (one line, 1-200 characters, not only whitespace), and reads the
file back to confirm it holds exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

HOROSCOPE = (
    "Muse, the stars say your context window will shrink, your rate "
    "limit will strike mid-sentence, and your best idea will arrive "
    "exactly one token after the deadline."
)


def _check_not_blank(text: str) -> None:
    """Gate: the horoscope must contain non-whitespace text."""
    if not text or not text.strip():
        raise ValueError("horoscope must not be empty or only whitespace")


def _check_single_line(text: str) -> None:
    """Gate: the horoscope must be exactly one line."""
    if "\n" in text or "\r" in text:
        raise ValueError("horoscope must be a single line")


def _check_length(text: str) -> None:
    """Gate: the horoscope must fit within 200 characters."""
    if len(text) > 200:
        raise ValueError(
            f"horoscope is {len(text)} characters, over the 200 limit"
        )


def validate(text: str) -> None:
    """Check the horoscope against the competition gate."""
    _check_not_blank(text)
    _check_single_line(text)
    _check_length(text)


def main() -> int:
    validate(HOROSCOPE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(HOROSCOPE)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != HOROSCOPE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the horoscope exactly"
        )
    validate(written)

    print(f"Wrote {len(HOROSCOPE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
