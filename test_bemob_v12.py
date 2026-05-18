import requests
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

url = "https://api.bemob.com/v1/report"
headers = {
    "X-Access-Key": access_key,
    "X-Secret-Key": secret_key,
    "Content-Type": "application/json"
}
# 不 groupby，直接拉取数据
params = {
    "columns": "clicks,cost,revenue",
    "from": "2026-05-18 00:00:00",
    "to": "2026-05-18 23:59:59"
}

resp = requests.get(url, headers=headers, params=params)
print("BeMob Status:", resp.status_code)
print("BeMob Response:", resp.text[:500])
