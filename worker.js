addEventListener('fetch', event => {
  event.respondWith(handleRequest(event.request))
})

async function handleRequest(request) {
  const url = new URL(request.url)
  const clickId = url.searchParams.get('clickid') || 'unknown'
  const zoneId = url.searchParams.get('zoneid') || 'unknown'

  // 1. 异步上报至 BeMob (异步执行，不阻塞跳转)
  // BeMob 官方 tracking 域名格式: http://track.bemob.com/click?clickId=...
  // 假设需要上报的数据点 (根据 BeMob 官方文档调整)
  const reportUrl = `https://track.your-bemob-domain.com/click?clickId=${clickId}&zoneid=${zoneId}`
  event.waitUntil(fetch(reportUrl).catch(e => console.error("BeMob report error:", e)))

  // 2. 路由分发
  if (url.pathname === '/tg') {
    const tgUrl = `tg://resolve?domain=gola8bot&start=${clickId}`
    return Response.redirect(tgUrl, 302)
  }
  
  if (url.pathname === '/viber') {
    const viberUrl = `https://msng.link/vi/gola8bot`
    return Response.redirect(viberUrl, 302)
  }

  return new Response("Not Found", { status: 404 })
}
