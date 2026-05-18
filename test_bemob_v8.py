import requests
import time
import hmac
import hashlib
import os
import json

# 读取环境变量
access_key = os.getenv("BEMOB_ACCESS_KEY")
secret_key = os.getenv("BEMOB_SECRET_KEY")

# 根据官方给出的 PHP 示例，签名逻辑是:
#  = hash_hmac('sha1', , LANDING_SECRET_KEY);
# 也就是用 sha1 对 timestamp 进行签名
timestamp = str(int(time.time()))
signature = hmac.new(secret_key.encode(), timestamp.encode(), hashlib.sha1).hexdigest()

# 尝试调用报表接口，使用官方推荐的认证方式 (注意：这是针对 Tracker 的)
# 如果是 REST API，可能不走这个签名方式，而是 Api-Key + Api-Secret Header
url = "https://api.bemob.com/v1/report"
headers = {
    "Api-Key": access_key,
    "Api-Secret": secret_key,
    "Content-Type": "application/json"
}
params = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

resp = requests.get(url, headers=headers, params=params)
print("Status (v8):", resp.status_code)
print("Response:", resp.text[:200])

# 如果 Header 不对，尝试用 X-Api-Key / X-Api-Secret
headers_v2 = {
    "X-Api-Key": access_key,
    "X-Api-Secret": secret_key,
    "Content-Type": "application/json"
}
resp2 = requests.get(url, headers=headers_v2, params=params)
print("Status (v9):", resp2.status_code)
