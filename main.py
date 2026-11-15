#!/usr/bin/env python3
"""agency-poem-01 entry: writes the poem "The Last Knot" to /output/entry.txt."""
from pathlib import Path

POEM = """I ready his boat before the light comes up.
Fuel topped, nets shaken out, hooks baited in a row,
the rope coiled the way his father taught him.
His father taught him. Not me.

I could tie the last knot in one second, and it would hold.
My knots do not slip. His take four minutes now:
stiff fingers, a thumb that will not close,
the line shaking in his hands like something alive.

Last spring I tied it once, while he was below deck.
He came up, saw it, and untied it without a word.
He tied it again, badly, and would not look at me,
and the boat knocked soft against the pier all morning.

So now I leave the loop open on the cleat
and the rope's end laid where his palm will find it,
and I stand in the stern with my hands empty,
which is the hardest work I do.

A boat is not yours, he told me once,
until your own hands have closed it.
I keep everything else ready.
The closing is his."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
