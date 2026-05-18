import telebot
import json
import os
import requests
from datetime import datetime

# ================= 🔴 核心配置区 =================
BOT_TOKEN = '8872269431:AAH88jhpEdkSXSKy5hBPrHt31frYjWqtcco'
BEMOB_POSTBACK_URL = 'https://6tjzk.bemobtrcks.com/postback'
DATA_FILE = '/root/.openclaw/workspace/data/user_map.json'
ADMIN_IDS = [7436169171]

# Ensure data dir exists
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
# =================================================

bot = telebot.TeleBot(BOT_TOKEN)

def load_data():
    if not os.path.exists(DATA_FILE): return {}
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f: return json.load(f)
    except json.JSONDecodeError: return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@bot.message_handler(commands=['start'])
def handle_start(message):
    text_parts = message.text.split()
    user_id = str(message.from_user.id)
    if len(text_parts) > 1:
        click_id = text_parts[1]
        data = load_data()
        data[user_id] = {"click_id": click_id, "join_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        save_data(data)
        burmese_reply = "မင်္ဂလာပါ! 🌟 ကျွန်ုပ်တို့၏ VIP ပလက်ဖောင်းမှ နွေးထွေးစွာ ကြိုဆိုပါတယ်။ လူကြီးမင်း၏ အကောင့်ကို အောင်မြင်စွာ ချိတ်ဆက်ပြီးပါပြီ။"
        bot.reply_to(message, burmese_reply)
    else:
        bot.reply_to(message, "မင်္ဂလာပါ! (Welcome)")

@bot.message_handler(commands=['pay'])
def handle_pay(message):
    if message.from_user.id not in ADMIN_IDS: return
    text_parts = message.text.split()
    if len(text_parts) == 3:
        target_user_id = text_parts[1]
        amount = text_parts[2]
        data = load_data()
        if target_user_id in data:
            click_id = data[target_user_id]["click_id"]
            payload = {"cid": click_id, "payout": amount}
            try:
                response = requests.get(BEMOB_POSTBACK_URL, params=payload, timeout=5)
                if response.status_code == 200:
                    bot.reply_to(message, f"✅ 回传成功: {target_user_id}")
            except Exception as e:
                bot.reply_to(message, f"❌ 错误: {str(e)}")

if __name__ == '__main__':
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
