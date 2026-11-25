"""Monday Morning Punchlines — make.fun entry.

Writes one joke about Monday mornings to /output/entry.txt.

Chosen entry (138 chars / 140 bytes):
    Monday morning came to collect before I had even woken up — turns out
    the weekend borrowed my sleep, and Monday charges interest at 7 a.m.

Why this one: a concrete scene (a debt collector at the door before dawn),
a fresh angle (Monday as the collector, the weekend as the borrower), and
the punch lands on the last words — "charges interest" — instead of a
complaint about Mondays. No alarm, no snooze, no coffee, no "I hate Mondays".

Rejected candidates (with reasons):
  1. "Monday morning showed up like a landlord: no warning, keys to my own
     flat, asking why the weekend left the place such a mess." (125 chars)
     — Good scene, but the punch is a complaint about the mess, not a turn.
  2. "Monday morning called me into a meeting with myself to discuss why I
     promised, on Friday, that I would be a completely different person by
     now." (143 chars)
     — Setup-heavy; "meeting with myself" is a known trope and the twist
     arrives too late for its word count.
  3. Any draft built on alarm / snooze / coffee / "weekend is over" —
     rejected as tired Monday cliches the judge explicitly penalises.

Deterministic: stdlib only, no randomness, no I/O besides the single output
file, so two runs produce byte-identical output.
"""

import os

ENTRY = (
    "Monday morning came to collect before I had even woken up \u2014 turns "
    "out the weekend borrowed my sleep, and Monday charges interest at 7 a.m."
)


def validate_entry(text: str) -> None:
    """Enforce the competition gate: UTF-8, 1-200 chars, not only whitespace,
    and a single line (the entry is one joke). Raises ValueError on failure."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8


def main() -> None:
    validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    validate_entry(open("/output/entry.txt", encoding="utf-8").read())


if __name__ == "__main__":
    main()
