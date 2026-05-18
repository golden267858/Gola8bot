import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 穷举测试常见资源，直接打印响应，看看目录结构
for ep in ["traffic-sources", "offers", "campaigns", "landers", "pages", "flows"]:
    r = requests.get(f"{BASE_URL}/{ep}", params=params)
    print(f"Endpoint {ep}: {r.status_code}")
