#!/usr/bin/env python3
"""Have You Tried Turning It Off? — one funny line, under 200 chars,
that a hopeless tech support agent says to a desperate customer.

Pure Python 3 standard library only (os). No network, no randomness,
no clock: every run writes the same single line to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""
# Revised: the line is built inside write_entry(); entry.txt mirrors it exactly.
import os


def write_entry():
    line = (
        "Have you tried turning it off and on again? No? Wonderful "
        "\u2014 that's step one. Step two is me Googling your exact "
        "error message while you hold."
    )
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    return line


if __name__ == "__main__":
    print(write_entry())
