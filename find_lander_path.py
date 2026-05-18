import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 尝试所有常见的 Lander 资源路径
potential_paths = ["landers", "landing-pages", "lp", "pages"]

for path in potential_paths:
    response = requests.post(f"{BASE_URL}/{path}", params=params, json={"name": "test", "url": "http://test.com", "status": "active"})
    print(f"POST {path}: {response.status_code}, {response.text}")
