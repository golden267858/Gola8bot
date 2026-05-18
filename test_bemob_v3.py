import requests
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 尝试另一种常见的 header 方式: 直接传入 Key 和 Secret
url = "https://api.bemob.com/v1/report"
headers = {
    "Api-Key": access_key,
    "Api-Secret": secret_key,
    "Content-Type": "application/json"
}
params = {"groupBy": "campaign", "period": "today"}

try:
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
