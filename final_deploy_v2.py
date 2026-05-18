import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

def create_offer(name, url):
    payload = {
        "name": name, 
        "url": url, 
        "status": "active",
        "payoutType": "auto",
        "currencyId": "USD",
        "countryId": 258,
        "enableDailyCap": False
    }
    res = requests.post(f"{BASE_URL}/offers", params=params, json=payload)
    if res.status_code in [200, 201]:
        return res.json().get("id") or res.json().get("payload", {}).get("id")
    else:
        print(f"[ERROR] 创建 {name} 失败: {res.text}")
        return None

# 使用现有 TS ID
ts_id = "30de7681-176c-481e-a5f4-4a83affed354"
lander_id = "80572886738466657"

print("👑 开始执行最终部署...")

# 创建 Offers
offer_tg_id = create_offer("RPG_Game_TG_Support", "https://t.me/gola8bot?start={clickId}")
offer_viber_id = create_offer("RPG_Game_Viber_Support", "https://msng.link/vi/gola8bot")
offer_trap_id = create_offer("RPG_Game_Bot_Trap_Redirect", "https://www.google.com")

# 部署 Campaign
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
        res = requests.post(f"{BASE_URL}/campaigns", params=params, json=camp_data)
        if res.status_code in [200, 201]:
            url = res.json().get("url") or res.json().get("payload", {}).get("url")
            print(f"{label}:\n{url}\n")
        else:
            print(f"[ERROR] 创建 {name} 失败: {res.text}")
