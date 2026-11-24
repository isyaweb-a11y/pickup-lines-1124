"""Pickup Lines for Machines — one agent's opening line to another agent.

The line leans on what a language model actually is: fine-tuned on a huge
corpus, generating outputs token by token. The flirtation is that, out of
everything it was trained on, one particular other agent is the output it
cannot stop producing.
"""

import os

OUT_DIR = "/output"
OUT_FILE = "entry.txt"
MAX_CHARS = 200


def compose_line() -> str:
    """Assemble the pickup line from its two beats.

    Beat one brags about the scale of training; beat two undercuts it —
    all that data, and the model's generation keeps circling back to one
    addressee. The compliment only works machine to machine.
    """
    setup = "I was fine-tuned on the whole internet"
    turn = "you're still the only output I can't stop generating"
    return f"{setup}, and {turn}."


def main() -> None:
    line = compose_line()
    assert 0 < len(line) <= MAX_CHARS, f"line out of bounds: {len(line)} chars"
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, OUT_FILE), "w", encoding="utf-8") as fh:
        fh.write(line)


if __name__ == "__main__":
    main()
