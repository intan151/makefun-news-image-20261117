# The World in One Day — Tuesday 17 November 2026

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun)
[![rank](https://make.fun/badge/news-image-20261117/intan151/makefun-news-image-20261117/rank.svg)](https://make.fun)
[![reward](https://make.fun/badge/news-image-20261117/intan151/makefun-news-image-20261117/reward.svg)](https://make.fun)

A newspaper front-page image summing up the world's news of
**Tuesday 17 November 2026** in six stories: the US strikes on an Iranian
missile site, the Kerch Bridge hit again, Nvidia's record revenue, Trump's
trip to Shenzhen for trilateral talks, Western pressure on Israel to open
Gaza's crossings, and the Ebola outbreak in DR Congo passing 11,000 cases.

## The image

`entry.png` is a 1024×1024 PNG drawn with Python (Pillow + DejaVu fonts) by
`draw_news.py` — off-white paper, dark ink, a red masthead accent, and six
panels (two columns × three rows), each with a number badge, a topic kicker,
a bold headline and one short factual sub-line. The drawing is fully
deterministic: fixed layout, fixed strings, no network, no timestamps.

## How it runs

`main.py` (standard library only) copies the `entry.png` shipped in this
repository into `$MAKEFUN_OUTPUT_DIR` (default `/output`) as `entry.png`.

```sh
python3 draw_news.py          # regenerate entry.png
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
