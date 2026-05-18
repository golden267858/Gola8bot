import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 1. 创建新 Offer
offer_data = {
    "name": "RPG Game TG Support",
    "url": "tg://resolve?domain=gola8bot&start={clickId}",
    "status": "active",
    "payoutType": "auto",
    "currencyId": "USD"
}
r_offer = requests.post(f"{BASE_URL}/offers", params=params, json=offer_data)
print(f"创建 Offer 响应: {r_offer.status_code}, {r_offer.json()}")
offer_id = r_offer.json()['payload']['id'] if r_offer.status_code == 200 else None

# 2. 找到 HilltopAds API 的 ID
ts_id = "30de7681-176c-481e-a5f4-4a83affed354" 

# 3. 创建 Campaign
# Lander ID 从用户处获得 (假设手动创建后的 ID)
lander_id = "f050d297-b248-43d9-93e1-7e040b2f1559" # 请替换为您手动获取的ID

if ts_id and offer_id and lander_id:
    camp_data = {
        "name": "MM - RPG Game Push",
        "trafficSourceId": ts_id,
        "status": "active",
        "flow": {
            "type": "redirect",
            "landerIds": [lander_id],
            "offerIds": [offer_id]
        }
    }
    r_camp = requests.post(f"{BASE_URL}/campaigns", params=params, json=camp_data)
    print(f"创建活动响应: {r_camp.status_code}, {r_camp.json()}")
else:
    print("缺失 ID")
