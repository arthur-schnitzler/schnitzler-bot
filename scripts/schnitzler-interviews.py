import json
import sys
import requests

from collections import defaultdict
from atproto import Client
from atproto_client.utils import TextBuilder

from config import (
    BS_HANDLE,
    BS_TOKEN,
    SCHNITZLER_INTERVIEWS_URL,
    SCHNITZLER_INTERVIEWS_DATA_URL,
)
from utils import current_day, years_ago

current_day = current_day()
tb = TextBuilder()
r = requests.get(SCHNITZLER_INTERVIEWS_DATA_URL).text.replace("var calendarData = ", "")
data = json.loads(r)
d = defaultdict(list)
for x in data:
    day = x["startDate"][5:]
    d[day] = x
print(d.keys())

print(f"searching for interviews for {current_day}")
try:
    item = dict(d)[current_day]
except KeyError:
    print(f"no match found for {current_day}")
    sys.exit(0)

if BS_HANDLE:
    print(item)
    url = f'{SCHNITZLER_INTERVIEWS_URL}{item["id"]}'
    ago = years_ago(item["startDate"].split("-")[0])
    title = item["name"].split("\n")[0]
    msg = f"Heute vor {ago} Jahren gab ich wieder einmal ein Interview: "
    tb.text(msg)
    tb.link(f"Schnitzler-Interviews: {title}", url)
    client = Client()
    client.login(BS_HANDLE, BS_TOKEN)
    post = client.send_post(tb)
    print(post)
else:
    print(
        "please run `./set_env_variables` or whatever else to set needed env variables"
    )
