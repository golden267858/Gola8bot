import requests
import time

def check_link(url):
    try:
        response = requests.get(url, timeout=10)
        return response.status_code == 200
    except:
        return False

def notify_telegram(message):
    # 此处假设存在 bot api 封装或调用方法
    print(f"Sending to Telegram: {message}")

def monitor():
    # 读取配置
    main_url = "https://t.me/example_main"
    backup_url = "https://t.me/example_backup"
    
    if not check_link(main_url):
        print("Main link failed, switching to backup.")
        notify_telegram("⚠️ 警告：主引流链接已失效，系统已自动切换至备用链接。 (အချက်ပေးချက်- ပင်မလင့်ခ် ပျက်သွားပြီဖြစ်၍ အရန်လင့်ခ်သို့ ပြောင်းလဲထားပါသည်။)")
        # 执行切换逻辑...
    else:
        print("Main link is active.")

if __name__ == "__main__":
    monitor()
