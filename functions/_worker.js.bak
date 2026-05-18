export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // --- 1. Telegram Bot Webhook 逻辑 ---
    if (path === '/bot' && request.method === 'POST') {
      try {
        const update = await request.json();
        if (update.message && update.message.text) {
          const text = update.message.text;
          const tgId = update.message.from.id.toString();
          
          if (text.startsWith('/start')) {
            const parts = text.split(' ');
            const clickid = parts.length > 1 ? parts[1] : 'unknown';
            
            // 使用 KV 命名空间存储 (已确认 GOLA8_DB 已绑定)
            await env.GOLA8_DB.put(tgId, clickid);
            
            const welcomeText = "ဂိုလာ၈ဂိမ်းမှကြိုဆိုပါတယ်။\nသင့်ရဲ့ဂိမ်းကစားရန်အတွက် - https://pg-vip-mm.pages.dev";
            const botToken = "8872269431:AAH88jhpEdkSXSKy5hBPrHt31frYjWqtcco";
            
            await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
              method: 'POST',
              headers: {'Content-Type': 'application/json'},
              body: JSON.stringify({ chat_id: tgId, text: welcomeText })
            });
          }
        }
      } catch (e) {
        console.log('Bot Webhook Error:', e);
      }
      return new Response("OK", { status: 200 });
    }

    // --- 2. 流量重定向逻辑 ---
    const clickid = url.searchParams.get('clickid') || '';
    const zoneid = url.searchParams.get('zoneid') || '';

    if (clickid) {
      const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
      ctx.waitUntil(fetch(bemobPostback, { method: 'GET', headers: { 'User-Agent': 'CF-Pages-Tracker' } }).catch(() => {}));
    }

    if (path.includes('/tg')) {
      return Response.redirect(`https://t.me/gola8bot?start=${clickid}`, 302);
    } else if (path.includes('/viber')) {
      return Response.redirect(`https://chats.viber.com/09672912388`, 302);
    }

    return env.ASSETS.fetch(request);
  }
};
