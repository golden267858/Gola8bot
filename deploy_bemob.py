import requests
import base64

# API Configuration
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"

# Auth setup
headers = {
    "Api-Key": ACCESS_KEY,
    "Api-Secret": SECRET_KEY,
    "Content-Type": "application/json"
}

def create_resource(endpoint, data):
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json=data)
    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception(f"Failed to create {endpoint}: {response.text}")

try:
    # 1. Create Traffic Source
    ts = create_resource("traffic-sources", {"name": "HilltopAds API"})
    
    # 2. Create Lander
    lander = create_resource("landers", {
        "name": "RPG Game CF Page",
        "url": "https://pg-vip-mm.pages.dev?clickid={clickId}"
    })
    
    # 3. Create Offer
    offer = create_resource("offers", {
        "name": "RPG Game TG Support",
        "url": "tg://resolve?domain=gola8bot&start={clickId}"
    })
    
    # 4. Create Campaign
    campaign = create_resource("campaigns", {
        "name": "MM - RPG Game Push",
        "trafficSourceId": ts['id'],
        "flow": {
            "type": "redirect",
            "landerIds": [lander['id']],
            "offerIds": [offer['id']]
        }
    })
    
    print(f"SUCCESS: Campaign created!")
    print(f"Tracking URL: {campaign.get('url', 'N/A')}")

except Exception as e:
    print(f"ERROR: {str(e)}")
