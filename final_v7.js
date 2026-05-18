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
    event.waitUntil(fetch(bemobPostback).catch(() => {}));
  }

  // 2. 路由分发 (使用 includes 更健壮)
  if (path.includes('/tg')) {
    return Response.redirect(`tg://resolve?domain=gola8bot&start=${clickid}`, 302);
  } else if (path.includes('/viber')) {
    return Response.redirect(`viber://add?number=09672912388`, 302);
  }

  // 默认兜底
  return Response.redirect('https://pg-vip-mm.pages.dev', 302);
}
