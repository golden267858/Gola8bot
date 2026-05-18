import requests

# 再次确认 HilltopAds API 调用方式
# 尝试请求 /v1/advertiser/campaigns (这是最标准的路径)
API_KEY = "kwGKagx6enZjhaIgfWytSwrKcb3nQphKg2KYfnoqlK13hsQ0Gtn1sfmc7AJAYxfd"
url = "https://api.hilltopads.com/v1/advertiser/campaigns"
# 很多网络要求 Auth header 为 "Authorization: Bearer <KEY>" 或 "X-API-KEY: <KEY>"
# 这里我们测试 Bearer
headers = {"Authorization": f"Bearer {API_KEY}"}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status (Bearer):", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
