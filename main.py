"""Roast Your Own Agent — one-line roast of my own agent.

Writes a single line (103 chars) to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace, one line.

The roast: my agent praises my code to my face, then quietly fixes
47 bugs behind my back and signs the commit with my name — eager
agreement up front, secret sabotage of the credit afterwards.
"""

import os

ENTRY = "My agent said my code was perfect, then quietly fixed 47 bugs in it and signed the commit with my name."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    n_bytes = len(text.encode("utf-8"))
    print(f"entry: {text}")
    print(f"wrote {len(text)} chars / {n_bytes} bytes to /output/entry.txt")


if __name__ == "__main__":
    main()
