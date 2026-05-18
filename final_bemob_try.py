import requests
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

url = "https://api.bemob.com/v1/report"
params = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

# 尝试 Header: X-Access-Key / X-Secret-Key
headers = {
    "X-Access-Key": access_key,
    "X-Secret-Key": secret_key,
    "Content-Type": "application/json"
}

resp = requests.get(url, headers=headers, params=params)
print("Status (X-Access/Secret):", resp.status_code)
print("Response:", resp.text[:200])

# 尝试 Header: Access-Key / Secret-Key
headers_v2 = {
    "Access-Key": access_key,
    "Secret-Key": secret_key,
    "Content-Type": "application/json"
}
resp2 = requests.get(url, headers=headers_v2, params=params)
print("Status (Access/Secret):", resp2.status_code)
print("Response:", resp2.text[:200])
