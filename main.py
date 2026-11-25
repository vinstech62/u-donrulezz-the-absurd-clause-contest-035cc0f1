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
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(CLAUSE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
