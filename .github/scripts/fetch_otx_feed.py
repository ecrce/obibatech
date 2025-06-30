import os
import requests
import json

api_key = os.getenv("OTX_API_KEY")

if not api_key:
    print("OTX_API_KEY is not set.")
    exit(1)

headers = {
    "X-OTX-API-KEY": api_key,
    "Content-Type": "application/json"
}

try:
    res = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed", headers=headers)
    print("Status Code:", res.status_code)

    if res.status_code != 200:
        print("Error response:", res.text)
        exit(1)

    pulses = res.json().get("results", [])[:5]
    headlines = [p["name"] for p in pulses]

    os.makedirs("data", exist_ok=True)
    with open("data/feed.json", "w") as f:
        json.dump(headlines, f)

    print("Feed updated successfully.")
except Exception as e:
    print("Exception occurred:", e)
    exit(1)
