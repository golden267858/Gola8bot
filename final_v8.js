addEventListener('fetch', event => {
  event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
  const url = new URL(event.request.url);
  const path = url.pathname;
  const clickid = url.searchParams.get('clickid') || '';
  const zoneid = url.searchParams.get('zoneid') || '';

  // 1. 异步上报财务对账数据到 BeMob
  if (clickid) {
    const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
    event.waitUntil(fetch(bemobPostback, { method: 'GET', headers: { 'User-Agent': 'CF-Worker-Tracker' } }).catch(() => {}));
  }

  // 2. 核心路由分发 (使用 HTTPS 标准唤醒链接)
  if (path.includes('/tg')) {
    // 强制使用 HTTPS 标准链接唤醒 TG
    return Response.redirect(`https://t.me/gola8bot?start=${clickid}`, 302);
  } else if (path.includes('/viber')) {
    // 强制使用 Viber 官方 HTTPS 中转链接
    return Response.redirect(`https://chats.viber.com/09672912388`, 302);
  }

  // 默认兜底
  return Response.redirect('https://pg-vip-mm.pages.dev', 302);
}
