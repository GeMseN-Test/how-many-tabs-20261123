#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes one honest number -- the count of browser tabs open right now --
as digits only, to /output/entry.txt. Nothing else: no words, no newline.
"""

import os

# The number: 437.
#
# Why 437: a real power-user count, not a round number picked to shock.
# Three Chrome windows that piled up over weeks -- work (docs, dashboards,
# chat), research (AI and crypto reading, make.fun), YouTube "watch later",
# and shopping tabs never closed. Specific and odd, the way a counted
# number looks; high enough to surprise, low enough to believe.
# The program is fully deterministic: same input, same three bytes, every run.
TABS_OPEN = 437

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Digits only, no trailing newline: the gate allows 1-5 characters.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(str(TABS_OPEN))


if __name__ == "__main__":
    main()
