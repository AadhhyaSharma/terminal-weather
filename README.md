<div align="center">

# 🌦️ terminal-weather

**Live weather forecasts, right in your terminal.**  
ASCII animations. 5-day forecast. No browser needed.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## What is this?

I hate switching windows just to check the weather. So I built a CLI tool that pulls live weather data and renders it as animated ASCII art right in the terminal.

Uses the free [wttr.in](https://wttr.in) API — no API key needed.

---

## Usage

```bash
python weather.py                    # auto-detect your city
python weather.py --city "Jaipur"    # specific city
python weather.py --city "London" --days 5   # 5-day forecast
python weather.py --city "Tokyo" --compact   # one-liner mode
```

---

## Files

```
terminal-weather/
├── weather.py     ← main script
├── renderer.py    ← ASCII art rendering
├── fetcher.py     ← wttr.in API wrapper
└── animations.py  ← rain / sun / cloud animations
```

---

## Built by

[@AadhhyaSharma](https://github.com/AadhhyaSharma) — 15-year-old builder from Jaipur 🇮🇳
