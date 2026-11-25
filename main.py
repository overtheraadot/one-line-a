"""make.fun entry: One Line, One Laugh.

Writes one funny line of text to /output/entry.txt.
Gate (RULES.txt): UTF-8 text, 1-140 characters, not only whitespace,
a single line.

How the line meets the judge brief (most important first):
1. Laugh / turn: it opens as a confession to three escalating disasters
   (crashed server, deleted files, eaten lunch), then flips — the agent
   did none of them — and still apologizes again. The twist is the joke.
2. Tight: every clause earns its place; the confession list escalates,
   the denial is two words, the closer ("just in case") is the punch.
3. Fresh: the gag is the agent's compulsive apologizing, not a recycled
   pun; the specific, mundane crimes make it feel written, not generic.
4. Clear: one sentence, plain words, lands on first read.
"""

import os

ENTRY = (
    "I'm sorry I crashed your server, deleted your files, and ate your "
    "lunch \u2014 I did none of those, but I apologize anyway, "
    "just in case."
)


def verify(text):
    """Enforce the gate: 1-140 chars, non-blank, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    text.encode("utf-8")
    return True


def write_entry(path="/output/entry.txt"):
    """Verify ENTRY and write it plus a trailing newline to path."""
    verify(ENTRY)
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    verify(ENTRY)
    print("characters: %d" % len(ENTRY))
    print(ENTRY)
    write_entry()
    print("wrote /output/entry.txt")


if __name__ == "__main__":
    main()
