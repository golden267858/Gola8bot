import requests
import time
import hmac
import hashlib

# BeMob 的标准做法通常是将 Access Key 作为 User，Secret 作为 Password 进行 Basic Auth
# 或者在 Header 中传递 Api-Key 和 Api-Secret
access_key = "366E9F2203B948178F38BC502DF0DF57"
secret_key = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="

url = "https://api.bemob.com/v1/report"
headers = {
    "Api-Key": access_key,
    "Api-Secret": secret_key
}
params = {"groupBy": "campaign", "period": "today"}

try:
    # 尝试直接请求
    resp = requests.get(url, headers=headers, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text)
except Exception as e:
    print("Error:", e)
