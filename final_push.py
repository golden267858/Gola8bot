import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 获取模板 Campaign 以获取完整 payload 结构
r = requests.get(f"{BASE_URL}/campaigns", params=params)
template = r.json()['payload'][0] # 使用第一个作为模板

def deploy_campaign(name, offer_id, lander_id, ts_id):
    # 构建精准 payload
    payload = {
        "name": name,
        "trafficSourceId": ts_id,
        "status": "active",
        "currencyId": "USD",
        "costModel": "cpc",
        "destinationType": "flow",
        "redirectMode": "302",
        "uniquenessPeriod": 24,
        "flow": {
            "type": "redirect",
            "landerIds": [lander_id],
            "offerIds": [offer_id]
        }
    }
    res = requests.post(f"{BASE_URL}/campaigns", params=params, json=payload)
    return res.json().get('url') if res.status_code in [200, 201] else res.text

ts_id = "30de7681-176c-481e-a5f4-4a83affed354"
lander_id = "80572886738466657"
# Offer 已通过手动创建，这里需要获取 ID
r_off = requests.get(f"{BASE_URL}/offers", params=params)
offers = {o['name']: o['id'] for o in r_off.json()['payload']}

print(f"🎯 TG URL: {deploy_campaign('MM_RPG_Game_Push_TG', offers['RPG_Game_TG_Support'], lander_id, ts_id)}")
print(f"🎯 Viber URL: {deploy_campaign('MM_RPG_Game_Push_Viber', offers['RPG_Game_Viber_Support'], lander_id, ts_id)}")
print(f"🛡 Trap URL: {deploy_campaign('MM_RPG_Game_Bot_Trap', offers['RPG_Game_Bot_Trap_Redirect'], lander_id, ts_id)}")
