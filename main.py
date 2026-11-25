#!/usr/bin/env python3
"""The Absurd Clause Contest — one absurd terms-of-service clause.

Writes a single original English sentence (133 characters) to
/output/entry.txt: deadpan legal boilerplate that quietly turns absurd.
Deterministic: the same line on every run. Python 3 standard library
only, no network, no randomness.
"""

import os

CLAUSE = (
    "You hereby grant us a non-exclusive, royalty-free license to your "
    "dreams, provided they are submitted in triplicate before breakfast."
)


def main():
    # Gate self-check: the sealed scorer only judges 1-200 character,
    # single-line, non-blank UTF-8 text. Fail loudly instead of
    # silently shipping an invalid entry.
    assert "\n" not in CLAUSE, "clause must be a single line"
    assert 1 <= len(CLAUSE) <= 200, "clause must be 1-200 characters"
    assert CLAUSE.strip(), "clause must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(CLAUSE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
