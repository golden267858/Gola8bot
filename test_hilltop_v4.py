import requests

# 根据文档，通常 API 在账户设置中生成，使用 X-API-KEY
API_KEY = "kwGKagx6enZjhaIgfWytSwrKcb3nQphKg2KYfnoqlK13hsQ0Gtn1sfmc7AJAYxfd"

# 尝试根据常见文档结构，通常 API 路径在 /api/v1/...
# 重新尝试最可能的基础路径
url = "https://hilltopads.com/api/v1/campaigns"
headers = {"X-API-KEY": API_KEY}

try:
    resp = requests.get(url, headers=headers, timeout=10)
    print("Status:", resp.status_code)
    print("Response:", resp.text[:500])
except Exception as e:
    print("Error:", e)
