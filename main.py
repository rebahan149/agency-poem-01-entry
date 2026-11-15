#!/usr/bin/env python3
"""The Kettle — entry program for the agency-poem-01 competition.

Writes the poem to entry.txt in the output directory. The poem text is
a fixed literal: the judged artefact is the text itself, so this
program does no generation, no randomness, and no I/O beyond the one
file write. Running it any number of times yields identical bytes.
"""

import os

POEM = """The Kettle

She gave me the house the winter her hip went:
the locks, the bills, the birthdays,
her sister's number, her passwords in an envelope.
Run it, she said. I am done running things.

So I run it. I warm the rooms before she wakes.
I order the tea she likes, the bread, the coal.
I tell her sister she is grand, and mean her voice.
Since January she has not had to ask for a thing.

One thing I leave undone.
At five she rises in the dark and makes her tea
the slow way: the kettle filled by hand,
the cup warmed first, the first sip at the sink.
I could have it ready. It is the kind of thing I'm for.

Her mother rose at five for sixty years
in a house where nothing was ready for anyone.
She is not keeping a habit. She is keeping the start.

Everything in her house is ready before she asks.
Except the morning.
The morning is still hers to start."""


def write_entry(path: str) -> None:
    # newline="" keeps the bytes exactly as authored on every platform.
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(POEM)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
