[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/zenganteng0987/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/zenganteng0987/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

# THE DAILY ATLAS — Wednesday 25 November 2026

A one-page newspaper image summing up the world's news of Wednesday
25 November 2026: 32 stories in 15 illustrated main cards plus an
ALSO list, a "THE DAY IN UTC" chronology strip, a "BY THE NUMBERS"
strip, and a "DATE CHECK" strip naming stories deliberately left out
because they happened before 25 November.

## Main stories

1. Shenzhou-24 lifts off with Pakistan's first astronaut (00:18 UTC)
2. US proposes new Section 301 tariffs on 14 partners; China faces 20%
3. Australia passes the Digital Duty of Care (Senate 36–23, House 97–43)
4. US Q3 GDP revised up to 4.3%; core PCE 3.3% year on year
5. Xi's graft probe fells Shanghai party chief Chen Jining
6. Huawei guilty on 10 of 12 counts in a US trial
7. Microsoft declares "Code Red" after its historic outage
8. Nvidia slides 5.9%; Dow closes above 50,000
9. Serang candy-factory fire: 26 dead, 28 still missing
10. Israeli strike kills Hamas internal-security chief in Gaza
11. All Cartagena supermarket hostages freed
12. Houthis claim strikes on a Saudi refinery and Riyadh (claim)
13. Abrego Garcia lands in Spain after leaving the US
14. Democrats reach 259 House seats, their largest majority since 1990
15. Euclid finds the most distant quasar yet (630m years after the Big Bang)

Also covered: NATO's space pledge, the Villavicencio car bomb, the
missing Congo plane, the UK's Rohingya genocide recognition, the
Ahmadi flogging, US consumer confidence at 103.3, the Nepal quake,
Syria's landmine casualties, the Shein $100m settlement, Russia's
2027 defence budget, the Davis Cup, California king tides, the
Giuliani Medal of Freedom, the Iowa lead-azide detonation, Puigdemont's
return, the Sarkozy trial order, and Anthropic below its IPO price.

Every story is dated: events from 23–24 November are marked with
their date, and the DATE CHECK strip explains what was left out
(Trump–Xi–Putin trilateral ~19–20 Nov, "El Chapo Isidro" arrested
20 Nov, ICJ Myanmar ruling 19 Nov, COP31 ended 22 Nov).

## How it works

`main.py` (Python 3 standard library only, no network) copies the
pre-rendered `entry.png` (1024×1024, under 1 MiB) into
`MAKEFUN_OUTPUT_DIR` (or `/output` if it exists, else the current
directory), verifies it is a 1024×1024 PNG under the 1 MiB limit,
prints its sha256, and exits 0.

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
