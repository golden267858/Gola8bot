import requests

def check_link(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

# 模拟检测逻辑
if not check_link("https://t.me/example_main"):
    print("FAILED")
else:
    print("OK")
