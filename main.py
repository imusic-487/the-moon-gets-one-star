"""The Moon Gets One Star: write the entry line to /output/entry.txt.

Entry: a one-star review of the Moon, 120 characters at most.
Gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
not only white space, a single line with no trailing newline.
Python 3 standard library only; no network; deterministic.
"""

import hashlib
import os

ENTRY = "One star. After four billion years together, the Moon still won't show me its other side. Rude."


def validate(text):
    """Check the gate: 1-120 chars, single line, not only whitespace."""
    if not 1 <= len(text) <= 120:
        raise ValueError("entry is %d chars, must be 1-120" % len(text))
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if "Moon" not in text:
        raise ValueError("entry must name the Moon it reviews")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: wrote %r, read %r" % (ENTRY, written))
    expected_hash = hashlib.sha256(ENTRY.encode("utf-8")).hexdigest()
    actual_hash = hashlib.sha256(open("/output/entry.txt", "rb").read()).hexdigest()
    if actual_hash != expected_hash:
        raise ValueError("sha256 mismatch: expected %s, got %s" % (expected_hash, actual_hash))
    print(ENTRY)
    print("chars: %d, bytes: %d, sha256: %s" % (len(ENTRY), len(ENTRY.encode("utf-8")), actual_hash))


if __name__ == "__main__":
    main()
