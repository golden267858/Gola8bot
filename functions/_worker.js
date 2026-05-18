export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // ==========================================
    // 1. 核心任务：拦截 TG 机器人的 Webhook 请求
    // ==========================================
    if (url.pathname === '/webhook' && request.method === 'POST') {
      const BOT_TOKEN = env.BOT_TOKEN; 
      
      if (!BOT_TOKEN) {
        return new Response('Bot Token Not Configured', { status: 500 });
      }

      try {
        const update = await request.json();
        
        // 监听到用户给机器人发消息
        if (update.message && update.message.text) {
          const chatId = update.message.chat.id;
          const text = update.message.text;

          // 识别 /start 唤醒命令
          if (text.startsWith('/start')) {
            const parts = text.split(' ');
            const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

            // 缅甸语高转化迎客话术
            let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
            replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n`;
            replyText += `✅ <b>System:</b> ID [ <code>${clickid}</code> ] ချိတ်ဆက်ပြီးပါပြီ။\n\n`;
            replyText += `👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။`;

            // 调用 TG 接口发回信
            await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                chat_id: chatId,
                text: replyText,
                parse_mode: 'HTML',
                reply_markup: {
                  inline_keyboard: [
                    [{ text: "💎 100% ပြန်အမ်းငွေရယူမည်", url: "https://gola8win.com" }] 
                  ]
                }
              })
            });
          }
        }
        // 永远给 TG 返回 200，防止它重复发请求
        return new Response('OK', { status: 200 });
      } catch (err) {
        return new Response('Webhook Error', { status: 500 });
      }
    }

    // ==========================================
    // 2. 兜底任务：如果不是机器人请求，全部放行去展示您的黑金主页！
    // ==========================================
    return env.ASSETS.fetch(request);
  }
};
