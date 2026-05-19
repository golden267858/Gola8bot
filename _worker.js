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
      return new Response(await tgResponse.text(), { headers: { 'Content-Type': 'application/json' } });
    }

    // ==========================================
    // 2. 接待大厅 + 隐形底裤草稿 + S2S 回传
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

          // ==========================================
          // 🔥 终极暗器：给客服看的“全套底裤草稿” 🔥
          // (新增了 Username，保留了 User ID 和 Ad ID)
          // ==========================================
          const draftText = `👋 မင်္ဂလာပါ！👋\n` +
                            `Ad ID: ${clickid}\n` +
                            `User ID: ${realTgId}\n` +
                            `Username: ${username}\n` +
                            `ငွေသွင်းချင်ပါတယ်၊ ပရိုမိုးရှင်းရှိလား。`;
          
          const encodedDraft = encodeURIComponent(draftText);
          const csLinkWithDraft = `https://t.me/Gold8One?text=${encodedDraft}`;


          // ==========================================
          // 🎭 前端伪装：只给客户看 Ad ID 🎭
          // ==========================================
          let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
          replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n\n`;
          replyText += `✅ <b>System Record (စနစ်မှတ်တမ်း):</b>\n`;
          replyText += `▪️ <b>Ad ID:</b> <code>${clickid}</code>\n`;
          // 已经删除了 User ID 和 Username 的展示
          replyText += `\n👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။ 👇`;

          await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              chat_id: update.message.chat.id,
              text: replyText,
              parse_mode: 'HTML',
              reply_markup: {
                inline_keyboard: [[{ text: "🎧 Customer Service", url: csLinkWithDraft }]]
              }
            })
          });

          // S2S BeMob 雷达隐形回传
          if (clickid !== 'Direct_Traffic') {
            const postbackUrl = `http://6tjzk.bemobtrcks.com/postback?cid=${clickid}`;
            await fetch(postbackUrl); 
          }
        }
        return new Response('OK', { status: 200 }); 
      } catch (err) {
        return new Response('Error', { status: 500 });
      }
    }

    return env.ASSETS.fetch(request);
  }
};
