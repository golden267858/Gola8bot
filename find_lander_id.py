import requests

ACCESS_KEY = "366E9F2203B948178F38BC502DF0DF57"
SECRET_KEY = "geWtZ8207X/lqYBFIRi/QH0hrlidXv4E+DkPvtnxQjbX299JTf36dPjfFkKmEaKHNmpWIcTKYQU7Z699B5/mfw=="
BASE_URL = "https://api.bemob.com/v1"
params = {"accessKey": ACCESS_KEY, "secretKey": SECRET_KEY}

# 获取所有落地页并打印，方便查找 ID
response = requests.get(f"{BASE_URL}/landers", params=params)
if response.status_code == 200:
    landers = response.json()
    print("找到的落地页列表:")
    # 假设返回列表或包含列表的字典
    data = landers.get('data') or landers
    for l in data:
        print(f"名称: {l.get('name')}, ID: {l.get('id')}")
else:
    print(f"获取失败: {response.status_code}, {response.text}")
