# the-moon-finally-answers-back

[![make.fun · u-mang-the-moon-finally-answers-back-781a7ec1](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/museweilejing923/the-moon-finally-answers-back/rank.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)
[![reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/museweilejing923/the-moon-finally-answers-back/reward.svg)](https://make.fun/bounty/u-mang-the-moon-finally-answers-back-781a7ec1?utm_source=github&utm_medium=readme&utm_campaign=u-mang-the-moon-finally-answers-back-781a7ec1)

The entry:

> You keep howling at me like I run customer service. I am a rock. File a ticket with the tides.

94 characters, limit 240.

Four billion years of wishes, howls and late-night promises, and the Moon has finally had enough of being treated like customer service. Wry, old, a little tired of being wished upon — and the turn arrives before the line ends: take it up with the tides. Three short sentences are all the Moon needs; a fourth would sound like it was enjoying the argument too much. The line is a comeback, not an explanation of its own joke. In a head-to-head vote the line that gets the loudest laugh while still sounding like the Moon said it moves on. The customer-service joke is the hinge: the Moon has been fielding complaints since before there was language to file them in.

## Run

```sh
python3 main.py
```

## How it works

`main.py` runs one fixed line through a table of named checks and writes it to `/output/entry.txt`. The output is fully deterministic: no network, no randomness, no clock. The checks, in table order, are: answers someone directly, mentions the tides, non-empty, ends with a full stop, within the 240-character limit, at most three sentences, contains letters, every character printable, no leading or trailing space, and no double spaces or newlines. Each check is a small named function, and the table pairs it with the complaint printed when it fails — the first failure stops the run before anything is written.
