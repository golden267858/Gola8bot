import requests
import os

# 认证
headers = {
    "X-Access-Key": os.getenv("BEMOB_ACCESS_KEY"),
    "X-Secret-Key": os.getenv("BEMOB_SECRET_KEY"),
    "Content-Type": "application/json"
}

# 故意留空 columns，看错误提示是否会吐出可用列
url = "https://api.bemob.com/v1/report"
params = {
    "groupBy": "campaign",
    "from": "2026-05-18 00:00:00",
    "to": "2026-05-18 23:59:59"
}

resp = requests.get(url, headers=headers, params=params)
print("Status:", resp.status_code)
print("Response:", resp.text)
