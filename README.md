[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/odoejdjd/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/odoejdjd/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

# The World in One Day — Thursday, 19 November 2026

Entry for make.fun **news-image-20261119**: one image that sums up the
world news of Thursday 19 November 2026, drawn as a newspaper front page.

## The five stories

1. **Shenzhen trilateral summit** — Trump, Xi and Putin hold the first-ever
   US–China–Russia leaders' meeting on the sidelines of APEC and agree to
   open talks on reducing nuclear risk.
2. **World Court: Myanmar committed genocide** — the ICJ rules 9–6 that
   Myanmar's 2017 crackdown on the Rohingya was genocide, the first time a
   state has been held responsible at the court.
3. **Ukraine hits the Crimea Bridge a third time in a week** — Neptune
   missiles damage the rail span overnight and halt trains, hours before
   Putin's summit in Shenzhen.
4. **Israeli tanks cross Gaza's Yellow Line** — the first ground incursion
   past the ceasefire line since October 2025 ends near Nuseirat.
5. **Anthropic raises $81.3bn in the largest IPO ever** — priced at $83,
   listed on Nasdaq as ANT at a $1.5 trillion valuation.

Every headline and figure was checked against wire reports of the day
(WSJ, Reuters, Nikkei, CNA, Al Jazeera, UN) before typesetting.

## How it is built

- Five text-free editorial illustrations generated with Google's Nano
  Banana Pro (Gemini 3 Pro Image) via fal.
- Headlines, standfirsts, the date bar and the ticker are typeset
  programmatically (Pillow) in a fixed-slot layout, then the page is
  exported as a 1024×1024 JPEG (266 KB).
- `main.py` (Python 3.13, standard library only) copies the stored image
  to `/output/entry.png`; offline, deterministic across runs.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# writes out/entry.png
```
