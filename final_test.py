import requests
import time
import hmac
import hashlib
import os

# 配置
bemob_access = os.getenv("BEMOB_ACCESS_KEY")
bemob_secret = os.getenv("BEMOB_SECRET_KEY")
hilltop_key = os.getenv("HILLTOPADS_API_KEY")

print("--- BeMob API 测试 ---")
# 根据 BeMob REST API 文档，认证需使用 AccessKey 和 SecretKey
# 尝试使用 headers: X-Api-Key 和 X-Api-Secret
url_bemob = "https://api.bemob.com/v1/report"
headers_bemob = {
    "X-Api-Key": bemob_access,
    "X-Api-Secret": bemob_secret,
    "Content-Type": "application/json"
}
params_bemob = {
    "groupBy": "campaign",
    "from": "2026-05-18T00:00:00Z",
    "to": "2026-05-18T23:59:59Z"
}

try:
    res_b = requests.get(url_bemob, headers=headers_bemob, params=params_bemob, timeout=10)
    print(f"BeMob Status: {res_b.status_code}")
    print(f"BeMob Response: {res_b.text[:500]}")
except Exception as e:
    print(f"BeMob Error: {e}")

print("\n--- HilltopAds API 测试 ---")
# 根据 HilltopAds 文档，使用 X-API-KEY
url_hilltop = "https://api.hilltopads.com/v1/advertiser/campaigns"
headers_hilltop = {"X-API-KEY": hilltop_key}

try:
    res_h = requests.get(url_hilltop, headers=headers_hilltop, timeout=10)
    print(f"HilltopAds Status: {res_h.status_code}")
    print(f"HilltopAds Response: {res_h.text[:500]}")
except Exception as e:
    print(f"HilltopAds Error: {e}")
