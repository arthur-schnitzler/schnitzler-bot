from atproto import Client
from atproto_client.utils import TextBuilder

from config import BS_HANDLE, BS_TOKEN, WEBSITE_URL
from utils import get_text, get_schnitzler_date

tb = TextBuilder()
date = get_schnitzler_date()
URL = f"{WEBSITE_URL}{date}.html"


if BS_HANDLE:
    msg = f"{get_text()}\n"
    tb.text(msg)
    tb.link(f"Schnitzler-Tagebuch, {date}", URL)
    client = Client()
    client.login(BS_HANDLE, BS_TOKEN)
    post = client.send_post(tb)
    print(post)
else:
    print(
        "please run `./set_env_variables` or whatever else to set needed env variables"
    )
