import requests

# API Configuration
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"

# 使用Query参数进行认证（上一次测试证明此方式已通过认证）
params = {
    "accessKey": ACCESS_KEY,
    "secretKey": SECRET_KEY
}

def create_resource(endpoint, data):
    # 补全了 status 字段以通过 422 校验
    data["status"] = "active"
    response = requests.post(f"{BASE_URL}/{endpoint}", params=params, json=data)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception(f"Failed to create {endpoint}: {response.status_code} - {response.text}")

try:
    print("Creating Traffic Source...")
    ts = create_resource("traffic-sources", {"name": "HilltopAds API"})
    
    print("Creating Lander...")
    lander = create_resource("landers", {
        "name": "RPG Game CF Page",
        "url": "https://pg-vip-mm.pages.dev?clickid={clickId}"
    })
    
    print("Creating Offer...")
    offer = create_resource("offers", {
        "name": "RPG Game TG Support",
        "url": "tg://resolve?domain=gola8bot&start={clickId}"
    })
    
    print("Creating Campaign...")
    # Campaign 可能需要特定的 flow 定义，尝试标准构建
    campaign = create_resource("campaigns", {
        "name": "MM - RPG Game Push",
        "trafficSourceId": ts['id'],
        "flow": {
            "type": "redirect",
            "landerIds": [lander['id']],
            "offerIds": [offer['id']]
        }
    })
    
    print(f"\nSUCCESS: Campaign created!")
    print(f"Tracking URL: {campaign.get('url', 'N/A')}")

except Exception as e:
    print(f"\nERROR: {str(e)}")
