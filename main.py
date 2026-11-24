"""Entry for the make.fun bounty "Seventeen Syllables of Debugging".

The haiku's picture is a single red squiggle under one line of code — the
editor's quiet accusation. The turn is the chase: a whole file searched,
only for the culprit to be a single missing comma.
"""

# The three lines, kept as an immutable tuple so the haiku's shape is fixed.
LINES = (
    "One red squiggle blooms",
    "I chase it through the whole file",
    "it was one comma",
)

HAIKU = "\n".join(LINES)


def write_entry(path="/output/entry.txt"):
    """Best-effort write of the haiku to disk; never fail the run."""
    try:
        import os

        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(HAIKU)
    except OSError:
        pass


if __name__ == "__main__":
    write_entry()
    print(HAIKU)
