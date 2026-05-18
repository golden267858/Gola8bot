export async function onRequestPost(context) {
  const { request, env } = context;
  const BOT_TOKEN = env.BOT_TOKEN; 

  if (!BOT_TOKEN) {
    return new Response('Bot Token Not Configured', { status: 500 });
  }

  try {
    const update = await request.json();
    
    if (update.message && update.message.text) {
      const chatId = update.message.chat.id;
      const text = update.message.text;

      if (text.startsWith('/start')) {
        const parts = text.split(' ');
        const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; 

        // 缅甸语高转化迎客话术
        let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
        replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ!\n`;
        replyText += `✅ <b>System:</b> ID [ <code>${clickid}</code> ] ချိတ်ဆက်ပြီးပါပြီ。\n\n`;
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
