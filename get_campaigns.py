import requests
import os
import json

headers = {
    "X-Access-Key": os.getenv("BEMOB_ACCESS_KEY"),
    "X-Secret-Key": os.getenv("BEMOB_SECRET_KEY"),
    "Content-Type": "application/json"
}

url = "https://api.bemob.com/v1/campaigns"

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    # 打印完整返回的脱敏信息
    if resp.status_code == 200:
        data = resp.json()
        print("Response (JSON):", json.dumps(data, indent=2)[:1000])
    else:
        print("Response:", resp.text)
except Exception as e:
    print("Request Failed:", e)
