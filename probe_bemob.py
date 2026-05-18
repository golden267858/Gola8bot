import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

endpoints = ["traffic-sources", "landers", "offers", "campaigns"]

for ep in endpoints:
    try:
        response = requests.get(f"{BASE_URL}/{ep}", params=params)
        print(f"GET {ep}: {response.status_code}")
    except Exception as e:
        print(f"GET {ep} FAILED: {str(e)}")
