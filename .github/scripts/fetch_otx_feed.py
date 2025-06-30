import requests
import json
import os

headers = {
    'X-OTX-API-KEY': os.getenv('OTX_API_KEY'),
    'Content-Type': 'application/json'
}

response = requests.get('https://otx.alienvault.com/api/v1/pulses/subscribed', headers=headers)
if response.status_code == 200:
    pulses = response.json().get("results", [])[:5]
    feed = [pulse["name"] for pulse in pulses]
    os.makedirs("data", exist_ok=True)
    with open("data/feed.json", "w") as f:
        json.dump(feed, f)
else:
    print("Failed to fetch OTX feed:", response.status_code)
    exit(1)

