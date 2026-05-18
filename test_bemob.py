import os
import requests
import json

API_KEY = os.getenv("BEMOB_API_KEY")
# 使用文档中常见的基础 URL
url = "https://api.bemob.com/v1/report"
# 根据前面的 Key 和 Secret，BeMob 通常使用 Bearer 认证
headers = {"Authorization": f"Bearer {API_KEY}"}
params = {"groupBy": "campaign", "period": "today"}

try:
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", json.dumps(resp.json(), indent=2)[:500])
except Exception as e:
    print("Error:", e)
