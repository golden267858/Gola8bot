import requests
import base64

# API Configuration
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"

# 尝试另一种常见的 Basic Auth 或不同的 Header 名字
# 这里尝试将 AccessKey:SecretKey 编码为 Base64 并使用 Authorization: Basic 头
auth_str = f"{ACCESS_KEY}:{SECRET_KEY}"
encoded_auth = base64.b64encode(auth_str.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded_auth}",
    "Content-Type": "application/json"
}

def create_resource(endpoint, data):
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json=data)
    print(f"DEBUG: {endpoint} response: {response.status_code}, {response.text}")
    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception(f"Failed to create {endpoint}: {response.text}")

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
