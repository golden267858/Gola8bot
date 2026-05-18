export default {
 async fetch(request, env, ctx) {
 const url = new URL(request.url);
 const clickid = url.searchParams.get('clickid') || '';
 const zoneid = url.searchParams.get('zoneid') || '';

 // 1. 异步上报财务对账数据到 BeMob
 if (clickid) {
 const bemobPostback = `https://6tjzk.bemobtrcks.com/postback?cid=${clickid}&payout=0&status=click&zone=${zoneid}`;
 ctx.waitUntil(
 fetch(bemobPostback, { method: 'GET', headers: { 'User-Agent': 'CF-Pages-Tracker' } })
 .catch(err => console.log('BeMob report error:', err))
 );
 }

 // 2. 核心重定向路由
 if (url.pathname === '/tg') {
 return Response.redirect(`tg://resolve?domain=gola8bot&start=${clickid}`, 302);
 } else if (url.pathname === '/viber') {
 return Response.redirect(`https://msng.link/vi/gola8bot`, 302);
 }

 // 3. 兜底：其余路径正常渲染原本的静态落地页(index.html)
 return env.ASSETS.fetch(request);
 }
};
