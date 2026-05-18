import requests
import os

# 根据官方文档，有两种方式:
# 1. Headers: X-API-Key 和 X-API-Secret
# 2. Query Params: accessKey 和 secretKey

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

url = "https://api.bemob.com/v1/report"
headers = {
    "X-API-Key": access_key,
    "X-API-Secret": secret_key,
    "Content-Type": "application/json"
}
params = {"groupBy": "campaign", "period": "today"}

try:
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status (X-API-Header):", resp.status_code)
    
    if resp.status_code != 200:
        # 尝试 Query Params
        params.update({"accessKey": access_key, "secretKey": secret_key})
        resp = requests.get(url, params=params, timeout=10)
        print("Status (Query Params):", resp.status_code)
        print("Response:", resp.text[:200])
except Exception as e:
    print("Error:", e)
