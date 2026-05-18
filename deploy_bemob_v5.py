import requests

# API Configuration
ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"

# 尝试 query 参数认证，常见于某些旧版 API
params = {
    "accessKey": ACCESS_KEY,
    "secretKey": SECRET_KEY
}

def create_resource(endpoint, data):
    response = requests.post(f"{BASE_URL}/{endpoint}", params=params, json=data)
    print(f"DEBUG: {endpoint} response: {response.status_code}, {response.text}")
    if response.status_code in [200, 201]:
        return response.json()
    else:
        raise Exception(f"Failed to create {endpoint}: {response.text}")

try:
    print("Creating Traffic Source...")
    ts = create_resource("traffic-sources", {"name": "HilltopAds API"})
except Exception as e:
    print(f"\nERROR: {str(e)}")
