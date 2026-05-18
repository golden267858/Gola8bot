import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 尝试遍历可能的路径查找 Lander ID
endpoints = ["landers", "landing-pages", "pages", "lp"]
for ep in endpoints:
    try:
        response = requests.get(f"{BASE_URL}/{ep}", params=params)
        if response.status_code == 200:
            print(f"在 {ep} 中找到列表:")
            print(response.json())
            break
    except:
        pass
