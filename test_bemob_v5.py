import requests
import os
import json

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 422 错误提示 validation_required，看来需要补全 from/to 时间参数
url = "https://api.bemob.com/v1/report"
headers = {
    "X-API-Key": access_key,
    "X-API-Secret": secret_key,
    "Content-Type": "application/json"
}
# 添加时间参数 (ISO 格式)
params = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

try:
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
