import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 1. 创建新 Offer - 补全所有必填字段
offer_data = {
    "name": "RPG Game TG Support",
    "url": "tg://resolve?domain=gola8bot&start={clickId}",
    "status": "active",
    "payoutType": "auto",
    "currencyId": "USD",
    "enableDailyCap": False,
    "countryId": 258 # Myanmar ID
}
r_offer = requests.post(f"{BASE_URL}/offers", params=params, json=offer_data)
print(f"创建 Offer 响应: {r_offer.status_code}, {r_offer.text}")
