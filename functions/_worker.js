export async function onRequestPost(context) {
  const { request, env } = context;
  
  // 从 Cloudflare 环境变量中读取您的 TG Bot Token
  const BOT_TOKEN = env.BOT_TOKEN; 

  if (!BOT_TOKEN) {
    return new Response('Bot Token Not Configured', { status: 500 });
  }

  try {
    const update = await request.json();
    
    // 监听用户的发信
    if (update.message && update.message.text) {
      const chatId = update.message.chat.id;
      const text = update.message.text;

      // 核心拦截：抓取带参的 /start 命令 (例如 /start BOSS_WIN)
      if (text.startsWith('/start')) {
        const parts = text.split(' ');
        const clickid = parts.length > 1 ? parts[1] : 'Direct_Traffic'; // 如果没带参数，标记为直达流量

        // 构建高转化缅甸语话术 (支持 HTML 格式)
        let replyText = `🔥 <b>VIP PREMIUM ACCESS</b> 🔥\n\n`;
        replyText += `🎉 ကြိုဆိုပါတယ်။ သင်၏ကံစမ်းမှုကိုစတင်လိုက်ပါ! (欢迎！开启您的好运！)\n\n`;
        replyText += `✅ <b>System:</b> ID [ <code>${clickid}</code> ] ချိတ်ဆက်ပြီးပါပြီ။\n`; 
        replyText += `(追踪参数已绑定，返佣不丢失)\n\n`;
        replyText += `👇 ကျေးဇူးပြု၍ အောက်ပါခလုတ်ကိုနှိပ်ပါ။ (请点击下方按钮继续)`;

        // 发送迎客消息给老哥，附带下方点击按钮
        await fetch(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            chat_id: chatId,
            text: replyText,
            parse_mode: 'HTML',
            reply_markup: {
              inline_keyboard: [
                [{ text: "💎 100% ပြန်အမ်းငွေရယူမည် (马上获取100%返利)", url: "https://gola8win.com" }] // 这里换成您的终极转化落地页/支付页
              ]
            }
          })
        });
      }
    }
    // 无论发生什么，必须给 Telegram 返回 200 OK，否则 TG 会疯狂重试
    return new Response('OK', { status: 200 });
  } catch (err) {
    return new Response('Webhook Error', { status: 500 });
  }
}
