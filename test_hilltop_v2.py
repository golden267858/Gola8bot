import os
import requests

API_KEY = os.getenv("HILLTOPADS_API_KEY")
# 检查 API 文档常用的 Base URL，尝试 /v1/advertiser/campaigns
url = "https://hilltopads.com/api/v1/advertiser/campaigns"
headers = {"X-API-KEY": API_KEY, "Content-Type": "application/json"}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
