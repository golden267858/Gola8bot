export async function onRequestGet(context) {
  const { request, env } = context;
  const url = new URL(request.url);
  const BOT_TOKEN = env.BOT_TOKEN;
  
  if (!BOT_TOKEN) {
    return new Response('请先在 Cloudflare 后台环境变量配置 BOT_TOKEN', { status: 500 });
  }
  
  // 核心：由 Cloudflare 服务器直接向 TG 官方发起 Webhook 绑定
  const tgUrl = `https://api.telegram.org/bot${BOT_TOKEN}/setWebhook?url=https://${url.hostname}/webhook`;
  const tgResponse = await fetch(tgUrl);
  const result = await tgResponse.text();
  
  return new Response(result, { headers: { 'Content-Type': 'application/json' } });
}
