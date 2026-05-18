import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

def create_item(endpoint, data):
    res = requests.post(f"{BASE_URL}/{endpoint}", params=params, json=data)
    if res.status_code in [200, 201]:
        return res.json().get('id') or res.json().get('payload', {}).get('id')
    else:
        print(f"[ERROR] {endpoint} failed: {res.text}")
        return None

print("⚡️ 部署启动...")

ts_id = create_item("traffic-sources", {"name": "HilltopAds_Traffic", "status": "active"})
lander_id = "80572886738466657"

# 修正：currencyId 使用 'USD'，补齐 enableDailyCap
offer_tg = create_item("offers", {"name": "RPG_Game_TG_Support", "url": "https://t.me/gola8bot?start={clickId}", "status": "active", "payoutType": "auto", "currencyId": "USD", "enableDailyCap": False})
offer_viber = create_item("offers", {"name": "RPG_Game_Viber_Support", "url": "https://msng.link/vi/gola8bot", "status": "active", "payoutType": "auto", "currencyId": "USD", "enableDailyCap": False})
offer_trap = create_item("offers", {"name": "RPG_Game_Bot_Trap_Redirect", "url": "https://www.google.com", "status": "active", "payoutType": "auto", "currencyId": "USD", "enableDailyCap": False})

if ts_id and all([offer_tg, offer_viber, offer_trap]):
    targets = [("MM_RPG_Game_Push_TG", offer_tg, "🎯 TG 战线"), ("MM_RPG_Game_Push_Viber", offer_viber, "🎯 Viber 战线"), ("MM_RPG_Game_Bot_Trap", offer_trap, "🛡 捕鼠夹战线")]
    for name, off_id, label in targets:
        camp = {
            "name": name,
            "trafficSourceId": ts_id,
            "status": "active",
            "costModel": "notTracked",
            "redirectMode": "http302",
            "currencyId": "USD",
            "flow": {"type": "redirect", "landerIds": [lander_id], "offerIds": [off_id]}
        }
        res = requests.post(f"{BASE_URL}/campaigns", params=params, json=camp)
        if res.status_code in [200, 201]:
            print(f"{label} URL: {res.json().get('url') or res.json().get('payload', {}).get('url')}")
        else:
            print(f"[ERROR] {name} failed: {res.text}")
