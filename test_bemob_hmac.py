import requests
import time
import hmac
import hashlib
import json
import base64
import os

access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 获取当前时间戳
timestamp = str(int(time.time()))

# 生成签名: HMAC-SHA1(timestamp, secret_key)
# 注意：BeMob Landing 签名使用的是 sha1
signature_data = hmac.new(secret_key.encode(), timestamp.encode(), hashlib.sha1).hexdigest()

# 构造 Header (BeMob API 的认证方式)
headers = {
    "X-Api-Key": access_key,
    "X-Api-Signature": signature_data,
    "X-Api-Timestamp": timestamp,
    "Content-Type": "application/json"
}

url = "https://api.bemob.com/v1/report"
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
