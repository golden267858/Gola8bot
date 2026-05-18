import requests
import os
import time

headers = {
    "X-Access-Key": os.getenv("BEMOB_ACCESS_KEY"),
    "X-Secret-Key": os.getenv("BEMOB_SECRET_KEY"),
    "Content-Type": "application/json"
}

test_cases = [
    {"columns": ["clicks", "cost", "revenue"], "from": "2026-05-18 00:00:00", "to": "2026-05-18 23:59:59"},
    {"groupBy": "campaignId", "columns": ["clicks", "cost", "revenue"], "from": "2026-05-18 00:00:00", "to": "2026-05-18 23:59:59"},
    {"groupBy": "Campaign", "columns": ["clicks", "cost", "revenue"], "from": "2026-05-18 00:00:00", "to": "2026-05-18 23:59:59"},
    {"groupBy": "campaign_id", "columns": ["clicks", "cost", "revenue"], "from": "2026-05-18 00:00:00", "to": "2026-05-18 23:59:59"}
]

for i, params in enumerate(test_cases):
    if i > 0:
        print("Waiting 15 seconds to avoid Rate Limit...")
        time.sleep(15)
        
    # 将 columns 转为逗号分隔字符串
    if "columns" in params and isinstance(params["columns"], list):
        params["columns"] = ",".join(params["columns"])
        
    resp = requests.get("https://api.bemob.com/v1/report", headers=headers, params=params)
    print(f"--- 测试 {i+1} ---")
    print(f"Params: {params}")
    print(f"Status: {resp.status_code}")
    print(f"Response: {resp.text}")

