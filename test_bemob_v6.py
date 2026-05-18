import requests
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

url = "https://api.bemob.com/v1/report"
# 也许是 Api-Key 而不是 X-Api-Key ? 
headers = {
    "Api-Key": access_key,
    "Api-Secret": secret_key
}
params = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

resp = requests.get(url, headers=headers, params=params)
print("Status:", resp.status_code)
print("Response:", resp.text[:500])
