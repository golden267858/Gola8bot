export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // ==========================================
    // 0. 绝杀开关：让 Cloudflare 替咱们去绑 Webhook！
    // ==========================================
    if (url.pathname === '/setup') {
      const BOT_TOKEN = env.BOT_TOKEN;
      if (!BOT_TOKEN) return new Response('请先在环境变量配置 BOT_TOKEN', { status: 500 });
      
      // Cloudflare 内网直接请求 Telegram，无视任何网络封锁
      const tgUrl = `https://api.telegram.org/bot${BOT_TOKEN}/setWebhook?url=https://${url.hostname}/webhook`;
      const tgResponse = await fetch(tgUrl);
      const result = await tgResponse.text();
      
      return new Response(result, { headers: { 'Content-Type': 'application/json' } });
    }

    // ==========================================
    // 1. 核心任务：拦截 TG 机器人的 Webhook 请求
    // ==========================================
    if (url.pathname === '/webhook' && request.method === 'POST') {
      const BOT_TOKEN = env.BOT_TOKEN; 
      if (!BOT_TOKEN) return new Response('Bot Token Not Configured', { status: 500 });

      try {
        const update = await request.json();
        
        if (update.message && update.message.text) {
          const chatId = update.message.chat.id;
          const text = update.message.text;

          if (text.startsWith('/start')) {
            const parts = text.split(' ');
            const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

            let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
            replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n`;
            replyText += `✅ <b>System:</b> ID [ <code>${clickid}</code> ] ချိတ်ဆက်ပြီးပါပြီ။\n\n`;
            replyText += `👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။`;

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
        return new Response('OK', { status: 200 });
      } catch (err) {
        return new Response('Webhook Error', { status: 500 });
      }
    }

    // ==========================================
    // 2. 兜底任务：放行黑金主页！
    // ==========================================
    return env.ASSETS.fetch(request);
  }
};
