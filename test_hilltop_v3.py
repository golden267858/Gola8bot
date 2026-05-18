import requests

# 猜测 HilltopAds 的正确 API 地址
# 许多此类广告平台的 API 地址形式为 api.hilltopads.com/v1/advertiser/...
API_KEY = "kwGKagx6enZjhaIgfWytSwrKcb3nQphKg2KYfnoqlK13hsQ0Gtn1sfmc7AJAYxfd"

# 尝试列出所有 campaigns
url = "https://api.hilltopads.com/v1/advertiser/campaigns"
headers = {"X-API-KEY": API_KEY}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
