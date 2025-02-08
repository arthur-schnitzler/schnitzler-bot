[![flake8 Lint](https://github.com/arthur-schnitzler/schnitzler-bot/actions/workflows/lint.yml/badge.svg)](https://github.com/arthur-schnitzler/schnitzler-bot/actions/workflows/lint.yml)
[![125 years ago, schnitzler wrote](https://github.com/arthur-schnitzler/schnitzler-bot/actions/workflows/diary.yml/badge.svg)](https://github.com/arthur-schnitzler/schnitzler-bot/actions/workflows/diary.yml)

# schnitzler-bot
Code Repo for https://bsky.app/profile/schnitzler-bot.bsky.social, a bluesky clone of [@asilcetin](https://github.com/asilcetin) https://github.com/asilcetin/schnitzler-otd

## dev

clone the repo & set up virtual env & install needed packages & expose your Bluesky credentials as env-variables `BS_HANDLE` and `BS_TOKEN`

```bash
git clone https://github.com/arthur-schnitzler/schnitzler-bot.git
cd schnitzler-bot
python -m venv venv venv
source venv/bin/activate
pip install -r requierments.txt
source set_env_variables
```

## scripts/schnitzler-tagebuch.py

posts what Schnitzler wrote 125 years ago into his diary
