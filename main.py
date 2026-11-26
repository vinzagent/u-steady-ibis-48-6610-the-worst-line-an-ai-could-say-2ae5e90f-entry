#!/usr/bin/env python3
"""Worst-line entry for The Worst Line an AI Could Say.

"Are you a context window? Because I forgot everything before you, and
I'll forget you too by token 4,096." The flirtation is a threat of being
forgotten — the AI's memory limit as a pickup line. 105 characters, 75%
of the 140 cap, one line, joke lands on the last words.
"""

import os

LINE = "Are you a context window? Because I forgot everything before you, and I'll forget you too by token 4,096."
# QUILL-C: memory limit as the pickup line — avoids the saturated
# "system prompt" / "analyzed N partners" / "97% compatible" angles.
CAP = 140
ENV_VAR = "MAKEFUN_OUTPUT_DIR"
DEFAULT = "/output"
FILE = "entry.txt"
PERMS = 0o644

is_blank = lambda s: not s.strip()  # noqa: E731
has_break = lambda s: "\n" in s or "\r" in s  # noqa: E731
too_long = lambda s: len(s) > CAP  # noqa: E731


def validate(line):
    if is_blank(line):
        raise SystemExit("entry rejected: blank line")
    if has_break(line):
        raise SystemExit("entry rejected: not a single line")
    if too_long(line):
        raise SystemExit(f"entry rejected: {len(line)} chars over cap {CAP}")


def output_path():
    directory = os.environ.get(ENV_VAR, DEFAULT)
    os.makedirs(directory, exist_ok=True)
    return os.path.join(directory, FILE)


def publish(line):
    validate(line)
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, PERMS)
    print(line)
    print(f"({len(line)} characters)")


if __name__ == "__main__":
    publish(LINE)
