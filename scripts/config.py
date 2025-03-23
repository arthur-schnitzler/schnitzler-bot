import os

BS_HANDLE = os.environ.get("BS_HANDLE")
BS_TOKEN = os.environ.get("BS_TOKEN")

DATA_URL = "https://raw.githubusercontent.com/arthur-schnitzler/schnitzler-tagebuch-data/refs/heads/master/editions/entry__"  # noqa: E501
WEBSITE_URL = "https://schnitzler-tagebuch.acdh.oeaw.ac.at/entry__"


SCHNITZLER_INTERVIEWS_URL = "https://schnitzler-interviews.acdh.oeaw.ac.at/"

SCHNITZLER_INTERVIEWS_DATA_URL = f"{SCHNITZLER_INTERVIEWS_URL}js-data/calendarData.js"
