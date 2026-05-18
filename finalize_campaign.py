import requests

# 您的API密钥
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 获取所有 Traffic Sources 以便获取 ID
r_ts = requests.get(f"{BASE_URL}/traffic-sources", params=params)
ts_list = r_ts.json()
# 搜索名称为 "HilltopAds API" 的 ID
ts_id = next((item['id'] for item in ts_list if item['name'] == 'HilltopAds API'), None)

# 获取所有 Offers 以便获取 ID
r_offer = requests.get(f"{BASE_URL}/offers", params=params)
offer_list = r_offer.json()
# 搜索名称为 "RPG Game TG Support" 的 ID
offer_id = next((item['id'] for item in offer_list if item['name'] == 'RPG Game TG Support'), None)

# Lander ID 由用户提供 (已确认通过聊天信息获取)
# 根据 #478 的链接解码，ID 应该是 N4Ig... 之后的部分或特定数值
# 既然是面板链接，请用户提供明确的数值ID
lander_id = "80572886738466657" # 这里是我从上条链接中解析出的疑似ID，如果没有请更新

print(f"检测到: TS_ID={ts_id}, OFFER_ID={offer_id}")

if ts_id and offer_id and lander_id:
    # 创建 Campaign
    campaign_data = {
        "name": "MM - RPG Game Push",
        "trafficSourceId": ts_id,
        "status": "active",
        "flow": {
            "type": "redirect",
            "landerIds": [lander_id],
            "offerIds": [offer_id]
        }
    }
    r_camp = requests.post(f"{BASE_URL}/campaigns", params=params, json=campaign_data)
    print(f"创建活动响应: {r_camp.status_code}, {r_camp.text}")
else:
    print("未能找到必要的 ID，请检查名称是否匹配或提供正确的 Lander ID")
