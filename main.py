#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The joke is a single line, no trailing newline, fully
deterministic: the same text on every run.
"""

import os
from pathlib import Path

# One original dad joke: a father at the barbecue, a ladder,
# and a pun on "raise the stakes" that lands on "steaks".
JOKE = (
    'My son asked why I always bring a ladder to the barbecue. '
    'I said, "Son, someone has to raise the steaks."'
)


def main() -> None:
    """Write the joke exactly, with no trailing newline."""
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # write_text with no newline: the file holds exactly JOKE.
    entry_path.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
