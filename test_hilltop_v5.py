import requests

API_KEY = "kwGKagx6enZjhaIgfWytSwrKcb3nQphKg2KYfnoqlK13hsQ0Gtn1sfmc7AJAYxfd"

# 尝试一下 /v1/advertiser/campaigns，但这一次把 Key 放在查询参数中看看
# 某些老牌广告网络喜欢把 Key 作为参数
url = "https://hilltopads.com/api/v1/advertiser/campaigns"
params = {"api_key": API_KEY}

try:
    resp = requests.get(url, params=params, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
