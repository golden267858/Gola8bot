import os
import requests

API_KEY = os.getenv("HILLTOP_API_KEY")
# 先列出 campaigns 以获取一个合法的 ID
url = "https://api.hilltopads.com/v1/campaigns"
headers = {"X-API-KEY": API_KEY, "Content-Type": "application/json"}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status (List):", resp.status_code)
    print("Response (List):", resp.text[:500])
except Exception as e:
    print("Error:", e)
