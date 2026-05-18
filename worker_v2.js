addEventListener('fetch', event => {
 event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
 const url = new URL(event.request.url);
 const clickid = url.searchParams.get('clickid') || '';
 const zoneid = url.searchParams.get('zoneid') || '';

 // 1. 异步上报
 if (clickid) {
   const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
   event.waitUntil(fetch(bemobPostback).catch(() => {}));
 }

 // 2. 路由分发
 if (url.pathname === '/tg') {
   return Response.redirect(`tg://resolve?domain=gola8bot&start=${clickid}`, 302);
 } else if (url.pathname === '/viber') {
   // 使用 Viber 链接
   return Response.redirect(`viber://add?number=09672912388`, 302);
 }

 return Response.redirect('https://pg-vip-mm.pages.dev', 302);
}
