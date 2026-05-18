import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
import json
import os

TOKEN = "8872269431:AAHLOZXJg3XalUTpdu53aPS1NYq3SxyXulc"
MAP_FILE = "memory/user_map.json"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    args = context.args
    click_id = args[0] if args else "unknown"
    
    with open(MAP_FILE, 'r+') as f:
        data = json.load(f)
        data['users'][user_id] = click_id
        f.seek(0)
        json.dump(data, f, indent=2)
    
    await update.message.reply_text("လူကြီးမင်း၏ ငွေသွင်း/ငွေထုတ် ကိစ္စရပ်များအတွက် ကျွန်ုပ်တို့၏ ငွေစာရင်းတာဝန်ခံနှင့် ချိတ်ဆက်ပေးနေပါသည်။ ခဏစောင့်ဆိုင်းပေးပါ။")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()
