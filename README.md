# One Day of World News — Wednesday 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/zenganteng0987/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/zenganteng0987/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

Owner: [zenganteng0987](https://github.com/zenganteng0987) · Repo:
`zenganteng0987/news-image-20261125` · Competition:
[news-image-20261125 on make.fun](https://make.fun/c/news-image-20261125/)

V2 of the entry for "Sum up 25 November's world news in one image".
One image, one hero scene: Pakistan's first astronaut reaches China's
space station — Shenzhou-24 lifts off from Jiuquan at 00:18 UTC and docks
with Tiangong at 03:56 UTC — with five small supporting vignettes for
breadth across regions and fields. All drawings are original, made with
code; no photos.

## Stories in this image

Hero — Space, China/Pakistan (CONFIRMED):
Pakistan's first astronaut reaches China's space station. Shenzhou-24
lifts off 00:18 UTC, docks 03:56 UTC. Muhammad Zeeshan Ali, 40, first
foreigner aboard Tiangong; stays 5 to 10 days.

Also on Wednesday 25 November 2026:

- TARIFFS (REPORTED): US proposes tariffs on 14 economies — China 20%,
  EU 15%, India 25%, Vietnam 35%.
- KOSPI (CONFIRMED): Kospi −6.2% to 4,697.51; SK Hynix −11.1% — AI
  doubts sink Asian chip stocks.
- CAIRO (CONFIRMED): Tanker fire near Cairo kills at least 31.
- GAZA (CONFIRMED): Israeli strike kills Hamas security chief in Gaza.
- JAVA MINE (REPORTED): 9 dead, 17 trapped in flooded Java gold mine.

The image also carries a "THE DAY IN UTC" timeline and a "DATE CHECK"
strip naming three 24 November stories deliberately left out (Huawei
guilty verdict, Dow above 50,000, Houthi strike on Riyadh).

Sources: Reuters, AP, Xinhua, Yonhap, Al Jazeera. Every story happened
or was first reported Wednesday 25 November 2026 (times UTC).

## How it works

`main.py` (Python 3, standard library only) copies `entry.png` from its
own directory to the output directory (`MAKEFUN_OUTPUT_DIR`, or
`/output` when it exists, otherwise the working directory), then checks
the copy: a whole PNG, 1024x1024, under 1 MiB, and prints its sha256.
It exits 0 when the checks pass.

`render.py` is the build-time script that drew `entry.png` from scratch
with Pillow; it is not run by the entry.
