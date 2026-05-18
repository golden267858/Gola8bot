import requests
import json
import sqlite3

# 配置
BOT_TOKEN = "7470053411:YOUR_BOT_TOKEN_HERE" # 老板请在此处替换真实 Bot Token
WEBHOOK_URL = "https://gola8bot.golden267858.workers.dev/bot" # 需将其挂载到您的 Worker 上
DB_NAME = "user_clicks.db"

# 初始化数据库
conn = sqlite3.connect(DB_NAME)
conn.execute("CREATE TABLE IF NOT EXISTS users (tg_id INTEGER PRIMARY KEY, clickid TEXT)")
conn.commit()

def handle_update(update):
    message = update.get("message", {})
    text = message.get("text", "")
    tg_id = message.get("from", {}).get("id")

    if text.startswith("/start"):
        parts = text.split(" ")
        clickid = parts[1] if len(parts) > 1 else "no_clickid"
        
        # 绑定存入数据库
        conn.execute("INSERT OR REPLACE INTO users (tg_id, clickid) VALUES (?, ?)", (tg_id, clickid))
        conn.commit()
        
        # 缅甸语欢迎语
        welcome_text = "ဂိုလာ၈ဂိမ်းမှကြိုဆိုပါတယ်။\nသင့်ရဲ့ဂိမ်းကစားရန်အတွက် - https://pg-vip-mm.pages.dev"
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", json={
            "chat_id": tg_id, "text": welcome_text
        })

# 注册 Webhook
def register_webhook():
    r = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/setWebhook?url={WEBHOOK_URL}")
    print(f"Webhook 注册: {r.text}")

if __name__ == "__main__":
    register_webhook()
