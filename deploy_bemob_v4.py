import requests

# API Configuration
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"

# 尝试将它们作为 Header，但名称可能是 X-Api-Key 和 X-Api-Secret
headers = {
    "X-Api-Key": ACCESS_KEY,
    "X-Api-Secret": SECRET_KEY,
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
    # 后续操作...
except Exception as e:
    print(f"\nERROR: {str(e)}")
