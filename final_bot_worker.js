addEventListener('fetch', event => {
  event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
  const request = event.request;
  const url = new URL(request.url);
  const path = url.pathname;

  // --- 1. Bot Webhook 处理逻辑 ---
  if (path === '/bot' && request.method === 'POST') {
    const update = await request.json();
    if (update.message && update.message.text) {
      const text = update.message.text;
      const tgId = update.message.from.id.toString();
      
      if (text.startsWith('/start')) {
        const parts = text.split(' ');
        const clickid = parts.length > 1 ? parts[1] : 'unknown';
        
        // 使用 KV 命名空间存储 (GOLA8_DB 需要在 Dashboard 手动创建并绑定给该 Worker)
        await GOLA8_DB.put(tgId, clickid);
        
        // 缅甸语欢迎语
        const welcomeText = "ဂိုလာ၈ဂိမ်းမှကြိုဆိုပါတယ်။\nသင့်ရဲ့ဂိမ်းကစားရန်အတွက် - https://pg-vip-mm.pages.dev";
        const botToken = "7470053411:YOUR_BOT_TOKEN"; // 老板请记得在后台替换
        
        await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
          body: JSON.stringify({ chat_id: tgId, text: welcomeText })
        });
      }
    }
    return new Response("OK", { status: 200 });
  }

  // --- 2. 原有的重定向逻辑 ---
  const clickid = url.searchParams.get('clickid') || '';
  const zoneid = url.searchParams.get('zoneid') || '';

  if (clickid) {
    const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
    event.waitUntil(fetch(bemobPostback, { method: 'GET', headers: { 'User-Agent': 'CF-Worker-Tracker' } }).catch(() => {}));
  }

  if (path.includes('/tg')) {
    return Response.redirect(`https://t.me/gola8bot?start=${clickid}`, 302);
  } else if (path.includes('/viber')) {
    return Response.redirect(`https://chats.viber.com/09672912388`, 302);
  }

  return Response.redirect('https://pg-vip-mm.pages.dev', 302);
}
