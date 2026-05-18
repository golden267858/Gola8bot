import requests
import os
import json

# 认证
headers = {
    "X-Access-Key": os.getenv("BEMOB_ACCESS_KEY"),
    "X-Secret-Key": os.getenv("BEMOB_SECRET_KEY"),
    "Content-Type": "application/json"
}

# 按照老板的顺序策略进行测试
scenarios = [
    ["campaign_id", "campaign_name", "clicks", "cost", "revenue"],
    ["campaignId", "campaignName", "total_cost", "total_revenue"],
    ["cpc", "cpm", "ctr", "roi", "profit"],
    ["clicks", "cost", "revenue"]
]

url = "https://api.bemob.com/v1/report"

for cols in scenarios:
    params = {
        "groupBy": "campaign",
        "columns": ",".join(cols),
        "from": "2026-05-18 00:00:00",
        "to": "2026-05-18 23:59:59"
    }
    resp = requests.get(url, headers=headers, params=params)
    print(f"Columns: {cols}")
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text[:500]}")
    print("-" * 30)

