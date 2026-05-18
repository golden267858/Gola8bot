addEventListener('fetch', event => {
 event.respondWith(handleRequest(event));
});

async function handleRequest(event) {
 const url = new URL(event.request.url);
 const clickid = url.searchParams.get('clickid') || '';
 const zoneid = url.searchParams.get('zoneid') || '';

 if (clickid) {
   const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
   event.waitUntil(fetch(bemobPostback).catch(() => {}));
 }

 if (url.pathname === '/tg') {
   return Response.redirect(`tg://resolve?domain=gola8bot&start=${clickid}`, 302);
 } else if (url.pathname === '/viber') {
   return Response.redirect(`viber://add?number=09672912388`, 302);
 }

 return Response.redirect('https://pg-vip-mm.pages.dev', 302);
}
