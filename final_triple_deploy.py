import requests
import os

# 使用您在对话中提供的密钥
BEMOB_ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
BEMOB_SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="

API_BASE = "https://api.bemob.com/v1"
# BeMob API 认证方式经测试：params 方式验证通过
params = {"accessKey": BEMOB_ACCESS_KEY, "secretKey": BEMOB_SECRET_KEY}

def create_item(endpoint, name, data_extra=None):
    payload = {"name": name, "status": "active"}
    if data_extra:
        payload.update(data_extra)
    res = requests.post(f"{API_BASE}/{endpoint}", params=params, json=payload)
    if res.status_code in [200, 201]:
        print(f"[SUCCESS] 创建 {name}")
        return res.json().get("id") or res.json().get("payload", {}).get("id")
    else:
        print(f"[ERROR] 创建 {name} 失败: {res.status_code} - {res.text}")
        return None

print("⚡️ CREAO 三线合一，全自动化战略级部署启动...")

# 1. 创建公共组件
ts_id = create_item("traffic-sources", "HilltopAds_Traffic")
# 使用您手动创建的 Lander ID
lander_id = "80572886738466657" 

# 2. 创建三个战线的 Offer
offer_tg_id = create_item("offers", "RPG_Game_TG_Support", {"url": "https://t.me/gola8bot?start={clickId}", "countryId": 258, "enableDailyCap": False})
offer_viber_id = create_item("offers", "RPG_Game_Viber_Support", {"url": "https://msng.link/vi/gola8bot", "countryId": 258, "enableDailyCap": False})
offer_trap_id = create_item("offers", "RPG_Game_Bot_Trap_Redirect", {"url": "https://www.google.com", "countryId": 258, "enableDailyCap": False})

# 3. 聚合创建三个核心 Campaign 计划
if all([ts_id, lander_id]):
    print("\n👑👑👑 开始全线合并 Campaign 计划... 👑👑👑")

    campaigns = [
        ("MM_RPG_Game_Push_TG", offer_tg_id, "🎯 TG 战线 Tracking URL"),
        ("MM_RPG_Game_Push_Viber", offer_viber_id, "🎯 Viber 战线 Tracking URL"),
        ("MM_RPG_Game_Bot_Trap", offer_trap_id, "🛡 捕鼠夹独立 Tracking URL")
    ]

    for name, offer_id, label in campaigns:
        if offer_id:
            camp_data = {
                "name": name,
                "trafficSourceId": ts_id,
                "status": "active",
                "flow": {"type": "redirect", "landerIds": [lander_id], "offerIds": [offer_id]}
            }
            res = requests.post(f"{API_BASE}/campaigns", params=params, json=camp_data)
            if res.status_code in [200, 201]:
                url = res.json().get("url") or res.json().get("payload", {}).get("url")
                print(f"{label}:\n{url}\n")
            else:
                print(f"[ERROR] 创建 Campaign {name} 失败: {res.status_code} - {res.text}")
else:
    print("❌ 核心组件流产，请检查上方报错！")
