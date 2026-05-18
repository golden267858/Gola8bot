import requests
import os
import json

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

url = "https://api.bemob.com/v1/report"
headers = {
    "X-Access-Key": access_key,
    "X-Secret-Key": secret_key,
    "Content-Type": "application/json"
}
# 使用正确的参数名: columns, from, to
params = {
    "groupBy": "campaign",
    "columns": "clicks,cost,revenue",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

resp = requests.get(url, headers=headers, params=params)
print("BeMob Status:", resp.status_code)
print("BeMob Response:", resp.text)
