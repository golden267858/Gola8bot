export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const clickid = url.searchParams.get('clickid') || '';
    const zoneid = url.searchParams.get('zoneid') || '';

    // 1. Telegram Bot Webhook
    if (path === '/bot' && request.method === 'POST') {
      try {
        const update = await request.json();
        if (update.message && update.message.text && update.message.text.startsWith('/start')) {
          const parts = update.message.text.split(' ');
          const clickid = parts.length > 1 ? parts[1] : 'unknown';
          await env.GOLA8_DB.put(update.message.from.id.toString(), clickid);
          await fetch(`https://api.telegram.org/bot8872269431:AAH88jhpEdkSXSKy5hBPrHt31frYjWqtcco/sendMessage`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ chat_id: update.message.from.id, text: "ဂိုလာ၈ဂိမ်းမှကြိုဆိုပါတယ်။\nသင့်ရဲ့ဂိမ်းကစားရန်အတွက် - https://pg-vip-mm.pages.dev" })
          });
        }
      } catch(e) {}
      return new Response("OK", { status: 200 });
    }

    // 2. 流量重定向
    if (path.includes('/tg')) return Response.redirect(`https://t.me/gola8bot?start=${clickid}`, 302);
    if (path.includes('/viber')) return Response.redirect(`https://chats.viber.com/09672912388`, 302);

    return env.ASSETS.fetch(request);
  }
};
