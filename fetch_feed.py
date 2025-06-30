import requests
import json
import os

headers = {
    "X-OTX-API-KEY": os.getenv("OTX_API_KEY")
}

r = requests.get("https://otx.alienvault.com/api/v1/pulses/subscribed", headers=headers)
data = r.json()["results"][:5]

with open("threat_feed.json", "w") as f:
    json.dump(data, f, indent=2)
