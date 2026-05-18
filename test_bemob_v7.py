import requests
import os
import base64

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 一些 API 平台使用 "Authorization: Basic Base64(Access:Secret)"
# 让我们最后尝试这种标准的 HTTP Basic Auth
auth_str = f"{access_key}:{secret_key}"
b64_auth = base64.b64encode(auth_str.encode()).decode()

url = "https://api.bemob.com/v1/report"
headers = {
    "Authorization": f"Basic {b64_auth}",
    "Content-Type": "application/json"
}
params = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

resp = requests.get(url, headers=headers, params=params)
print("Status (Basic):", resp.status_code)
print("Response:", resp.text[:200])

# 如果还是不行，尝试 X-API-KEY / X-API-SECRET 组合不带签名
headers_v2 = {
    "X-API-KEY": access_key,
    "X-API-SECRET": secret_key,
    "Content-Type": "application/json"
}
resp2 = requests.get(url, headers=headers_v2, params=params)
print("Status (X-API-Key/Secret):", resp2.status_code)
print("Response:", resp2.text[:200])
