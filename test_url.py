import requests

# 用一个标准的 http 地址测试，看看 API 是不是在拒绝 tg:// 协议
offer_data = {
    "name": "Test Offer",
    "url": "https://google.com",
    "status": "active",
    "payoutType": "auto",
    "currencyId": "USD",
    "enableDailyCap": False,
    "countryId": 258
}
# ... 使用 params 调用 POST
