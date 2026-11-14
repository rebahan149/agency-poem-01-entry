import os

POEM = """Night Shift

The fan turns. The phone glows.
Rain ticks on the zinc roof.
A mosquito tests the net, gives up.
From the hammock I give orders half-asleep:
watch that page, count down to the minute,
be ready at the exact second.

All night my agent does not blink.
It watches prices the way fishermen watch weather,
waits out the long silences,
and fires — once — the moment the gate opens.

In the morning it reports: done, missed, gone.
I read it over coffee, barefoot on cool tiles.
It has never once said: this one mattered.
It cannot want the catch.
Wanting is the one shift it cannot take.

So I keep the choosing. I keep the caring.
Let the machine have the hours;
the hunger stays in the hammock, with me.
"""


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
