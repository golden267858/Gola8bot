export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // ==========================================
    // 1. 绝杀开关：无视防火墙，由云端服务器亲自去绑定 Webhook！
    // ==========================================
    if (url.pathname === '/setup') {
      const BOT_TOKEN = env.BOT_TOKEN;
      if (!BOT_TOKEN) return new Response('❌ 请先在 Cloudflare 环境变量中配置 BOT_TOKEN', { status: 500 });
      
      const tgUrl = `https://api.telegram.org/bot${BOT_TOKEN}/setWebhook?url=https://${url.hostname}/webhook`;
      const tgResponse = await fetch(tgUrl);
      return new Response(await tgResponse.text(), { 
        headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } 
      });
    }

    // ==========================================
    // 2. 接待大厅：拦截 TG 机器人的所有消息
    // ==========================================
    if (url.pathname === '/webhook' && request.method === 'POST') {
      const BOT_TOKEN = env.BOT_TOKEN; 
      if (!BOT_TOKEN) return new Response('OK', { status: 200 }); 

      try {
        const update = await request.json();
        
        if (update.message && update.message.text && update.message.text.startsWith('/start')) {
          const parts = update.message.text.split(' ');
          const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

          let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
          replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n`;
          replyText += `✅ <b>System:</b> ID [ <code>${clickid}</code> ] ချိတ်ဆက်ပြီးပါပြီ。\n\n`;
          replyText += `👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။`;

          await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: update.message.chat.id,
              text: replyText,
              parse_mode: 'HTML',
              reply_markup: {
                inline_keyboard: [[{ text: "💎 100% ပြန်အမ်းငွေရယူမည်", url: "https://gola8win.com" }]]
              }
            })
          });
        }
        return new Response('OK', { status: 200 }); // 给 TG 官方返回收到
      } catch (err) {
        return new Response('Error', { status: 500 });
      }
    }

    // ==========================================
    // 3. 兜底放行：正常访问一律吐出黑金落地页！
    // ==========================================
    return env.ASSETS.fetch(request);
  }
};
