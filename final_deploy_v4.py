import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 1. 使用已存在的 TS
ts_id = "30de7681-176c-481e-a5f4-4a83affed354"
lander_id = "80572886738466657"

def create_offer(name, url):
    payload = {
        "name": name, 
        "url": url, 
        "status": "active",
        "payoutType": "auto",
        "currencyId": "USD", # 修正为 string code
        "countryId": 258,
        "enableDailyCap": False
    }
    res = requests.post(f"{BASE_URL}/offers", params=params, json=payload)
    if res.status_code in [200, 201]:
        return res.json().get('id') or res.json().get('payload', {}).get('id')
    else:
        print(f"[ERROR] Offer {name} failed: {res.text}")
        return None

offer_tg = create_offer("RPG_Game_TG_Support", "https://t.me/gola8bot?start={clickId}")
offer_viber = create_offer("RPG_Game_Viber_Support", "https://msng.link/vi/gola8bot")
offer_trap = create_offer("RPG_Game_Bot_Trap_Redirect", "https://www.google.com")

if all([offer_tg, offer_viber, offer_trap]):
    targets = [("MM_RPG_Game_Push_TG", offer_tg), ("MM_RPG_Game_Push_Viber", offer_viber), ("MM_RPG_Game_Bot_Trap", offer_trap)]
    for name, off_id in targets:
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
            print(f"{name} 部署成功: {res.json().get('url')}")
        else:
            print(f"[ERROR] Campaign {name} failed: {res.text}")
