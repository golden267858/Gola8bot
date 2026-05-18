export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    // ==========================================
    // 1. Webhook 激活开关
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
    // 2. 接待大厅 + S2S 隐形回传雷达
    // ==========================================
    if (url.pathname === '/webhook' && request.method === 'POST') {
      const BOT_TOKEN = env.BOT_TOKEN; 
      if (!BOT_TOKEN) return new Response('OK', { status: 200 }); 

      try {
        const update = await request.json();
        
        if (update.message && update.message.text && update.message.text.startsWith('/start')) {
          const parts = update.message.text.split(' ');
          const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

          const realTgId = update.message.from.id;
          const username = update.message.from.username ? `@${update.message.from.username}` : '未设置';

          let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
          replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n\n`;
          replyText += `✅ <b>System Record (စနစ်မှတ်တမ်း):</b>\n`;
          replyText += `▪️ <b>Ad ID:</b> <code>${clickid}</code>\n`;
          replyText += `▪️ <b>User ID:</b> <code>${realTgId}</code>\n`;
          if (username !== '未设置') {
             replyText += `▪️ <b>Username:</b> ${username}\n`;
          }
          replyText += `\n👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။`;

          // 动作 A：给客户发欢迎语和客服按钮
          await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: update.message.chat.id,
              text: replyText,
              parse_mode: 'HTML',
              reply_markup: {
                inline_keyboard: [[{ text: "🎧 Customer Service (联系人工客服)", url: "https://t.me/Gold8One" }]]
              }
            })
          });

          // ==========================================
          // 🔥 动作 B：给 BeMob 发送转化捷报 (S2S Postback) 🔥
          // ==========================================
          // 如果 clickid 不是默认词，说明是买量来的，立刻上报转化！
          if (clickid !== 'Direct_Traffic') {
            // 已经为您精准替换为真实的 BeMob 回传地址
            const postbackUrl = `http://6tjzk.bemobtrcks.com/postback?cid=${clickid}`;
            await fetch(postbackUrl); 
          }
        }
        return new Response('OK', { status: 200 }); 
      } catch (err) {
        return new Response('Error', { status: 500 });
      }
    }

    // ==========================================
    // 3. 兜底护航：主页展示
    // ==========================================
    return env.ASSETS.fetch(request);
  }
};
