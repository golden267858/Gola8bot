import requests
import base64
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 构造 Base64 认证字符串
auth_str = f"{access_key}:{secret_key}"
encoded_auth = base64.b64encode(auth_str.encode()).decode()

url = "https://api.bemob.com/v1/report"
headers = {
    "Authorization": f"Basic {encoded_auth}",
    "Content-Type": "application/json"
}
params = {"groupBy": "campaign", "period": "today"}

try:
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
