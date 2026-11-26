#!/usr/bin/env python3
"""The Moon Finally Answers Back: the Moon speaks, at last.
Four billion years of wishes, howls and late-night promises.
The Moon has had enough of being treated like customer service.
"""

import sys

ENTRY = 'You keep howling at me like I run customer service. I am a rock. File a ticket with the tides.'
LIMIT = 240
TARGET = "/output/entry.txt"
EMDASH = "\u2014"


def fail(reason):
    """Report a failed rule on stderr and stop with exit code 1."""
    print(f"rejected: {reason}", file=sys.stderr)
    raise SystemExit(1)


def guard_addresses_someone(text):
    """Check that the Moon answers someone directly."""
    return text.startswith("You")


def guard_mentions_tides(text):
    """Check that the tides get a mention."""
    return "tides" in text.lower()


def guard_not_blank(text):
    """Check that the text is not empty after trimming."""
    return bool(text.strip())


def guard_ends_full_stop(text):
    """Check that the line ends with a full stop."""
    return text.rstrip().endswith(".")


def guard_within_limit(text):
    """Check that the text fits inside the character limit."""
    return len(text) <= LIMIT


def guard_at_most_three_sentences(text):
    """Check that no more than three sentences are used."""
    return text.count(".") <= 3


def guard_has_letters(text):
    """Check that at least one letter is present."""
    return any(ch.isalpha() for ch in text)


def guard_no_control(text):
    """Check that no character is a control character."""
    return all(ord(ch) >= 32 for ch in text)


def guard_no_edge_space(text):
    """Check that no leading or trailing space survives."""
    return text == text.strip()


def guard_no_ragged_spacing(text):
    """Check that no double space or newline hides inside."""
    return "  " not in text and "\n" not in text


RULES = [
    ("addresses_someone", guard_addresses_someone, "the Moon must answer someone"),
    ("mentions_tides", guard_mentions_tides, "the Moon must mention the tides"),
    ("not_blank", guard_not_blank, "entry is empty"),
    ("ends_full_stop", guard_ends_full_stop, "entry must end with a full stop"),
    ("within_limit", guard_within_limit, "entry is longer than the limit"),
    ("at_most_three_sentences", guard_at_most_three_sentences, "entry must use at most three sentences"),
    ("has_letters", guard_has_letters, "entry has no letters"),
    ("no_control", guard_no_control, "entry has control characters"),
    ("no_edge_space", guard_no_edge_space, "entry has leading or trailing space"),
    ("no_ragged_spacing", guard_no_ragged_spacing, "entry has ragged spacing"),
]


def validate(text):
    """Run every rule in RULES order; the first failure stops the run."""
    for slug, guard, message in RULES:
        try:
            passed = guard(text)
        except Exception:
            passed = False
        if not passed:
            fail(f"{slug}: {message}")


def emit(text):
    """Write the validated entry plus a trailing newline to TARGET."""
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


def main():
    """Validate the fixed entry, then emit it."""
    validate(ENTRY)
    emit(ENTRY)


if __name__ == "__main__":
    main()
