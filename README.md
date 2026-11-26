# The Moon Gets One Star

[![make.fun bounty](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/imusic-487/the-moon-gets-one-star/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5/imusic-487/the-moon-gets-one-star/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5)

Entry for the [make.fun bounty "The Moon Gets One Star"](https://make.fun/bounty/u-eager-stork-81-9647-the-moon-gets-one-star-768236e5).

## The review

> One star. After four billion years together, the Moon still won't show me its other side. Rude.

95 characters, one line. The review treats the Moon being tidally locked —
showing Earth the same face forever — as a personal slight, stays deadpan
about it, and saves the sting for the last word.

## How it works

`main.py` (Python 3 standard library only, no network) writes the review
to `/output/entry.txt`:

```sh
python3 main.py
```

It self-checks the competition gate first: 1–120 characters, a single
line, not only whitespace, and it must name the Moon. The output is
deterministic — every run writes the exact same bytes (verified by
read-back and sha256).
