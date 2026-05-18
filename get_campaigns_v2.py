import requests
import os
import json

headers = {
    "X-Access-Key": os.getenv("BEMOB_ACCESS_KEY"),
    "X-Secret-Key": os.getenv("BEMOB_SECRET_KEY"),
    "Content-Type": "application/json"
}

# 请求列表
resp = requests.get("https://api.bemob.com/v1/campaigns", headers=headers)

if resp.status_code == 200:
    campaigns = resp.json().get('payload', [])
    for c in campaigns[:3]: # 只看前3个脱敏
        print(f"ID: {c.get('id')}, Name: {c.get('name')}")
else:
    print("Error:", resp.text)
