export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // ==========================================
    // 1. Webhook 激活开关 (无视墙，直连TG)
    // ==========================================
    if (url.pathname === '/setup') {
      const BOT_TOKEN = env.BOT_TOKEN;
      if (!BOT_TOKEN) return new Response('❌ 请先配置 BOT_TOKEN', { status: 500 });
      
      const tgUrl = `https://api.telegram.org/bot${BOT_TOKEN}/setWebhook?url=https://${url.hostname}/webhook`;
      const tgResponse = await fetch(tgUrl);
      return new Response(await tgResponse.text(), { 
        headers: { 'Content-Type': 'application/json', 'Cache-Control': 'no-store' } 
      });
    }

    // ==========================================
    // 2. 接待大厅：拦截消息，扒出客户“真实底裤”
    // ==========================================
    if (url.pathname === '/webhook' && request.method === 'POST') {
      const BOT_TOKEN = env.BOT_TOKEN; 
      if (!BOT_TOKEN) return new Response('OK', { status: 200 }); 

      try {
        const update = await request.json();
        
        if (update.message && update.message.text && update.message.text.startsWith('/start')) {
          // 1. 抓取广告买量的 ClickID
          const parts = update.message.text.split(' ');
          const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

          // 2. 扒出该客户在 Telegram 的绝对真实唯一 ID
          const realTgId = update.message.from.id;
          // 3. 顺手扒出客户的 TG 用户名（如果有的话）
          const username = update.message.from.username ? `@${update.message.from.username}` : '未设置';

          // 组装双语高逼格话术（展示给客户看，也是给客服留底）
          let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
          replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n\n`;
          
          replyText += `✅ <b>System Record (စနစ်မှတ်တမ်း):</b>\n`;
          replyText += `▪️ <b>Ad ID (来源追踪):</b> <code>${clickid}</code>\n`;
          replyText += `▪️ <b>User ID (您的真实ID):</b> <code>${realTgId}</code>\n`;
          if (username !== '未设置') {
             replyText += `▪️ <b>Username (TG账号):</b> ${username}\n`;
          }
          replyText += `\n👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။ (请点击下方联系人工客服)`;

          await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: update.message.chat.id,
              text: replyText,
              parse_mode: 'HTML',
              reply_markup: {
                // 这里已经换成了您的人工客服专属通道！
                inline_keyboard: [[{ text: "🎧 Customer Service (联系人工客服)", url: "https://t.me/Gold8One" }]]
              }
            })
          });
        }
        return new Response('OK', { status: 200 }); 
      } catch (err) {
        return new Response('Error', { status: 500 });
      }
    }

    // ==========================================
    // 3. 兜底护航：正常访问一律吐出黑金落地页！
    // ==========================================
    return env.ASSETS.fetch(request);
  }
};
