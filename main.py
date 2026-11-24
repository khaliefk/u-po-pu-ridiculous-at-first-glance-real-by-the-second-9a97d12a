#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (<=200 chars) pitching a bizarre startup idea
that sounds absurd until the business logic lands.
"""

import os

ENTRY = (
    "We sell monthly excuse insurance: cancel any plan and a former "
    "diplomat sends your friends an excuse so gracious they thank you for "
    "it, so chronic flakers pay to stay liked."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") <= 1, "entry must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
